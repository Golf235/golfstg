export async function onRequest(context) {
  const url = new URL(context.request.url);
  const pathname = url.pathname;

  // Performance optimization: Only run middleware cookie logic for HTML documents
  const isDoc = pathname === '/' || pathname.endsWith('.html') || !pathname.includes('.');
  if (!isDoc) {
    return await context.next();
  }

  // Read country header from Cloudflare Edge
  const country = context.request.headers.get('cf-ipcountry') || 'CH';

  const EU_COUNTRIES = [
    'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 
    'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 
    'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE'
  ];

  let currency = 'USD';
  if (country === 'CH') {
    currency = 'CHF';
  } else if (EU_COUNTRIES.includes(country)) {
    currency = 'EUR';
  }

  // Get current response
  const response = await context.next();
  
  // Clone response to make headers mutable
  const newResponse = new Response(response.body, response);

  // Set the currency cookie
  newResponse.headers.append('Set-Cookie', `wmc_current_currency=${currency}; Path=/; Max-Age=31536000; SameSite=Lax`);

  // Set language cookie if not set (German for CH/DE/AT, English for others)
  const cookieHeader = context.request.headers.get('Cookie') || '';
  if (!cookieHeader.includes('golfyr_lang=')) {
    const isGermanSpeaking = ['CH', 'DE', 'AT'].includes(country);
    const lang = isGermanSpeaking ? 'de' : 'en';
    newResponse.headers.append('Set-Cookie', `golfyr_lang=${lang}; Path=/; Max-Age=31536000; SameSite=Lax`);
  }

  return newResponse;
}
