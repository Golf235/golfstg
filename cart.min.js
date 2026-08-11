 /**
 * Golfyr Persistent Cart & Stripe Checkout Integration
 */

(function() {
    // 1. Product Catalog with Stripe Price IDs (Placeholders for sandbox testing)
    const PRODUCT_CATALOG = {
        "cap": { id: "cap", name: "Golfyr Cap", price: 39, image: "./25.webp", priceId: "price_1PabcCapTest01" },
        "bucket-hat": { id: "bucket-hat", name: "Golfyr Bucket Hat", price: 49, image: "./3.webp", priceId: "price_1PabcHatTest02" },
        "tote-bag": { id: "tote-bag", name: "Golfyr Tote Bag", price: 21, image: "./7.webp", priceId: "price_1PabcToteTest03" },
        "tri-fold-towel": { id: "tri-fold-towel", name: "Golfyr Tri-Fold Towel", price: 21, image: "./5.webp", priceId: "price_1PabcTowelTest04" },
        "t-shirt": { id: "t-shirt", name: "Golfyr T-Shirt", price: 49, image: "./15.webp", priceId: "price_1PabcTshirtTest05" },
        "shirt": { id: "shirt", name: "Golfyr Shirt", price: 79, image: "./11.webp", priceId: "price_1PabcShirtTest06" },
        "short-sleeve-polo": { id: "short-sleeve-polo", name: "Golfyr Short-Sleeve Polo", price: 69, image: "./22.webp", priceId: "price_1PabcPoloTest07" },
        "maker": { id: "maker", name: "The Maker Putter", price: 890, image: "./maker-1.webp", priceId: "price_1PabcMakerTest08" },
        "maker-tour": { id: "maker-tour", name: "The Maker Tour Putter", price: 890, image: "./Maker Tour - Golfyr_files/39_Golfyr_Maker3_Tour_16457_V1_sRGB_300dpi-3.webp", priceId: "price_1PabcMakerTour09" },
        "configurator": { id: "configurator", name: "Custom Carbon Club Set", price: 890, image: "./maker_premier.webp", priceId: "price_1PabcConfigTest10" }
    };

    // 2. Hardcoded Fixed Price Matrices (Rule of Three: CHF, EUR, USD)
    const PRICE_MATRIX = {
        "cap": { CHF: 39, EUR: 39, USD: 39 },
        "bucket-hat": { CHF: 49, EUR: 49, USD: 49 },
        "tote-bag": { CHF: 21, EUR: 21, USD: 21 },
        "tri-fold-towel": { CHF: 21, EUR: 21, USD: 21 },
        "t-shirt": { CHF: 49, EUR: 49, USD: 49 },
        "shirt": { CHF: 79, EUR: 79, USD: 79 },
        "short-sleeve-polo": { CHF: 69, EUR: 69, USD: 69 },
        "maker": { CHF: 890, EUR: 890, USD: 890 },
        "maker-tour": { CHF: 1179, EUR: 1179, USD: 1179 },
        "configurator": { CHF: 5400, EUR: 5400, USD: 5400 } // base price for Premier Set
    };

    // 3. Location State Manager
    const LocationState = {
        get: function() {
            try {
                const data = sessionStorage.getItem('golfyr_location');
                return data ? JSON.parse(data) : null;
            } catch (e) {
                return null;
            }
        },
        save: function(data) {
            try {
                sessionStorage.setItem('golfyr_location', JSON.stringify(data));
            } catch (e) {}
        },
        detect: function(callback) {
            // Check if there is a test_country parameter in the URL
            const urlParams = new URLSearchParams(window.location.search);
            const testCountry = urlParams.get('test_country');
            const cacheKey = testCountry ? `golfyr_location_test_${testCountry}` : 'golfyr_location';
            
            try {
                const cached = sessionStorage.getItem(cacheKey);
                if (cached) {
                    const parsed = JSON.parse(cached);
                    this.save(parsed);
                    callback(parsed);
                    return;
                }
            } catch (e) {}

            const url = testCountry ? `/api/detect-location?test_country=${testCountry}` : '/api/detect-location';
            fetch(url)
                .then(res => {
                    if (!res.ok) throw new Error("API not available");
                    return res.json();
                })
                .then(data => {
                    try {
                        sessionStorage.setItem(cacheKey, JSON.stringify(data));
                    } catch (e) {}
                    this.save(data);
                    callback(data);
                })
                .catch(err => {
                    console.warn("Location detection API failed or not running. Using client-side detection/fallback:", err);
                    
                    let fallbackLoc = { country: 'CH', currency: 'CHF', vatRate: 0.081, displayType: 'gross' };
                    if (testCountry) {
                        const uc = testCountry.toUpperCase();
                        const EU_COUNTRIES = [
                            'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 
                            'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 
                            'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE'
                        ];
                        const VAT_RATES = {
                            'CH': 0.081, 'AT': 0.20, 'BE': 0.21, 'BG': 0.20, 'HR': 0.25, 'CY': 0.19,
                            'CZ': 0.21, 'DK': 0.25, 'EE': 0.22, 'FI': 0.24, 'FR': 0.20, 'DE': 0.19,
                            'GR': 0.24, 'HU': 0.27, 'IE': 0.23, 'IT': 0.22, 'LV': 0.21, 'LT': 0.21,
                            'LU': 0.17, 'MT': 0.18, 'NL': 0.21, 'PL': 0.23, 'PT': 0.23, 'RO': 0.19,
                            'SK': 0.20, 'SI': 0.22, 'ES': 0.21, 'SE': 0.25
                        };
                        
                        if (uc === 'CH') {
                            fallbackLoc = { country: 'CH', currency: 'CHF', vatRate: 0.081, displayType: 'gross' };
                        } else if (EU_COUNTRIES.includes(uc)) {
                            fallbackLoc = { country: uc, currency: 'EUR', vatRate: VAT_RATES[uc] || 0.19, displayType: 'gross' };
                        } else {
                            fallbackLoc = { country: uc, currency: 'USD', vatRate: 0, displayType: 'net' };
                        }
                    } else {
                        // Attempt to detect from browser locale timezone as a smart fallback if no API
                        try {
                            const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
                            if (tz.includes("Europe/Zurich")) {
                                fallbackLoc = { country: 'CH', currency: 'CHF', vatRate: 0.081, displayType: 'gross' };
                            } else if (tz.includes("Europe/")) {
                                fallbackLoc = { country: 'DE', currency: 'EUR', vatRate: 0.19, displayType: 'gross' };
                            } else {
                                fallbackLoc = { country: 'US', currency: 'USD', vatRate: 0, displayType: 'net' };
                            }
                        } catch (e) {}
                    }
                    
                    try {
                        sessionStorage.setItem(cacheKey, JSON.stringify(fallbackLoc));
                    } catch (e) {}
                    this.save(fallbackLoc);
                    callback(fallbackLoc);
                });
        }
    };

    // 4. Bilingual Translations for Cart Items and Selections
    const CART_TRANSLATIONS = {
        de: {
            // Product names
            "The Premier Set": "Das Premier Set",
            "The Maker Premier": "Der Maker Premier",
            "The Maker Tour": "Die Maker Tour",
            "Das Premier Set": "Das Premier Set",
            "Der Maker Premier": "Der Maker Premier",
            "Die Maker Tour": "Die Maker Tour",
            
            // Categories
            "Model": "Modell",
            "Length": "Länge",
            "Grip": "Griff",
            "Offset": "Offset",
            "Putter Grip": "Putter-Griff",
            "Putter Length": "Putter-Länge",
            "Putter Offset": "Offset",
            "Shaft Flex": "Flex",
            "Shaft Size": "Größe",
            "Grip Type": "Griff-Typ",
            "Grip Size": "Griff-Größe",
            "Bag": "Tasche",
            "Bag Tag": "Anhänger",

            // Values
            "Standbag White": "Stand Bag Weiß",
            "Standbag Grey": "Stand Bag Grau",
            "Cartbag White": "Cart Bag Weiß",
            "Cartbag Grey": "Cart Bag Grau",
            "Stand Bag White": "Stand Bag Weiß",
            "Stand Bag Grey": "Stand Bag Grau",
            "Cart Bag White": "Cart Bag Weiß",
            "Cart Bag Grey": "Cart Bag Grau",
            "Stiff": "Stiff",
            "Regular": "Regular",
            "Light": "Light",
            "Standard": "Standard",
            "Standard Light": "Standard Light",
            "Light short": "Light short",
            "Midsize": "Midsize",
            "Undersize": "Undersize",
            "Jumbo": "Jumbo",
            "The Maker": "The Maker",
            "The Maker Tour": "The Maker Tour",
            "Full-Shaft": "Full-Shaft",
            "Zero": "Kein",
            "Celeste": "Celeste",
            "Copper": "Copper",
            "Dark Maroon": "Dark Maroon",
            "Lavender": "Lavender",
            "Lilac": "Lilac"
        }
    };

    // 5. React Fiber tree option state extraction helpers
    function findConfiguratorFiber() {
        const rootEl = document.querySelector("#root > div") || document.getElementById("root");
        if (!rootEl) return null;
        
        const key = Object.keys(rootEl).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactContainer$'));
        if (!key) return null;
        
        let rootFiber = rootEl[key];
        let foundNode = null;
        
        function traverse(node) {
            if (!node || foundNode) return;
            
            if (node.memoizedState && typeof node.memoizedState === 'object' && 'memoizedState' in node.memoizedState) {
                let hook = node.memoizedState;
                let count = 0;
                let bagHook = null;
                let flexHook = null;
                while (hook && typeof hook === 'object' && 'memoizedState' in hook) {
                    if (count === 4) bagHook = hook;
                    if (count === 5) flexHook = hook;
                    count++;
                    hook = hook.next;
                }
                
                if (count >= 13 && 
                    bagHook && bagHook.memoizedState && typeof bagHook.memoizedState === 'object' && 
                    (bagHook.memoizedState.category === 'standbag' || bagHook.memoizedState.category === 'cartbag') &&
                    flexHook && flexHook.memoizedState && typeof flexHook.memoizedState === 'object' &&
                    ('id' in flexHook.memoizedState)) {
                    foundNode = node;
                    return;
                }
            }
            
            if (node.child) traverse(node.child);
            if (node.sibling) traverse(node.sibling);
        }
        
        traverse(rootFiber.current || rootFiber);
        return foundNode;
    }

    function findConfiguratorFiberFromEvent(target) {
        if (!target) return null;
        const key = Object.keys(target).find(k => k.startsWith('__reactFiber$'));
        if (!key) return null;
        
        let node = target[key];
        while (node) {
            if (node.memoizedState && typeof node.memoizedState === 'object' && 'memoizedState' in node.memoizedState) {
                let hook = node.memoizedState;
                let count = 0;
                let bagHook = null;
                let flexHook = null;
                while (hook && typeof hook === 'object' && 'memoizedState' in hook) {
                    if (count === 4) bagHook = hook;
                    if (count === 5) flexHook = hook;
                    count++;
                    hook = hook.next;
                }
                if (count >= 13 && 
                    bagHook && bagHook.memoizedState && typeof bagHook.memoizedState === 'object' && 
                    (bagHook.memoizedState.category === 'standbag' || bagHook.memoizedState.category === 'cartbag')) {
                    return node;
                }
            }
            node = node.return;
        }
        return null;
    }

    function getSelectionsFromFiber(target) {
        let node = findConfiguratorFiberFromEvent(target);
        if (!node) {
            node = findConfiguratorFiber();
        }
        if (!node) return null;
        
        let hook = node.memoizedState;
        const hooks = [];
        while (hook && typeof hook === 'object' && 'memoizedState' in hook) {
            hooks.push(hook.memoizedState);
            hook = hook.next;
        }
        
        const bag = hooks[4];
        const flex = hooks[5];
        const shaftSize = hooks[6];
        const gripSize = hooks[7];
        const putterLength = hooks[8];
        const gripType = hooks[9];
        const putter = hooks[10];
        const putterOffset = hooks[11];
        const bagTag = hooks[12];

        const cleanName = (obj) => {
            if (!obj || !obj.name) return null;
            return obj.name.split('(')[0].trim();
        };

        const selections = {};
        if (putter) selections["Putter Type"] = cleanName(putter);
        if (putterOffset) selections["Putter Offset"] = cleanName(putterOffset);
        if (putterLength) selections["Putter Length"] = cleanName(putterLength);
        if (flex) selections["Shaft Flex"] = cleanName(flex);
        if (shaftSize) selections["Shaft Size"] = cleanName(shaftSize);
        if (gripType) selections["Grip Type"] = cleanName(gripType);
        if (gripSize) selections["Grip Size"] = cleanName(gripSize);
        if (bag) selections["Bag"] = cleanName(bag);
        if (bagTag) selections["Bag Tag"] = cleanName(bagTag);

        return selections;
    }

    // 6. Edge/Client Cookie & Price formatting
    function setCurrencyCookie(currency) {
        document.cookie = `wmc_current_currency=${currency}; path=/; max-age=31536000`;
    }

    function updatePagePricesAndVAT(loc) {
        const currency = loc.currency;
        const displayType = loc.displayType;
        const country = loc.country;
        const vatRate = loc.vatRate;

        // 1. Update text nodes containing "CHF" dynamically
        const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
        let node;
        while (node = walker.nextNode()) {
            if (node.nodeValue.includes("CHF")) {
                node.nodeValue = node.nodeValue.replace(/CHF/g, currency);
            }
        }

        // 2. Update accessory product page pricing dynamically
        const pathname = window.location.pathname.toLowerCase();
        let currentProduct = null;
        if (pathname.includes("cap.html")) currentProduct = "cap";
        else if (pathname.includes("bucket-hat.html")) currentProduct = "bucket-hat";
        else if (pathname.includes("tote-bag.html")) currentProduct = "tote-bag";
        else if (pathname.includes("tri-fold-towel.html")) currentProduct = "tri-fold-towel";
        else if (pathname.includes("t-shirt.html")) currentProduct = "t-shirt";
        else if (pathname.includes("shirt.html")) currentProduct = "shirt";
        else if (pathname.includes("short-sleeve-polo.html")) currentProduct = "short-sleeve-polo";
        
        if (currentProduct && PRICE_MATRIX[currentProduct]) {
            const priceVal = PRICE_MATRIX[currentProduct][currency];
            
            const priceEl = document.getElementById("tote-price-value");
            if (priceEl) priceEl.textContent = priceVal;
            
            const summaryPriceEl = document.getElementById("summary-price-value");
            if (summaryPriceEl) summaryPriceEl.textContent = priceVal;
        }

        // 3. Update VAT labels (incl. / excl. tax)
        const vatLabels = document.querySelectorAll("[data-translate='nav-cart-suffix']");
        vatLabels.forEach(el => {
            if (displayType === 'gross') {
                const pct = (vatRate * 100).toFixed(1).replace('.0', '');
                el.textContent = ` (incl. ${pct}% VAT)`;
            } else {
                el.textContent = ` (excl. VAT)`;
            }
        });

        const inclVatLabels = Array.from(document.querySelectorAll("body *")).filter(el => {
            return el.children.length === 0 && el.textContent.includes("PRICE INCL. VAT");
        });
        inclVatLabels.forEach(el => {
            if (displayType === 'gross') {
                el.textContent = "PRICE INCL. VAT";
            } else {
                el.textContent = "PRICE EXCL. VAT";
            }
        });
    }

    // 7. LocalStorage Cart Manager
    const CartManager = {
        getCart: function() {
            try {
                const cartData = localStorage.getItem('golfyr_cart');
                return cartData ? JSON.parse(cartData) : [];
            } catch (e) {
                console.error("Failed to parse cart data:", e);
                return [];
            }
        },

        saveCart: function(cart) {
            localStorage.setItem('golfyr_cart', JSON.stringify(cart));
            this.updateWidget();
            this.renderDrawer();
        },

        getOptionsKey: function(options) {
            if (!options || Object.keys(options).length === 0) return "";
            const sorted = {};
            Object.keys(options).sort().forEach(k => {
                sorted[k] = options[k];
            });
            return JSON.stringify(sorted);
        },

        getProductPrice: function(productId, name, currency) {
            if (productId === "configurator" || productId === "maker" || productId === "maker-tour") {
                if (name && name.includes("Tour")) return PRICE_MATRIX["maker-tour"][currency];
                if (name && (name.includes("Premier Set") || name.includes("Das Premier Set"))) return PRICE_MATRIX["configurator"][currency];
                return PRICE_MATRIX["maker"][currency];
            }
            return PRICE_MATRIX[productId] ? PRICE_MATRIX[productId][currency] : (PRODUCT_CATALOG[productId] ? PRODUCT_CATALOG[productId].price : 0);
        },

        addItem: function(productId, quantity = 1, options = {}, nameOverride = null, priceOverride = null, imageOverride = null) {
            const product = PRODUCT_CATALOG[productId];
            if (!product) return;

            let cart = this.getCart();
            const optString = this.getOptionsKey(options);
            
            // Find if an item with the same product ID and same options already exists
            const existingItem = cart.find(item => item.id === productId && this.getOptionsKey(item.options) === optString);

            if (existingItem) {
                existingItem.quantity += quantity;
                if (nameOverride !== null) existingItem.name = nameOverride;
                if (imageOverride !== null) existingItem.image = imageOverride;
            } else {
                const cartItemId = optString ? `${productId}_${btoa(unescape(encodeURIComponent(optString))).replace(/=/g, "")}` : productId;
                cart.push({
                    cartItemId: cartItemId,
                    id: product.id,
                    name: nameOverride || product.name,
                    image: imageOverride || product.image,
                    priceId: product.priceId,
                    quantity: quantity,
                    options: options
                });
            }

            this.saveCart(cart);
        },

        updateQuantity: function(cartItemId, quantity) {
            let cart = this.getCart();
            const item = cart.find(item => item.cartItemId === cartItemId);
            if (item) {
                item.quantity = parseInt(quantity);
                if (item.quantity <= 0) {
                    cart = cart.filter(item => item.cartItemId !== cartItemId);
                }
                this.saveCart(cart);
            }
        },

        removeItem: function(cartItemId) {
            let cart = this.getCart();
            cart = cart.filter(item => item.cartItemId !== cartItemId);
            this.saveCart(cart);
        },

        clearCart: function() {
            this.saveCart([]);
        },

        getTotals: function() {
            const cart = this.getCart();
            const loc = LocationState.get() || { currency: 'CHF' };
            const cur = loc.currency;
            let count = 0;
            let total = 0;
            cart.forEach(item => {
                count += item.quantity;
                total += this.getProductPrice(item.id, item.name, cur) * item.quantity;
            });
            return { count, total };
        },

        updateWidget: function() {
            const { count, total } = this.getTotals();
            const loc = LocationState.get() || { currency: 'CHF' };
            const cur = loc.currency;
            
            // Update widget badge counts on page
            const badges = document.querySelectorAll(".cart-badge");
            badges.forEach(badge => {
                badge.textContent = count;
                badge.style.display = count > 0 ? "flex" : "none";
            });

            // Update price display text (e.g. "CHF 890")
            const priceWidgets = document.querySelectorAll(".cart-widget > span");
            priceWidgets.forEach(widget => {
                // Keep the suffix tag if present
                const suffix = widget.querySelector("[data-translate='nav-cart-suffix']") || widget.querySelector("span");
                let suffixText = "";
                if (suffix) {
                    suffix.style.display = count > 0 ? "inline" : "none";
                    suffixText = suffix.outerHTML;
                } else if (count > 0) {
                    suffixText = " (incl. tax)";
                }
                widget.innerHTML = `${cur} ${total.toLocaleString()}${suffixText}`;
            });
        },

        // Inject the drawer HTML if it doesn't exist
        initDrawerUI: function() {
            if (document.getElementById("cart-drawer-overlay")) return;

            const drawerHTML = `
                <div id="cart-drawer-overlay" class="cart-drawer-overlay"></div>
                <div id="cart-drawer" class="cart-drawer">
                    <div class="cart-drawer-header">
                        <h2>Shopping Cart</h2>
                        <button id="cart-drawer-close" class="cart-drawer-close" aria-label="Close Cart">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </button>
                    </div>
                    <div id="cart-drawer-items" class="cart-drawer-items">
                        <!-- Dynamic Cart Items -->
                    </div>
                    <div class="cart-drawer-footer">
                        <div class="cart-drawer-total">
                            <span>Total:</span>
                            <span id="cart-drawer-total-price">CHF 0</span>
                        </div>
                        <button id="cart-drawer-checkout" class="cart-drawer-checkout-btn">
                            <span class="checkout-spinner" id="checkout-spinner"></span>
                            <span>Proceed to Checkout</span>
                        </button>
                    </div>
                </div>
            `;

            const container = document.createElement("div");
            container.innerHTML = drawerHTML;
            document.body.appendChild(container);

            // Hook up close actions
            document.getElementById("cart-drawer-close").addEventListener("click", () => this.closeDrawer());
            document.getElementById("cart-drawer-overlay").addEventListener("click", () => this.closeDrawer());

            // Hook up checkout button
            document.getElementById("cart-drawer-checkout").addEventListener("click", () => this.checkout());
        },

        renderDrawer: function() {
            this.initDrawerUI();
            const itemsContainer = document.getElementById("cart-drawer-items");
            const cart = this.getCart();
            const loc = LocationState.get() || { currency: 'CHF' };
            const cur = loc.currency;

            if (cart.length === 0) {
                itemsContainer.innerHTML = `
                    <div class="cart-empty-message">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity: 0.3; margin-bottom: 16px; color: var(--text-primary);">
                            <circle cx="9" cy="21" r="1" fill="currentColor"/>
                            <circle cx="20" cy="21" r="1" fill="currentColor"/>
                            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        <p>Your cart is empty</p>
                    </div>
                `;
                document.getElementById("cart-drawer-checkout").disabled = true;
                document.getElementById("cart-drawer-total-price").textContent = `${cur} 0`;
                return;
            }

            document.getElementById("cart-drawer-checkout").disabled = false;
            let itemsHTML = "";
            const lang = localStorage.getItem('golfyr_lang') || 'en';

            cart.forEach(item => {
                // Translate name if there is a translation
                const displayName = lang === 'de' ? (CART_TRANSLATIONS.de[item.name] || item.name) : item.name;
                const price = this.getProductPrice(item.id, item.name, cur);
                
                // Build options list HTML
                let optionsHTML = "";
                if (item.options && Object.keys(item.options).length > 0) {
                    optionsHTML += `<div class="cart-item-options">`;
                    for (const [key, value] of Object.entries(item.options)) {
                        const displayKey = lang === 'de' ? (CART_TRANSLATIONS.de[key] || key) : key;
                        const displayVal = lang === 'de' ? (CART_TRANSLATIONS.de[value] || value) : value;
                        optionsHTML += `
                            <div class="cart-item-option">
                                <span class="option-label">${displayKey}:</span>
                                <span class="option-value">${displayVal}</span>
                            </div>
                        `;
                    }
                    optionsHTML += `</div>`;
                }

                itemsHTML += `
                    <div class="cart-item" data-id="${item.cartItemId}">
                        <img src="${item.image}" alt="${displayName}" class="cart-item-image">
                        <div class="cart-item-details">
                            <h3>${displayName}</h3>
                            ${optionsHTML}
                            <div class="cart-item-price">${cur} ${price}</div>
                            <div class="cart-item-actions">
                                <div class="cart-item-qty-selector">
                                    <button class="qty-btn dec-qty-btn" onclick="window.GolfyrCart.changeQuantity('${item.cartItemId}', -1)">-</button>
                                    <span class="qty-display">${item.quantity}</span>
                                    <button class="qty-btn inc-qty-btn" onclick="window.GolfyrCart.changeQuantity('${item.cartItemId}', 1)">+</button>
                                </div>
                                <button class="cart-item-remove" onclick="window.GolfyrCart.removeItem('${item.cartItemId}')">
                                    Remove
                                </button>
                            </div>
                        </div>
                    </div>
                `;
            });
            itemsContainer.innerHTML = itemsHTML;

            const { total } = this.getTotals();
            document.getElementById("cart-drawer-total-price").textContent = `${cur} ${total.toLocaleString()}`;
        },

        openDrawer: function() {
            this.renderDrawer();
            document.getElementById("cart-drawer-overlay").classList.add("active");
            document.getElementById("cart-drawer").classList.add("open");
            document.body.style.overflow = "hidden"; // Prevent background scroll
        },

        closeDrawer: function() {
            document.getElementById("cart-drawer-overlay").classList.remove("active");
            document.getElementById("cart-drawer").classList.remove("open");
            document.body.style.overflow = ""; // Re-enable background scroll
        },

        changeQuantity: function(cartItemId, delta) {
            const cart = this.getCart();
            const item = cart.find(item => item.cartItemId === cartItemId);
            if (item) {
                const newQty = item.quantity + delta;
                this.updateQuantity(cartItemId, newQty);
            }
        },

        checkout: function() {
            const checkoutBtn = document.getElementById("cart-drawer-checkout");
            const spinner = document.getElementById("checkout-spinner");
            
            checkoutBtn.disabled = true;
            spinner.style.display = "inline-block";
            
            const cart = this.getCart();
            const loc = LocationState.get() || { country: 'CH', currency: 'CHF', vatRate: 0.081, displayType: 'gross' };

            // Retrieve the active currency price for each item to pass to the backend
            const itemsWithPrices = cart.map(item => {
                return {
                    ...item,
                    price: this.getProductPrice(item.id, item.name, loc.currency)
                };
            });

            console.log("Initiating Stripe Checkout for:", itemsWithPrices, loc);

            // POST to our Serverless Function
            fetch("/api/create-checkout-session", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    items: itemsWithPrices,
                    currency: loc.currency,
                    country: loc.country,
                    vatRate: loc.vatRate,
                    displayType: loc.displayType
                })
            })
            .then(res => {
                if (res.ok) {
                    return res.json();
                }
                return res.text().then(text => {
                    let errMsg = "Checkout session creation failed.";
                    try {
                        const errData = JSON.parse(text);
                        errMsg = errData.error || errMsg;
                    } catch (e) {
                        errMsg = `Server returned HTTP ${res.status}: ${text.substring(0, 150)}...`;
                    }
                    throw new Error(errMsg);
                });
            })
            .then(data => {
                if (data.url) {
                    // Redirect directly to Stripe Checkout
                    window.location.href = data.url;
                } else {
                    throw new Error("Invalid checkout response");
                }
            })
            .catch(err => {
                console.error("Stripe Redirect Error:", err);
                
                setTimeout(() => {
                    spinner.style.display = "none";
                    checkoutBtn.disabled = false;
                    
                    alert(`[Stripe Redirect Error]\nError details: ${err.message || err}\n\n[Stripe Sandbox Simulation]\n\nRedirection failed. Stripe Dynamic price_data Payload:\n${JSON.stringify(itemsWithPrices.map(i => {
                        const netPrice = loc.displayType === 'gross' && loc.vatRate > 0 
                            ? i.price / (1 + parseFloat(loc.vatRate)) 
                            : i.price;
                        return {
                            name: i.name,
                            netPrice: parseFloat(netPrice.toFixed(2)),
                            quantity: i.quantity,
                            tax_behavior: 'exclusive',
                            tax_code: 'txcd_10000000',
                            options: i.options
                        };
                    }), null, 2)}\n\nRedirecting to Success Page...`);
                    
                    // Clear cart and redirect to home
                    localStorage.removeItem('golfyr_cart');
                    window.location.href = "index.html";
                }, 1000);
            });
        }
    };

    // Export globally
    window.GolfyrCart = CartManager;

    // Handle back-forward cache pageshow event to sync cart count when returning to pages
    window.addEventListener("pageshow", () => {
        CartManager.updateWidget();
        const loc = LocationState.get();
        if (loc) {
            updatePagePricesAndVAT(loc);
            CartManager.updateWidget();
        }
    });

    // 8. Document Load Hookups
    document.addEventListener("DOMContentLoaded", () => {
        // Fetch location, set cookie, update page prices & VAT, and render widgets
        LocationState.detect((loc) => {
            setCurrencyCookie(loc.currency);
            updatePagePricesAndVAT(loc);
            CartManager.updateWidget();
        });

        // Inject back button on product detail pages
        const imageColumn = document.querySelector(".tote-image-column");
        if (imageColumn) {
            const backBtn = document.createElement("a");
            backBtn.className = "product-back-btn";
            backBtn.href = "javascript:history.back()";
            backBtn.setAttribute("aria-label", "Go back");
            backBtn.innerHTML = `
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M15 18L9 12L15 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            `;
            imageColumn.insertBefore(backBtn, imageColumn.firstChild);
        }

        // Hook up Cart widget buttons in Header to open the drawer
        document.body.addEventListener("click", (e) => {
            const widget = e.target.closest(".cart-widget");
            if (widget) {
                e.preventDefault();
                CartManager.openDrawer();
            }
        });

        // 9. Page Detection & Add-To-Cart Overrides
        const pathname = window.location.pathname.toLowerCase();
        const cleanPath = pathname.replace(/\/$/, "");
        function isPage(name) {
            return cleanPath.endsWith("/" + name) || cleanPath.endsWith("/" + name + ".html");
        }

        let currentProduct = null;

        if (isPage("cap")) currentProduct = "cap";
        else if (isPage("bucket-hat")) currentProduct = "bucket-hat";
        else if (isPage("tote-bag")) currentProduct = "tote-bag";
        else if (isPage("tri-fold-towel")) currentProduct = "tri-fold-towel";
        else if (isPage("t-shirt")) currentProduct = "t-shirt";
        else if (isPage("shirt")) currentProduct = "shirt";
        else if (isPage("short-sleeve-polo")) currentProduct = "short-sleeve-polo";
        else if (isPage("maker")) currentProduct = "maker";
        else if (isPage("maker-tour")) currentProduct = "maker-tour";
        else if (isPage("configurator")) currentProduct = "configurator";

        if (currentProduct) {
            console.log(`Detected product page for: ${currentProduct}`);
            
            // Override the triggerAddToCart function globally on product pages
            window.triggerAddToCart = function() {
                const qtyElement = document.getElementById("tote-qty-display") || { textContent: "1" };
                const quantity = parseInt(qtyElement.textContent) || 1;

                const button = document.getElementById("add-to-cart-btn");
                const spinner = document.getElementById("cart-btn-spinner");
                const text = document.getElementById("cart-btn-text");

                if (button) button.disabled = true;
                if (spinner) spinner.style.display = "inline-block";
                if (text) text.textContent = "Adding...";

                setTimeout(() => {
                    if (spinner) spinner.style.display = "none";
                    if (text) text.textContent = "Added!";

                    // Add to our persistent cart!
                    CartManager.addItem(currentProduct, quantity);
                    
                    // Automatically pop out the cart drawer
                    CartManager.openDrawer();

                    // Pulse cart badge animation using GSAP if present
                    const badge = document.querySelector(".cart-badge");
                    if (badge && typeof gsap !== "undefined") {
                        gsap.fromTo(badge, 
                            { scale: 1 }, 
                            { scale: 1.3, duration: 0.15, yoyo: true, repeat: 1, ease: "power1.inOut" }
                        );
                    }

                    setTimeout(() => {
                        if (button) button.disabled = false;
                        if (text) {
                            const translateKey = text.getAttribute("data-translate");
                            text.textContent = translateKey ? (window.translations?.[window.currentLang]?.[translateKey] || "Add to Cart") : "Add to Cart";
                        }
                    }, 1500);

                }, 800);
            };
        }

        // 10. Configurator Button Click Interception
        if (isPage("configurator")) {
            document.addEventListener("click", (e) => {
                const btn = e.target.closest("button");
                if (!btn) return;
                const text = btn.textContent.trim().toLowerCase();
                if (text.includes("add to cart") || text.includes("in den warenkorb")) {
                    e.preventDefault();
                    console.log("Configurator Add to Cart intercepted during capture phase!");
                    
                    // Try to parse the price from the page
                    let priceVal = 890;
                    const elements = Array.from(document.querySelectorAll("body *")).filter(el => {
                        return el.children.length === 0 && el.textContent.includes("CHF");
                    });
                    if (elements.length > 0) {
                        const txt = elements[0].textContent;
                        const match = txt.replace(/[^\d]/g, "");
                        if (match) {
                            priceVal = parseInt(match);
                        }
                    }
                    
                    // Parse options from DOM & Fiber
                    let selections = getSelectionsFromFiber(e.target) || {};
                    
                    // Get model name from H1 title
                    const modelName = document.querySelector(".configurator-title")?.textContent.trim() || "Custom Carbon Club Set";
                    
                    // Get active image thumbnail from the configurator page
                    const mainImg = document.querySelector("#root main > div:first-child img");
                    const imageSrc = mainImg ? mainImg.getAttribute("src") : "./maker_premier.webp";
                    
                    // If it's a standalone Putter (The Maker Premier or The Maker Tour)
                    if (modelName.toLowerCase().includes("maker")) {
                        const filtered = {};
                        if (selections["Putter Length"]) filtered["Length"] = selections["Putter Length"];
                        if (selections["Grip Type"]) filtered["Grip"] = selections["Grip Type"];
                        if (selections["Putter Offset"]) filtered["Offset"] = selections["Putter Offset"];
                        selections = filtered;
                    } else {
                        const cleaned = {};
                        if (selections["Shaft Flex"]) cleaned["Shaft Flex"] = selections["Shaft Flex"];
                        if (selections["Shaft Size"]) cleaned["Shaft Size"] = selections["Shaft Size"];
                        if (selections["Grip Size"]) cleaned["Grip Size"] = selections["Grip Size"];
                        if (selections["Putter Length"]) cleaned["Putter Length"] = selections["Putter Length"];
                        if (selections["Grip Type"]) cleaned["Putter Grip"] = selections["Grip Type"];
                        if (selections["Putter Offset"]) cleaned["Putter Offset"] = selections["Putter Offset"];
                        if (selections["Bag"]) cleaned["Bag"] = selections["Bag"];
                        if (selections["Bag Tag"]) cleaned["Bag Tag"] = selections["Bag Tag"];
                        selections = cleaned;
                    }
                    
                    // Add configurator product to cart
                    CartManager.addItem("configurator", 1, selections, modelName, priceVal, imageSrc);
                    CartManager.openDrawer();
                }
            }, true);
        }
    });
})();
