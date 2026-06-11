import re

with open("riser.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Rename title
html = html.replace("<title>The Mover - Golfyr</title>", "<title>The Riser - Golfyr</title>")

# 2. Rename CSS & HTML class structures (intro, why, where, for-who)
html = html.replace("mover-intro", "riser-intro")
html = html.replace("mover-why", "riser-why")
html = html.replace("mover-where", "riser-where")
html = html.replace("mover-for-who", "riser-for-who")

# 3. Rename translation key prefixes (mover-hero, mover-intro, mover-why, mover-where, mover-specs, mover-who)
# but NOT in the shop/All our Clubs slider section for the Mover card!
# Let's do selective replacements for data-translates of the main page sections
html = html.replace('data-translate="mover-hero-title"', 'data-translate="riser-hero-title"')
html = html.replace('data-translate="mover-hero-buy-btn"', 'data-translate="riser-hero-buy-btn"')
html = html.replace('data-translate="mover-hero-config-btn"', 'data-translate="riser-hero-config-btn"')
html = html.replace('data-translate="mover-intro-title"', 'data-translate="riser-intro-title"')
html = html.replace('data-translate="mover-intro-body"', 'data-translate="riser-intro-body"')
html = html.replace('data-translate="mover-why-title"', 'data-translate="riser-why-title"')
html = html.replace('data-translate="mover-where-title"', 'data-translate="riser-where-title"')
html = html.replace('data-translate="mover-where-subtitle"', 'data-translate="riser-where-subtitle"')
html = html.replace('data-translate="mover-where-point1"', 'data-translate="riser-where-point1"')
html = html.replace('data-translate="mover-where-point2"', 'data-translate="riser-where-point2"')
html = html.replace('data-translate="mover-where-point3"', 'data-translate="riser-where-point3"')
html = html.replace('data-translate="mover-where-point4"', 'data-translate="riser-where-point4"')
html = html.replace('data-translate="mover-specs-title"', 'data-translate="riser-specs-title"')
html = html.replace('data-translate="mover-specs-subtitle"', 'data-translate="riser-specs-subtitle"')
html = html.replace('data-translate="mover-who-title"', 'data-translate="riser-who-title"')
html = html.replace('data-translate="mover-who-body"', 'data-translate="riser-who-body"')

# Rename Hero Title text
html = html.replace('<h1 data-translate="riser-hero-title">The Mover</h1>', '<h1 data-translate="riser-hero-title">The Riser</h1>')
# Rename Intro Text copy
html = html.replace('Move forward. Play with ease.', 'Precision when it counts.')
html = html.replace('As the name suggests, the Mover helps you to move forward in the game.', 'When it\'s time to go for the pin, one thing matters most: precision.')

# 4. Restructure "Why the Riser?" Section (from 4 tabs/slides to exactly 3)
# Let's locate the Swiper tab navigation wrapper and replace it
tab_nav_old = """                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="mover-why-tab1">Versatile Usage</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="mover-why-tab2">Generous Sweet Zone</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="mover-why-tab3">Optimized Weight Distribution</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="mover-why-tab4">Consistent Control</div>
                                </div>"""

tab_nav_new = """                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="riser-why-tab1">Built for approach shots</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="riser-why-tab2">Stable & controlled</div>
                                </div>
                                <div class="swiper-slide">
                                    <div class="menu-tab" data-translate="riser-why-tab3">Bridges the game</div>
                                </div>"""

html = html.replace(tab_nav_old, tab_nav_new)

# Let's replace the Why Swiper images block
why_images_old = """                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Mover - Golfyr_files/GFY_Sevenclubgame_Mover.gif" class="img-fluid" alt="Versatile Usage">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Mover - Golfyr_files/why-the-mover-2.jpg" class="img-fluid" alt="Generous Sweet Zone">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Mover - Golfyr_files/why-the-mover-3.jpg" class="img-fluid" alt="Optimized Weight Distribution">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Mover - Golfyr_files/why-the-mover-4.jpg" class="img-fluid" alt="Consistent Control">
                                                </div>
                                            </div>"""

why_images_new = """                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Riser - Golfyr_files/GFY_Sevenclubgame_Riser.gif" class="img-fluid" alt="Built for approach shots">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Riser - Golfyr_files/why-the-riser-3.jpg" class="img-fluid" alt="Stable & controlled">
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="image-wrapper">
                                                    <img src="./The Riser - Golfyr_files/why-the-riser-4.jpg" class="img-fluid" alt="Bridges the game">
                                                </div>
                                            </div>"""

html = html.replace(why_images_old, why_images_new)

# Let's replace the Why Swiper content descriptions block
why_content_old = """                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="mover-why-tab1">
                                                        Versatile Usage
                                                    </div>
                                                    <div class="content" data-translate="mover-why-desc1">
                                                        Designed for hybrid shots – from the tee, off the ground, and in all kinds of terrain.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="mover-why-tab2">
                                                        Generous Sweet Zone
                                                    </div>
                                                    <div class="content" data-translate="mover-why-desc2">
                                                        The fully carbon construction delivers reliable performance, even on imperfect hits.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="mover-why-tab3">
                                                        Optimized Weight Distribution
                                                    </div>
                                                    <div class="content" data-translate="mover-why-desc3">
                                                        Strategically placed mass in the clubhead ensures consistent ball flight and solid distances, no matter where you strike the ball.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="mover-why-tab4">
                                                        Consistent Control
                                                    </div>
                                                    <div class="content" data-translate="mover-why-desc4">
                                                        The Mover helps you hit distances precisely with the confidence to handle any situation on the course.
                                                    </div>
                                                </div>
                                            </div>"""

why_content_new = """                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="riser-why-tab1">
                                                        Built for approach shots
                                                    </div>
                                                    <div class="content" data-translate="riser-why-desc1">
                                                        Optimized for controlled, targeted shots into the green.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="riser-why-tab2">
                                                        Stable & controlled
                                                    </div>
                                                    <div class="content" data-translate="riser-why-desc2">
                                                        Promotes a smooth, consistent ball flight, even on off-center hits.
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="swiper-slide">
                                                <div class="content-wrapper">
                                                    <div class="title" data-translate="riser-why-tab3">
                                                        Bridges the game
                                                    </div>
                                                    <div class="content" data-translate="riser-why-desc3">
                                                        The Riser connects your long game with your short game.
                                                    </div>
                                                </div>
                                            </div>"""

html = html.replace(why_content_old, why_content_new)

# 5. Where do you play section adjustments
html = html.replace('Where do you play the Mover?', 'Where do you play the Riser?')
html = html.replace('The Mover is your ultimate utility club – designed for long-range shots from the tee, the fairway, or tough lies.', 'The Riser is your precision tool for controlled approach shots onto the green.')
html = html.replace('<img src="./The Mover - Golfyr_files/Mover.png" class="img-fluid club-graphic" alt="The Mover Graphic">', '<img src="./The Riser - Golfyr_files/Riser.png" class="img-fluid club-graphic" alt="The Riser Graphic">')

# 6. Tech Specs Section (From 5 spec slides to exactly 3 spec slides: Loft 39°, Length 36.75″, Lie 61°)
# Let's replace the entire swiper-wrapper inside swiper-club-tech-specs-slider
specs_wrapper_old = """                            <div class="swiper-wrapper">
                                <!-- Spec 1: Loft -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Mover - Golfyr_files/techspecs-mover-loft.png" class="img-fluid spec-img" alt="Loft Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-loft-name">Loft</div>
                                        <div class="techspec-value">22°</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-loft-desc">
                                        The static loft describes the angle of the clubface when the club is at rest.
                                    </div>
                                </div>
                                
                                <!-- Spec 2: Swing Weight -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Mover - Golfyr_files/techspecs-mover-swing-weight.png" class="img-fluid spec-img" alt="Swing Weight Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-weight-name">Swing Weight</div>
                                        <div class="techspec-value">D2</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-weight-desc">
                                        Swing weight describes how “heavy” a club feels during the swing.
                                    </div>
                                </div>
                                
                                <!-- Spec 3: Length -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Mover - Golfyr_files/techspecs-mover-length.png" class="img-fluid spec-img" alt="Length Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-length-name">Length</div>
                                        <div class="techspec-value">40.75″</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-length-desc">
                                        The length of a club determines how far and how precisely you can hit. Longer means more power; shorter gives you more control.
                                    </div>
                                </div>
                                
                                <!-- Spec 4: Lie -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Mover - Golfyr_files/techspecs-mover-lie.png" class="img-fluid spec-img" alt="Lie Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-lie-name">Lie</div>
                                        <div class="techspec-value">60°</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-lie-desc">
                                        Lie describes the angle between the clubhead, parallel to the ground, and the tilt of the shaft towards the hands.
                                    </div>
                                </div>
                                
                                <!-- Spec 5: Volume -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Mover - Golfyr_files/techspecs-mover-volume.png" class="img-fluid spec-img" alt="Volume Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-volume-name">Volume (Head)</div>
                                        <div class="techspec-value">240cc</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-volume-desc">
                                        The larger the clubhead volume, the more forgiving and stable the club is. Smaller heads offer more control and feel but require greater precision.
                                    </div>
                                </div>
                            </div>"""

specs_wrapper_new = """                            <div class="swiper-wrapper">
                                <!-- Spec 1: Loft -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Riser - Golfyr_files/techspecs-riser-loft.png" class="img-fluid spec-img" alt="Loft Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-loft-name">Loft</div>
                                        <div class="techspec-value">39°</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-loft-desc">
                                        The static loft describes the angle of the clubface when the club is at rest.
                                    </div>
                                </div>
                                
                                <!-- Spec 2: Length -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Riser - Golfyr_files/techspecs-riser-length.png" class="img-fluid spec-img" alt="Length Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-length-name">Length</div>
                                        <div class="techspec-value">36.75″</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-length-desc">
                                        The length of a club determines how far and how precisely you can hit. Longer means more power; shorter gives you more control.
                                    </div>
                                </div>
                                
                                <!-- Spec 3: Lie -->
                                <div class="swiper-slide spec-slide">
                                    <div class="image-wrapper">
                                        <img src="./The Riser - Golfyr_files/techspecs-riser-lie.png" class="img-fluid spec-img" alt="Lie Spec">
                                    </div>
                                    <div class="techspec-wrapper">
                                        <div class="techspec-name" data-translate="opener-specs-lie-name">Lie</div>
                                        <div class="techspec-value">61°</div>
                                    </div>
                                    <div class="description" data-translate="opener-specs-lie-desc">
                                        Lie describes the angle between the clubhead, parallel to the ground, and the tilt of the shaft towards the hands.
                                    </div>
                                </div>
                            </div>"""

html = html.replace(specs_wrapper_old, specs_wrapper_new)

# 7. Who is the Riser for section backgrounds and texts
who_section_old = """        <section class="responsive-image-content full-width riser-for-who" id="for-who">
            <div class="background sticky-bg">
                <picture>
                    <source media="(max-width: 480px)" srcset="./The Mover - Golfyr_files/for-who-the-mover-430.jpg">
                    <source media="(max-width: 768px)" srcset="./The Mover - Golfyr_files/for-who-the-mover-768.jpg">
                    <img src="./The Mover - Golfyr_files/for-who-the-mover-1920.jpg" alt="For Who The Mover" class="img-fluid">
                </picture>
            </div>
            <div class="overlay-shadow"></div>
            
            <div class="content-wrapper">
                <div class="container h-100">
                    <div class="row h-100">
                        <div class="col-12 col-md-8 col-lg-6 d-flex flex-column justify-content-end h-100 pb-5">
                            <div class="content d-flex flex-column">
                                <div class="head" data-translate="riser-who-title">Who is the <br>Mover for?</div>
                                <div class="additional-content" data-translate="riser-who-body">
                                    Whether you need to bridge long distances on par-5 holes, hit a safe alternative shot off the tee, or launch the ball out of difficult semi-rough, the Mover provides players of all skill levels with unmatched versatility and power.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

who_section_new = """        <section class="responsive-image-content full-width riser-for-who" id="for-who">
            <div class="background sticky-bg">
                <picture>
                    <source media="(max-width: 480px)" srcset="./The Riser - Golfyr_files/for-who-the-riser-430.jpg">
                    <source media="(max-width: 768px)" srcset="./The Riser - Golfyr_files/for-who-the-riser-768.jpg">
                    <img src="./The Riser - Golfyr_files/for-who-the-riser-1920.jpg" alt="For Who The Riser" class="img-fluid">
                </picture>
            </div>
            <div class="overlay-shadow"></div>
            
            <div class="content-wrapper">
                <div class="container h-100">
                    <div class="row h-100">
                        <div class="col-12 col-md-8 col-lg-6 d-flex flex-column justify-content-end h-100 pb-5">
                            <div class="content d-flex flex-column">
                                <div class="head" data-translate="riser-who-title">Who is the <br>Riser for?</div>
                                <div class="additional-content" data-translate="riser-who-body">
                                    For anyone looking for more control on mid-range shots, especially when targeting the green. If you value consistency on approach shots and a solid feel at impact, the Riser will be a trusted companion in your bag.
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

html = html.replace(who_section_old, who_section_new)

# 8. Hero images for The Riser
hero_picture_old = """                <picture>
                    <source media="(max-width: 768px)" srcset="./The Mover - Golfyr_files/260323_Marketing_Header_Images_05_768x1024-768x1024.jpg">
                    <img src="./The Mover - Golfyr_files/260323_Marketing_Header_Images_04_1024x576-1024x576.jpg" alt="The Mover Hero">
                </picture>"""

# Wait, let's check what images are in "The Riser - Golfyr_files".
# We saw: "10-12-1024x576.jpg" (119301 bytes). That's a perfect header image for the Riser!
# Wait, let's see if there is a mobile header or if we should just use that one.
# In the tag dump output we had:
# No other header image listed in "The Riser - Golfyr_files", but wait, is there another image?
# Let's check: "10-12-1024x576.jpg" is a great 1024x576 image.
# We can use "./The Riser - Golfyr_files/10-12-1024x576.jpg" as the main hero image!
hero_picture_new = """                <picture>
                    <img src="./The Riser - Golfyr_files/10-12-1024x576.jpg" alt="The Riser Hero">
                </picture>"""

html = html.replace(hero_picture_old, hero_picture_new)

# 9. Update the Swiper initialization script breakpoints (limit slidesPerView to 3 since there are 3 slides)
swiper_init_old = """                    1200: {
                        slidesPerView: 4,
                        spaceBetween: 24
                    }"""

swiper_init_new = """                    1200: {
                        slidesPerView: 3,
                        spaceBetween: 24
                    }"""

html = html.replace(swiper_init_old, swiper_init_new)

# 10. Update links inside riser.html's "Our Clubs" Swiper slides:
# For Card 2: Mover -> it is already pointing to `./mover.html`
# For Card 3: Riser -> it is currently pointing to `./index.html#riser` or `./index.html#riser` links.
# Let's make it point to `./riser.html`!
# Let's find:
# `<a href="./index.html#riser" class="btn btn-light btn-sm" data-translate="clubs-discover">Discover more</a>`
# `<a href="./index.html#riser" class="club-card-footer" data-translate="club-riser-title">The Riser</a>`
html = html.replace('href="./index.html#riser"', 'href="./riser.html"')

# 11. Rename CSS classes overrides in headings override block:
html = html.replace('.mover-intro', '.riser-intro')
html = html.replace('.mover-why-section', '.riser-why-section')
html = html.replace('.mover-where-section', '.riser-where-section')
html = html.replace('.mover-for-who', '.riser-for-who')

with open("riser.html", "w", encoding="utf-8") as f:
    f.write(html)

print("riser.html renamed and restructured successfully!")
