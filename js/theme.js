(function($) {
    "use strict";
    
    // Page Loader
    $(window).on('load', function() {
        $('.page-loader').fadeOut('slow');
    });

    $(document).ready(function() {
        // Initialize WOW.js
        new WOW().init();

        // Initialize Owl Carousel
        $("#owl-intro-text").owlCarousel({
            singleItem: true,
            autoPlay: 6000,
            stopOnHover: true,
            navigation: false,
            navigationText: false,
            pagination: true,
            paginationNumbers: false,
            transitionStyle: "fadeUp"
        });

        // Smooth Scroll
        $('a.page-scroll').on('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - 60
            }, 1500, 'easeInOutExpo');
            event.preventDefault();
        });

        // Active Navigation
        $(window).scroll(function() {
            var scrollDistance = $(window).scrollTop();
            
            // Highlight menu item based on scroll position
            $('section').each(function(i) {
                if ($(this).position().top <= scrollDistance + 100) {
                    $('.navbar-nav a.active').removeClass('active');
                    $('.navbar-nav a').eq(i).addClass('active');
                }
            });
        });

        // Sticky Navbar
        $(window).scroll(function() {
            if ($(window).scrollTop() > 100) {
                $('.navbar').addClass('navbar-shrink');
            } else {
                $('.navbar').removeClass('navbar-shrink');
            }
        });

        // Portfolio Isotope Filter
        var $container = $('#portfolio');
        $container.isotope();

        $('#filters').on('click', 'a', function(e) {
            e.preventDefault();
            var filterValue = $(this).attr('data-filter');
            $container.isotope({ filter: filterValue });

            $('#filters a').removeClass('active');
            $(this).addClass('active');
        });

        // Scroll to Top
        $(window).scroll(function() {
            if ($(this).scrollTop() > 100) {
                $('.scrolltotop').fadeIn();
            } else {
                $('.scrolltotop').fadeOut();
            }
        });

        $('.scrolltotop').click(function(e) {
            e.preventDefault();
            $('html, body').animate({scrollTop: 0}, 'slow');
        });

        // Skills Animation
        $('.skill-bar').waypoint(function() {
            $('.progress .progress-bar').each(function() {
                $(this).css("width", $(this).attr("aria-valuenow") + '%');
            });
        }, { offset: '80%'} );

        // Contact Form
        $('#contact-form').on('submit', function(e) {
            e.preventDefault();
            var name = $('#name').val();
            var email = $('#email').val();
            var message = $('textarea').val();

            // Here you would typically send the form data to your server
            // For now, we'll just show a success message
            $(this).find('button').text('Message Sent!').addClass('success');
            this.reset();
            
            setTimeout(() => {
                $(this).find('button').text('Send Message').removeClass('success');
            }, 3000);
        });

        // Initialize Stellar.js
        if (!Modernizr.touch) {
            $(window).stellar({
                horizontalScrolling: false,
                responsive: true,
                scrollProperty: 'scroll',
                parallaxElements: false,
                horizontalOffset: 0,
                verticalOffset: 0
            });
        }

        // Mobile Menu Toggle
        $('.navbar-toggle').on('click', function() {
            $(this).toggleClass('active');
            $('.navbar-collapse').toggleClass('show');
        });

        // Close mobile menu on click
        $('.navbar-nav a').on('click', function() {
            $('.navbar-collapse').removeClass('show');
            $('.navbar-toggle').removeClass('active');
        });
    });
})(jQuery);
