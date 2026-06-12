module.exports = async (req, res) => {
  // Read country header (Cloudflare cf-ipcountry or Vercel x-vercel-ip-country)
  const country = req.headers['cf-ipcountry'] || req.headers['x-vercel-ip-country'] || 'CH';
  
  // List of EU country codes
  const EU_COUNTRIES = [
    'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 
    'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 
    'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE'
  ];

  // VAT rates by country
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
    vatRate = VAT_RATES[country] || 0.19; // default to 19% if somehow missing
    displayType = 'gross';
  } else {
    currency = 'USD';
    vatRate = 0;
    displayType = 'net';
  }

  // Support local development parameter overrides (e.g. ?test_country=DE)
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  const testCountry = url.searchParams.get('test_country');
  
  if (testCountry) {
    const uc = testCountry.toUpperCase();
    if (uc === 'CH') {
      return res.status(200).json({ country: 'CH', currency: 'CHF', vatRate: 0.081, displayType: 'gross' });
    } else if (EU_COUNTRIES.includes(uc)) {
      return res.status(200).json({ country: uc, currency: 'EUR', vatRate: VAT_RATES[uc] || 0.19, displayType: 'gross' });
    } else {
      return res.status(200).json({ country: uc, currency: 'USD', vatRate: 0, displayType: 'net' });
    }
  }

  return res.status(200).json({
    country,
    currency,
    vatRate,
    displayType
  });
};
