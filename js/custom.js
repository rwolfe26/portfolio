document.addEventListener('DOMContentLoaded', function() {
    // Initialize WOW.js for scroll animations
    new WOW().init();

    // Smooth scroll for navigation links
    document.querySelectorAll('a.page-scroll').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 60,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Navbar color change on scroll
    const navbar = document.querySelector('#main-navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.9)';
            navbar.style.boxShadow = 'none';
        }
    });

    // Portfolio filter animation
    const portfolioItems = document.querySelectorAll('.portfolio_single_content');
    document.querySelectorAll('#filters a').forEach(filter => {
        filter.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all filters
            document.querySelectorAll('#filters a').forEach(f => 
                f.parentElement.classList.remove('active_prot_menu'));
            
            // Add active class to current filter
            this.parentElement.classList.add('active_prot_menu');
            
            const filterValue = this.getAttribute('data-filter');
            
            portfolioItems.forEach(item => {
                if (filterValue === '*' || item.classList.contains(filterValue.substring(1))) {
                    item.style.opacity = '1';
                    item.style.transform = 'scale(1)';
                    item.style.display = 'block';
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'scale(0.8)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // Contact form handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = {
                name: this.querySelector('#name').value,
                email: this.querySelector('#email').value,
                message: this.querySelector('textarea').value
            };

            // Here you would typically send the form data to your backend
            // For now, we'll just show a success message
            const button = this.querySelector('button[type="submit"]');
            const originalText = button.textContent;
            button.textContent = 'Message Sent!';
            button.style.backgroundColor = '#4CAF50';
            
            // Reset form
            this.reset();
            
            // Reset button after 3 seconds
            setTimeout(() => {
                button.textContent = originalText;
                button.style.backgroundColor = '';
            }, 3000);
        });
    }

    // Skill bars animation
    const animateSkillBars = () => {
        document.querySelectorAll('.progress-bar').forEach(bar => {
            const width = bar.style.width;
            bar.style.width = '0';
            setTimeout(() => {
                bar.style.width = width;
            }, 100);
        });
    };

    // Trigger skill bars animation when scrolled into view
    const skillsSection = document.querySelector('.our-skills');
    if (skillsSection) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateSkillBars();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        observer.observe(skillsSection);
    }

    // Parallax effect for intro section
    const parallaxSection = document.querySelector('#text-carousel-intro-section');
    if (parallaxSection) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            parallaxSection.style.backgroundPositionY = `${scrolled * 0.5}px`;
        });
    }
});
