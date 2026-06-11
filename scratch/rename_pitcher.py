with open("pitcher.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Title
html = html.replace("<title>The Riser - Golfyr</title>", "<title>The Pitcher - Golfyr</title>")

# 2. Rename classes (intro, why, where, for-who)
html = html.replace("riser-intro", "pitcher-intro")
html = html.replace("riser-why", "pitcher-why")
html = html.replace("riser-where", "pitcher-where")
html = html.replace("riser-for-who", "pitcher-for-who")

# 3. Rename CSS override class selectors
html = html.replace(".riser-intro", ".pitcher-intro")
html = html.replace(".riser-why-section", ".pitcher-why-section")
html = html.replace(".riser-where-section", ".pitcher-where-section")
html = html.replace(".riser-for-who", ".pitcher-for-who")

# 4. Translations namespaces
html = html.replace('data-translate="riser-hero-title"', 'data-translate="pitcher-hero-title"')
html = html.replace('data-translate="riser-hero-buy-btn"', 'data-translate="pitcher-hero-buy-btn"')
html = html.replace('data-translate="riser-hero-config-btn"', 'data-translate="pitcher-hero-config-btn"')
html = html.replace('data-translate="riser-intro-title"', 'data-translate="pitcher-intro-title"')
html = html.replace('data-translate="riser-intro-body"', 'data-translate="pitcher-intro-body"')
html = html.replace('data-translate="riser-why-title"', 'data-translate="pitcher-why-title"')
html = html.replace('data-translate="riser-why-tab1"', 'data-translate="pitcher-why-tab1"')
html = html.replace('data-translate="riser-why-desc1"', 'data-translate="pitcher-why-desc1"')
html = html.replace('data-translate="riser-why-tab2"', 'data-translate="pitcher-why-tab2"')
html = html.replace('data-translate="riser-why-desc2"', 'data-translate="pitcher-why-desc2"')
html = html.replace('data-translate="riser-why-tab3"', 'data-translate="pitcher-why-tab3"')
html = html.replace('data-translate="riser-why-desc3"', 'data-translate="pitcher-why-desc3"')
html = html.replace('data-translate="riser-where-title"', 'data-translate="pitcher-where-title"')
html = html.replace('data-translate="riser-where-subtitle"', 'data-translate="pitcher-where-subtitle"')
html = html.replace('data-translate="riser-where-point1"', 'data-translate="pitcher-where-point1"')
html = html.replace('data-translate="riser-where-point2"', 'data-translate="pitcher-where-point2"')
html = html.replace('data-translate="riser-where-point3"', 'data-translate="pitcher-where-point3"')
html = html.replace('data-translate="riser-where-point4"', 'data-translate="pitcher-where-point4"')
html = html.replace('data-translate="riser-specs-title"', 'data-translate="pitcher-specs-title"')
html = html.replace('data-translate="riser-specs-subtitle"', 'data-translate="pitcher-specs-subtitle"')
html = html.replace('data-translate="riser-who-title"', 'data-translate="pitcher-who-title"')
html = html.replace('data-translate="riser-who-body"', 'data-translate="pitcher-who-body"')

# 5. Static text fallbacks
html = html.replace('<h1 data-translate="pitcher-hero-title">The Riser</h1>', '<h1 data-translate="pitcher-hero-title">The Pitcher</h1>')
html = html.replace('Precision when it counts.', 'Short game. Sharp edge.')
html = html.replace('When it\'s time to go for the pin, one thing matters most: precision. The Riser is built for exactly that – your trusted tool for controlled approach shots. With 39° loft, it closes the gap between your long clubs and the short game. Thanks to our exclusive Carbonics technology with a 100% carbon body, optimized weight distribution, and a large sweet zone, the Riser offers maximum stability, forgiveness, and reliable precision onto the green.',
                    'When it comes to the short game, you need trust, control, and the right tool. The Pitcher is built exactly for that. With 48° loft, a face designed for maximum spin performance, and our Carbonics Technology, it helps you land the ball close to the pin and stop it fast. The 100% carbon body with optimized weight distribution delivers forgiveness, stability, and consistent contact – even on delicate, feel-based shots around the green.')

# 6. Hero background pictures
hero_pic_old = """                <picture>
                    <img src="./The Riser - Golfyr_files/10-12-1024x576.jpg" alt="The Riser Hero">
                </picture>"""
hero_pic_new = """                <picture>
                    <source media="(max-width: 480px)" srcset="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_015_498X1024-498x1024.jpg">
                    <source media="(max-width: 768px)" srcset="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_014_768x1024-768x1024.jpg">
                    <img src="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_013_1024x576-1024x576.jpg" alt="The Pitcher Hero">
                </picture>"""
html = html.replace(hero_pic_old, hero_pic_new)

# 7. Why Tab names
html = html.replace('Built for approach shots', 'Maximum control')
html = html.replace('Stable & controlled', 'Spin & Stop')
html = html.replace('Bridges the game', 'Consistent results')

# 8. Why images
html = html.replace('./The Riser - Golfyr_files/GFY_Sevenclubgame_Riser.gif', './The Pitcher - Golfyr_files/GFY_Sevenclubgame_Pitcher.gif')
html = html.replace('./The Riser - Golfyr_files/why-the-riser-3.jpg', './The Pitcher - Golfyr_files/why-the-pitcher-3.jpg')
html = html.replace('./The Riser - Golfyr_files/why-the-riser-4.jpg', './The Pitcher - Golfyr_files/why-the-pitcher-4.jpg')

# 9. Why descriptions
html = html.replace('Optimized for controlled, targeted shots into the green.', 'Designed for short approach shots with high precision and spin performance.')
html = html.replace('Promotes a smooth, consistent ball flight, even on off-center hits.', 'Grooves engineered for clean contact to generate spin and stop the ball quickly on the green.')
html = html.replace('The Riser connects your long game with your short game.', 'Forgiving on slight mishits and reliable from a wide range of lies.')

# 10. Where do you play
html = html.replace('Where do you play the Riser?', 'Where do you play the Pitcher?')
html = html.replace('The Riser is your precision tool for controlled approach shots onto the green.', 'The Pitcher is your precise specialist for controlled approach shots and high chips.')
html = html.replace('./The Riser - Golfyr_files/Riser.png', './The Pitcher - Golfyr_files/Pitcher.png')
html = html.replace('The Riser Graphic', 'The Pitcher Graphic')

# Where points
old_points = """                                <li data-translate="riser-where-point1">Ideal for distances between 90 and 120 meters (depending on skill level)</li>
                                <li data-translate="riser-where-point2">Perfect when precision matters more than distance</li>
                                <li data-translate="riser-where-point3">Effective from fairway, light rough, or flat bunker</li>
                                <li data-translate="riser-where-point4">Especially useful for tight pins or bunker-protected greens</li>"""

new_points = """                                <li data-translate="pitcher-where-point1">Ideal for distances between 60 and 100 meters</li>
                                <li data-translate="pitcher-where-point2">Perfect for precise approaches from fairway, semi-rough, or challenging lies</li>
                                <li data-translate="pitcher-where-point3">First choice for high, stopping chips and pitches over obstacles</li>
                                <li data-translate="pitcher-where-point4">Helps you land the ball close to the pin and stop it quickly</li>"""
html = html.replace(old_points, new_points)

# 11. Tech specs value changes
# Spec 1 Loft
html = html.replace('<img src="./The Riser - Golfyr_files/techspecs-riser-loft.png" class="img-fluid spec-img" alt="Loft Spec">',
                    '<img src="./The Pitcher - Golfyr_files/techspecs-pitcher-loft.png" class="img-fluid spec-img" alt="Loft Spec">')
html = html.replace('<div class="techspec-value">39°</div>', '<div class="techspec-value">48°</div>')

# Spec 2 Length
html = html.replace('<img src="./The Riser - Golfyr_files/techspecs-riser-length.png" class="img-fluid spec-img" alt="Length Spec">',
                    '<img src="./The Pitcher - Golfyr_files/techspecs-pitcher-length.png" class="img-fluid spec-img" alt="Length Spec">')
html = html.replace('<div class="techspec-value">36.75″</div>', '<div class="techspec-value">35.75″</div>')

# Spec 3 Lie
html = html.replace('<img src="./The Riser - Golfyr_files/techspecs-riser-lie.png" class="img-fluid spec-img" alt="Lie Spec">',
                    '<img src="./The Pitcher - Golfyr_files/techspecs-pitcher-lie.png" class="img-fluid spec-img" alt="Lie Spec">')
html = html.replace('<div class="techspec-value">61°</div>', '<div class="techspec-value">62°</div>')

# 12. Who is it for backgrounds and content
html = html.replace('./The Riser - Golfyr_files/for-who-the-riser-430.jpg', './The Pitcher - Golfyr_files/for-who-the-pitcher-430.jpg')
html = html.replace('./The Riser - Golfyr_files/for-who-the-riser-768.jpg', './The Pitcher - Golfyr_files/for-who-the-pitcher-768.jpg')
html = html.replace('./The Riser - Golfyr_files/for-who-the-riser-1920.jpg', './The Pitcher - Golfyr_files/for-who-the-pitcher-1920.jpg')
html = html.replace('For Who The Riser', 'For Who The Pitcher')

html = html.replace('Who is the <br>Riser for?', 'Who is the <br>Pitcher for?')
html = html.replace('For anyone looking for more control on mid-range shots, especially when targeting the green. If you value consistency on approach shots and a solid feel at impact, the Riser will be a trusted companion in your bag.',
                    'The Pitcher is made for any player looking for more confidence and control in their short game. Whether you’re approaching the flag or playing from just off the green – this club helps you dial in your touch and score with precision.')

# 13. Footer clubs Swiper adjustments:
# Card 3 (Riser) needs the discover button back!
old_riser_card = """                            <!-- Card 3: Riser -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./013.jpg" alt="The Riser" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-riser-desc">When you’re in a position to attack the green, the focus shifts to the short game <br class="tablet-desktop-br"> and distance gives way to precision.</p>
                                    </div>
                                </div>
                                <a href="./riser.html" class="club-card-footer" data-translate="club-riser-title">The Riser</a>
                            </div>"""

new_riser_card = """                            <!-- Card 3: Riser -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./013.jpg" alt="The Riser" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-riser-desc">When you’re in a position to attack the green, the focus shifts to the short game <br class="tablet-desktop-br"> and distance gives way to precision.</p>
                                        <a href="./riser.html" class="btn btn-light btn-sm" data-translate="clubs-discover">Discover more</a>
                                    </div>
                                </div>
                                <a href="./riser.html" class="club-card-footer" data-translate="club-riser-title">The Riser</a>
                            </div>"""
html = html.replace(old_riser_card, new_riser_card)

# Card 4 (Pitcher) needs the discover button removed and link pointing to `./pitcher.html`!
old_pitcher_card = """                            <!-- Card 4: Pitcher -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./014.jpg" alt="The Pitcher" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-pitcher-desc">Spin is crucial in short game. Now you’re targeting the pin, <br class="tablet-desktop-br"> the Pitcher helps you to land the ball close to the flag.</p>
                                        <a href="./index.html#pitcher" class="btn btn-light btn-sm" data-translate="clubs-discover">Discover more</a>
                                    </div>
                                </div>
                                <a href="./index.html#pitcher" class="club-card-footer" data-translate="club-pitcher-title">The Pitcher</a>
                            </div>"""

new_pitcher_card = """                            <!-- Card 4: Pitcher -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./014.jpg" alt="The Pitcher" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-pitcher-desc">Spin is crucial in short game. Now you’re targeting the pin, <br class="tablet-desktop-br"> the Pitcher helps you to land the ball close to the flag.</p>
                                    </div>
                                </div>
                                <a href="./pitcher.html" class="club-card-footer" data-translate="club-pitcher-title">The Pitcher</a>
                            </div>"""
html = html.replace(old_pitcher_card, new_pitcher_card)

# Replace all other leftover links pointing to #pitcher with ./pitcher.html
# e.g., in other card slots if any
html = html.replace('href="./index.html#pitcher"', 'href="./pitcher.html"')
html = html.replace('href="#pitcher"', 'href="./pitcher.html"')

with open("pitcher.html", "w", encoding="utf-8") as f:
    f.write(html)

print("pitcher.html updated successfully!")
