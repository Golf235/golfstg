export async function onRequest(context) {
  const request = context.request;
  const url = new URL(request.url);
  
  // Read country header
  let country = request.headers.get('cf-ipcountry') || 'CH';
  
  // Support local development parameter overrides (e.g. ?test_country=DE)
  const testCountry = url.searchParams.get('test_country');
  if (testCountry) {
    country = testCountry.toUpperCase();
  }
  
  const EU_COUNTRIES = [
    'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 
    'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 
    'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE'
  ];

  const VAT_RATES = {
    'CH': 0.081,
    'AT': 0.20, 'BE': 0.21, 'BG': 0.20, 'HR': 0.25, 'CY': 0.19,
    'CZ': 0.21, 'DK': 0.25, 'EE': 0.22, 'FI': 0.24, 'FR': 0.20,
    'DE': 0.19, 'GR': 0.24, 'HU': 0.27, 'IE': 0.23, 'IT': 0.22,
    'LV': 0.21, 'LT': 0.21, 'LU': 0.17, 'MT': 0.18, 'NL': 0.21,
    'PL': 0.23, 'PT': 0.23, 'RO': 0.19, 'SK': 0.20, 'SI': 0.22,
    'ES': 0.21, 'SE': 0.25
  };

  let currency = 'USD';
  let vatRate = 0;
  let displayType = 'net';

  if (country === 'CH') {
    currency = 'CHF';
    vatRate = 0.081;
    displayType = 'gross';
  } else if (EU_COUNTRIES.includes(country)) {
    currency = 'EUR';
    vatRate = VAT_RATES[country] || 0.19;
    displayType = 'gross';
  } else {
    currency = 'USD';
    vatRate = 0;
    displayType = 'net';
  }

  const payload = {
    country,
    currency,
    vatRate,
    displayType
  };

  return new Response(JSON.stringify(payload), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}
