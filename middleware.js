import { NextResponse } from 'next/server';

export function middleware(request) {
  const response = NextResponse.next();
  
  // Detect country from headers (Cloudflare CF-IPCountry or Vercel x-vercel-ip-country)
  const country = request.headers.get('cf-ipcountry') || request.headers.get('x-vercel-ip-country') || 'CH';
  
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
  } else {
    currency = 'USD';
  }

  // Set the currency cookie that the configurator reads
  response.cookies.set('wmc_current_currency', currency, { path: '/' });
  
  // Set language cookie if not already set (German for CH/DE/AT, English for others)
  const currentLang = request.cookies.get('golfyr_lang')?.value;
  if (!currentLang) {
    const isGermanSpeaking = ['CH', 'DE', 'AT'].includes(country);
    response.cookies.set('golfyr_lang', isGermanSpeaking ? 'de' : 'en', { path: '/' });
  }

  return response;
}
