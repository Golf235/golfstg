import re

with open("pitcher.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Page Title
html = html.replace("<title>The Pitcher - Golfyr</title>", "<title>The Butler - Golfyr</title>")

# 2. Section Class Names (Intro, Why, Where, For Who)
html = html.replace("pitcher-intro", "butler-intro")
html = html.replace("pitcher-why", "butler-why")
html = html.replace("pitcher-where", "butler-where")
html = html.replace("pitcher-for-who", "butler-for-who")

# 3. CSS Class Selector Overrides
html = html.replace(".pitcher-intro", ".butler-intro")
html = html.replace(".pitcher-why-section", ".butler-why-section")
html = html.replace(".pitcher-where-section", ".butler-where-section")
html = html.replace(".pitcher-for-who", ".butler-for-who")

# 4. Translation namespace tags (pitcher- -> butler-)
html = html.replace('data-translate="pitcher-hero-title"', 'data-translate="butler-hero-title"')
html = html.replace('data-translate="pitcher-hero-buy-btn"', 'data-translate="butler-hero-buy-btn"')
html = html.replace('data-translate="pitcher-hero-config-btn"', 'data-translate="butler-hero-config-btn"')
html = html.replace('data-translate="pitcher-intro-title"', 'data-translate="butler-intro-title"')
html = html.replace('data-translate="pitcher-intro-body"', 'data-translate="butler-intro-body"')
html = html.replace('data-translate="pitcher-why-title"', 'data-translate="butler-why-title"')
html = html.replace('data-translate="pitcher-why-tab1"', 'data-translate="butler-why-tab1"')
html = html.replace('data-translate="pitcher-why-desc1"', 'data-translate="butler-why-desc1"')
html = html.replace('data-translate="pitcher-why-tab2"', 'data-translate="butler-why-tab2"')
html = html.replace('data-translate="pitcher-why-desc2"', 'data-translate="butler-why-desc2"')
html = html.replace('data-translate="pitcher-why-tab3"', 'data-translate="butler-why-tab3"')
html = html.replace('data-translate="pitcher-why-desc3"', 'data-translate="butler-why-desc3"')
html = html.replace('data-translate="pitcher-where-title"', 'data-translate="butler-where-title"')
html = html.replace('data-translate="pitcher-where-subtitle"', 'data-translate="butler-where-subtitle"')
html = html.replace('data-translate="pitcher-where-point1"', 'data-translate="butler-where-point1"')
html = html.replace('data-translate="pitcher-where-point2"', 'data-translate="butler-where-point2"')
html = html.replace('data-translate="pitcher-where-point3"', 'data-translate="butler-where-point3"')
html = html.replace('data-translate="pitcher-where-point4"', 'data-translate="butler-where-point4"')
html = html.replace('data-translate="pitcher-specs-title"', 'data-translate="butler-specs-title"')
html = html.replace('data-translate="pitcher-specs-subtitle"', 'data-translate="butler-specs-subtitle"')
html = html.replace('data-translate="pitcher-who-title"', 'data-translate="butler-who-title"')
html = html.replace('data-translate="pitcher-who-body"', 'data-translate="butler-who-body"')

# 5. Static Text Fallbacks for Hero and Intro
html = html.replace('<h1 data-translate="butler-hero-title">The Pitcher</h1>', '<h1 data-translate="butler-hero-title">The Butler</h1>')
html = html.replace('Short game. Sharp edge.', 'Always at your service – from fairway to rough.')
html = html.replace('When it comes to the short game, you need trust, control, and the right tool. The Pitcher is built exactly for that. With 48° loft, a face designed for maximum spin performance, and our Carbonics Technology, it helps you land the ball close to the pin and stop it fast. The 100% carbon body with optimized weight distribution delivers forgiveness, stability, and consistent contact – even on delicate, feel-based shots around the green.',
                    'The Butler is the quiet hero of the #sevenclubgame – always there when you need it. With its wide sole and balanced design, it takes care of the tough terrain: fairway, semi-rough, rough, or tricky lies. Thanks to Carbonics Technology and a fully carbon body, the Butler delivers stability, control, and confidence with every shot. Its shape glides effortlessly through the turf, reduces errors, and supports your natural rhythm, no matter the lie. Just swing, land it solid, no detours.')

# 6. Hero image pictures
old_hero_pic = """                <picture>
                    <source media="(max-width: 480px)" srcset="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_015_498X1024-498x1024.jpg">
                    <source media="(max-width: 768px)" srcset="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_014_768x1024-768x1024.jpg">
                    <img src="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_013_1024x576-1024x576.jpg" alt="The Pitcher Hero">
                </picture>"""
new_hero_pic = """                <picture>
                    <source media="(max-width: 480px)" srcset="./The Butler - Golfyr_files/260323_Marketing_Header_Images_09_498X1024-1-498x1024.jpg">
                    <source media="(max-width: 768px)" srcset="./The Butler - Golfyr_files/260323_Marketing_Header_Images_08_768x1024-1-768x1024.jpg">
                    <img src="./The Butler - Golfyr_files/260323_Marketing_Header_Images_07_1024x576-1-1024x576.jpg" alt="The Butler Hero">
                </picture>"""
html = html.replace(old_hero_pic, new_hero_pic)

# 7. Why Choose Heading, Tabs, Images and Descriptions
html = html.replace('Why the Pitcher?', 'Why the Butler?')

# Tab titles
html = html.replace('Maximum control', 'Versatile and reliable')
html = html.replace('Spin & Stop', 'Wide sole for better turf interaction')
html = html.replace('Consistent results', 'Stable, balanced body')

# Why images
html = html.replace('./The Pitcher - Golfyr_files/GFY_Sevenclubgame_Pitcher.gif', './The Butler - Golfyr_files/GFY_Sevenclubgame_Butler.gif')
html = html.replace('./The Pitcher - Golfyr_files/why-the-pitcher-3.jpg', './The Butler - Golfyr_files/why-the-butler-2.jpg')
html = html.replace('./The Pitcher - Golfyr_files/why-the-pitcher-4.jpg', './The Butler - Golfyr_files/why-the-butler-3.jpg')

# Why descriptions
html = html.replace('Designed for short approach shots with high precision and spin performance.', 'The Butler is built for all-around-use, bridging the gap between longer and shorter clubs when versatility matters most.')
html = html.replace('Grooves engineered for clean contact to generate spin and stop the ball quickly on the green.', 'The specially designed sole helps you move cleanly through the ground, even in tough lies. Less digging, more control.')
html = html.replace('Forgiving on slight mishits and reliable from a wide range of lies.', 'Its carbon construction allows for optimal weight distribution, giving you greater control and consistency, even on imperfect ground contact.')

# 8. Where Do You Play Section
html = html.replace('Where do you play the Pitcher?', 'Where do you play the Butler?')
html = html.replace('The Pitcher is your precise specialist for controlled approach shots and high chips.', 'The Butler is your reliable club for mid-range shots and challenging lies.')
html = html.replace('./The Pitcher - Golfyr_files/Pitcher.png', './The Butler - Golfyr_files/Butler_V5-2.png')
html = html.replace('The Pitcher Graphic', 'The Butler Graphic')

old_points = """                                <li data-translate="pitcher-where-point1">Ideal for distances between 60 and 100 meters</li>
                                <li data-translate="pitcher-where-point2">Perfect for precise approaches from fairway, semi-rough, or challenging lies</li>
                                <li data-translate="pitcher-where-point3">First choice for high, stopping chips and pitches over obstacles</li>
                                <li data-translate="pitcher-where-point4">Helps you land the ball close to the pin and stop it quickly</li>"""

new_points = """                                <li data-translate="butler-where-point1">Ideal for mid-range shots between tee and green</li>
                                <li data-translate="butler-where-point2">Perfect from semi-rough, rough, or fairway</li>
                                <li data-translate="butler-where-point3">Consistent ball flight and solid ground contact</li>
                                <li data-translate="butler-where-point4">Go-to club for controlled transport shots from imperfect lies</li>"""
html = html.replace(old_points, new_points)

# 9. Tech Specs Section
# Replace Loft slide
old_loft_spec = """                                <!-- Spec 1: Loft -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Pitcher - Golfyr_files/techspecs-pitcher-loft.png" class="img-fluid spec-img" alt="Loft Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-loft-name">Loft</div>
                                        <div class="techspec-value">48°</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-loft-desc">
                                        The static loft describes the angle of the clubface when the club is at rest.
                                    </div>
                                </div>"""

new_loft_spec = """                                <!-- Spec 1: Loft -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Butler - Golfyr_files/techspecs-butler-loft.png" class="img-fluid spec-img" alt="Loft Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-loft-name">Loft</div>
                                        <div class="techspec-value">30°</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-loft-desc">
                                        The static loft describes the angle of the clubface when the club is at rest.
                                    </div>
                                </div>"""
html = html.replace(old_loft_spec, new_loft_spec)

# Replace Length and Lie slides with Swing Weight, Length, Lie (4 slides total)
old_other_specs = """                                <!-- Spec 2: Length -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Pitcher - Golfyr_files/techspecs-pitcher-length.png" class="img-fluid spec-img" alt="Length Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-length-name">Length</div>
                                        <div class="techspec-value">35.75″</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-length-desc">
                                        The length of a club determines how far and how precisely you can hit. Longer means more power; shorter gives you more control.
                                    </div>
                                </div>
                                
                                <!-- Spec 3: Lie -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Pitcher - Golfyr_files/techspecs-pitcher-lie.png" class="img-fluid spec-img" alt="Lie Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-lie-name">Lie</div>
                                        <div class="techspec-value">62°</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-lie-desc">
                                        Lie describes the angle between the clubhead, parallel to the ground, and the tilt of the shaft towards the hands.
                                    </div>
                                </div>"""

new_other_specs = """                                <!-- Spec 2: Swing Weight -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Butler - Golfyr_files/techspecs-butler-swing-weight.png" class="img-fluid spec-img" alt="Swing Weight Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-weight-name">Swing Weight</div>
                                        <div class="techspec-value">D0</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-weight-desc">
                                        Swing weight describes how “heavy” a club feels during the swing.
                                    </div>
                                </div>
                                
                                <!-- Spec 3: Length -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Butler - Golfyr_files/techspecs-butler-length.png" class="img-fluid spec-img" alt="Length Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-length-name">Length</div>
                                        <div class="techspec-value">38.25″</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-length-desc">
                                        The length of a club determines how far and how precisely you can hit. Longer means more power; shorter gives you more control.
                                    </div>
                                </div>
                                
                                <!-- Spec 4: Lie -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Butler - Golfyr_files/techspecs-butler-lie.png" class="img-fluid spec-img" alt="Lie Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-lie-name">Lie</div>
                                        <div class="techspec-value">61°</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-lie-desc">
                                        Lie describes the angle between the clubhead, parallel to the ground, and the tilt of the shaft towards the hands.
                                    </div>
                                </div>"""
html = html.replace(old_other_specs, new_other_specs)

# 10. Who is it for Section
html = html.replace('./The Pitcher - Golfyr_files/for-who-the-pitcher-430.jpg', './The Butler - Golfyr_files/for-who-the-butler-430-498x1024.jpg')
html = html.replace('./The Pitcher - Golfyr_files/for-who-the-pitcher-768.jpg', './The Butler - Golfyr_files/for-who-the-butler-768-768x1024.jpg')
html = html.replace('./The Pitcher - Golfyr_files/for-who-the-pitcher-1920.jpg', './The Butler - Golfyr_files/for-who-the-butler-1920.jpg')
html = html.replace('For Who The Pitcher', 'For Who The Butler')

html = html.replace('Who is the <br>Pitcher for?', 'Who is the <br>Butler for?')
html = html.replace('The Pitcher is made for any player looking for more confidence and control in their short game. Whether you’re approaching the flag or playing from just off the green – this club helps you dial in your touch and score with precision.',
                    'For anyone looking for a reliable, go-to club. Perfect when the ball isn’t sitting perfectly.')

# 11. Footer Clubs Swiper adjustments:
# Card 4 (Pitcher) - needs discover button added back and link pointing to `./pitcher.html`
old_pitcher_card = """                            <!-- Card 4: Pitcher -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./014.jpg" alt="The Pitcher" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-pitcher-desc">Spin is crucial in short game. Now you’re targeting the pin, <br class="tablet-desktop-br"> the Pitcher helps you to land the ball close to the flag.</p>
                                    </div>
                                </div>
                                <a href="./pitcher.html" class="club-card-footer" data-translate="club-pitcher-title">The Pitcher</a>
                            </div>"""

new_pitcher_card = """                            <!-- Card 4: Pitcher -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./014.jpg" alt="The Pitcher" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-pitcher-desc">Spin is crucial in short game. Now you’re targeting the pin, <br class="tablet-desktop-br"> the Pitcher helps you to land the ball close to the flag.</p>
                                        <a href="./pitcher.html" class="btn btn-light btn-sm" data-translate="clubs-discover">Discover more</a>
                                    </div>
                                </div>
                                <a href="./pitcher.html" class="club-card-footer" data-translate="club-pitcher-title">The Pitcher</a>
                            </div>"""
html = html.replace(old_pitcher_card, new_pitcher_card)

# Card 7 (Butler) - needs discover button removed and link pointing to `./butler.html`
old_butler_card = """                            <!-- Card 7: Butler -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./017.jpg" alt="The Butler" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-butler-desc">The Butler is the most versatile companion. <br class="tablet-desktop-br"> The wide sole helps to glide through any ground conditions.</p>
                                        <a href="./index.html#butler" class="btn btn-light btn-sm" data-translate="clubs-discover">Discover more</a>
                                    </div>
                                </div>
                                <a href="./index.html#butler" class="club-card-footer" data-translate="club-butler-title">The Butler</a>
                            </div>"""

new_butler_card = """                            <!-- Card 7: Butler -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./017.jpg" alt="The Butler" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-butler-desc">The Butler is the most versatile companion. <br class="tablet-desktop-br"> The wide sole helps to glide through any ground conditions.</p>
                                    </div>
                                </div>
                                <a href="./butler.html" class="club-card-footer" data-translate="club-butler-title">The Butler</a>
                            </div>"""
html = html.replace(old_butler_card, new_butler_card)

# Replace all leftover links pointing to #butler with ./butler.html
html = html.replace('href="./index.html#butler"', 'href="./butler.html"')
html = html.replace('href="#butler"', 'href="./butler.html"')

# Write the butler.html
with open("butler.html", "w", encoding="utf-8") as f:
    f.write(html)

print("butler.html created successfully!")
