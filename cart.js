(function() {
    // 1. Hardcoded Product Catalog
    const PRODUCT_CATALOG = {
        "cap": { id: "cap", name: "Golfyr Club Cap", price: 39, image: "./25.webp", priceId: "price_1PabcCapTest01" },
        "bucket-hat": { id: "bucket-hat", name: "Golfyr Bucket Hat", price: 49, image: "./3.webp", priceId: "price_1PabcBucketTest02" },
        "tote-bag": { id: "tote-bag", name: "The 7>14 Tote Bag", price: 21, image: "./tote_bag.webp", priceId: "price_1PabcToteTest03" },
        "tri-fold-towel": { id: "tri-fold-towel", name: "Golfyr Tri-Fold Towel", price: 21, image: "./5.webp", priceId: "price_1PabcTowelTest04" },
        "t-shirt": { id: "t-shirt", name: "Golfyr T-Shirt", price: 49, image: "./15.webp", priceId: "price_1PabcTshirtTest05" },
        "shirt": { id: "shirt", name: "Golfyr Shirt", price: 79, image: "./11.webp", priceId: "price_1PabcShirtTest06" },
        "short-sleeve-polo": { id: "short-sleeve-polo", name: "Golfyr Short Sleeve Polo", price: 69, image: "./22.webp", priceId: "price_1PabcPoloTest07" },
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
        set: function(state) {
            try {
                sessionStorage.setItem('golfyr_location', JSON.stringify(state));
            } catch (e) {}
        },
        detect: function(callback) {
            const cached = this.get();
            if (cached) {
                if (callback) callback(cached);
                return;
            }

            // Fallback default state
            const fallback = { country: 'CH', currency: 'CHF', vatRate: 0.081, displayType: 'gross' };

            // Request location info from Cloudflare trace or geolocation API
            fetch("https://1.1.1.1/cdn-cgi/trace")
                .then(res => res.text())
                .then(text => {
                    const lines = text.split("\n");
                    let countryCode = "CH"; // default fallback
                    for (const line of lines) {
                        if (line.startsWith("loc=")) {
                            countryCode = line.split("=")[1].toUpperCase();
                            break;
                        }
                    }
                    
                    // Determine currency, VAT rate, and display mode based on country
                    let currency = "CHF";
                    let vatRate = 0.081; // Swiss standard VAT rate (8.1%)
                    let displayType = "gross"; // gross pricing (VAT incl.) for B2C

                    const euCountries = [
                        'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 
                        'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 
                        'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE'
                    ];

                    if (euCountries.includes(countryCode)) {
                        currency = "EUR";
                        // Set standard EU VAT rate mappings
                        const vatRates = {
                            DE: 0.19, FR: 0.20, IT: 0.22, ES: 0.21, NL: 0.21, AT: 0.20, BE: 0.21
                        };
                        vatRate = vatRates[countryCode] || 0.20; // fallback to 20% standard VAT
                    } else if (countryCode === "US") {
                        currency = "USD";
                        vatRate = 0.0; // Sales tax calculated at checkout
                        displayType = "net"; // Net pricing (excluding taxes)
                    } else if (countryCode === "GB") {
                        currency = "GBP";
                        vatRate = 0.20; // UK VAT rate (20%)
                    }

                    const state = { country: countryCode, currency, vatRate, displayType };
                    this.set(state);
                    if (callback) callback(state);
                })
                .catch(() => {
                    this.set(fallback);
                    if (callback) callback(fallback);
                });
        }
    };

    // 4. Cart Logic Manager
    const CartManager = {
        getCart: function() {
            try {
                const data = localStorage.getItem('golfyr_cart');
                return data ? JSON.parse(data) : [];
            } catch (e) {
                return [];
            }
        },

        saveCart: function(cart) {
            try {
                localStorage.setItem('golfyr_cart', JSON.stringify(cart));
            } catch (e) {}
            this.updateWidget();
        },

        getOptionsKey: function(options) {
            if (!options) return "";
            const keys = Object.keys(options).sort();
            const sorted = {};
            keys.forEach(k => {
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
            const item = cart.find(i => i.cartItemId === cartItemId);
            if (item) {
                item.quantity = Math.max(1, quantity);
                this.saveCart(cart);
            }
        },

        removeItem: function(cartItemId) {
            let cart = this.getCart();
            cart = cart.filter(i => i.cartItemId !== cartItemId);
            this.saveCart(cart);
        },

        getCartTotal: function(currency) {
            const cart = this.getCart();
            const cur = currency || (LocationState.get() ? LocationState.get().currency : 'CHF');
            let total = 0;
            cart.forEach(item => {
                total += this.getProductPrice(item.id, item.name, cur) * item.quantity;
            });
            return total;
        },

        getCartCount: function() {
            const cart = this.getCart();
            let count = 0;
            cart.forEach(item => {
                count += item.quantity;
            });
            return count;
        },

        // Redraw cart badge counter in Header, and the cart list items in the drawer
        updateWidget: function() {
            const count = this.getCartCount();
            const badges = document.querySelectorAll(".cart-badge");
            badges.forEach(b => {
                b.textContent = count;
                b.style.display = count > 0 ? "flex" : "none";
            });

            // Build dynamic list inside the Drawer body
            const cartList = document.querySelector(".cart-list");
            if (!cartList) return;

            const cart = this.getCart();
            const loc = LocationState.get() || { country: 'CH', currency: 'CHF', vatRate: 0.081, displayType: 'gross' };
            const cur = loc.currency;

            if (cart.length === 0) {
                cartList.innerHTML = `
                    <div class="cart-empty-state">
                        <p data-translate="cart-empty">Ihr Warenkorb ist leer.</p>
                        <a href="shop.html" class="btn btn-dark" data-translate="cart-back-shop" style="margin-top: 20px;">Zurück zum Shop</a>
                    </div>
                `;
                
                // Hide footer total & checkout elements when cart is empty
                const footer = document.querySelector(".cart-drawer-footer");
                if (footer) footer.style.display = "none";
                
                // Translate the empty state nodes
                if (window.translateDOM) {
                    window.translateDOM(window.currentLanguage || 'en');
                }
                return;
            }

            // Show footer total section when items exist
            const footer = document.querySelector(".cart-drawer-footer");
            if (footer) footer.style.display = "block";

            let html = "";
            cart.forEach(item => {
                const price = this.getProductPrice(item.id, item.name, cur);
                const itemTotal = price * item.quantity;

                // Render option detail badges if they exist
                let optionsHtml = "";
                if (item.options && Object.keys(item.options).length > 0) {
                    optionsHtml = `<div class="cart-item-options">`;
                    for (const [key, val] of Object.entries(item.options)) {
                        optionsHtml += `<span class="cart-option-badge">${key}: ${val}</span>`;
                    }
                    optionsHtml += `</div>`;
                }

                html += `
                    <div class="cart-item" data-id="${item.cartItemId}">
                        <div class="cart-item-image">
                            <img src="${item.image}" alt="${item.name}">
                        </div>
                        <div class="cart-item-details">
                            <div class="cart-item-header">
                                <h4 class="cart-item-name">${item.name}</h4>
                                <button class="cart-item-remove" data-id="${item.cartItemId}">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    </svg>
                                </button>
                            </div>
                            ${optionsHtml}
                            <div class="cart-item-price-row">
                                <div class="quantity-selector">
                                    <button class="qty-btn minus" data-id="${item.cartItemId}">-</button>
                                    <span class="qty-val">${item.quantity}</span>
                                    <button class="qty-btn plus" data-id="${item.cartItemId}">+</button>
                                </div>
                                <span class="cart-item-price">${formatPrice(itemTotal, cur)}</span>
                            </div>
                        </div>
                    </div>
                `;
            });

            cartList.innerHTML = html;

            // Draw VAT Tax breakdown information
            const subtotalVal = document.querySelector(".subtotal-val");
            const taxVal = document.querySelector(".tax-val");
            const totalVal = document.querySelector(".total-val");
            const vatInfo = document.querySelector(".vat-info");

            const total = this.getCartTotal(cur);
            const rate = parseFloat(loc.vatRate);
            
            let subtotal = total;
            let tax = 0;

            if (loc.displayType === "gross" && rate > 0) {
                // VAT is already included in prices (gross)
                subtotal = total / (1 + rate);
                tax = total - subtotal;
            } else if (rate > 0) {
                // VAT is excluded from catalog pricing (net)
                subtotal = total;
                tax = total * rate;
            }

            if (subtotalVal) subtotalVal.textContent = formatPrice(subtotal, cur);
            if (taxVal) taxVal.textContent = formatPrice(tax, cur);
            if (totalVal) totalVal.textContent = formatPrice(subtotal + tax, cur);
            
            if (vatInfo) {
                const label = loc.displayType === "gross" ? "incl." : "excl.";
                vatInfo.textContent = `(${label} ${loc.country} VAT/MwSt. ${(rate * 100).toFixed(1)}%)`;
            }

            // Hook up events on newly created quantity/remove buttons
            cartList.querySelectorAll(".qty-btn.minus").forEach(b => {
                b.addEventListener("click", () => {
                    const id = b.getAttribute("data-id");
                    const item = cart.find(i => i.cartItemId === id);
                    if (item) this.updateQuantity(id, item.quantity - 1);
                });
            });

            cartList.querySelectorAll(".qty-btn.plus").forEach(b => {
                b.addEventListener("click", () => {
                    const id = b.getAttribute("data-id");
                    const item = cart.find(i => i.cartItemId === id);
                    if (item) this.updateQuantity(id, item.quantity + 1);
                });
            });

            cartList.querySelectorAll(".cart-item-remove").forEach(b => {
                b.addEventListener("click", () => {
                    const id = b.getAttribute("data-id");
                    this.removeItem(id);
                });
            });

            // Translate newly loaded items inside the drawer
            if (window.translateDOM) {
                window.translateDOM(window.currentLanguage || 'en');
            }
        },

        checkout: function() {
            const checkoutBtn = document.querySelector(".btn-checkout");
            const spinner = document.querySelector(".checkout-spinner");
            if (checkoutBtn) checkoutBtn.disabled = true;
            if (spinner) spinner.style.display = "inline-block";

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
                    displayType: loc.displayType,
                    cancelUrl: window.location.href
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

    // Helper Utility: format prices nicely based on active currency
    function formatPrice(amount, currency) {
        const cur = currency || "CHF";
        if (cur === "CHF") {
            return amount.toLocaleString("de-CH", { style: "currency", currency: "CHF" });
        } else if (cur === "EUR") {
            return amount.toLocaleString("de-DE", { style: "currency", currency: "EUR" });
        } else {
            return amount.toLocaleString("en-US", { style: "currency", currency: "USD" });
        }
    }

    // Helper Utility: set cookie for language & currency
    function setCurrencyCookie(val) {
        document.cookie = `wmc_current_currency=${val}; Path=/; Max-Age=31536000; SameSite=Lax`;
    }

    // Dynamic price updates across catalog pages based on LocationState
    function updatePagePricesAndVAT(loc) {
        const cur = loc.currency;
        const rate = parseFloat(loc.vatRate);
        const isGross = loc.displayType === "gross";

        // Update single-item prices dynamically
        document.querySelectorAll("[data-product-price]").forEach(el => {
            const productId = el.getAttribute("data-product-price");
            // If the element has a name attribute or option, resolve pricing accordingly
            const name = el.getAttribute("data-product-name") || "";
            const basePrice = CartManager.getProductPrice(productId, name, cur);
            if (basePrice > 0) {
                el.textContent = formatPrice(basePrice, cur);
            }
        });

        // Update VAT breakdown labels across catalog pages
        document.querySelectorAll("[data-vat-rate]").forEach(el => {
            el.textContent = `${(rate * 100).toFixed(1)}%`;
        });
        document.querySelectorAll("[data-vat-behavior]").forEach(el => {
            el.textContent = isGross ? "inkl." : "exkl.";
        });
        document.querySelectorAll("[data-vat-currency]").forEach(el => {
            el.textContent = cur;
        });
    }

    // 5. Drawer UI Initialization & Page Event Handlers
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
            backBtn.href = "shop.html#accessories";
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
                e.stopPropagation();
                const drawer = document.querySelector(".cart-drawer");
                const overlay = document.querySelector(".cart-drawer-overlay");
                if (drawer && overlay) {
                    drawer.classList.add("active");
                    overlay.classList.add("active");
                    document.body.style.overflow = "hidden"; // lock page scroll
                }
            }
        });

        // Hook up Cart Drawer Close button
        const closeBtn = document.querySelector(".cart-drawer-close");
        if (closeBtn) {
            closeBtn.addEventListener("click", () => {
                const drawer = document.querySelector(".cart-drawer");
                const overlay = document.querySelector(".cart-drawer-overlay");
                if (drawer && overlay) {
                    drawer.classList.remove("active");
                    overlay.classList.remove("active");
                    document.body.style.overflow = ""; // restore page scroll
                }
            });
        }

        // Hook up Cart Drawer Overlay (click outside to close)
        const overlay = document.querySelector(".cart-drawer-overlay");
        if (overlay) {
            overlay.addEventListener("click", () => {
                const drawer = document.querySelector(".cart-drawer");
                if (drawer) {
                    drawer.classList.remove("active");
                    overlay.classList.remove("active");
                    document.body.style.overflow = "";
                }
            });
        }

        // Hook up Add to Cart Button in product detail pages
        document.body.addEventListener("click", (e) => {
            const addBtn = e.target.closest("[data-add-to-cart]");
            if (addBtn) {
                e.preventDefault();
                e.stopPropagation();
                
                const productId = addBtn.getAttribute("data-add-to-cart");
                const qtyVal = document.querySelector(".quantity-selector .qty-val");
                const qty = qtyVal ? parseInt(qtyVal.textContent) || 1 : 1;

                // Capture options if they are selected on the page
                const options = {};
                
                // 1. Color options
                const colorEl = document.querySelector(".color-option.active");
                if (colorEl) options["Color"] = colorEl.getAttribute("data-color-name") || colorEl.textContent.trim();
                
                // 2. Size options (e.g. Shirts/Apparel sizes)
                const sizeEl = document.querySelector(".size-selector button.active");
                if (sizeEl) options["Size"] = sizeEl.textContent.trim();

                // Add to Cart
                CartManager.addItem(productId, qty, options);

                // Auto-open the cart drawer to show insertion
                const drawer = document.querySelector(".cart-drawer");
                const overlay = document.querySelector(".cart-drawer-overlay");
                if (drawer && overlay) {
                    drawer.classList.add("active");
                    overlay.classList.add("active");
                    document.body.style.overflow = "hidden";
                }
            }
        });

        // Hook up Checkout Button
        const checkoutBtn = document.querySelector(".btn-checkout");
        if (checkoutBtn) {
            checkoutBtn.addEventListener("click", (e) => {
                e.preventDefault();
                e.stopPropagation();
                CartManager.checkout();
            });
        }
    });

    // Make Cart API publicly available globally
    window.CartAPI = CartManager;
})();
