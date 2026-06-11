document.addEventListener("DOMContentLoaded", () => {

    const swipersMap = document.querySelectorAll('.swiper-map');
    const slidersMapNext = document.querySelectorAll('.swiper-map-button-next');
    const slidersMapPrev = document.querySelectorAll('.swiper-map-button-prev');

    for(i=0; i < swipersMap.length; i++) {
        swipersMap[i].classList.add('swiper-map-' + i);
        slidersMapNext[i].classList.add('swiper-map-button-next-' + i);
        slidersMapPrev[i].classList.add('swiper-map-button-prev-' + i);

        var mySwiper = new Swiper('.swiper-map-' + i, {
            // Optional parameters
            direction: 'horizontal',
            loop: false,
            zoom: true,
            slidesPerView: 1,

            // If we need pagination
            // pagination: {
            //   el: '.swiper-pagination',
            // },
        
            // Navigation arrows
            navigation: {
            nextEl: '.swiper-map-button-next',
            prevEl: '.swiper-map-button-prev',
            },
        
            // And if we need scrollbar
            // scrollbar: {
            // el: '.swiper-scrollbar',
            // draggable: true,
            // },    
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {

    const swipersGolfMap = document.getElementsByClassName('golfMapCourseImagesSwiper');

    for(i=0; i < swipersGolfMap.length; i++) {
        swipersGolfMap[i].classList.add('swiper-map-v2-' + i);

        var mySwiperCourse = new Swiper('.swiper-map-v2-' + i, {
            // Optional parameters
            direction: 'horizontal',
            loop: false,
			//centeredSlides: false,
            //zoom: true,
            slidesPerView: 1,
			spaceBetween: 0,
			effect: "fade",
            grabCursor: true,
            navigation: {
                nextEl: '.swiper-map-button-next',
                prevEl: '.swiper-map-button-prev',
            },
                
        });
    }
	
	const swipersGolfMapInfo = document.getElementsByClassName('golfMapCourseInfoSwiper');

    for(i=0; i < swipersGolfMapInfo.length; i++) {
        swipersGolfMapInfo[i].classList.add('swiper-map-v2-info-' + i);

        var mySwiperInfo = new Swiper('.swiper-map-v2-info-' + i, {
            // Optional parameters
            direction: 'horizontal',
            loop: false,
            //zoom: true,
            //centeredSlides: false,
            slidesPerView: 2,
			slidesPerGroup: 1,
			spaceBetween: 0,
            // slidesOffsetAfter: 1,
			pagination: {
				el: ".swiper-pagination",
				type: "fraction",
			},
            grabCursor: true,
            breakpoints: {
                1920: {
                slidesPerView: 2,
                }
            },
		});
    }
	
	if(mySwiperCourse && mySwiperInfo) {
    	mySwiperInfo.controller.control = mySwiperCourse;
		mySwiperInfo.controller.by = 'slide';
    	mySwiperCourse.controller.control = mySwiperInfo;
		mySwiperCourse.controller.by = 'slide';
	}
});