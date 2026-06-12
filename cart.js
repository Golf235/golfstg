/**
 * Golfyr Persistent Cart & Stripe Checkout Integration
 */

(function() {
    // 1. Product Catalog with Stripe Price IDs (Placeholders for sandbox testing)
    const PRODUCT_CATALOG = {
        "cap": { id: "cap", name: "Golfyr Cap", price: 39, image: "./25.png", priceId: "price_1PabcCapTest01" },
        "bucket-hat": { id: "bucket-hat", name: "Golfyr Bucket Hat", price: 39, image: "./1.png", priceId: "price_1PabcHatTest02" },
        "tote-bag": { id: "tote-bag", name: "Golfyr Tote Bag", price: 49, image: "./tote_bag.png", priceId: "price_1PabcToteTest03" },
        "tri-fold-towel": { id: "tri-fold-towel", name: "Golfyr Tri-Fold Towel", price: 29, image: "./towel_folded.jpg", priceId: "price_1PabcTowelTest04" },
        "t-shirt": { id: "t-shirt", name: "Golfyr T-Shirt", price: 59, image: "./2.png", priceId: "price_1PabcTshirtTest05" },
        "shirt": { id: "shirt", name: "Golfyr Shirt", price: 79, image: "./7.png", priceId: "price_1PabcShirtTest06" },
        "short-sleeve-polo": { id: "short-sleeve-polo", name: "Golfyr Short-Sleeve Polo", price: 69, image: "./22.png", priceId: "price_1PabcPoloTest07" },
        "maker": { id: "maker", name: "The Maker Putter", price: 890, image: "./maker-1.png", priceId: "price_1PabcMakerTest08" },
        "maker-tour": { id: "maker-tour", name: "The Maker Tour Putter", price: 890, image: "./Maker Tour - Golfyr_files/39_Golfyr_Maker3_Tour_16457_V1_sRGB_300dpi-3.png", priceId: "price_1PabcMakerTour09" },
        "configurator": { id: "configurator", name: "Custom Carbon Club Set", price: 890, image: "./maker_premier.png", priceId: "price_1PabcConfigTest10" }
    };

    // 2. Bilingual Translations for Cart Items and Selections
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

    // 3. React Fiber tree option state extraction helpers
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

    // 4. LocalStorage Cart Manager
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

        addItem: function(productId, quantity = 1, options = {}, nameOverride = null, priceOverride = null, imageOverride = null) {
            const product = PRODUCT_CATALOG[productId];
            if (!product) return;

            let cart = this.getCart();
            const optString = this.getOptionsKey(options);
            
            // Find if an item with the same product ID and same options already exists
            const existingItem = cart.find(item => item.id === productId && this.getOptionsKey(item.options) === optString);

            if (existingItem) {
                existingItem.quantity += quantity;
                if (priceOverride !== null) existingItem.price = priceOverride;
                if (nameOverride !== null) existingItem.name = nameOverride;
                if (imageOverride !== null) existingItem.image = imageOverride;
            } else {
                // Generate a unique ID for the cart row
                const cartItemId = optString ? `${productId}_${btoa(unescape(encodeURIComponent(optString))).replace(/=/g, "")}` : productId;
                cart.push({
                    cartItemId: cartItemId,
                    id: product.id,
                    name: nameOverride || product.name,
                    price: priceOverride || product.price,
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
            let count = 0;
            let total = 0;
            cart.forEach(item => {
                count += item.quantity;
                total += item.price * item.quantity;
            });
            return { count, total };
        },

        updateWidget: function() {
            const { count, total } = this.getTotals();
            
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
                const suffixText = suffix ? suffix.outerHTML : " (incl. tax)";
                widget.innerHTML = `CHF ${total.toLocaleString()}${suffixText}`;
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
                document.getElementById("cart-drawer-total-price").textContent = "CHF 0";
                return;
            }

            document.getElementById("cart-drawer-checkout").disabled = false;
            let itemsHTML = "";
            const lang = localStorage.getItem('golfyr_lang') || 'en';

            cart.forEach(item => {
                // Translate name if there is a translation
                const displayName = lang === 'de' ? (CART_TRANSLATIONS.de[item.name] || item.name) : item.name;
                
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
                            <div class="cart-item-price">CHF ${item.price}</div>
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
            document.getElementById("cart-drawer-total-price").textContent = `CHF ${total.toLocaleString()}`;
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

            console.log("Initiating Stripe Checkout for:", cart);

            // POST to our Serverless Function
            fetch("/api/create-checkout-session", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ items: cart })
            })
            .then(res => {
                if (res.ok) {
                    return res.json();
                }
                throw new Error("Checkout session creation failed.");
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
                
                // Fallback Mode: For testing without a serverless backend
                setTimeout(() => {
                    spinner.style.display = "none";
                    checkoutBtn.disabled = false;
                    
                    alert(`[Stripe Sandbox Simulation]\n\nRedirection failed because serverless functions require local backend hosting (vercel dev).\n\nStripe Dynamic price_data Payload:\n${JSON.stringify(cart.map(i => ({
                        name: i.name,
                        price: i.price,
                        quantity: i.quantity,
                        options: i.options
                    })), null, 2)}\n\nRedirecting to Success Page...`);
                    
                    // Clear cart and redirect to home
                    localStorage.removeItem('golfyr_cart');
                    window.location.href = "index.html";
                }, 1000);
            });
        }
    };

    // Export globally
    window.GolfyrCart = CartManager;

    // 5. Document Load Hookups
    document.addEventListener("DOMContentLoaded", () => {
        // Init widget numbers
        CartManager.updateWidget();

        // Hook up Cart widget buttons in Header to open the drawer
        document.body.addEventListener("click", (e) => {
            const widget = e.target.closest(".cart-widget");
            if (widget) {
                e.preventDefault();
                CartManager.openDrawer();
            }
        });

        // 6. Page Detection & Add-To-Cart Overrides
        const pathname = window.location.pathname.toLowerCase();
        let currentProduct = null;

        if (pathname.includes("cap.html")) currentProduct = "cap";
        else if (pathname.includes("bucket-hat.html")) currentProduct = "bucket-hat";
        else if (pathname.includes("tote-bag.html")) currentProduct = "tote-bag";
        else if (pathname.includes("tri-fold-towel.html")) currentProduct = "tri-fold-towel";
        else if (pathname.includes("t-shirt.html")) currentProduct = "t-shirt";
        else if (pathname.includes("shirt.html")) currentProduct = "shirt";
        else if (pathname.includes("short-sleeve-polo.html")) currentProduct = "short-sleeve-polo";
        else if (pathname.includes("maker.html") && !pathname.includes("maker-tour.html")) currentProduct = "maker";
        else if (pathname.includes("maker-tour.html")) currentProduct = "maker-tour";
        else if (pathname.includes("configurator.html")) currentProduct = "configurator";

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
                            // Reset text translation dynamically
                            const translateKey = text.getAttribute("data-translate");
                            text.textContent = translateKey ? (window.translations?.[window.currentLang]?.[translateKey] || "Add to Cart") : "Add to Cart";
                        }
                    }, 1500);

                }, 800);
            };
        }

        // 7. Configurator Button Click Interception
        if (pathname.includes("configurator.html")) {
            // Listen in the capture phase (true) to intercept before React can stop propagation
            document.addEventListener("click", (e) => {
                const btn = e.target.closest("button");
                if (!btn) return;
                const text = btn.textContent.trim().toLowerCase();
                if (text.includes("add to cart") || text.includes("in den warenkorb")) {
                    e.preventDefault();
                    console.log("Configurator Add to Cart intercepted during capture phase!");
                    
                    // Try to parse the price from the page
                    let priceVal = 890;
                    // Find elements containing 'CHF'
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
                    const imageSrc = mainImg ? mainImg.getAttribute("src") : "./maker_premier.png";
                    
                    // If it's a standalone Putter (The Maker Premier or The Maker Tour)
                    if (modelName.toLowerCase().includes("maker")) {
                        const filtered = {};
                        if (selections["Putter Length"]) filtered["Length"] = selections["Putter Length"];
                        if (selections["Grip Type"]) filtered["Grip"] = selections["Grip Type"];
                        if (selections["Putter Offset"]) filtered["Offset"] = selections["Putter Offset"];
                        selections = filtered;
                    } else {
                        // For the Premier Set, keep and rename options to be clean
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
