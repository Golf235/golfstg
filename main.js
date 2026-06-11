//gsap.registerPlugin(ScrollTrigger);

var sections = document.querySelectorAll("section");

/**
 * Control/Animate Videos & Animation-Timeline
 */
sections.forEach((section, sectionID) => {
  var tlScroll = gsap.timeline();
  let vid = section.querySelector("video");

  //If there is a Video That is not Hero-Video module
  if (
    vid &&
    !section.classList.contains("hero-video") &&
    !section.classList.contains("product-wrapper") &&
    !section.classList.contains("info-video-gallery") &&
    !section.classList.contains("hero-video-home-p1") &&
    !section.classList.contains("hero-video-default-p1") &&
    !section.classList.contains("hero-video-home-p1") &&
    !section.classList.contains("simple-video-player")
  ) {
    //Get "next" Video
    if (sectionID >= 0 && sectionID < sections.length - 1) {
      let nextvid = sections[sectionID + 1].querySelector("video");
    }

    let logo = section.querySelector(".logo");
    let title = section.querySelector(".title");
    let content = section.querySelector(".content");
    let scrollCta = section.querySelector(".scroll-cta");

    /**
     * Setup Timeline
     */
    var tl = gsap.timeline();

    // vid.ontimeupdate = (event) => {
    //     if(vid.currentTime == vid.duration) {
    //         tl.restart();
    //         console.log('Restart Timeline');
    //     }
    // }

    //Scroll Arrow Bounce
    if (section.querySelector(".scroll-cta")) {
      tlScroll.from(
        section.querySelector(".scroll-cta").querySelector(".chevron"),
        { duration: 0.5, y: -15, ease: "circ.in", repeat: -1, yoyo: true }
      );
    }

    vid.onended = (event) => {
      // vid.currentTime = 0;
      vid.play();
      tl.play(0);
    };

    //Check if Video ready
    vid.onloadedmetadata = (event) => {
      vid.muted = true;
      vid.pause();

      if (section.classList.contains("hero-first")) {
        //Remove Logo
        tl.fromTo(
          logo,
          { opacity: 1 },
          { opacity: 0, duration: 1, delay: 2 },
          "-=0"
        );
      }

      // if(scrollCta.style.opacity == 1) {
      //     tl.fromTo(scrollCta, {opacity: 1}, {opacity: 0, duration: 1, delay: 0}, "-=0");
      // }

      //Show Title
      //tl.fromTo(title, {opacity: 0}, {opacity: 1, duration: 1, delay: 0}, "-=0");

      if (section.classList.contains("hero-first")) {
        tl.fromTo(
          title,
          { opacity: 0 },
          { opacity: 1, duration: 1, delay: 0 },
          "-=0"
        );
        title.querySelectorAll("p").forEach((para) => {
          tl.fromTo(
            para,
            { y: 300, opacity: 0 },
            { y: 0, opacity: 1, duration: 1, delay: 0 },
            "-=0.5"
          );
        });
      }

      //Split Title into Paragraphs
      // title.querySelectorAll("p").forEach( (para) => {
      //     tl.fromTo(para, {y: 300, opacity: 0}, {y: 0, opacity: 1, duration: 1, delay: 0}, "-=0.5");
      // })

      //Hide Title
      // tl.fromTo(title, {opacity: 1}, {opacity: 0, duration: 1, delay: 1}, "-=0");
      // if(section.classList.contains('hero-first')) {
      //     tl.fromTo(title, {opacity: 1}, {opacity: 0, duration: 1, delay: 1}, "-=0");
      // }

      if (section.classList.contains("hero-first")) {
        tl.fromTo(
          title,
          { opacity: 1 },
          { opacity: 0, duration: 1, delay: 1 },
          "-=0"
        );
      }

      //Show Content
      tl.fromTo(
        content,
        { opacity: 0 },
        { opacity: 1, duration: 1, delay: 0 },
        "-=0.5"
      );

      //Split Content into Paragraphs
      content.querySelectorAll("p").forEach((para) => {
        tl.fromTo(
          para,
          { y: 300, opacity: 0 },
          { y: 0, opacity: 1, duration: 1, delay: 0 },
          "-=0.5"
        );
      });

      //Hide Content
      tl.fromTo(
        content,
        { opacity: 1 },
        { opacity: 0, duration: 1, delay: 5 },
        "-=0"
      );

      //Hide Title
      // if(section.classList.contains('hero-first')) {
      //     tl.fromTo(title, {opacity: 1}, {opacity: 0, duration: 1, delay: 1}, "-=0");
      // }

      //Show Scroll CTA
      tl.fromTo(
        scrollCta,
        { opacity: 0 },
        { opacity: 1, duration: 1, delay: 0 },
        "-=0"
      );

      //Pause Timeline, wait for Video to start
      tl.pause();

      // var heroOffset = hero.offsetTop - hero.offsetHeight;

      /**
       * Scrolltrigger controls Video playback
       */
      ScrollTrigger.create({
        trigger: section,
        scroller: "body",
        start: "top bottom",
        end: "bottom top",
        scrub: 0.25,
        // markers: true,
        preventOverlaps: true,
        toggleClass: { targets: section, className: "is-active" },
        // invalidateOnRefresh: true,
        onEnter: () => {
          if (sections[sectionID].classList.contains("is-active")) {
            vid.play();
            tl.play();
          } else {
            vid.pause();
            tl.pause();
          }
        },
        onEnterBack: () => {
          if (sections[sectionID].classList.contains("is-active")) {
            vid.play();
            tl.play();
          } else {
            vid.pause();
            tl.pause();
          }
        },
        onLeave: () => {
          if (sections[sectionID].classList.contains("is-active")) {
            vid.play();
            tl.play();
          } else {
            vid.pause();
            tl.pause();
          }
        },
        onLeaveBack: () => {
          if (sections[sectionID].classList.contains("is-active")) {
            vid.play();
            tl.play();
          } else {
            vid.pause();
            tl.pause();
          }
        },
      });
    };
  }
});

/**
 * Section Scroller
 */
// let sectionScroller = ScrollTrigger.create({
//     trigger: 'section:first-of-type',
//     scroller: 'body',
//     start: 'bottom bottom',
//     endTrigger: 'section:last-of-type',
//     end: 'top top',
//     invalidateOnRefresh: false,
//     // scrub: 0.25,
//     snap: {
//         snapTo: 1 / (sections.length - 1),
//         // directional: false,
//         duration: {min: 0.025, max: 0.5}, // the snap animation should be at least 0.25 seconds, but no more than 0.75 seconds (determined by velocity)
//         // delay: 0.125, // wait 0.125 seconds from the last scroll event before doing the snapping
//         delay: 0.75,
//         ease: "power1.inOut" // the ease of the snap animation ("power3" by default)
//     },
// })

/**
 * Text-Teaser Animation
 */
var textTeasers = document.querySelectorAll(".text-teaser");

textTeasers.forEach((textTeaser) => {
  let logo = textTeaser.querySelector(".logo");
  let title = textTeaser.querySelector(".title");
  let content = textTeaser.querySelector(".content");
  let svnfrtn = textTeaser.querySelector(".svnfrtn");
  let scrollCta = textTeaser.querySelector(".scroll-cta");
  var tlScroll = gsap.timeline();

  //Scroll Arrow Bounce
  tlScroll.from(
    textTeaser.querySelector(".scroll-cta").querySelector(".chevron"),
    { duration: 0.5, y: -15, ease: "circ.in", repeat: -1, yoyo: true }
  );

  var tl = gsap.timeline({ repeat: -1, repeatDelay: 2 });

  //Show Content
  tl.fromTo(
    content,
    { opacity: 0 },
    { opacity: 1, duration: 1, delay: -1 },
    "-=0.5"
  );

  //Split Content into Paragraphs
  content.querySelectorAll("p").forEach((para) => {
    tl.fromTo(
      para,
      { y: 300, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, delay: 0 },
      "-=0.5"
    );
  });

  //Hide Content
  tl.fromTo(
    content,
    { opacity: 1 },
    { opacity: 0, duration: 1, delay: 5 },
    "-=0"
  );

  //Show Logo
  tl.fromTo(logo, { opacity: 0 }, { opacity: 1, duration: 1, delay: 0 }, "-=0");

  logo.querySelectorAll("img").forEach((para) => {
    tl.fromTo(
      para,
      { y: 300, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, delay: 0 },
      "-=0.5"
    );
  });

  //Show Title
  tl.fromTo(
    title,
    { opacity: 0 },
    { opacity: 1, duration: 1, delay: 0 },
    "-=0"
  );

  //Split Title into Paragraphs
  title.querySelectorAll("p").forEach((para) => {
    tl.fromTo(
      para,
      { y: 300, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, delay: 0 },
      "-=0.5"
    );
  });

  //Show 7>14
  tl.fromTo(
    svnfrtn,
    { opacity: 0 },
    { opacity: 1, duration: 1, delay: 0 },
    "-=0"
  );

  svnfrtn.querySelectorAll("p").forEach((para) => {
    tl.fromTo(
      para,
      { y: 300, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, delay: 0 },
      "-=0.5"
    );
  });

  //Hide 7>14
  tl.fromTo(
    svnfrtn,
    { opacity: 1 },
    { opacity: 0, duration: 1, delay: 1 },
    "-=0"
  );

  //Hide Title
  tl.fromTo(
    title,
    { opacity: 1 },
    { opacity: 0, duration: 1, delay: 1 },
    "-=0"
  );

  //Hide Logo
  tl.fromTo(logo, { opacity: 1 }, { opacity: 0, duration: 1, delay: 1 }, "-=0");

  //Show Scroll CTA
  tl.fromTo(
    scrollCta,
    { opacity: 0 },
    { opacity: 1, duration: 1, delay: 0 },
    "-=0"
  );

  tl.pause();

  ScrollTrigger.create({
    trigger: textTeaser,
    scroller: "body",
    start: "top bottom",
    end: "bottom top",
    scrub: 1,
    toggleClass: { targets: textTeaser, className: "is-active" },
    invalidateOnRefresh: true,
    onEnter: () => {
      tl.play();
    },
    onEnterBack: () => {
      if (textTeaser.classList.contains("is-active")) {
        tl.play();
      }
    },
    onLeave: () => {
      tl.pause();
    },
    onLeaveBack: () => {
      tl.pause();
    },
  });
});

/**
 * Text-Teaser Animation
 */
var newsLetterTeasers = document.querySelectorAll(".newsletter-teaser");

newsLetterTeasers.forEach((newsLetterTeaser) => {
  let title = newsLetterTeaser.querySelector(".title");
  let content = newsLetterTeaser.querySelector(".content");

  var tl = gsap.timeline({ repeat: 0 });

  //Show Title
  tl.fromTo(
    title,
    { opacity: 0 },
    { opacity: 1, duration: 1, delay: 0 },
    "-=0"
  );

  //Split Title into Paragraphs
  title.querySelectorAll("p").forEach((para) => {
    tl.fromTo(
      para,
      { y: 300, opacity: 0 },
      { y: 0, opacity: 1, duration: 1, delay: 0 },
      "-=0.5"
    );
  });

  //Show Content
  tl.fromTo(
    content,
    { opacity: 0 },
    { opacity: 1, duration: 1, delay: 0 },
    "-=0"
  );

  tl.pause();

  ScrollTrigger.create({
    trigger: newsLetterTeaser,
    scroller: "body",
    start: "top center",
    end: "bottom center",
    scrub: 1,
    // toggleActions: "restart none none reverse",
    toggleClass: { targets: newsLetterTeaser, className: "is-active" },
    invalidateOnRefresh: true,
    onEnter: () => {
      tl.restart();
    },
    onEnterBack: () => {
      tl.restart();
    },
    onLeave: () => {
      tl.pause(0);
    },
    onLeaveBack: () => {
      tl.pause(0);
    },
  });
});

/**
 * Control Accordion
 */
// document.querySelectorAll('.acc-colleagues').forEach( (accordion, accordionIdx)  => {
//     accordion.querySelectorAll('.card-colleague').forEach( (card, cardIdx ) => {
//         card.querySelector('.card-header').onclick = () => {
//             accordion.querySelectorAll('.card-colleague').forEach( (card, cardIdx ) => {
//                 if(card.querySelector('.card-header').getAttribute('aria-expanded') == 'true') {
//                     card.classList.add('no-show');
//                     card.classList.remove('show');
//                     console.log('Open');
//                 } else {
//                     card.classList.remove('no-show');
//                     card.classList.add('show');
//                     console.log('Close');
//                 }
//             })
//         }
//     })
// })

// document.querySelectorAll('.accordion-infos').forEach( (accordion, accordionIdx) => {
//     accordion.querySelector('.card-header').classList.remove('collapsed');
//     accordion.querySelector('.card-header').setAttribute('aria-expanded', 'true');
//     accordion.querySelector('.collapse').classList.add('show');
// })

// jQuery( document ).ready(function() {
//     jQuery('.acc-colleagues .card-header').click( function(e) {
//         jQuery('.collapse').collapse('hide');
//         jQuery('.card-colleague').removeClass('show');
//         jQuery(this).parent().toggleClass('show');
//         console.log('Let\'s go');
//     });
// });

document.addEventListener("DOMContentLoaded", () => {
  document
    .querySelectorAll(".acc-colleagues")
    .forEach((accordion, accordionIdx) => {
      accordion.querySelectorAll(".card-colleague").forEach((card, cardIdx) => {
        card.querySelector(".card-header").onclick = () => {
          //console.log('Click Accordion');
          accordion
            .querySelectorAll(".card-colleague")
            .forEach((card, cardIdx) => {
              card.classList.remove("show");
              card.querySelector(".card-header").classList.add("collapsed");
              card.querySelector(".collapse").classList.remove("show");
            });
        };
      });
    });
});

document.addEventListener("DOMContentLoaded", () => {
  let accordionTeam = document.querySelector(".accordion-team");
  let subAccordionTeam = document.querySelector(".colleague");

  if (accordionTeam) {
    //console.log('Hello Accordion');
    accordionTeam.querySelectorAll(".header").forEach((header) => {
      header.onclick = () => {
        //Close all
        accordionTeam.querySelectorAll(".colleague").forEach((colleague) => {
          colleague.classList.remove("show");
        });
        //Show active
        header.parentElement.classList.add("show");
      };
    });

    // accordion.querySelectorAll('.inner-header').forEach( (header) => {
    //     header.onclick = () => {
    //         //Close all
    //         // accordion.querySelectorAll('.inner').forEach( (inner) => {
    //         //     inner.classList.remove('show');
    //         //     console.log(inner);
    //         //     console.log('Remove inner Show');
    //         // })
    //         //Show active
    //         header.parentElement.classList.toggle('show');
    //     }
    // })
  }
});

/**
 * Animate Scroll CTA in Hero-Videos Module
 */
document.addEventListener("DOMContentLoaded", () => {
  var heroVideos = document.querySelectorAll(".hero-video");

  if (heroVideos) {
    heroVideos.forEach((heroVideo) => {
      var tlScroll = gsap.timeline();
      tlScroll.from(
        heroVideo.querySelector(".scroll-cta").querySelector(".chevron"),
        { duration: 0.5, y: -15, ease: "circ.in", repeat: -1, yoyo: true }
      );
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  var heroVideos = document.querySelectorAll(".hero-video-home-p1");

  if (heroVideos) {
    heroVideos.forEach((heroVideo) => {
      var tlScroll = gsap.timeline();
      tlScroll.from(
        heroVideo.querySelector(".scroll-cta").querySelector(".chevron"),
        { duration: 0.5, y: -15, ease: "circ.in", repeat: -1, yoyo: true }
      );
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  var heroVideos = document.querySelectorAll(".hero-image-v3");

  if (heroVideos) {
    heroVideos.forEach((heroVideo) => {
      var tlScroll = gsap.timeline();
      tlScroll.from(
        heroVideo.querySelector(".scroll-cta").querySelector(".chevron"),
        { duration: 0.5, y: -15, ease: "circ.in", repeat: -1, yoyo: true }
      );
    });
  }
});

/**
 * Animate Scroll CTA in Hero-Images Module
 */
document.addEventListener("DOMContentLoaded", () => {
  var heroImages = document.querySelectorAll(".hero-image");

  if (heroImages) {
    heroImages.forEach((heroImage) => {
      var tlScroll = gsap.timeline();
      tlScroll.from(
        heroImage.querySelector(".scroll-cta").querySelector(".chevron"),
        { duration: 0.5, y: -15, ease: "circ.in", repeat: -1, yoyo: true }
      );
    });
  }
});

/**
 * Show/Hide Navigation Header Responsive
 * Fixed on mobile/ Show after scroll on Tablet/Desktop
 */
document.addEventListener("DOMContentLoaded", () => {
  if (document.querySelector(".lp-product-header")) {
    let firstSection = document.querySelectorAll("section");
    let mm = gsap.matchMedia();

    mm.add("(min-width: 768px)", () => {
      //console.log('Desktop trigger');

      if (
        document
          .querySelector(".lp-product-header")
          .classList.contains("is-fixed")
      ) {
        document
          .querySelector(".lp-product-header")
          .classList.toggle("is-fixed");
      }

      if (firstSection) {
        ScrollTrigger.create({
          trigger: firstSection[0],
          scroller: "body",
          start: "top center",
          end: "bottom center",
          scrub: 1,
          //toggleActions: "restart none none reverse",
          //toggleClass: {targets: document.querySelector('.lp-product-header'), className: 'is-fixed'},
          invalidateOnRefresh: true,
          //markers: true,
          onEnterBack: () => {
            //console.log('On-EnterBack');
            document
              .querySelector(".lp-product-header")
              .classList.toggle("is-fixed");
          },
          onLeave: () => {
            //console.log('On-Leave');
            document
              .querySelector(".lp-product-header")
              .classList.toggle("is-fixed");
          },
        });
      }
    });

    mm.add("(max-width: 767px)", () => {
      // mobile setup code here...
      // console.log('Mobile trigger');
      if (firstSection) {
        if (
          !document
            .querySelector(".lp-product-header")
            .classList.contains("is-fixed")
        ) {
          document
            .querySelector(".lp-product-header")
            .classList.toggle("is-fixed");
        }
      }
    });

    // Add Hamburger Menu Activation
    //const hamburgerNav = document.querySelector('.hamburger');
    //if (hamburgerNav) {
    //    hamburgerNav.onclick = () => {
    //        hamburgerNav.classList.toggle('is-active');
    //    }
    //}
  }
});

document.addEventListener("DOMContentLoaded", () => {
  // Add Hamburger Menu Activation
  const hamburgerNav = document.querySelector(".hamburger");
  if (hamburgerNav) {
    hamburgerNav.onclick = () => {
      hamburgerNav.classList.toggle("is-active");
    };
  }
});

document.addEventListener("DOMContentLoaded", () => {
  let heroDoubleBlock = document.querySelector(".hero-double-block");

  if (heroDoubleBlock) {
    let bottomImage = heroDoubleBlock.querySelector(".image-bottom");
    let contentWrapper = heroDoubleBlock.querySelector(".content-wrapper");

    ScrollTrigger.create({
      trigger: contentWrapper,
      //start: () => `top 50%-=${contentWrapper.offsetHeight / 2}`,
      start: "center center",

      endTrigger: bottomImage,
      //end: () => `bottom 50%+=${contentWrapper.offsetHeight}`,
      end: "center center",

      // the nect line (with the arrow function) is 'a functional value' () =>
      // end: () => `${brandImageNotPin.offsetHeight - brandImagePin.offsetHeight}px 20%`,

      // this line ensures the functional value gets recalculated on resize
      invalidateOnRefresh: true,

      pin: contentWrapper,
      // pinSpacing: true,
      //   markers: {
      //     startColor: "purple",
      //     endColor: "fuschia",
      //     fontSize: "3rem",
      //     indent: 200
      //   }
    });
  }
});

// document.addEventListener("DOMContentLoaded", function(event) {
//     console.log('Swiper loaded...');
//     const swiper = new Swiper('.swiper', {
//         // Optional parameters
//         direction: 'horizontal',
//         loop: false,

//         breakpoints: {
//             // when window width is >= 320px
//             320: {
//               slidesPerView: 1,
//             },
//             // when window width is >= 768px
//             768: {
//               slidesPerView: 2,
//               spaceBetween: 30
//             },
//             // when window width is >= 992px
//             992: {
//               slidesPerView: 3,
//               spaceBetween: 40
//             }
//         },

//         // If we need pagination
//         // pagination: {
//         //   el: '.swiper-pagination',
//         // },

//         // Navigation arrows
//         navigation: {
//           nextEl: '.swiper-button-next',
//           prevEl: '.swiper-button-prev',
//         },

//         // And if we need scrollbar
//         scrollbar: {
//           el: '.swiper-scrollbar',
//           draggable: true,
//         },
//       });
// });

document.addEventListener("DOMContentLoaded", () => {
  const swipersInfo = document.querySelectorAll(".swiper-info");
  const slidersNext = document.querySelectorAll(".swiper-info-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-info-button-prev");

  for (i = 0; i < swipersInfo.length; i++) {
    swipersInfo[i].classList.add("swiper-info-" + i);
    slidersNext[i].classList.add("swiper-info-button-next-" + i);
    slidersPrev[i].classList.add("swiper-info-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-info-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 2,
          spaceBetween: 8,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          spaceBetween: 8,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-info-button-next",
        prevEl: ".swiper-info-button-prev",
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
  const swipersClub = document.querySelectorAll(".swiper-club");
  const slidersClubNext = document.querySelectorAll(".swiper-club-button-next");
  const slidersClubPrev = document.querySelectorAll(".swiper-club-button-prev");

  for (i = 0; i < swipersClub.length; i++) {
    swipersClub[i].classList.add("swiper-club-" + i);
    slidersClubNext[i].classList.add("swiper-club-button-next-" + i);
    slidersClubPrev[i].classList.add("swiper-club-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-club-" + i, {
      // Optional parameters
      direction: "horizontal",
      loop: false,
      slidesPerView: 1,
      /*
            breakpoints: {
                // when window width is >= 320px
                320: {
                slidesPerView: 1,
                },
                // when window width is >= 768px
                768: {
                slidesPerView: 2,
                spaceBetween: 8
                },
                // when window width is >= 992px
                992: {
                slidesPerView: 2,
                spaceBetween: 8
                }
            },
            */

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-club-button-next",
        prevEl: ".swiper-club-button-prev",
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
  const swipersTeam = document.querySelectorAll(".swiper-team");
  const slidersTeamNext = document.querySelectorAll(".swiper-team-button-next");
  const slidersTeamPrev = document.querySelectorAll(".swiper-team-button-prev");

  for (i = 0; i < swipersTeam.length; i++) {
    swipersTeam[i].classList.add("swiper-team-" + i);
    slidersTeamNext[i].classList.add("swiper-team-button-next-" + i);
    slidersTeamPrev[i].classList.add("swiper-team-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-team-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 2,
          spaceBetween: 8,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          spaceBetween: 8,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-team-button-next",
        prevEl: ".swiper-team-button-prev",
      },

      // And if we need scrollbar
      scrollbar: {
        el: ".swiper-scrollbar",
        draggable: true,
      },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersProducts = document.querySelectorAll(
    ".swiper-products-category"
  );
  const slidersNext = document.querySelectorAll(
    ".swiper-products-category-button-next"
  );
  const slidersPrev = document.querySelectorAll(
    ".swiper-products-category-button-prev"
  );

  for (i = 0; i < swipersProducts.length; i++) {
    swipersProducts[i].classList.add("swiper-products-category-" + i);
    slidersNext[i].classList.add("swiper-products-category-button-next-" + i);
    slidersPrev[i].classList.add("swiper-products-category-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-products-category-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1.5,
          slidesPerGroup: 1,
          spaceBetween: 12,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1.5,
          slidesPerGroup: 1,
          spaceBetween: 12,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          slidesPerGroup: 3,
          spaceBetween: 24,
        },
        // when window width is >= 992px
        1200: {
          slidesPerView: 4,
          slidesPerGroup: 4,
          spaceBetween: 24,
        },
      },
      // If we need pagination
      //pagination: {
      //el: '.swiper-products-category-pagination',
      //clickable: true,
      /*Return bullets as numbers*/
      //renderBullet: function (index, className) {
      //return '<span class="' + className + '">' + (index + 1) + "</span>";
      //},
      //},

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-products-category-button-next",
        prevEl: ".swiper-products-category-button-prev",
      },

      //And if we need scrollbar
      scrollbar: {
        el: ".swiper-scrollbar",
        draggable: true,
      },
    });

    mySwiper.on("slideChangeTransitionEnd", function () {
      let shopNavigation = document.querySelector(".shop-navigation");
      if (!shopNavigation.classList.contains("sticky")) {
        //shopNavigation.classList.add('sticky');
        ScrollTrigger.refresh();
      }
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersProducts = document.querySelectorAll(".swiper-upsells");
  //const slidersNext = document.querySelectorAll('.swiper-upsells-button-next');
  //const slidersPrev = document.querySelectorAll('.swiper-upsells-button-prev');

  for (i = 0; i < swipersProducts.length; i++) {
    swipersProducts[i].classList.add("swiper-upsells-" + i);
    //slidersNext[i].classList.add('swiper-upsells-button-next-' + i);
    //slidersPrev[i].classList.add('swiper-upsells-button-prev-' + i);

    var mySwiper = new Swiper(".swiper-upsells-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1.5,
          slidesPerGroup: 1,
          spaceBetween: 12,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1.5,
          slidesPerGroup: 1,
          spaceBetween: 12,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          slidesPerGroup: 3,
          spaceBetween: 24,
        },
        // when window width is >= 992px
        1200: {
          slidesPerView: 4,
          slidesPerGroup: 4,
          spaceBetween: 24,
        },
      },
      // If we need pagination
      //pagination: {
      //el: '.swiper-upsells-pagination',
      //clickable: true,
      /*Return bullets as numbers*/
      //renderBullet: function (index, className) {
      //return '<span class="' + className + '">' + (index + 1) + "</span>";
      //},
      //},

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-upsells-button-next",
        prevEl: ".swiper-upsells-button-prev",
      },

      // And if we need scrollbar
      scrollbar: {
        el: ".swiper-scrollbar",
        draggable: true,
      },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersProducts = document.querySelectorAll(".swiper-crosssells");
  //const slidersNext = document.querySelectorAll('.swiper-crosssells-button-next');
  //const slidersPrev = document.querySelectorAll('.swiper-crosssells-button-prev');

  for (i = 0; i < swipersProducts.length; i++) {
    swipersProducts[i].classList.add("swiper-crosssells-" + i);
    //slidersNext[i].classList.add('swiper-upsells-button-next-' + i);
    //slidersPrev[i].classList.add('swiper-upsells-button-prev-' + i);

    var mySwiper = new Swiper(".swiper-crosssells-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1.5,
          slidesPerGroup: 1,
          spaceBetween: 12,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1.5,
          slidesPerGroup: 1,
          spaceBetween: 12,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          slidesPerGroup: 3,
          spaceBetween: 24,
        },
        // when window width is >= 992px
        1200: {
          slidesPerView: 4,
          slidesPerGroup: 4,
          spaceBetween: 24,
        },
      },
      // If we need pagination
      //pagination: {
      //el: '.swiper-crosssells-pagination',
      //clickable: true,
      /*Return bullets as numbers*/
      //renderBullet: function (index, className) {
      //return '<span class="' + className + '">' + (index + 1) + "</span>";
      //},
      //},

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-crosssells-button-next",
        prevEl: ".swiper-crosssells-button-prev",
      },

      // And if we need scrollbar
      scrollbar: {
        el: ".swiper-scrollbar",
        draggable: true,
      },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersProducts = document.querySelectorAll(".swiper-related");
  //const slidersNext = document.querySelectorAll('.swiper-related-button-next');
  //const slidersPrev = document.querySelectorAll('.swiper-related-button-prev');

  for (i = 0; i < swipersProducts.length; i++) {
    swipersProducts[i].classList.add("swiper-related-" + i);
    //slidersNext[i].classList.add('swiper-related-button-next-' + i);
    //slidersPrev[i].classList.add('swiper-related-button-prev-' + i);

    var mySwiper = new Swiper(".swiper-related-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1.5,
          slidesPerGroup: 1,
          spaceBetween: 12,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1.5,
          slidesPerGroup: 1,
          spaceBetween: 12,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          slidesPerGroup: 3,
          spaceBetween: 24,
        },
        // when window width is >= 992px
        1200: {
          slidesPerView: 4,
          slidesPerGroup: 4,
          spaceBetween: 24,
        },
      },
      // If we need pagination
      //pagination: {
      //el: '.swiper-related-pagination',
      //clickable: true,
      /*Return bullets as numbers*/
      //renderBullet: function (index, className) {
      //return '<span class="' + className + '">' + (index + 1) + "</span>";
      //},
      //},

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-related-button-next",
        prevEl: ".swiper-related-button-prev",
      },

      // And if we need scrollbar
      scrollbar: {
        el: ".swiper-scrollbar",
        draggable: true,
      },
    });
  }
});

/*document.addEventListener("DOMContentLoaded", () => {

    const swiperVideos = document.querySelectorAll('.videoGalleryMainSwiper');
    const swiperVideoThumbs = document.querySelectorAll('.videoGalleryThumbSwiper');
    const swiperVideoContent = document.querySelectorAll('.videoGalleryContentSwiper');
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

    for(i=0; i < swiperVideos.length; i++) {
        swiperVideos[i].classList.add('swiper-videogallery-' + i);
        swiperVideoThumbs[i].classList.add('swiper-videogallerythumbs-' + i);
		if( swiperVideoContent.length ) {
        	swiperVideoContent[i].classList.add('swiper-videogallerycontent-' + i);
		}
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
                slidesPerView:1,
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
                    for(i=0; i < videos.length; i++) {
                        videos[i].muted = true;
						
						if(togglePlay[0].classList.contains('paused')) {
                            togglePlay[0].classList.remove('paused');
                            togglePlay[0].classList.add('playing');
                        } else if(togglePlay[0].classList.contains('playing')) {
                            videos[mySwiper.realIndex].play();
                        }

                        if(!toggleMute[0].classList.contains('mute')) {
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
		
        togglePlay[i].onclick = function() {
            if(videos[mySwiper.realIndex].paused !== true) {
                videos[mySwiper.realIndex].pause();
                this.classList.remove('playing');
                this.classList.add('paused');
            } else {
                videos[mySwiper.realIndex].play();
                this.classList.remove('paused');
                this.classList.add('playing');
            }
        }
		
		toggleStop[i].onclick = function() {
            videos[mySwiper.realIndex].pause(); 
            videos[mySwiper.realIndex].currentTime = 0;
            
            if(togglePlay[0].classList.contains('playing')) {
                togglePlay[0].classList.remove('playing');
                togglePlay[0].classList.add('paused');
            } 
        }


        toggleMute[i].onclick = function() {
            videos[mySwiper.realIndex].muted = !videos[mySwiper.realIndex].muted;

            if(videos[mySwiper.realIndex].muted != true) {
                this.classList.remove('mute');
                this.classList.add('unmute');
            } else {
                this.classList.remove('unmute');
                this.classList.add('mute');
            }
        }
    }

    for(j=0; j < swiperVideoThumbs.length; j++) {
        var mySwiperThumbs = new Swiper('.swiper-videogallerythumbs-' + j, {
            // Optional parameters
            direction: 'horizontal',
            zoom: true,
            loop: false,
            slidesPerView: 6,
            spaceBetween: 24
        });
    } 

    for(k=0; k < swiperVideoContent.length; k++) {
        var mySwiperContent = new Swiper('.swiper-videogallerycontent-' + k, {
            // Optional parameters
            direction: 'horizontal',
            zoom: true,
            loop: false,
            slidesPerView: 1,
            spaceBetween: 24,
            // thumbs: {
            //     swiper: swiperVideoThumbs[k],
            // }
        });
    }

	if(mySwiper && mySwiperContent) {
    	mySwiperContent.controller.control = mySwiper;
    	mySwiper.controller.control = mySwiperContent;
	}

});*/

document.addEventListener("DOMContentLoaded", () => {
  const swiperProductVideos = document.querySelectorAll(
    ".videoProductMainSwiper"
  );
  const swiperProductVideoThumbs = document.querySelectorAll(
    ".videoProductThumbSwiper"
  );
  const swiperProductVideoContent = document.querySelectorAll(
    ".videoGalleryContentSwiper"
  );
  const toggleMute = document.querySelectorAll(".audio-toggle");
  const togglePlay = document.querySelectorAll(".audio-play");
  const toggleStop = document.querySelectorAll(".audio-stop");
  const slidersVideoGalleryNext = document.querySelectorAll(
    ".swiper-productvideogallery-button-next"
  );
  const slidersVideoGalleryPrev = document.querySelectorAll(
    ".swiper-productvideogallery-button-prev"
  );

  // const videos = swiperVideos[i].querySelectorAll('video');

  // for(i=0; i < videos.length; i++) {
  //     videos[i].onclick = function() {
  //         this.muted = !this.muted;
  //     }
  // }

  for (i = 0; i < swiperProductVideos.length; i++) {
    swiperProductVideos[i].classList.add("swiper-productvideogallery-" + i);
    swiperProductVideoThumbs[i].classList.add(
      "swiper-productvideogallerythumbs-" + i
    );
    if (swiperProductVideoContent.length) {
      swiperProductVideoContent[i].classList.add(
        "swiper-productvideogallerycontent-" + i
      );
    }
    toggleMute[i].classList.add("audio-toggle-" + i);
    togglePlay[i].classList.add("audio-play-" + i);
    toggleStop[i].classList.add("audio-stop-" + i);
    slidersVideoGalleryNext[i].classList.add(
      "swiper-productvideogallery-button-next-" + i
    );
    slidersVideoGalleryPrev[i].classList.add(
      "swiper-productvideogallery-button-prev-" + i
    );

    const videos = swiperProductVideos[i].querySelectorAll("video");

    var mySwiper = new Swiper(".swiper-productvideogallery-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,

      thumbs: {
        swiper: swiperProductVideoThumbs[i],
      },

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1,
          spaceBetween: 8,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 1,
          spaceBetween: 8,
        },
      },
      on: {
        slideChange: function () {
          for (i = 0; i < videos.length; i++) {
            videos[i].muted = true;

            if (togglePlay[0].classList.contains("paused")) {
              togglePlay[0].classList.remove("paused");
              togglePlay[0].classList.add("playing");
            } else if (togglePlay[0].classList.contains("playing")) {
              videos[mySwiper.realIndex].play();
            }

            if (!toggleMute[0].classList.contains("mute")) {
              toggleMute[0].classList.remove("unmute");
              toggleMute[0].classList.add("mute");
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
        nextEl: ".swiper-productvideogallery-button-next",
        prevEl: ".swiper-productvideogallery-button-prev",
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
        this.classList.remove("playing");
        this.classList.add("paused");
      } else {
        videos[mySwiper.realIndex].play();
        this.classList.remove("paused");
        this.classList.add("playing");
      }
    };

    toggleStop[i].onclick = function () {
      videos[mySwiper.realIndex].pause();
      videos[mySwiper.realIndex].currentTime = 0;

      if (togglePlay[0].classList.contains("playing")) {
        togglePlay[0].classList.remove("playing");
        togglePlay[0].classList.add("paused");
      }
    };

    toggleMute[i].onclick = function () {
      videos[mySwiper.realIndex].muted = !videos[mySwiper.realIndex].muted;

      if (videos[mySwiper.realIndex].muted != true) {
        this.classList.remove("mute");
        this.classList.add("unmute");
      } else {
        this.classList.remove("unmute");
        this.classList.add("mute");
      }
    };
  }

  for (j = 0; j < swiperProductVideoThumbs.length; j++) {
    var mySwiperProductThumbs = new Swiper(
      ".swiper-productvideogallerythumbs-" + j,
      {
        // Optional parameters
        direction: "horizontal",
        zoom: true,
        loop: false,
        slidesPerView: 3,
        grid: {
          rows: 2,
        },
        spaceBetween: 24,
      }
    );
  }

  for (k = 0; k < swiperProductVideoContent.length; k++) {
    var mySwiperProductContent = new Swiper(
      ".swiper-productvideogallerycontent-" + k,
      {
        // Optional parameters
        direction: "horizontal",
        zoom: true,
        loop: false,
        slidesPerView: 6,
        grid: {
          rows: 1,
        },
        spaceBetween: 24,
        // thumbs: {
        //     swiper: swiperVideoThumbs[k],
        // }
      }
    );
  }

  if (mySwiper && mySwiperProductContent) {
    mySwiperProductContent.controller.control = mySwiper;
    mySwiper.controller.control = mySwiperProductContent;
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersMap = document.querySelectorAll(".swiper-map");
  const slidersMapNext = document.querySelectorAll(".swiper-map-button-next");
  const slidersMapPrev = document.querySelectorAll(".swiper-map-button-prev");

  for (i = 0; i < swipersMap.length; i++) {
    swipersMap[i].classList.add("swiper-map-" + i);
    slidersMapNext[i].classList.add("swiper-map-button-next-" + i);
    slidersMapPrev[i].classList.add("swiper-map-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-map-" + i, {
      // Optional parameters
      direction: "horizontal",
      loop: false,
      zoom: true,
      slidesPerView: 1,

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-map-button-next",
        prevEl: ".swiper-map-button-prev",
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
  const swipersProduct = document.querySelectorAll(".swiper-single-product");
  const swipersProductNext = document.querySelectorAll(
    ".swiper-single-product-button-next"
  );
  const swipersProductPrev = document.querySelectorAll(
    ".swiper-single-product-button-prev"
  );

  for (i = 0; i < swipersProduct.length; i++) {
    swipersProduct[i].classList.add("swiper-single-product-" + i);
    swipersProductNext[i].classList.add(
      "swiper-single-product-button-next-" + i
    );
    swipersProductPrev[i].classList.add(
      "swiper-single-product-button-prev-" + i
    );

    var mySwiper = new Swiper(".swiper-single-product-" + i, {
      // Optional parameters
      direction: "horizontal",
      loop: false,
      //zoom: true,
      slidesPerView: 1,

      // If we need pagination
      pagination: {
        el: ".swiper-single-product-pagination",
        clickable: true,
      },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-single-product-button-next",
        prevEl: ".swiper-single-product-button-prev",
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
  const map = document.querySelector(".map svg");

  if (map) {
    let maker = {
      areaActive: map.querySelector("#Maker_active"),
      area: map.querySelector("#Maker_geometric"),
      areashow: map.querySelector("#Maker_area"),
      connectors: map.querySelector("#Maker_pointer"),
      infoBox: map.querySelector("#Maker_club"),
    };

    maker.infoBox.style.opacity = "0";
    maker.areaActive.style.opacity = "0";
    maker.connectors.style.opacity = "0";

    let saver = {
      areaActive: map.querySelector("#_1Saver_active"),
      areaActive2: map.querySelector("#_2Saver_active"),
      areaShow: map.querySelector("#_1Saver_area"),
      areaShow2: map.querySelector("#_2Saver_area"),
      area: map.querySelector("#_1Saver_geometric"),
      area2: map.querySelector("#_2Saver_geometric"),
      connectors: map.querySelector("#_1Saver_pointer"),
      connectors2: map.querySelector("#_2Saver_pointer"),
      infoBox: map.querySelector("#Saver_club"),
    };

    saver.infoBox.style.opacity = "0";
    saver.areaActive.style.opacity = "0";
    saver.areaActive2.style.opacity = "0";
    saver.connectors.style.opacity = "0";
    saver.connectors2.style.opacity = "0";

    let pitcher = {
      areaActive: map.querySelector("#Pitcher_active"),
      area: map.querySelector("#Pitcher_geometric"),
      areaShow: map.querySelector("#Pitcher_area"),
      connectors: map.querySelector("#Pitcher_pointer"),
      infoBox: map.querySelector("#Pitcher_club"),
    };

    pitcher.infoBox.style.opacity = "0";
    pitcher.areaActive.style.opacity = "0";
    pitcher.connectors.style.opacity = "0";

    let riser = {
      areaActive: map.querySelector("#Riser_active"),
      area: map.querySelector("#Riser_geometric"),
      connectors: map.querySelector("#Riser_pointer"),
      infoBox: map.querySelector("#Riser_club"),
    };

    riser.infoBox.style.opacity = "0";
    riser.areaActive.style.opacity = "0";
    riser.connectors.style.opacity = "0";

    let butler = {
      areaActive: map.querySelector("#Butler_active"),
      area: map.querySelector("#Butler_geometric"),
      connectors: map.querySelector("#Butler_pointer"),
      infoBox: map.querySelector("#Butler_club"),
    };

    butler.infoBox.style.opacity = "0";
    butler.areaActive.style.opacity = "0";
    butler.connectors.style.opacity = "0";

    let mover = {
      areaActive: map.querySelector("#Mover_active"),
      area: map.querySelector("#Mover_geometric"),
      connectors: map.querySelector("#Mover_pointer"),
      infoBox: map.querySelector("#Mover_club"),
    };

    mover.infoBox.style.opacity = "0";
    mover.areaActive.style.opacity = "0";
    mover.connectors.style.opacity = "0";

    let opener = {
      areaActive: map.querySelector("#Opener_active"),
      area: map.querySelector("#Opener_geometric"),
      connectors: map.querySelector("#Opener_pointer"),
      infoBox: map.querySelector("#Opener_club"),
    };

    opener.infoBox.style.opacity = "0";
    opener.areaActive.style.opacity = "0";
    opener.connectors.style.opacity = "0";

    maker.area.onmouseover = function () {
      maker.area.style.opacity = "1";
      //maker.areashow.style.opacity = '1';
      maker.areaActive.style.opacity = "1";
      maker.connectors.style.opacity = "1";
      maker.infoBox.style.opacity = "1";
    };

    maker.area.onmouseout = function () {
      maker.area.style.opacity = "0";
      //maker.areashow.style.opacity = '0';
      maker.areaActive.style.opacity = "0";
      maker.connectors.style.opacity = "0";
      maker.infoBox.style.opacity = "0";
    };

    saver.area.onmouseover = function () {
      saver.area.style.opacity = "1";
      saver.area2.style.opacity = "1";
      saver.areaActive.style.opacity = "1";
      saver.areaActive2.style.opacity = "1";
      //saver.areaShow.style.opacity = '1';
      //saver.areaShow2.style.opacity = '1';
      saver.connectors.style.opacity = "1";
      saver.connectors2.style.opacity = "1";
      saver.infoBox.style.opacity = "1";
    };

    saver.area2.onmouseover = function () {
      saver.area.style.opacity = "1";
      saver.area2.style.opacity = "1";
      saver.areaActive.style.opacity = "1";
      saver.areaActive2.style.opacity = "1";
      //saver.areaShow.style.opacity = '1';
      //saver.areaShow2.style.opacity = '1';
      saver.connectors.style.opacity = "1";
      saver.connectors2.style.opacity = "1";
      saver.infoBox.style.opacity = "1";
    };

    saver.area.onmouseout = function () {
      saver.area.style.opacity = "0";
      saver.area2.style.opacity = "0";
      saver.areaActive.style.opacity = "0";
      saver.areaActive2.style.opacity = "0";
      //saver.areaShow.style.opacity = '0';
      //saver.areaShow2.style.opacity = '0';
      saver.connectors.style.opacity = "0";
      saver.connectors2.style.opacity = "0";
      saver.infoBox.style.opacity = "0";
    };

    saver.area2.onmouseout = function () {
      saver.area.style.opacity = "0";
      saver.area2.style.opacity = "0";
      saver.areaActive.style.opacity = "0";
      saver.areaActive2.style.opacity = "0";
      //saver.areaShow.style.opacity = '0';
      //saver.areaShow2.style.opacity = '0';
      saver.connectors.style.opacity = "0";
      saver.connectors2.style.opacity = "0";
      saver.infoBox.style.opacity = "0";
    };

    pitcher.area.onmouseover = function () {
      pitcher.area.style.opacity = "1";
      pitcher.areaActive.style.opacity = "1";
      //pitcher.areaShow.style.opacity = '1';
      pitcher.connectors.style.opacity = "1";
      pitcher.infoBox.style.opacity = "1";
    };

    pitcher.area.onmouseout = function () {
      pitcher.area.style.opacity = "0";
      pitcher.areaActive.style.opacity = "0";
      pitcher.connectors.style.opacity = "0";
      pitcher.infoBox.style.opacity = "0";
    };

    riser.area.onmouseover = function () {
      riser.area.style.opacity = "1";
      riser.areaActive.style.opacity = "1";
      riser.connectors.style.opacity = "1";
      riser.infoBox.style.opacity = "1";
    };

    riser.area.onmouseout = function () {
      riser.area.style.opacity = "0";
      riser.areaActive.style.opacity = "0";
      riser.connectors.style.opacity = "0";
      riser.infoBox.style.opacity = "0";
    };

    butler.area.onmouseover = function () {
      butler.area.style.opacity = "1";
      butler.areaActive.style.opacity = "1";
      butler.connectors.style.opacity = "1";
      butler.infoBox.style.opacity = "1";
    };

    butler.area.onmouseout = function () {
      butler.area.style.opacity = "0";
      butler.areaActive.style.opacity = "0";
      butler.connectors.style.opacity = "0";
      butler.infoBox.style.opacity = "0";
    };

    mover.area.onmouseover = function () {
      mover.area.style.opacity = "1";
      mover.areaActive.style.opacity = "1";
      mover.connectors.style.opacity = "1";
      mover.infoBox.style.opacity = "1";
    };

    mover.area.onmouseout = function () {
      mover.area.style.opacity = "0";
      mover.areaActive.style.opacity = "0";
      mover.connectors.style.opacity = "0";
      mover.infoBox.style.opacity = "0";
    };

    opener.area.onmouseover = function () {
      opener.area.style.opacity = "1";
      opener.areaActive.style.opacity = "1";
      opener.connectors.style.opacity = "1";
      opener.infoBox.style.opacity = "1";
    };

    opener.area.onmouseout = function () {
      opener.area.style.opacity = "0";
      opener.areaActive.style.opacity = "0";
      opener.connectors.style.opacity = "0";
      opener.infoBox.style.opacity = "0";
    };
  }
});

document.addEventListener("DOMContentLoaded", () => {
  if (document.querySelector(".team-slider")) {
    let teamSlider = document.querySelector(".team-slider");
    let openBios = teamSlider.querySelectorAll(".open");
    let closeBios = teamSlider.querySelectorAll(".close");

    openBios.forEach(function (openBio) {
      openBio.addEventListener("click", function () {
        let slideID = openBio.getAttribute("data-open");
        let slide = teamSlider.querySelector('[data-slide="' + slideID + '"]');
        let open = teamSlider.querySelector('[data-open="' + slideID + '"]');
        let close = teamSlider.querySelector('[data-close="' + slideID + '"]');

        slide.querySelector(".images-wrapper > .cover-hover").style.opacity = 1;
        slide.querySelector(".content").style.opacity = 1;
        open.style.display = "none";
        close.style.display = "block";
      });
    });

    closeBios.forEach(function (closeBio) {
      closeBio.addEventListener("click", function () {
        let slideID = closeBio.getAttribute("data-close");
        let slide = teamSlider.querySelector('[data-slide="' + slideID + '"]');
        let open = teamSlider.querySelector('[data-open="' + slideID + '"]');
        let close = teamSlider.querySelector('[data-close="' + slideID + '"]');

        slide.querySelector(".images-wrapper > .cover-hover").style.opacity = 0;
        slide.querySelector(".content").style.opacity = 0;
        open.style.display = "block";
        close.style.display = "none";
      });
    });
  }
});

//Anchor Links on Load
//jQuery.noConflict();
$(document).ready(function () {
  if (window.location.hash.length > 0 && window.location.hash != "#/") {
    //Get Header height
    headerHeight = $("header").height();
    window.scrollTo(0, $(window.location.hash).offset().top - headerHeight);
    //console.log('Scroller activated to: ' + window.location.hash + ' at position: ' + $(window.location.hash).offset().top);
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const simpleLightBoxes = document.querySelectorAll(".lightboxgallery");

  for (i = 0; i < simpleLightBoxes.length; i++) {
    simpleLightBoxes[i].classList.add("lightbox-gallery-" + i);

    var mySimpleLightBox = new SimpleLightbox(
      ".lightbox-gallery-" + i + " .row .col-6 .image-wrapper a",
      {
        overlayOpacity: 0.85,
      }
    );
    // mySimpleLightBox.open();
    mySimpleLightBox.on("error.simplelightbox", function (e) {
      console.log(e); // some usefull information
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  var elems = document.querySelectorAll(".shop-navigation a");

  if (elems.length) {
    elems[0].classList.toggle("active");
  }

  for (i = 0; i < elems.length; i++) {
    var clicked = elems[i];
    clicked.addEventListener("click", function () {
      var active = document.querySelector(".shop-navigation a.active");
      if (active) {
        active.classList.remove("active");
      }

      this.classList.add("active");
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementsByClassName("shop-navigation").length) {
    let shopNavigation = gsap.timeline({
      // yes, we can add it to an entire timeline!
      scrollTrigger: {
        trigger: ".shop-navigation",
        endTrigger: ".products-by-category",
        pin: true, // pin the trigger element while active
        pinSpacing: false,
        //start: "top top+=" + document.querySelector("header").offsetHeight,
        start: () =>
          `top top+=${document.querySelector("header").offsetHeight}`,
        end: "bottom center",
        invalidateOnRefresh: true,
        scrub: 1, // smooth scrubbing, takes 1 second to "catch up" to the scrollbar
        toggleClass: "sticky",
        //markers: true,
      },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  var elems = document.querySelectorAll(".page-sub-navigation a");

  if (elems.length) {
    elems[0].classList.toggle("active");
  }

  for (i = 0; i < elems.length; i++) {
    var clicked = elems[i];
    clicked.addEventListener("click", function () {
      var active = document.querySelector(".page-sub-navigation a.active");
      if (active) {
        active.classList.remove("active");
      }

      this.classList.add("active");
    });
  }
});

// document.addEventListener("DOMContentLoaded", () => {
//   if (document.getElementsByClassName("page-sub-navigation").length) {
//     let shopNavigation = gsap.timeline({
//       // yes, we can add it to an entire timeline!
//       scrollTrigger: {
//         trigger: ".page-sub-navigation",
//         endTrigger: ".info-form-bgimage-p1",
//         pin: true, // pin the trigger element while active
//         pinSpacing: false,
//         //start: "top top+=" + document.querySelector("header").offsetHeight,
//         start: () =>
//           `top top+=${document.querySelector("header").offsetHeight}`,
//         end: "bottom center",
//         invalidateOnRefresh: true,
//         scrub: 1, // smooth scrubbing, takes 1 second to "catch up" to the scrollbar
//         toggleClass: "sticky",
//         //markers: true,
//       },
//     });
//   }
// });

/*
document.addEventListener("DOMContentLoaded", () => {
		
	if(document.getElementsByClassName('footer-logo-wrapper').length) {
		ScrollTrigger.create({
			trigger: ".footer-logo",
			//endTrigger: ".footer-content",
			pin: ".footer-logo", // pin the trigger element while active
			pinSpacing: false,
			invalidateOnRefresh: true,
			//start: "top center-=100%",
			//start: () => "top center-=" + document.querySelector(".footer-logo").offsetHeight,
			//start: () => `top center-=${document.querySelector(".footer-logo").offsetHeight}`,
			start: () => `top center`,
			//end: () => "top center",
			end: () => "+=350",
			scrub: 1, // smooth scrubbing, takes 1 second to "catch up" to the scrollbar
			//toggleClass: "sticky",
			//markers: true,
			onRefresh: () => {
				//console.log('Trigger Refreshed...');
			},
			id: "footer-scroller",
		});
	}
});
*/

document.addEventListener("DOMContentLoaded", () => {
  let wrapper = document.getElementById("detail-wrapper");
  let productContainer = document.getElementsByClassName("product")[0];
  let headerHeight = document.querySelector("header").offsetHeight;

  let mm = gsap.matchMedia();

  if (wrapper) {
    mm.add("(min-width: 1200px)", () => {
      /*gsap.timeline({
			scrollTrigger: {
			  trigger: ".detail-wrapper",
			  endTrigger: ".product",
			  pin: ".details", // pin the trigger element while active
			  pinSpacing: false,
			  invalidateOnRefresh: true,
			  start: () => "top top+=" + headerHeight,
			  //start: () => `top top+=${headerHeight}`,
			  //end: () => `+=${document.getElementsByClassName('product')[0].offsetHeight}`,
			  //end: () => "bottom top-=" + document.querySelector("header").offsetHeight + document.getElementById('detail-wrapper'),
			  end: () => `bottom top+=${document.querySelector("header").offsetHeight + document.getElementById('detail-wrapper').offsetHeight}`,
			  //scrub: 1, // smooth scrubbing, takes 1 second to "catch up" to the scrollbar
			  //toggleClass: "sticky",
			  //markers: true,
			  onRefresh: () => {
				//console.log('Trigger Refreshed... Product Container Height: ' + document.getElementsByClassName('product')[0].offsetHeight);
			  },
			},
		  });*/

      ScrollTrigger.create({
        trigger: ".detail-wrapper",
        endTrigger: ".product",
        pin: ".details", // pin the trigger element while active
        pinSpacing: false,
        invalidateOnRefresh: true,
        start: () => "top top+=" + headerHeight,
        //start: () => `top top+=${headerHeight}`,
        //end: () => `+=${document.getElementsByClassName('product')[0].offsetHeight}`,
        //end: () => "bottom top-=" + document.querySelector("header").offsetHeight + document.getElementById('detail-wrapper'),
        end: () =>
          `bottom top+=${
            document.querySelector("header").offsetHeight +
            document.getElementById("detail-wrapper").offsetHeight
          }`,
        //scrub: 1, // smooth scrubbing, takes 1 second to "catch up" to the scrollbar
        //toggleClass: "sticky",
        //markers: true,
        onRefresh: () => {
          //console.log('Trigger Refreshed... Product Container Height: ' + document.getElementsByClassName('product')[0].offsetHeight);
        },
        id: "product-details-scroller",
      });
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  let accButtons = document.getElementsByClassName("accordion-collapse");

  if (accButtons.length) {
    for (i = 0; i < accButtons.length; i++) {
      var clicked = accButtons[i];
      //let productContainerHeight = document.getElementsByClassName('product')[0].offsetHeight;
      clicked.addEventListener("shown.bs.collapse", function () {
        ScrollTrigger.refresh();
        //console.log('ScrollTriggers refreshed by shown.');
      });
      clicked.addEventListener("hidden.bs.collapse", function () {
        ScrollTrigger.refresh();
        //console.log('ScrollTriggers refreshed by hidden.');
      });
    }
  }
});

/*
const resizeObserver = new ResizeObserver((entries) => {
	console.log('Refresh ScrollTriggers!');
  ScrollTrigger.refresh();
});
resizeObserver.observe(document.querySelector('main'));
*/
/*
const myObserver = new ResizeObserver(entries => {
  entries.forEach(entry => {
    console.log('height', entry.contentRect.height);
	ScrollTrigger.refresh();
  });
});

const someEl = document.querySelector('.product');
//myObserver.observe(someEl);
*/
/*
const locoScroll = new LocomotiveScroll({
	el: document.querySelector(".smooth-scroll"),
	smooth: true
});
*/
/*
function handleLazyLoad(config={}) {
  let lazyImages = gsap.utils.toArray("img[loading='lazy']"),
      timeout = gsap.delayedCall(config.timeout || 1, ScrollTrigger.refresh).pause(),
      lazyMode = config.lazy !== false,
      imgLoaded = lazyImages.length,
      onImgLoad = () => lazyMode ? timeout.restart(true) : --imgLoaded || ScrollTrigger.refresh();
  lazyImages.forEach((img, i) => {
    lazyMode || (img.loading = "eager");
    img.naturalWidth ? onImgLoad() : img.addEventListener("load", onImgLoad);
  });
}

// usage: you can optionally set lazy to false to change all images to load="eager". timeout is how many seconds it throttles the loading events that call ScrollTrigger.refresh()
handleLazyLoad({ lazy: false, timeout: 1 });

window.addEventListener("resize", () => {
		ScrollTrigger.refresh();
	}
);
*/

/*
document.addEventListener('DOMContentLoaded', function () {
 const lazyImages = Array.from(document.querySelectorAll("img[loading='lazy']"));
 lazyImages.forEach(function (lazyImage) {
   lazyImage.addEventListener('load', function () {
	   console.log('Lazy Load Image loaded...');
     ScrollTrigger.refresh();
   });
 });
});
*/

document.addEventListener("DOMContentLoaded", () => {
  let specToggles = document.getElementsByClassName("specification");

  if (specToggles.length) {
    for (i = 0; i < specToggles.length; i++) {
      var clicked = specToggles[i];

      clicked.addEventListener("click", function () {
        this.classList.toggle("active");
        //console.log('Toggle Clicked.');
      });
    }
  }
});

window.addEventListener("resize", function (event) {
  let activeSpecs = document.getElementsByClassName("specification");

  if (activeSpecs.length) {
    for (i = 0; i < activeSpecs.length; i++) {
      var activeSpec = activeSpecs[i];
      activeSpec.classList.remove("active");
    }
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersSimple = document.querySelectorAll(".simpleSlider");
  const slidersNext = document.querySelectorAll(".swiper-simple-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-simple-button-prev");

  for (i = 0; i < swipersSimple.length; i++) {
    swipersSimple[i].classList.add("swiper-simple-" + i);
    slidersNext[i].classList.add("swiper-simple-button-next-" + i);
    slidersPrev[i].classList.add("swiper-simple-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-simple-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1,
          spaceBetween: 16,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 2,
          spaceBetween: 16,
        },
        1200: {
          slidesPerView: 3,
          spaceBetween: 16,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-simple-button-next",
        prevEl: ".swiper-simple-button-prev",
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
  const swipersSimpleV2 = document.querySelectorAll(".simpleSliderV2");
  const slidersNext = document.querySelectorAll(".swiper-simplev2-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-simplev2-button-prev");

  for (i = 0; i < swipersSimpleV2.length; i++) {
    swipersSimpleV2[i].classList.add("swiper-simplev2-" + i);
    slidersNext[i].classList.add("swiper-simplev2-button-next-" + i);
    slidersPrev[i].classList.add("swiper-simplev2-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-simplev2-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 2,
          spaceBetween: 16,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          spaceBetween: 16,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-simplev2-button-next",
        prevEl: ".swiper-simplev2-button-prev",
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
  const swipersSimple4Cols = document.querySelectorAll(".simpleSlider4Cols");

  for (i = 0; i < swipersSimple4Cols.length; i++) {
    swipersSimple4Cols[i].classList.add("swiper-simple4cols-" + i);

    var mySwiper = new Swiper(".swiper-simple4cols-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
          spaceBetween: -12,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 4,
          spaceBetween: 0,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 4,
          spaceBetween: 0,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      //navigation: {
      //nextEl: '.swiper-simplev2-button-next',
      //prevEl: '.swiper-simplev2-button-prev',
      //},

      // And if we need scrollbar
      // scrollbar: {
      // el: '.swiper-scrollbar',
      // draggable: true,
      // },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersPastEvents = document.querySelectorAll(".pastEventsSlider");
  const slidersNext = document.querySelectorAll(
    ".swiper-pastevents-button-next"
  );
  const slidersPrev = document.querySelectorAll(
    ".swiper-pastevents-button-prev"
  );

  for (i = 0; i < swipersPastEvents.length; i++) {
    swipersPastEvents[i].classList.add("swiper-pastevents-" + i);
    slidersNext[i].classList.add("swiper-pastevents-button-next-" + i);
    slidersPrev[i].classList.add("swiper-pastevents-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-pastevents-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 2,
          spaceBetween: 16,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 2,
          spaceBetween: 24,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-pastevents-button-next",
        prevEl: ".swiper-pastevents-button-prev",
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
  const swipersReviews = document.querySelectorAll(".reviewsSlider");
  const slidersNext = document.querySelectorAll(".swiper-reviews-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-reviews-button-prev");

  for (i = 0; i < swipersReviews.length; i++) {
    swipersReviews[i].classList.add("swiper-reviews-" + i);
    slidersNext[i].classList.add("swiper-reviews-button-next-" + i);
    slidersPrev[i].classList.add("swiper-reviews-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-reviews-" + i, {
      // Optional parameters
      //Every Slide height is different.
      autoHeight: true,
      direction: "horizontal",
      zoom: true,
      loop: true,

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 1,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-reviews-button-next",
        prevEl: ".swiper-reviews-button-prev",
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
  const swipersSimpleMakers = document.querySelectorAll(".simpleSliderMakers");
  const slidersNext = document.querySelectorAll(".swiper-makers-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-makers-button-prev");

  for (i = 0; i < swipersSimpleMakers.length; i++) {
    swipersSimpleMakers[i].classList.add("swiper-makers-" + i);
    slidersNext[i].classList.add("swiper-makers-button-next-" + i);
    slidersPrev[i].classList.add("swiper-makers-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-makers-" + i, {
      // Optional parameters
      direction: "horizontal",
      slidesPerView: "auto",
      noSwipingSelector: "a",
      zoom: true,
      loop: false,
      spaceBetween: 0,
      //effect: "fade",

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-makers-button-next",
        prevEl: ".swiper-makers-button-prev",
      },

      // And if we need scrollbar
      // scrollbar: {
      // el: '.swiper-scrollbar',
      // draggable: true,
      // },
      on: {
        /*activeIndexChange: function(e) {
					console.log(e);
					this.slides[this.activeIndex].onclick = function() {
					mySwiper.slideNext();
					}
				},*/
        /*click: function(swiper, event) {
					if(!event.target.classList.contains('swiper-no-swiping')) {
						swiper.slideNext();
					}
				},*/
      },
    });

    /*mySwiper.slides[mySwiper.activeIndex].onclick = function(e) {
			mySwiper.slideNext();
		}*/
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersSimpleMakers = document.querySelectorAll(".simpleSliderTech");
  const slidersNext = document.querySelectorAll(".swiper-tech-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-tech-button-prev");

  for (i = 0; i < swipersSimpleMakers.length; i++) {
    swipersSimpleMakers[i].classList.add("swiper-tech-" + i);
    slidersNext[i].classList.add("swiper-tech-button-next-" + i);
    slidersPrev[i].classList.add("swiper-tech-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-tech-" + i, {
      // Optional parameters
      direction: "horizontal",
      slidesPerView: "auto",
      noSwipingSelector: "a",
      zoom: true,
      loop: false,
      spaceBetween: 0,
      //effect: "fade",

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-tech-button-next",
        prevEl: ".swiper-tech-button-prev",
      },

      // And if we need scrollbar
      // scrollbar: {
      // el: '.swiper-scrollbar',
      // draggable: true,
      // },
      on: {
        /*activeIndexChange: function(e) {
					console.log(e);
					this.slides[this.activeIndex].onclick = function() {
					mySwiper.slideNext();
					}
				},*/
        /*click: function(swiper, event) {
					if(!event.target.classList.contains('swiper-no-swiping') && !event.target.parentNode.classList.contains('swiper-no-swiping')) {
						swiper.slideNext();
					}
				},*/
      },
    });

    /*mySwiper.slides[mySwiper.activeIndex].onclick = function(e) {
			mySwiper.slideNext();
		}*/
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersSimpleBlog = document.querySelectorAll(".simpleSliderBlog");
  const slidersNext = document.querySelectorAll(".swiper-blog-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-blog-button-prev");

  for (i = 0; i < swipersSimpleBlog.length; i++) {
    swipersSimpleBlog[i].classList.add("swiper-blog-" + i);
    slidersNext[i].classList.add("swiper-blog-button-next-" + i);
    slidersPrev[i].classList.add("swiper-blog-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-blog-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,
      spaceBetween: 0,
      //effect: "fade",
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 2,
          spaceBetween: 16,
        },
        // when window width is >= 992px
        1200: {
          slidesPerView: 3,
          spaceBetween: 24,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-blog-button-next",
        prevEl: ".swiper-blog-button-prev",
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
  const swipersClubTechSpec = document.querySelectorAll(
    ".swiper-club-tech-specs-slider"
  );
  const slidersNext = document.querySelectorAll(
    ".swiper-club-tech-specs-button-next"
  );
  const slidersPrev = document.querySelectorAll(
    ".swiper-club-tech-specs-button-prev"
  );

  for (i = 0; i < swipersClubTechSpec.length; i++) {
    swipersClubTechSpec[i].classList.add("swiper-club-tech-specs-" + i);
    slidersNext[i].classList.add("swiper-club-tech-specs-button-next-" + i);
    slidersPrev[i].classList.add("swiper-club-tech-specs-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-club-tech-specs-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,
      spaceBetween: 0,
      //effect: "fade",
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1,
          spaceBetween: 16,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 4,
          spaceBetween: 24,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-club-tech-specs-button-next",
        prevEl: ".swiper-club-tech-specs-button-prev",
      },

      // And if we need scrollbar
      scrollbar: {
        el: ".swiper-club-tech-specs-scrollbar",
        draggable: true,
      },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersClubs = document.querySelectorAll(".swiper-the-clubs-slider");
  const slidersNext = document.querySelectorAll(
    ".swiper-the-clubs-button-next"
  );
  const slidersPrev = document.querySelectorAll(
    ".swiper-the-clubs-button-prev"
  );

  for (i = 0; i < swipersClubs.length; i++) {
    swipersClubs[i].classList.add("swiper-the-clubs-" + i);
    slidersNext[i].classList.add("swiper-the-clubs-button-next-" + i);
    slidersPrev[i].classList.add("swiper-the-clubs-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-the-clubs-" + i, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,
      spaceBetween: 0,
      //effect: "fade",
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1,
          spaceBetween: 16,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 4,
          spaceBetween: 24,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-the-clubs-button-next",
        prevEl: ".swiper-the-clubs-button-prev",
      },

      // And if we need scrollbar
      scrollbar: {
        el: ".swiper-the-clubs-scrollbar",
        draggable: true,
      },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersSimpleMakers = document.querySelectorAll(
    ".simpleSliderMakers3Col"
  );
  const slidersNext = document.querySelectorAll(
    ".swiper-makers3col-button-next"
  );
  const slidersPrev = document.querySelectorAll(
    ".swiper-makers3col-button-prev"
  );

  for (i = 0; i < swipersSimpleMakers.length; i++) {
    swipersSimpleMakers[i].classList.add("swiper-makers3col-" + i);
    slidersNext[i].classList.add("swiper-makers3col-button-next-" + i);
    slidersPrev[i].classList.add("swiper-makers3col-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-makers3col-" + i, {
      // Optional parameters
      direction: "horizontal",
      //slidesPerView: 3,
      zoom: true,
      loop: false,
      spaceBetween: 0,
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 3,
          spaceBetween: 24,
        },
      },
      //effect: "fade",

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-makers3col-button-next",
        prevEl: ".swiper-makers3col-button-prev",
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
  const swipersBlogPosts = document.querySelectorAll(
    ".swiper-page-sub-navigation-slider"
  );
  const sliderScrollBar = document.querySelectorAll(
    ".swiper-page-sub-navigation-scrollbar"
  );
  //const slidersPager = document.querySelectorAll('.swiper-blogposts-pagination');

  for (j = 0; j < swipersBlogPosts.length; j++) {
    swipersBlogPosts[j].classList.add("swiper-page-sub-navigation-slider-" + j);
    sliderScrollBar[j].classList.add(
      "swiper-page-sub-navigation-scrollbar-" + j
    );

    var mySwiper = new Swiper(".swiper-page-sub-navigation-slider-" + j, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,
      slidesPerView: "auto",

      breakpoints: {
        // when window width is >= 320px
        320: {
          spaceBetween: 40,
        },
        // when window width is >= 768px
        768: {
          spaceBetween: 40,
        },
        // when window width is >= 992px
        992: {
          spaceBetween: 40,
        },
        1200: {
          spaceBetween: 40,
        },
        1440: {
          spaceBetween: 60,
        },
      },
      //navigation: {
      //  nextEl: ".swiper-blogposts-button-next-" + j,
      //  prevEl: ".swiper-blogposts-button-prev-" + j,
      //},
      //pagination: {
      //el: '.swiper-blogposts-pagination-' + i,
      //dynamicBullets: true,
      //clickable: true,
      //type: 'bullets',
      //},

      // And if we need scrollbar
      scrollbar: {
        el: ".swiper-page-sub-navigation-scrollbar-" + j,
        draggable: true,
      },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersBlogPosts = document.querySelectorAll(
    ".swiper-blogposts-slider"
  );
  const slidersNext = document.querySelectorAll(
    ".swiper-blogposts-button-next"
  );
  const slidersPrev = document.querySelectorAll(
    ".swiper-blogposts-button-prev"
  );
  const sliderScrollBar = document.querySelectorAll(
    ".swiper-blogposts-scrollbar"
  );
  //const slidersPager = document.querySelectorAll('.swiper-blogposts-pagination');

  for (j = 0; j < swipersBlogPosts.length; j++) {
    swipersBlogPosts[j].classList.add("swiper-blogposts-slider-" + j);
    slidersNext[j].classList.add("swiper-blogposts-button-next-" + j);
    slidersPrev[j].classList.add("swiper-blogposts-button-prev-" + j);
    //slidersPager[i].classList.add('swiper-blogposts-pagination-' + i);
    //slidersPager[i].classList.remove('swiper-pagination-fraction');
    sliderScrollBar[j].classList.add("swiper-blogposts-scrollbar-" + j);

    var mySwiper = new Swiper(".swiper-blogposts-slider-" + j, {
      // Optional parameters
      direction: "horizontal",
      zoom: true,
      loop: false,

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 2,
          spaceBetween: 12,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          spaceBetween: 24,
        },
      },
      navigation: {
        nextEl: ".swiper-blogposts-button-next-" + j,
        prevEl: ".swiper-blogposts-button-prev-" + j,
      },
      //pagination: {
      //el: '.swiper-blogposts-pagination-' + i,
      //dynamicBullets: true,
      //clickable: true,
      //type: 'bullets',
      //},

      // And if we need scrollbar
      scrollbar: {
        el: ".swiper-blogposts-scrollbar-" + j,
        draggable: true,
      },
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersSimpleValues = document.querySelectorAll(".simpleSliderValues");
  const slidersNext = document.querySelectorAll(".swiper-values-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-values-button-prev");

  for (i = 0; i < swipersSimpleValues.length; i++) {
    swipersSimpleValues[i].classList.add("swiper-values-" + i);
    slidersNext[i].classList.add("swiper-values-button-next-" + i);
    slidersPrev[i].classList.add("swiper-values-button-prev-" + i);

    var mySwiper = new Swiper(".swiper-values-" + i, {
      // Optional parameters
      //direction: 'horizontal',
      //slidesPerView: "auto",
      zoom: true,
      loop: false,
      spaceBetween: 16,
      //effect: "fade",

      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 1,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 2,
          spaceBetween: 16,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 3,
          spaceBetween: 16,
        },
      },

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-values-button-next",
        prevEl: ".swiper-values-button-prev",
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
  const swipersSimpleTimelineDotNav = document.querySelectorAll(
    ".simpleSliderTimelineDotNav"
  );

  for (i = 0; i < swipersSimpleTimelineDotNav.length; i++) {
    swipersSimpleTimelineDotNav[i].classList.add("swiper-timelinedotnav-" + i);

    var mySwiperTimelineDotNav = new Swiper(".swiper-timelinedotnav-" + i, {
      // Optional parameters
      direction: "horizontal",
      allowTouchMove: false,
      zoom: true,
      loop: false,
      //loopFillGroupWithBlank: true,
      spaceBetween: 0,
      slidesPerView: 1,
      //slidesPerGroup: 2,
      //freeMode: true,
      watchSlidesProgress: true,
      //effect: "fade",

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      //navigation: {
      //nextEl: '.swiper-timeline-button-next',
      //prevEl: '.swiper-timeline-button-prev',
      //},

      // And if we need scrollbar
      // scrollbar: {
      // el: '.swiper-scrollbar',
      // draggable: true,
      // },
      breakpoints: {
        // when window width is >= 320px
        320: {
          slidesPerView: 4,
        },
        // when window width is >= 768px
        768: {
          slidesPerView: 1,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: 1,
        },
      },
    });
  }

  const swipersSimpleTimeline = document.querySelectorAll(
    ".simpleSliderTimeline"
  );
  const slidersNext = document.querySelectorAll(".swiper-timeline-button-next");
  const slidersPrev = document.querySelectorAll(".swiper-timeline-button-prev");

  for (i = 0; i < swipersSimpleTimeline.length; i++) {
    swipersSimpleTimeline[i].classList.add("swiper-timeline-" + i);
    slidersNext[i].classList.add("swiper-timeline-button-next-" + i);
    slidersPrev[i].classList.add("swiper-timeline-button-prev-" + i);

    var mySwiperTimeline = new Swiper(".swiper-timeline-" + i, {
      // Optional parameters
      direction: "horizontal",
      slidesPerView: "auto",
      zoom: true,
      loop: false,
      spaceBetween: 12,
      thumbs: {
        swiper: mySwiperTimelineDotNav,
      },
      //effect: "fade",

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-timeline-button-next",
        prevEl: ".swiper-timeline-button-prev",
      },

      // And if we need scrollbar
      // scrollbar: {
      // el: '.swiper-scrollbar',
      // draggable: true,
      // },
    });
  }

  /*if(mySwiperTimeline && mySwiperTimelineDotNav) {
    	mySwiperTimelineDotNav.controller.control = mySwiperTimeline;
		mySwiperTimelineDotNav.controller.by = 'slide';
    	mySwiperTimeline.controller.control = mySwiperTimelineDotNav;
		mySwiperTimeline.controller.by = 'slide';
	}*/
});

document.addEventListener("DOMContentLoaded", () => {
  //Sticky Background with class "sticky-bg". Element should be 100vh
  var stickySections = document.querySelectorAll(".double-image");
  //var stickyBGs = document.querySelectorAll('.sticky-bg');
  var i = 0;
  let mm = gsap.matchMedia();

  mm.add("(min-width: 1200px)", () => {
    stickySections.forEach((stickySection) => {
      var stickyBG = stickySection.getElementsByClassName("sticky-bg");
      if (stickyBG) {
        ScrollTrigger.create({
          trigger: stickySection,
          scroller: "body",
          start: "top top",
          end: "bottom top",
          //markers: true,
          scrub: true,
          pin: stickyBG,
          pinSpacing: false,
          toggleClass: { targets: stickyBG, className: "sticky-active" },
          invalidateOnRefresh: true,
          id: "stickyBG-" + i,
        });
      }
      i++;
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  //Sticky Background with class "sticky-bg". Element should be 100vh
  var stickySections = document.querySelectorAll(".image-large-content");
  //var stickyBGs = document.querySelectorAll('.sticky-bg');
  var i = 0;
  let mm = gsap.matchMedia();

  mm.add("(min-width: 1200px) and not (orientation: landscape)", () => {
    stickySections.forEach((stickySection) => {
      if (stickySection.classList.contains("sticky-bg")) {
        var stickyBG = stickySection;
      }
      if (stickyBG) {
        ScrollTrigger.create({
          trigger: stickySection,
          scroller: "body",
          start: "top top",
          end: "bottom top",
          //markers: true,
          scrub: true,
          pin: stickyBG,
          pinSpacing: false,
          toggleClass: { targets: stickyBG, className: "sticky-active" },
          invalidateOnRefresh: true,
          id: "stickyBG-" + i,
        });
      }
      i++;
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  //Sticky Background with class "sticky-bg". Element should be 100vh
  var stickyRespSections = document.querySelectorAll(
    ".responsive-image-content"
  );
  //var stickyBGs = document.querySelectorAll('.sticky-bg');
  var i = 0;
  //Block on Mobile & Tablet
  let mm = gsap.matchMedia();

  mm.add("(min-width: 1200px) and not (orientation: landscape)", () => {
    stickyRespSections.forEach((stickySection) => {
      var stickyRespBG = stickySection.getElementsByClassName("sticky-bg");
      if (stickyRespBG) {
        ScrollTrigger.create({
          trigger: stickySection,
          scroller: "body",
          start: "top top",
          end: "bottom top",
          //markers: true,
          scrub: true,
          pin: stickyRespBG,
          pinSpacing: false,
          toggleClass: { targets: stickyRespBG, className: "sticky-active" },
          invalidateOnRefresh: true,
          id: "stickyRespBG-" + i,
        });
      }
      i++;
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  var stickyNavbars = document.querySelectorAll(".nav-wrapper");
  var i = 0;
  stickyNavbars.forEach((stickyNavbar) => {
    var stickyNav = stickyNavbar.getElementsByClassName("navbar-p1");
    ScrollTrigger.create({
      trigger: stickyNavbar,
      scroller: "body",
      start: "top top",
      end: "bottom top",
      //markers: true,
      scrub: true,
      endTrigger: "footer",
      pin: stickyNav,
      pinSpacing: false,
      toggleClass: { targets: stickyNav, className: "sticky-active" },
      invalidateOnRefresh: true,
      id: "stickyNav-" + i,
    });
    i++;
  });
});

document.addEventListener("DOMContentLoaded", () => {
  var navbars = document.querySelectorAll(".default-p1-header-1920 .navbar");
  var footer = document.getElementsByTagName("footer");
  var i = 0;
  let mm = gsap.matchMedia();

  //set default white background for Mobile and Tablet
  mm.add("(max-width: 1200px)", () => {
    navbars.forEach((navbar) => {
      if (!navbar.classList.contains("default-dark")) {
        navbar.classList.add("dark");
      }
    });
  });

  mm.add("(min-width: 1200px)", () => {
    navbars.forEach((navbar) => {
      if (!navbar.classList.contains("default-dark")) {
        var sections = document.getElementsByTagName("section");
        ScrollTrigger.create({
          trigger: sections[1],
          scroller: "body",
          start: "top center",
          end: "bottom top",
          //markers: true,
          scrub: true,
          endTrigger: footer[0],
          //pin: stickyNav,
          //pinSpacing: false,
          toggleClass: { targets: navbar, className: "dark" },
          invalidateOnRefresh: true,
          id: "sections-" + i,
        });
        i++;
      }
    });
  });
});

//fundamentals Video Sticky
document.addEventListener("DOMContentLoaded", () => {
  var videoSections = document.querySelectorAll(".info-video-gallery-v4");
  var headerElem = document.getElementsByTagName("header");
  var i = 0;
  let mm = gsap.matchMedia();

  mm.add("(min-width: 1200px)", () => {
    videoSections.forEach((videoSection) => {
      var videoSwiper = videoSection.getElementsByClassName(
        "videoGalleryMainWrapper"
      );
      var thumbSwiper = videoSection.getElementsByClassName(
        "videoGalleryThumbSwiperVert"
      );
      ScrollTrigger.create({
        trigger: thumbSwiper[0],
        scroller: "body",
        start: `top ${headerElem[0].offset}`,
        end: () => `bottom ${videoSwiper[0].offsetHeight}`,
        //markers: true,
        scrub: true,
        endTrigger: thumbSwiper[0],
        pin: videoSwiper,
        pinSpacing: false,
        //toggleClass: { targets: navbar, className: 'dark' },
        invalidateOnRefresh: true,
        id: "videoWrapper-" + i,
      });
      i++;
    });
  });
});

window.addEventListener("resize", () => {
  ScrollTrigger.refresh();
  console.log("Refresh Scrolltrigger!");
});

/*
 * Navigation Background Color Switch
 */
document.addEventListener("DOMContentLoaded", () => {
  var navBar = Array.from(
    document.querySelectorAll(".default-p1-header .navbar")
  );
  var navBarToggler = Array.from(
    document.querySelectorAll(".default-p1-header .navbar .navbar-toggler")
  );

  //console.log(navBarToggler);
  if (navBarToggler[0]) {
    navBarToggler[0].addEventListener("click", () => {
      if (navBarToggler[0].classList.contains("is-active")) {
        navBar[0].classList.add("is-active");
      } else {
        navBar[0].classList.remove("is-active");
      }
    });
  }
});

/*
 * MiniCart Active Switch
 */
document.addEventListener("DOMContentLoaded", () => {
  var miniCart = Array.from(
    document.querySelectorAll(".default-p1-header .custom-mini-cart")
  );
  var miniCartToggle = Array.from(
    document.querySelectorAll(
      ".default-p1-header .custom-mini-cart .wc-menu-cart__toggle-button"
    )
  );

  //console.log(navBarToggler);
  if (miniCartToggle[0]) {
    miniCartToggle[0].addEventListener("click", () => {
      if (miniCartToggle[0].classList.contains("active")) {
        miniCart[0].classList.remove("is-active");
      } else {
        miniCart[0].classList.add("is-active");
      }
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  document
    .querySelectorAll(".simple-video-player")
    .forEach((simpleVideoSection) => {
      let simpleVideoWrapper =
        simpleVideoSection.getElementsByClassName("video-wrapper")[0];
      let simpleVideo = simpleVideoSection.getElementsByTagName("video")[0];
      let playBtn = simpleVideoSection.getElementsByClassName("play")[0];
      let pauseBtn = simpleVideoSection.getElementsByClassName("pause")[0];

      if (simpleVideo) {
        simpleVideoWrapper.addEventListener("mouseover", () => {
          // console.log('Mouse Over');
          if (
            simpleVideo.currentTime > 0 &&
            !simpleVideo.paused &&
            !simpleVideo.ended &&
            simpleVideo.readyState > 2
          ) {
            pauseBtn.style.display = "block";
          }
        });

        simpleVideoWrapper.addEventListener("mouseout", () => {
          // console.log('Mouse Out');
          if (
            simpleVideo.currentTime > 0 &&
            !simpleVideo.paused &&
            !simpleVideo.ended &&
            simpleVideo.readyState > 2
          ) {
            pauseBtn.style.display = "none";
          }
        });

        simpleVideoWrapper.addEventListener("click", () => {
          if (
            simpleVideo.currentTime > 0 &&
            !simpleVideo.paused &&
            !simpleVideo.ended &&
            simpleVideo.readyState > 2
          ) {
            simpleVideo.pause();
            simpleVideo.muted = "true";
            pauseBtn.style.display = "none";
            playBtn.style.display = "block";
          } else {
            simpleVideo.play();
            simpleVideo.muted = false;
            playBtn.style.display = "none";
            pauseBtn.style.display = "block";
            setTimeout(function () {
              pauseBtn.style.display = "none";
            }, 1000);
          }
        });
      }
    });
});

window.addEventListener("load", (event) => {
  //Sticky Background with class "sticky-bg". Element should be 100vh
  var stickySections = document.querySelectorAll(".masonry-gallery");
  var i = 0;
  let mm = gsap.matchMedia();

  mm.add("(min-width: 1200px)", () => {
    stickySections.forEach((stickySection) => {
      var stickyTriggers = stickySection.querySelectorAll(".is-sticky");
      stickyTriggers.forEach((stickyTrigger) => {
        ScrollTrigger.create({
          trigger: stickySection,
          //scroller: "body",
          start: "top top",
          end: "bottom top",
          //markers: true,
          scrub: true,
          pin: stickyTrigger,
          pinSpacing: false,
          toggleClass: { targets: stickyTrigger, className: "sticky-active" },
          invalidateOnRefresh: true,
          id: "stickyTrigger-" + i,
        });
        i++;
      });
    });
  });
});

window.addEventListener("load", (event) => {
  //Sticky Background with class "sticky-bg". Element should be 100vh
  var stickySections = document.querySelectorAll(".simple-slider-makers");
  var i = 0;
  stickySections.forEach((stickySection) => {
    var stickyTriggers = stickySection.querySelectorAll(".is-sticky");
    stickyTriggers.forEach((stickyTrigger) => {
      ScrollTrigger.create({
        trigger: stickySection,
        //scroller: "body",
        start: "top top",
        end: "bottom top",
        //markers: true,
        scrub: true,
        pin: stickyTrigger,
        pinSpacing: false,
        toggleClass: { targets: stickyTrigger, className: "sticky-active" },
        invalidateOnRefresh: true,
        id: "stickyTrigger-" + i,
      });
      i++;
    });
  });
});

/**
 * Head Banner Sticky Responsive
 */
window.addEventListener("load", (event) => {
  var stickySections = document.querySelectorAll(".hero-video-home-p1");
  var footerSection = document.getElementsByTagName("footer");
  //responsive
  let mm = gsap.matchMedia();

  var i = 0;
  if (stickySections) {
    mm.add("(min-width: 1200px) and not (orientation: landscape)", () => {
      stickySections.forEach((stickySection) => {
        ScrollTrigger.create({
          trigger: stickySection,
          //scroller: "body",
          start: "top top",
          end: "bottom bottom",
          endTrigger: footerSection,
          //markers: true,
          scrub: true,
          pin: stickySection,
          pinSpacing: false,
          toggleClass: { targets: stickySection, className: "sticky-active" },
          invalidateOnRefresh: true,
          id: "stickyTrigger-" + i,
        });
        i++;
      });
    });
  }
});

/**
 * Head Banner Blog Sticky Responsive
 */
window.addEventListener("load", (event) => {
  var stickySections = document.querySelectorAll(".hero-blog-p1");
  var footerSection = document.getElementsByTagName("footer");
  //responsive
  let mm = gsap.matchMedia();

  var i = 0;
  if (stickySections) {
    mm.add("(min-width: 1200px) and not (orientation: landscape)", () => {
      stickySections.forEach((stickySection) => {
        ScrollTrigger.create({
          trigger: stickySection,
          //scroller: "body",
          start: "top top",
          end: "bottom bottom",
          endTrigger: footerSection,
          //markers: true,
          scrub: true,
          pin: stickySection,
          pinSpacing: false,
          toggleClass: { targets: stickySection, className: "sticky-active" },
          invalidateOnRefresh: true,
          id: "stickyTrigger-" + i,
        });
        i++;
      });
    });
  }
});

window.addEventListener("load", (event) => {
  let downloadMediaContainer = document.querySelectorAll(".download-media");
  let i = 0;
  let docsPage = 2;

  if (downloadMediaContainer[0]) {
    downloadMediaContainer.forEach((downloadMediacontainer) => {
      downloadMediacontainer.classList.add("container-" + i);
      let articles =
        downloadMediacontainer.querySelectorAll(".article-wrapper");
      let articlesNr = 3;
      let loadMoreBtn =
        downloadMediacontainer.querySelectorAll(".load-more-docs");

      let mobile = window.matchMedia("(max-width: 767px)");

      if (articles.length > 3) {
        loadMoreBtn[0].style.display = "block";
      } else {
        loadMoreBtn[0].style.display = "none";
      }

      loadMoreBtn[0].addEventListener("click", function (j) {
        articles.forEach((article, idx) => {
          // console.log('Idx ' + idx + ' DocsPage: ' + docsPage);
          if (idx + 1 > 3 * docsPage) {
            articles[idx].classList.add("d-none");
          } else {
            articles[idx].classList.remove("d-none");
            articles[idx].classList.add("d-flex");
          }
          articlesNr++;
        });
        //    console.log('Pages: ' + (docsPage * 4));
        //    console.log('Articles: ' + articles.length);
        if (docsPage * 3 >= articles.length) {
          loadMoreBtn[0].style.display = "none";
        }

        docsPage++;
      });
      i++;
    });
  }
});

window.addEventListener("load", (event) => {
  let shopDirectory = document.querySelectorAll(".shop-directory");

  if (shopDirectory[0]) {
    let buttonsFilter = shopDirectory[0].querySelectorAll(".btn-filter");
    let accordionShops = shopDirectory[0].querySelectorAll(".accordion");
    let loadMoreBtn = shopDirectory[0].querySelectorAll(".load-more-shops")[0];
    let shopPage = 1;
    let currentFilter = "all";
    let currentShopsNumber = 0;

    if (accordionShops[0]) {
      let shops = accordionShops[0].querySelectorAll(".accordion-item");

      displayPage = (shopPage) => {
        let shopNr = 0;

        shops.forEach((shop) => {
          if (
            shop.classList.contains(currentFilter) ||
            currentFilter == "all"
          ) {
            if (shopNr >= 7 * shopPage) {
              shop.style.display = "none";
            } else {
              shop.style.display = "block";
            }

            shopNr++;
          }
        });

        if (currentShopsNumber > 7 * shopPage) {
          loadMoreBtn.style.display = "block";
        } else {
          loadMoreBtn.style.display = "none";
        }
      };

      getCurrentShopsNumber = () => {
        currentShopsNumber = 0;
        shops.forEach((shop) => {
          if (
            shop.classList.contains(currentFilter) ||
            currentFilter == "all"
          ) {
            currentShopsNumber++;
          }
        });
      };

      getCurrentShopsNumber();
      displayPage(shopPage);

      buttonsFilter.forEach((buttonFilter) => {
        buttonFilter.onclick = (e) => {
          e.preventDefault();
          //console.log(buttonFilter.getAttribute('data-slug'));
          resetButtons();
          buttonFilter.classList.add("active");
          filterShops(buttonFilter.getAttribute("data-slug"));

          if (buttonFilter.getAttribute("data-slug") == "teaching-pros") {
            currentFilter = "trainer-only";
          } else {
            currentFilter = buttonFilter.getAttribute("data-slug");
          }

          getCurrentShopsNumber();

          if (currentShopsNumber > 7 * shopPage) {
            loadMoreBtn.style.display = "block";
          } else {
            loadMoreBtn.style.display = "none";
          }

          displayPage(1);
          getCurrentShopsNumber();
          //Refresh ScrollTrigger
          ScrollTrigger.refresh();
        };
      });

      loadMoreBtn.onclick = (e) => {
        e.preventDefault();
        shopPage++;
        displayPage(shopPage);
        //Refresh ScrollTrigger
        ScrollTrigger.refresh();
      };

      resetButtons = () => {
        buttonsFilter.forEach((buttonFilter) => {
          buttonFilter.classList.remove("active");
        });
      };

      filterShops = (filter) => {
        switch (filter) {
          case "all":
            shops.forEach((shop) => {
              shop.style.display = "block";
            });
            break;
          case "off-course":
            shops.forEach((shop) => {
              if (shop.classList.contains("off-course")) {
                shop.style.display = "block";
              } else {
                shop.style.display = "none";
              }
            });
            break;
          case "on-course":
            shops.forEach((shop) => {
              if (shop.classList.contains("on-course")) {
                shop.style.display = "block";
              } else {
                shop.style.display = "none";
              }
            });
            break;

          case "teaching-pros":
            shops.forEach((shop) => {
              if (shop.classList.contains("trainer-only")) {
                shop.style.display = "block";
              } else {
                shop.style.display = "none";
              }
            });
            break;
          default:
          // code block
        }
      };
    }
  }
});

window.addEventListener("load", (event) => {
  let duration = 2500, // these are miliseconds
    activeIndex = 0; // first item to activate
  let headlines = $(".hero-video-home-p1 h1 > span");

  if (headlines) {
    // start the loop
    //$(window).on('load', activateNext);
    activateNextHeadline();
  }

  function activateNextHeadline() {
    if (headlines.length > 1) {
      // activate current item
      headlines
        .addClass("hide-headline")
        .eq(activeIndex)
        .removeClass("hide-headline");

      // increase activeIndex and make reset at end of collection
      if (++activeIndex >= headlines.length) activeIndex = 0;

      // run the function again after duration
      setTimeout(function () {
        activateNextHeadline(activeIndex);
      }, duration);
    }
  }
});

// ------ Count-Up in numbers About page ------
document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".countup");

  const animateCountUp = (element) => {
    // Retrieve the target value from the data attribute
    const targetValue = parseInt(element.getAttribute("data-value"));
    const duration = 2000; // Adjust the animation duration in milliseconds
    let startTime = null;

    // Ease-in-out function for smoother animation
    const easeInOutQuad = (t) => (t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t);

    const step = (timestamp) => {
      if (!startTime) startTime = timestamp;
      const progress = Math.min((timestamp - startTime) / duration, 1);
      const easedProgress = easeInOutQuad(progress); // Apply easing
      const currentValue = Math.floor(easedProgress * targetValue);

      // Format the number with single quotes
      element.textContent = currentValue
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, "'");

      if (progress < 1) {
        window.requestAnimationFrame(step);
      } else {
        element.textContent = targetValue
          .toString()
          .replace(/\B(?=(\d{3})+(?!\d))/g, "'"); // Ensure final value is correct
      }
    };

    window.requestAnimationFrame(step);
  };

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCountUp(entry.target);
          observer.unobserve(entry.target); // Stop observing after animating
        }
      });
    },
    { threshold: 0.1 }
  );

  counters.forEach((counter) => {
    observer.observe(counter);
  });
});

/**
 * Sticky Newsletter
 */
/**
 * Head Banner Blog Sticky Responsive
 */
document.addEventListener("DOMContentLoaded", (event) => {
  let formAccordions = document.querySelectorAll(".form-accordion");
  let formAccordionsMini = document.querySelectorAll(".form-accordion-mini");

  if (formAccordions[0]) {
    let formAccordionsCloseBtn =
      formAccordions[0].querySelectorAll(".close-btn");
    let collapseElement = formAccordions[0].querySelectorAll(".collapse");

    if (
      localStorage.getItem("collapse_news_" + collapseElement[0].id) === "true"
    ) {
      formAccordions[0].style.display = "none";
      formAccordionsMini[0].style.display = "flex";
    } else {
      formAccordionsMini[0].style.display = "none";
      formAccordions[0].style.display = "flex";
    }

    formAccordionsCloseBtn[0].addEventListener("click", function () {
      formAccordions[0].style.display = "none";
      formAccordionsMini[0].style.display = "flex";
      let bsCollapse = new bootstrap.Collapse(collapseElement[0], {
        toggle: false,
      });
      bsCollapse.hide();
      //Set Open-Status in Local Storage
      localStorage.setItem("collapse_news_" + collapseElement[0].id, true);
    });

    formAccordionsMini[0].addEventListener("click", function () {
      formAccordionsMini[0].style.display = "none";
      formAccordions[0].style.display = "flex";
      //Remove Open-Status in Local Storage
      localStorage.removeItem("collapse_news_" + collapseElement[0].id);
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersCTANavContent = document.querySelectorAll(
    ".simpleSliderCTANavContent"
  );
  // const slidersNext = document.querySelectorAll('.swiper-ctanavcontent-button-next');
  // const slidersPrev = document.querySelectorAll('.swiper-ctanavcontent-button-prev');

  for (i = 0; i < swipersCTANavContent.length; i++) {
    swipersCTANavContent[i].classList.add("swiper-ctanavcontent-" + i);
    // slidersNext[i].classList.add('swiper-ctanavcontent-button-next-' + i);
    // slidersPrev[i].classList.add('swiper-ctanavcontent-button-prev-' + i);

    var mySwiperCTANavContent = new Swiper(".swiper-ctanavcontent-" + i, {
      // Optional parameters
      direction: "horizontal",
      slidesPerView: 1,
      zoom: true,
      loop: false,
      spaceBetween: 12,
      noSwipingClass: "swiper-no-swiping",
      initialSlide: 0,
      allowTouchMove: false,
      // thumbs: {
      // 	swiper: mySwiperCTANavThumb,
      // },
      //effect: "fade",

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      // navigation: {
      // nextEl: '.swiper-ctanavcontent-button-next',
      // prevEl: '.swiper-ctanavcontent-button-prev',
      // },

      // And if we need scrollbar
      // scrollbar: {
      // el: '.swiper-scrollbar',
      // draggable: true,
      // },
      breakpoints: {
        // when window width is >= 768px
        768: {
          slidesPerView: "auto",
          spaceBetween: 16,
          centeredSlides: true,
          centeredSlidesBounds: true,
          initialSlide: 0,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: "auto",
          spaceBetween: 16,
          centeredSlides: true,
          centeredSlidesBounds: true,
          initialSlide: 0,
        },
        1440: {
          slidesPerView: "auto",
          spaceBetween: 20,
          centeredSlides: true,
          centeredSlidesBounds: true,
          initialSlide: 0,
        },
        1920: {
          slidesPerView: "auto",
          spaceBetween: 24,
          centeredSlides: true,
          centeredSlidesBounds: true,
          slidesPerGroup: 1,
          initialSlide: 0,
        },
      },
    });

    let sliderNavButtonWrapper = document.querySelectorAll(
      ".slider-cta-nav .button-wrapper"
    );
    let sliderNavButtons = sliderNavButtonWrapper[0].getElementsByTagName("a");

    for (i = 0; i < sliderNavButtons.length; i++) {
      //console.log(sliderNavButtons[i].getAttribute('data-slide-id'));
      sliderNavButtons[i].addEventListener("click", function (e) {
        e.preventDefault();
        for (j = 0; j < sliderNavButtons.length; j++) {
          sliderNavButtons[j].classList.remove("active");
        }
        this.classList.add("active");
        mySwiperCTANavContent.slideTo(this.getAttribute("data-slide-id"));

        for (k = 0; k < mySwiperCTANavContent.slides.length; k++) {
          mySwiperCTANavContent.slides[k].classList.remove("activeslide");
          mySwiperCTANavContent.slides[
            this.getAttribute("data-slide-id")
          ].classList.add("activeslide");
        }
      });
    }
  }

  /*if(mySwiperTimeline && mySwiperTimelineDotNav) {
    	mySwiperTimelineDotNav.controller.control = mySwiperTimeline;
		mySwiperTimelineDotNav.controller.by = 'slide';
    	mySwiperTimeline.controller.control = mySwiperTimelineDotNav;
		mySwiperTimeline.controller.by = 'slide';
	}*/
});

document.addEventListener("DOMContentLoaded", () => {
  const swipersSliderTabNav = document.querySelectorAll(".simpleSliderTabNav");

  for (i = 0; i < swipersSliderTabNav.length; i++) {
    swipersSliderTabNav[i].classList.add("swiper-slidertabnav-" + i);

    var mySwiperSliderTabNav = new Swiper(".swiper-slidertabnav-" + i, {
      // Optional parameters
      direction: "horizontal",
      //allowTouchMove: false,
      zoom: true,
      loop: false,
      //loopFillGroupWithBlank: true,
      spaceBetween: 16,
      slidesPerView: "auto",
      centeredSlides: true,
      centeredSlidesBounds: true,
      slideToClickedSlide: true,
      initialSlide: 0,
      //slidesPerGroup: 2,
      //freeMode: true,
      //watchSlidesProgress: true,

      breakpoints: {
        // when window width is >= 320px
        320: {
          spaceBetween: 16,
        },
        // when window width is >= 768px
        768: {
          centeredSlides: false,
          centeredSlidesBounds: false,
          spaceBetween: 16,
        },
        // when window width is >= 992px
        992: {
          centeredSlides: false,
          centeredSlidesBounds: false,
          spaceBetween: 16,
        },
        1440: {
          centeredSlides: false,
          centeredSlidesBounds: false,
          spaceBetween: 20,
        },
      },
    });
  }

  const swipersTabNavContentImages = document.querySelectorAll(
    ".simpleSliderTabNavContentImages"
  );

  for (i = 0; i < swipersTabNavContentImages.length; i++) {
    swipersTabNavContentImages[i].classList.add(
      "swiper-tabnavcontentimages-" + i
    );
    // slidersNext[i].classList.add('swiper-ctanavcontent-button-next-' + i);
    // slidersPrev[i].classList.add('swiper-ctanavcontent-button-prev-' + i);

    var mySwiperTabNavContentImages = new Swiper(
      ".swiper-tabnavcontentimages-" + i,
      {
        // Optional parameters
        direction: "horizontal",
        slidesPerView: 1,
        zoom: true,
        loop: false,
        spaceBetween: 12,
        allowTouchMove: false,
        noSwipingClass: "swiper-no-swiping",
        // thumbs: {
        // 	swiper: mySwiperSliderTabNav,
        // },
        //effect: "fade",

        // If we need pagination
        // pagination: {
        //   el: '.swiper-pagination',
        // },

        // Navigation arrows
        // navigation: {
        //     nextEl: '.swiper-tabnavcontent-button-next',
        //     prevEl: '.swiper-tabnavcontent-button-prev',
        // },

        // And if we need scrollbar
        // scrollbar: {
        // el: '.swiper-scrollbar',
        // draggable: true,
        // },
        breakpoints: {
          // when window width is >= 768px
          768: {
            slidesPerView: "auto",
            spaceBetween: 16,
            // centeredSlides: true,
            // centeredSlidesBounds: true,
          },
          // when window width is >= 992px
          992: {
            slidesPerView: "auto",
            spaceBetween: 16,
            // centeredSlides: true,
            // centeredSlidesBounds: true,
          },
          1440: {
            slidesPerView: "auto",
            spaceBetween: 20,
            // centeredSlides: true,
            // centeredSlidesBounds: true,
          },
          1920: {
            slidesPerView: "auto",
            spaceBetween: 24,
            // centeredSlides: true,
            // centeredSlidesBounds: true,
          },
        },
      }
    );
  }

  const swipersTabNavContent = document.querySelectorAll(
    ".simpleSliderTabNavContent"
  );
  // const slidersNext = document.querySelectorAll('.swiper-ctanavcontent-button-next');
  // const slidersPrev = document.querySelectorAll('.swiper-ctanavcontent-button-prev');

  for (i = 0; i < swipersTabNavContent.length; i++) {
    swipersTabNavContent[i].classList.add("swiper-tabnavcontent-" + i);
    // slidersNext[i].classList.add('swiper-ctanavcontent-button-next-' + i);
    // slidersPrev[i].classList.add('swiper-ctanavcontent-button-prev-' + i);

    var mySwiperTabNavContent = new Swiper(".swiper-tabnavcontent-" + i, {
      // Optional parameters
      direction: "horizontal",
      slidesPerView: 1,
      zoom: true,
      loop: false,
      spaceBetween: 12,
      noSwipingClass: "swiper-no-swiping",
      thumbs: {
        swiper: mySwiperSliderTabNav,
      },
      //effect: "fade",

      // If we need pagination
      // pagination: {
      //   el: '.swiper-pagination',
      // },

      // Navigation arrows
      navigation: {
        nextEl: ".swiper-tabnavcontent-button-next",
        prevEl: ".swiper-tabnavcontent-button-prev",
      },

      // And if we need scrollbar
      // scrollbar: {
      // el: '.swiper-scrollbar',
      // draggable: true,
      // },
      breakpoints: {
        // when window width is >= 768px
        768: {
          slidesPerView: "auto",
          spaceBetween: 16,
          // centeredSlides: true,
          // centeredSlidesBounds: true,
        },
        // when window width is >= 992px
        992: {
          slidesPerView: "auto",
          spaceBetween: 16,
          // centeredSlides: true,
          // centeredSlidesBounds: true,
        },
        1440: {
          slidesPerView: "auto",
          spaceBetween: 20,
          // centeredSlides: true,
          // centeredSlidesBounds: true,
        },
        1920: {
          slidesPerView: "auto",
          spaceBetween: 24,
          // centeredSlides: true,
          // centeredSlidesBounds: true,
        },
      },
    });

    mySwiperTabNavContent.controller.control = mySwiperTabNavContentImages;
    mySwiperTabNavContentImages.controller.control = mySwiperTabNavContent;
    mySwiperTabNavContentImages.controller.control = mySwiperSliderTabNav;
    mySwiperSliderTabNav.controller.control = mySwiperTabNavContentImages;
  }

  // if(swipersTabNavContent && swipersTabNavContentImages) {
  // 	swipersTabNavContent.controller.control = swipersTabNavContentImages;
  //     swipersTabNavContent.controller.by = 'slide';
  // }

  /*if(mySwiperTimeline && mySwiperTimelineDotNav) {
    	mySwiperTimelineDotNav.controller.control = mySwiperTimeline;
		mySwiperTimelineDotNav.controller.by = 'slide';
    	mySwiperTimeline.controller.control = mySwiperTimelineDotNav;
		mySwiperTimeline.controller.by = 'slide';
	}*/
});

document.addEventListener("DOMContentLoaded", () => {
  let wrapper = document.getElementById("rethink-golf-headline");
  let productContainer = document.getElementsByClassName("rethink-golf")[0];
  let headerHeight = document.querySelector("header").offsetHeight;

  let mm = gsap.matchMedia();

  let paddingBottom = 0;

  mm.add("(min-width: 992px)", () => {
    paddingBottom = 80;
  });

  mm.add("(min-width: 1200px)", () => {
    paddingBottom = 80;
  });

  mm.add("(min-width: 1440px)", () => {
    paddingBottom = 80;
  });

  mm.add("(min-width: 1920px)", () => {
    paddingBottom = 120;
  });

  if (wrapper) {
    mm.add("(min-width: 992px)", () => {
      ScrollTrigger.create({
        trigger: ".rethink-golf-headline",
        endTrigger: ".rethink-golf",
        pin: ".rethink-golf-headline", // pin the trigger element while active
        pinSpacing: false,
        invalidateOnRefresh: true,
        //markers: true,
        start: () => "top top+=" + headerHeight,
        end: () =>
          `bottom top+=${
            document.querySelector("header").offsetHeight +
            document.getElementById("rethink-golf-headline").offsetHeight +
            paddingBottom
          }`,
        id: "rethink-golf-headline-scroller",
      });
    });
  }
});
