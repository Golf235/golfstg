import Stripe from 'stripe';

export async function onRequest(context) {
  const request = context.request;

  // Handle CORS preflight options request
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      }
    });
  }

  // Only allow POST requests
  if (request.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method Not Allowed' }), {
      status: 405,
      headers: {
        'Content-Type': 'application/json',
        'Allow': 'POST'
      }
    });
  }

  try {
    const body = await request.json();
    const { items, currency, country, vatRate, displayType } = body;

    if (!items || !Array.isArray(items) || items.length === 0) {
      return new Response(JSON.stringify({ error: 'Missing or invalid cart items.' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const activeCurrency = (currency || 'CHF').toLowerCase();
    const rate = parseFloat(vatRate) || 0;
    const isGross = displayType === 'gross';
    
    const origin = new URL(request.url).origin;

    // Map cart items to Stripe Line Items using dynamic price_data
    const lineItems = items.map(item => {
      // Create a nice description string of the selected options
      let description = "";
      if (item.options && Object.keys(item.options).length > 0) {
        description = Object.entries(item.options)
          .map(([key, val]) => `${key}: ${val}`)
          .join(" | ");
      }

      // Convert image path to absolute URL for Stripe
      let absoluteImages = [];
      if (item.image) {
        let cleanImage = item.image;
        if (cleanImage.startsWith('./')) {
          cleanImage = cleanImage.slice(2);
        }
        if (cleanImage.startsWith('/')) {
          cleanImage = cleanImage.slice(1);
        }
        
        // Handle absolute protocols and safely URL-encode spaces/special characters
        const imageUrl = cleanImage.startsWith('http://') || cleanImage.startsWith('https://')
          ? cleanImage
          : `${origin}/${cleanImage}`;
          
        absoluteImages.push(encodeURI(imageUrl));
      }

      // Calculate Net Price in cents
      const unitAmountGross = item.price; // in main currency unit
      const unitAmountNet = isGross ? (unitAmountGross / (1 + rate)) : unitAmountGross;
      const unitAmountCents = Math.round(unitAmountNet * 100);

      return {
        price_data: {
          currency: activeCurrency,
          product_data: {
            name: item.name,
            description: description || undefined,
            images: absoluteImages.length > 0 ? absoluteImages : undefined,
            tax_code: 'txcd_10000000', // physical goods
          },
          unit_amount: unitAmountCents,
          tax_behavior: 'exclusive',
        },
        quantity: item.quantity,
        adjustable_quantity: {
          enabled: true,
          minimum: 1,
          maximum: 99
        }
      };
    });

    const allowedShippingCountries = [
      'CH', // Switzerland
      'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 
      'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 
      'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', // EU 27
      'GB', // United Kingdom
      'US', // United States
      'CA'  // Canada
    ];

    const stripeKey = context.env.STRIPE_SECRET_KEY;
    if (!stripeKey) {
      throw new Error("STRIPE_SECRET_KEY environment variable is not configured in Cloudflare Pages dashboard.");
    }

    // Initialize Stripe using Worker fetch client
    const stripe = new Stripe(stripeKey, {
      httpClient: Stripe.createFetchHttpClient(),
    });

    // Create Stripe Checkout Session
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: lineItems,
      mode: 'payment',
      automatic_tax: { enabled: true },
      shipping_address_collection: {
        allowed_countries: allowedShippingCountries,
      },
      success_url: `${origin}/index.html?checkout_success=true&session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${origin}/shop.html?checkout_canceled=true`,
    });

    return new Response(JSON.stringify({ url: session.url }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });
  } catch (err) {
    console.error("Stripe Session Creation Failed:", err);
    return new Response(JSON.stringify({ error: err.message || 'Internal Server Error' }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });
  }
}
