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

    // 2. LocalStorage Cart Manager
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

        addItem: function(productId, quantity = 1, options = {}) {
            const product = PRODUCT_CATALOG[productId];
            if (!product) return;

            let cart = this.getCart();
            const existingItem = cart.find(item => item.id === productId);

            if (existingItem) {
                existingItem.quantity += quantity;
            } else {
                cart.push({
                    id: product.id,
                    name: product.name,
                    price: product.price,
                    image: product.image,
                    priceId: product.priceId,
                    quantity: quantity,
                    options: options
                });
            }

            this.saveCart(cart);
        },

        updateQuantity: function(productId, quantity) {
            let cart = this.getCart();
            const item = cart.find(item => item.id === productId);
            if (item) {
                item.quantity = parseInt(quantity);
                if (item.quantity <= 0) {
                    cart = cart.filter(item => item.id !== productId);
                }
                this.saveCart(cart);
            }
        },

        removeItem: function(productId) {
            let cart = this.getCart();
            cart = cart.filter(item => item.id !== productId);
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
            const priceWidgets = document.querySelectorAll(".cart-widget span");
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
            cart.forEach(item => {
                itemsHTML += `
                    <div class="cart-item" data-id="${item.id}">
                        <img src="${item.image}" alt="${item.name}" class="cart-item-image">
                        <div class="cart-item-details">
                            <h3>${item.name}</h3>
                            <div class="cart-item-price">CHF ${item.price}</div>
                            <div class="cart-item-actions">
                                <div class="cart-item-qty-selector">
                                    <button class="qty-btn dec-qty-btn" onclick="window.GolfyrCart.changeQuantity('${item.id}', -1)">-</button>
                                    <span class="qty-display">${item.quantity}</span>
                                    <button class="qty-btn inc-qty-btn" onclick="window.GolfyrCart.changeQuantity('${item.id}', 1)">+</button>
                                </div>
                                <button class="cart-item-remove" onclick="window.GolfyrCart.removeItem('${item.id}')">
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

        changeQuantity: function(productId, delta) {
            const cart = this.getCart();
            const item = cart.find(item => item.id === productId);
            if (item) {
                const newQty = item.quantity + delta;
                this.updateQuantity(productId, newQty);
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
                    
                    // Show a styled modal informing the user of the payload that would be sent to Stripe
                    alert(`[Stripe Sandbox Simulation]\\n\\nRedirection failed because serverless functions require local backend hosting (vercel dev).\\n\\nStripe Line Items Payload:\\n${JSON.stringify(cart.map(i => ({ price_id: i.priceId, quantity: i.quantity })), null, 2)}\\n\\nRedirecting to Success Page...`);
                    
                    // Clear cart and redirect to home
                    localStorage.removeItem('golfyr_cart');
                    window.location.href = "index.html";
                }, 1000);
            });
        }
    };

    // Export globally
    window.GolfyrCart = CartManager;

    // 3. Document Load Hookups
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

        // 4. Page Detection & Add-To-Cart Overrides
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

        // 5. Configurator Button Click Interception
        if (pathname.includes("configurator.html")) {
            document.addEventListener("click", (e) => {
                const btn = e.target.closest("button");
                if (!btn) return;
                const text = btn.textContent.trim().toLowerCase();
                if (text === "add to cart" || text === "in den warenkorb") {
                    e.preventDefault();
                    console.log("Configurator Add to Cart intercepted!");
                    
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
                    
                    // Add configurator product to cart
                    CartManager.addItem("configurator", 1);
                    CartManager.openDrawer();
                }
            });
        }
    });
})();
