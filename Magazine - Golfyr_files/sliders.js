/**
 * Video Sliders (Fundamentals/#sevenclubgame)
 */
document.addEventListener("DOMContentLoaded", () => {

    if (document.querySelectorAll('.videoGalleryMainSwiperVert').length > 0) {
        const swiperVideos = document.querySelectorAll('.videoGalleryMainSwiperVert');
        const swiperVideoThumbs = document.querySelectorAll('.videoGalleryThumbSwiperVert');

        const toggleMute = document.querySelectorAll('.audio-toggle');
        const togglePlay = document.querySelectorAll('.audio-play');
        const toggleStop = document.querySelectorAll('.audio-stop');
        const slidersVideoGalleryNext = document.querySelectorAll('.swiper-videogallery-button-next');
        const slidersVideoGalleryPrev = document.querySelectorAll('.swiper-videogallery-button-prev');

        // const videos = swiperVideos[i].querySelectorAll('video');

        // for(i=0; i < videos.length; i++) {
        //     videos[i].onclick = function() {
        //         this.muted = !this.muted;
        //     }
        // }

        //    for (i = 0; i < swiperVideos.length; i++) {
        /**** first slider idx=0 ****/
        var i = 0;
        swiperVideos[i].classList.add('swiper-videogallery-' + i);
        swiperVideoThumbs[i].classList.add('swiper-videogallerythumbs-' + i);
        toggleMute[i].classList.add('audio-toggle-' + i);
        togglePlay[i].classList.add('audio-play-' + i);
        toggleStop[i].classList.add('audio-stop-' + i);

        slidersVideoGalleryNext[i].classList.add('swiper-videogallery-button-next-' + i);
        slidersVideoGalleryPrev[i].classList.add('swiper-videogallery-button-prev-' + i);

        const videos = swiperVideos[i].querySelectorAll('video');

        // for(i=0; i < videos.length; i++) {
        //     videos[i].onclick = function() {
        //         this.muted = !this.muted;
        //     }
        // }

        var mySwiper = new Swiper('.swiper-videogallery-' + i, {
            // Optional parameters
            direction: 'horizontal',
            zoom: true,
            loop: false,

            thumbs: {
                swiper: swiperVideoThumbs[i],
            },

            breakpoints: {
                // when window width is >= 320px
                320: {
                    slidesPerView: 1,
                },
                // when window width is >= 768px
                768: {
                    slidesPerView: 1,
                    spaceBetween: 8
                },
                // when window width is >= 992px
                992: {
                    slidesPerView: 1,
                    spaceBetween: 8
                }
            },
            on: {
                slideChange: function () {
                    for (i = 0; i < videos.length; i++) {
                        videos[i].muted = true;

                        if (togglePlay[0].classList.contains('paused')) {
                            togglePlay[0].classList.remove('paused');
                            togglePlay[0].classList.add('playing');
                        } else if (togglePlay[0].classList.contains('playing')) {
                            videos[mySwiper.realIndex].play();
                        }

                        if (!toggleMute[0].classList.contains('mute')) {
                            toggleMute[0].classList.remove('unmute');
                            toggleMute[0].classList.add('mute');
                        }
                    }
                },
            },

            // If we need pagination
            // pagination: {
            //   el: '.swiper-pagination',
            // },

            // Navigation arrows
            navigation: {
                nextEl: '.swiper-videogallery-button-next',
                prevEl: '.swiper-videogallery-button-prev',
            },

            // And if we need scrollbar
            // scrollbar: {
            // el: '.swiper-scrollbar',
            // draggable: true,
            // },    
        });

        togglePlay[i].onclick = function () {
            if (videos[mySwiper.realIndex].paused !== true) {
                videos[mySwiper.realIndex].pause();
                this.classList.remove('playing');
                this.classList.add('paused');
            } else {
                videos[mySwiper.realIndex].play();
                this.classList.remove('paused');
                this.classList.add('playing');
            }
        }

        toggleStop[i].onclick = function () {
            videos[mySwiper.realIndex].pause();
            videos[mySwiper.realIndex].currentTime = 0;

            if (togglePlay[0].classList.contains('playing')) {
                togglePlay[0].classList.remove('playing');
                togglePlay[0].classList.add('paused');
            }
        }

        toggleMute[i].onclick = function () {
            videos[mySwiper.realIndex].muted = !videos[mySwiper.realIndex].muted;

            if (videos[mySwiper.realIndex].muted != true) {
                this.classList.remove('mute');
                this.classList.add('unmute');
            } else {
                this.classList.remove('unmute');
                this.classList.add('mute');
            }
        }
        //    }

        /**** second slider idx=1 ****/
        var i = 1;
        swiperVideos[i].classList.add('swiper-videogallery-' + i);

        var mySwiper2 = new Swiper('.swiper-videogallery-' + i, {
            // Optional parameters
            direction: 'horizontal',
            zoom: true,
            loop: false,

            //           thumbs: {
            //               swiper: swiperVideoThumbs[i],
            //           },

            breakpoints: {
                // when window width is >= 320px
                320: {
                    slidesPerView: 1,
                },
                // when window width is >= 768px
                768: {
                    slidesPerView: 1,
                    spaceBetween: 8
                },
                // when window width is >= 992px
                992: {
                    slidesPerView: 1,
                    spaceBetween: 8
                }
            },
            on: {
                slideChange: function () {
                    for (i = 0; i < videos.length; i++) {
                        videos[i].muted = true;

                        if (togglePlay[0].classList.contains('paused')) {
                            togglePlay[0].classList.remove('paused');
                            togglePlay[0].classList.add('playing');
                        } else if (togglePlay[0].classList.contains('playing')) {
                            videos[mySwiper.realIndex].play();
                        }

                        if (!toggleMute[0].classList.contains('mute')) {
                            toggleMute[0].classList.remove('unmute');
                            toggleMute[0].classList.add('mute');
                        }
                    }
                },
            },

            // If we need pagination
            // pagination: {
            //   el: '.swiper-pagination',
            // },

            // Navigation arrows
            //navigation: {
            //    nextEl: '.swiper-videogallery-button-next',
            //    prevEl: '.swiper-videogallery-button-prev',
            //},

            // And if we need scrollbar
            // scrollbar: {
            // el: '.swiper-scrollbar',
            // draggable: true,
            // },    
        });

        /*** end second slider ***/

        for (j = 0; j < swiperVideoThumbs.length; j++) {
            var mySwiperThumbs = new Swiper('.swiper-videogallerythumbs-' + j, {
                // Optional parameters
                direction: 'vertical',
                breakpoints: {
                    1200: {
                        spaceBetween: 18
                    },
                    // when window width is >= 768px
                    1400: {
                        spaceBetween: 22
                    },
                    // when window width is >= 992px
                    1600: {
                        
                        spaceBetween: 24
                    }
                },
                zoom: true,
                loop: false,
                slidesPerView: 6
            });
        }

        if (mySwiper && mySwiper2) {
            mySwiper.controller.control = mySwiper2;
            mySwiper2.controller.control = mySwiper;
        }
    }
});

/**
 * Timeline Sliders
 */
document.addEventListener("DOMContentLoaded", () => {
    const timelines = document.querySelectorAll('.simpleSliderTimelineV2');
    const thumbs = document.querySelectorAll('.simpleSliderTimelineV2Thumbs');
    const nextButtons = document.querySelectorAll('.swiper-timelinev2-button-next');
    const prevButtons = document.querySelectorAll('.swiper-timelinev2-button-prev');
	//const nextButtonsMobile = document.querySelectorAll('.swiper-timelinev2-button-mobile-next');
    //const prevButtonsMobile = document.querySelectorAll('.swiper-timelinev2-button-mobile-prev');

    timelines.forEach((timeline, index) => {
        timeline.classList.add(`swiper-timelinev2-${index}`);
        nextButtons[index].classList.add(`swiper-timelinev2-button-next-${index}`);
        prevButtons[index].classList.add(`swiper-timelinev2-button-prev-${index}`);
		//nextButtonsMobile[index].classList.add(`swiper-timelinev2-button-mobile-next-${index}`);
        //prevButtonsMobile[index].classList.add(`swiper-timelinev2-button-mobile-prev-${index}`);

        const timelineSwiper = new Swiper(`.swiper-timelinev2-${index}`, {
            loop: false,
            spaceBetween: 16,
            scrollbar: {
                el: '.swiper-scrollbar-main',
                draggable: true,
            },
			/*navigation: {
				nextEl: `.swiper-timelinev2-button-mobile-next-${index}`,
				prevEl: `.swiper-timelinev2-button-mobile-prev-${index}`,
			},*/
            breakpoints: {
                320: { slidesPerView: 1 },
                768: { slidesPerView: 1, spaceBetween: 16 },
                992: { slidesPerView: 1, spaceBetween: 24, slidesOffsetAfter: 2, },
            },
        });
		
        if (thumbs[index]) {
            thumbs[index].classList.add(`swiper-timelinev2thumbs-${index}`);
            let saveSlide = '';
            let numberSlides = '';
            const thumbsSwiper = new Swiper(`.swiper-timelinev2thumbs-${index}`, {
                loop: false,
                direction: 'horizontal',
                resistanceRatio: 0,
                breakpoints: {
                    320: { 
						slidesPerView: 1, 
						slidesPerGroup: 1, 
						spaceBetween: 16, 
					},
                    768: { 
						slidesPerView: 1.5, 
						slidesPerGroup: 1, 
						spaceBetween: 16, 
					},
                    992: { 
                        slidesPerView: 2, 
                        spaceBetween: 24, 
                        slidesOffsetAfter: 2, 
						allowTouchMove: false,
                    },
                },
                navigation: {
                    nextEl: `.swiper-timelinev2-button-next-${index}`,
                    prevEl: `.swiper-timelinev2-button-prev-${index}`,
                },
                scrollbar: {
                    el: '.swiper-scrollbar-thumbs',
                    draggable: true,
                },
                dragCursor: true,
                on: {
                    afterInit: function () {
                        numberSlides = this.slides.length;
                        saveSlide = this.slides[0];
                        //console.log('NumberSlides: ' + numberSlides);
                        let desktop = window.matchMedia('(min-width: 992px)');
                        if(desktop.matches) {
                            this.removeSlide(0);
                        }                      
                    },
                    resize: function () {
                        let desktop = window.matchMedia('(min-width: 992px)');
                        if(desktop.matches) {
							this.allowTouchMove = false;
                            if(this.slides.length == numberSlides) {
                                this.removeSlide(0);
                            }    
							/*this.navigation.nextEl = `.swiper-timelinev2-button-next-${index}`;
							this.navigation.prevEl = `.swiper-timelinev2-button-prev-${index}`;*/
                        } else {
							this.allowTouchMove = true;
                            if(this.slides.length < numberSlides) {
                                this.prependSlide(saveSlide);
                            }
							/*this.navigation.nextEl = `.swiper-timelinev2-button-mobile-next-${index}`;
							this.navigation.prevEl = `.swiper-timelinev2-button-mobile-prev-${index}`;*/
                        }                      
                    },
					activeIndexChange: function() {
                        this.slides[this.activeIndex].onclick = function() {
                            thumbsSwiper.slideNext();
                        }
                    },
                  },
            });
			
			thumbsSwiper.slides[thumbsSwiper.activeIndex].onclick = function() {
                thumbsSwiper.slideNext();
            }

            thumbsSwiper.controller.control = timelineSwiper;
            timelineSwiper.controller.control = thumbsSwiper;
        }
    });
    
});

$(document).on('mouseover', '.simple-slider-timeline-v2', function() {
    // Check if the last slide is active
    if ($('.last-swipe').hasClass('swiper-slide-active')) {
        $('.swiper-timelinev2-button-next').addClass('disabled');
    } else {
        $('.swiper-timelinev2-button-next').removeClass('disabled');
    }
});
$(document).on('click', '.simple-slider-timeline-v2', function() {
    // Check if the last slide is active
    if ($('.last-swipe').hasClass('swiper-slide-active')) {
        $('.swiper-timelinev2-button-next').addClass('disabled');
    } else {
        $('.swiper-timelinev2-button-next').removeClass('disabled');
    }
});