import re

with open("pitcher.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Page Title
html = html.replace("<title>The Pitcher - Golfyr</title>", "<title>The Saver - Golfyr</title>")

# 5. Static Text Fallbacks for Hero and Intro
html = html.replace('<h1 data-translate="saver-hero-title">The Pitcher</h1>', '<h1 data-translate="saver-hero-title">The Saver</h1>')
html = html.replace('Short game. Sharp edge.', 'Your escape artist.')
html = html.replace('When it comes to the short game, you need trust, control, and the right tool. The Pitcher is built exactly for that. With 48° loft, a face designed for maximum spin performance, and our Carbonics Technology, it helps you land the ball close to the pin and stop it fast. The 100% carbon body with optimized weight distribution delivers forgiveness, stability, and consistent contact – even on delicate, feel-based shots around the green.',
                    "Whether you're stuck in the bunker, deep in the rough, or facing a delicate chip around the green – the Saver is built for tough situations. With its high loft and smart bounce, it gives you the control and spin needed for high, soft shots that stop quickly – even under pressure. Like every club in the #sevenclubgame, the Saver features a 100% carbon body with a hollow construction. This allows for optimized weighting, a large sweet zone, and a uniquely soft, responsive feel at impact – perfect for the demands of the short game.")

# 6. Hero image pictures
old_hero_pic = """                <picture>
                    <source media="(max-width: 480px)" srcset="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_015_498X1024-498x1024.jpg">
                    <source media="(max-width: 768px)" srcset="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_014_768x1024-768x1024.jpg">
                    <img src="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_013_1024x576-1024x576.jpg" alt="The Pitcher Hero">
                </picture>"""
new_hero_pic = """                <picture>
                    <source media="(max-width: 480px)" srcset="./The Saver - Golfyr_files/260323_Marketing_Header_Images_018_498X1024-1-498x1024.jpg">
                    <source media="(max-width: 768px)" srcset="./The Saver - Golfyr_files/260323_Marketing_Header_Images_017_768x1024-1-768x1024.jpg">
                    <img src="./The Saver - Golfyr_files/260323_Marketing_Header_Images_016_1024x576-1-1024x576.jpg" alt="The Saver Hero">
                </picture>"""
html = html.replace(old_hero_pic, new_hero_pic)

# 7. Why Choose Heading, Tabs, Images and Descriptions
html = html.replace('Why the Pitcher?', 'Why the Saver?')

# 4. Translation namespace tags (pitcher- -> saver-)
html = html.replace('data-translate="pitcher-hero-title"', 'data-translate="saver-hero-title"')
html = html.replace('data-translate="pitcher-hero-buy-btn"', 'data-translate="saver-hero-buy-btn"')
html = html.replace('data-translate="pitcher-hero-config-btn"', 'data-translate="saver-hero-config-btn"')
html = html.replace('data-translate="pitcher-intro-title"', 'data-translate="saver-intro-title"')
html = html.replace('data-translate="pitcher-intro-body"', 'data-translate="saver-intro-body"')
html = html.replace('data-translate="pitcher-why-title"', 'data-translate="saver-why-title"')
html = html.replace('data-translate="pitcher-where-title"', 'data-translate="saver-where-title"')
html = html.replace('data-translate="pitcher-where-subtitle"', 'data-translate="saver-where-subtitle"')
html = html.replace('data-translate="pitcher-where-point1"', 'data-translate="saver-where-point1"')
html = html.replace('data-translate="pitcher-where-point2"', 'data-translate="saver-where-point2"')
html = html.replace('data-translate="pitcher-where-point3"', 'data-translate="saver-where-point3"')
html = html.replace('data-translate="pitcher-where-point4"', 'data-translate="saver-where-point4"')
html = html.replace('data-translate="pitcher-specs-title"', 'data-translate="saver-specs-title"')
html = html.replace('data-translate="pitcher-specs-subtitle"', 'data-translate="saver-specs-subtitle"')
html = html.replace('data-translate="pitcher-who-title"', 'data-translate="saver-who-title"')
html = html.replace('data-translate="pitcher-who-body"', 'data-translate="saver-who-body"')

# 5. Static Text Fallbacks for Hero and Intro
html = html.replace('<h1 data-translate="saver-hero-title">The Pitcher</h1>', '<h1 data-translate="saver-hero-title">The Saver</h1>')
html = html.replace('Short game. Sharp edge.', 'Your escape artist.')
html = html.replace('When it comes to the short game, you need trust, control, and the right tool. The Pitcher is built exactly for that. With 48° loft, a face designed for maximum spin performance, and our Carbonics Technology, it helps you land the ball close to the pin and stop it fast. The 100% carbon body with optimized weight distribution delivers forgiveness, stability, and consistent contact – even on delicate, feel-based shots around the green.',
                    "Whether you're stuck in the bunker, deep in the rough, or facing a delicate chip around the green – the Saver is built for tough situations. With its high loft and smart bounce, it gives you the control and spin needed for high, soft shots that stop quickly – even under pressure. Like every club in the #sevenclubgame, the Saver features a 100% carbon body with a hollow construction. This allows for optimized weighting, a large sweet zone, and a uniquely soft, responsive feel at impact – perfect for the demands of the short game.")

# 6. Hero image pictures
old_hero_pic = """                <picture>
                    <source media="(max-width: 480px)" srcset="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_015_498X1024-498x1024.jpg">
                    <source media="(max-width: 768px)" srcset="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_014_768x1024-768x1024.jpg">
                    <img src="./The Pitcher - Golfyr_files/260323_Marketing_Header_Images_013_1024x576-1024x576.jpg" alt="The Pitcher Hero">
                </picture>"""
new_hero_pic = """                <picture>
                    <source media="(max-width: 480px)" srcset="./The Saver - Golfyr_files/260323_Marketing_Header_Images_018_498X1024-1-498x1024.jpg">
                    <source media="(max-width: 768px)" srcset="./The Saver - Golfyr_files/260323_Marketing_Header_Images_017_768x1024-1-768x1024.jpg">
                    <img src="./The Saver - Golfyr_files/260323_Marketing_Header_Images_016_1024x576-1-1024x576.jpg" alt="The Saver Hero">
                </picture>"""
html = html.replace(old_hero_pic, new_hero_pic)

# 7. Why Choose Heading, Tabs, Images and Descriptions
html = html.replace('Why the Pitcher?', 'Why the Saver?')

# Replace the navigation tabs swiper wrapper (3 tabs -> 4 tabs)
old_tabs = """                        <div class="swiper simpleSliderTabNav">
                            <div class="swiper-wrapper">
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="pitcher-why-tab1">Maximum control</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="pitcher-why-tab2">Spin & Stop</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="pitcher-why-tab3">Consistent results</div>
                                </div>
                            </div>
                        </div>"""

new_tabs = """                        <div class="swiper simpleSliderTabNav">
                            <div class="swiper-wrapper">
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="saver-why-tab1">Highest loft in the set</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="saver-why-tab2">Forgiving bounce</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="saver-why-tab3">Built for the short game</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="saver-why-tab4">Spin and touch</div>
                                </div>
                            </div>
                        </div>"""
html = html.replace(old_tabs, new_tabs)

# Replace the swiper images (3 slides -> 4 slides)
old_images = """                                    <div class="swiper simpleSliderTabNavContentImages">
                                        <div class="swiper-wrapper">
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Pitcher - Golfyr_files/GFY_Sevenclubgame_Pitcher.gif" class="img-fluid" alt="Maximum control">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Pitcher - Golfyr_files/why-the-pitcher-3.jpg" class="img-fluid" alt="Spin & Stop">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Pitcher - Golfyr_files/why-the-pitcher-4.jpg" class="img-fluid" alt="Consistent results">
                                                </div>
                                            </div>
                                        </div>
                                    </div>"""

new_images = """                                    <div class="swiper simpleSliderTabNavContentImages">
                                        <div class="swiper-wrapper">
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Saver - Golfyr_files/GFY_Sevenclubgame_Saver.gif" class="img-fluid" alt="Highest loft in the set">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Saver - Golfyr_files/why-the-saver-2.jpg" class="img-fluid" alt="Forgiving bounce">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Saver - Golfyr_files/why-the-saver-3.jpg" class="img-fluid" alt="Built for the short game">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Saver - Golfyr_files/why-the-saver-4.jpg" class="img-fluid" alt="Spin and touch">
                                                </div>
                                            </div>
                                        </div>
                                    </div>"""
html = html.replace(old_images, new_images)

# Replace the swiper descriptions (3 slides -> 4 slides)
old_descs = """                                    <div class="swiper simpleSliderTabNavContent pitcher-why-text-swiper">
                                        <div class="swiper-wrapper">
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="pitcher-why-tab1">
                                                        Maximum control
                                                    </div>
                                                    <div class="content" data-translate="pitcher-why-desc1">
                                                        Designed for short approach shots with high precision and spin performance.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="pitcher-why-tab2">
                                                        Spin & Stop
                                                    </div>
                                                    <div class="content" data-translate="pitcher-why-desc2">
                                                        Grooves engineered for clean contact to generate spin and stop the ball quickly on the green.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="pitcher-why-tab3">
                                                        Consistent results
                                                    </div>
                                                    <div class="content" data-translate="pitcher-why-desc3">
                                                        Forgiving on slight mishits and reliable from a wide range of lies.
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>"""

new_descs = """                                    <div class="swiper simpleSliderTabNavContent saver-why-text-swiper">
                                        <div class="swiper-wrapper">
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="saver-why-tab1">
                                                        Highest loft in the set
                                                    </div>
                                                    <div class="content" data-translate="saver-why-desc1">
                                                        Perfect for high, soft shots with minimal roll.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="saver-why-tab2">
                                                        Forgiving bounce
                                                    </div>
                                                    <div class="content" data-translate="saver-why-desc2">
                                                        Clever sole design glides through sand or thick grass without digging in.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="saver-why-tab3">
                                                        Built for the short game
                                                    </div>
                                                    <div class="content" data-translate="saver-why-desc3">
                                                        For controlled, soft shots around the green.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="saver-why-tab4">
                                                        Spin and touch
                                                    </div>
                                                    <div class="content" data-translate="saver-why-desc4">
                                                        Designed to stop the ball quickly – even from tough lies.
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>"""
html = html.replace(old_descs, new_descs)

# Adjust Swiper button wrappers to target saver-why-buttons
html = html.replace("pitcher-why-buttons", "saver-why-buttons")
html = html.replace("pitcher-why-content-col", "saver-why-content-col")

# 8. Where Do You Play Section
html = html.replace("Where do you play the Pitcher?", "Where do you play the Saver?")
html = html.replace("The Pitcher is your precise specialist for controlled approach shots and high chips.",
                    "True to its name, the Saver helps you in your short game whenever you need height, spin, and control.")
html = html.replace("./The Pitcher - Golfyr_files/Pitcher.png", "./The Saver - Golfyr_files/Saver.png")
html = html.replace("The Pitcher Graphic", "The Saver Graphic")

old_points = """                                <li data-translate="pitcher-where-point1">Ideal for distances between 60 and 100 meters</li>
                                <li data-translate="pitcher-where-point2">Perfect for precise approaches from fairway, semi-rough, or challenging lies</li>
                                <li data-translate="pitcher-where-point3">First choice for high, stopping chips and pitches over obstacles</li>
                                <li data-translate="pitcher-where-point4">Helps you land the ball close to the pin and stop it quickly</li>"""

new_points = """                                <li data-translate="saver-where-point1">Ideal for deep bunker shots with little green to the pin</li>
                                <li data-translate="saver-where-point2">Perfect for lob shots over obstacles</li>
                                <li data-translate="saver-where-point3">Precise chips from semi-rough onto fast, sloping greens</li>
                                <li data-translate="saver-where-point4">Specifically designed for high control in the short game</li>"""
html = html.replace(old_points, new_points)

# 9. Tech Specs Section
# Spec 1 Loft
html = html.replace('<img src="./The Pitcher - Golfyr_files/techspecs-pitcher-loft.png" class="img-fluid spec-img" alt="Loft Spec">',
                    '<img src="./The Saver - Golfyr_files/techspecs-saver-loft.png" class="img-fluid spec-img" alt="Loft Spec">')
html = html.replace('<div class="techspec-value">48°</div>', '<div class="techspec-value">58°</div>')

# Spec 2 Length
html = html.replace('<img src="./The Pitcher - Golfyr_files/techspecs-pitcher-length.png" class="img-fluid spec-img" alt="Length Spec">',
                    '<img src="./The Saver - Golfyr_files/techspecs-saver-length.png" class="img-fluid spec-img" alt="Length Spec">')
html = html.replace('<div class="techspec-value">35.75″</div>', '<div class="techspec-value">35.25″</div>')

# Spec 3 Lie
html = html.replace('<img src="./The Pitcher - Golfyr_files/techspecs-pitcher-lie.png" class="img-fluid spec-img" alt="Lie Spec">',
                    '<img src="./The Saver - Golfyr_files/techspecs-saver-lie.png" class="img-fluid spec-img" alt="Lie Spec">')
html = html.replace('<div class="techspec-value">62°</div>', '<div class="techspec-value">64°</div>')

# 10. Who is it for Section
html = html.replace('./The Pitcher - Golfyr_files/for-who-the-pitcher-430.jpg', './The Saver - Golfyr_files/for-who-the-saver-430-498x1024.jpg')
html = html.replace('./The Pitcher - Golfyr_files/for-who-the-pitcher-768.jpg', './The Saver - Golfyr_files/for-who-the-saver-768-768x1024.jpg')
html = html.replace('./The Pitcher - Golfyr_files/for-who-the-pitcher-1920.jpg', './The Saver - Golfyr_files/for-who-the-saver-1920.jpg')
html = html.replace('For Who The Pitcher', 'For Who The Saver')

html = html.replace('Who is the <br>Pitcher for?', 'Who is the <br>Saver for?')
html = html.replace('The Pitcher is made for any player looking for more confidence and control in their short game. Whether you’re approaching the flag or playing from just off the green – this club helps you dial in your touch and score with precision.',
                    'The Saver is made for players who want more confidence and control in their short game – whether you’re blasting out of the bunker, hitting a lob over an obstacle, or chipping onto a fast pin. A club for moments where height, feel, and precision decide the outcome.')

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

# Card 6 (Saver) - needs discover button removed and link pointing to `./saver.html`
old_saver_card = """                            <!-- Card 6: Saver -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./018.jpg" alt="The Saver" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-saver-desc">It’s all in the name: the Saver is there to get you <br class="tablet-desktop-br"> out of trouble in the short game.</p>
                                        <a href="./index.html#saver" class="btn btn-light btn-sm" data-translate="clubs-discover">Discover more</a>
                                    </div>
                                </div>
                                <a href="./index.html#saver" class="club-card-footer" data-translate="club-saver-title">The Saver</a>
                            </div>"""

new_saver_card = """                            <!-- Card 6: Saver -->
                            <div class="swiper-slide">
                                <div class="club-card">
                                    <img src="./018.jpg" alt="The Saver" class="club-card-image">
                                    <div class="club-card-overlay">
                                        <p data-translate="club-saver-desc">It’s all in the name: the Saver is there to get you <br class="tablet-desktop-br"> out of trouble in the short game.</p>
                                    </div>
                                </div>
                                <a href="./saver.html" class="club-card-footer" data-translate="club-saver-title">The Saver</a>
                            </div>"""
html = html.replace(old_saver_card, new_saver_card)

# 12. Generic Section Class Names (Intro, Why, Where, For Who)
html = html.replace("pitcher-intro", "saver-intro")
html = html.replace("pitcher-why", "saver-why")
html = html.replace("pitcher-where", "saver-where")
html = html.replace("pitcher-for-who", "saver-for-who")

# 13. CSS Class Selector Overrides
html = html.replace(".pitcher-intro", ".saver-intro")
html = html.replace(".pitcher-why-section", ".saver-why-section")
html = html.replace(".pitcher-where-section", ".saver-where-section")
html = html.replace(".pitcher-for-who", ".saver-for-who")

# Replace all leftover links pointing to #saver with ./saver.html
html = html.replace('href="./index.html#saver"', 'href="./saver.html"')
html = html.replace('href="#saver"', 'href="./saver.html"')

# Write the saver.html
with open("saver.html", "w", encoding="utf-8") as f:
    f.write(html)

print("saver.html created successfully!")
