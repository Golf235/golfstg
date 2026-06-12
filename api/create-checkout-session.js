const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

module.exports = async (req, res) => {
  // Only allow POST requests
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const { items } = req.body;

    if (!items || !Array.isArray(items) || items.length === 0) {
      return res.status(400).json({ error: 'Missing or invalid cart items.' });
    }

    // Map cart items to Stripe Line Items
    const lineItems = items.map(item => {
      return {
        price: item.priceId, // The Stripe Price ID mapped in cart.js
        quantity: item.quantity,
        // Natively allows customers to modify item quantities on the Stripe Checkout page
        adjustable_quantity: {
          enabled: true,
          minimum: 1,
          maximum: 99
        }
      };
    });

    // Create Stripe Checkout Session
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ['card'],
      line_items: lineItems,
      mode: 'payment',
      // Dynamic success/cancel redirects using the request origin header
      success_url: `${req.headers.origin}/index.html?checkout_success=true&session_id={CHECKOUT_SESSION_ID}`,
      cancel_url: `${req.headers.origin}/shop.html?checkout_canceled=true`,
    });

    // Return the Stripe Checkout URL to redirect the client
    return res.status(200).json({ url: session.url });
  } catch (err) {
    console.error("Stripe Session Creation Failed:", err);
    return res.status(500).json({ error: err.message || 'Internal Server Error' });
  }
};
