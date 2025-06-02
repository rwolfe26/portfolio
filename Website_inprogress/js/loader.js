(function() {
    const loader = document.querySelector('.page-loader');
    const particleCanvas = document.querySelector('.particles');
    let isLoading = true;

    // Create loading animation
    function createLoadingAnimation() {
        const dots = document.createElement('div');
        dots.className = 'loading-dots';
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement('div');
            dot.className = 'dot';
            dots.appendChild(dot);
        }
        loader.appendChild(dots);
    }

    // Initialize loading screen
    function initLoader() {
        createLoadingAnimation();
        
        // Hide loader when everything is loaded
        window.addEventListener('load', () => {
            isLoading = false;
            setTimeout(() => {
                loader.style.opacity = '0';
                setTimeout(() => {
                    loader.style.display = 'none';
                    // Initialize particle animation after loader is hidden
                    if (particleCanvas) {
                        particleCanvas.style.opacity = '1';
                    }
                }, 500);
            }, 500);
        });
    }

    // Add loader styles
    function addLoaderStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .page-loader {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: var(--primary);
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 9999;
                transition: opacity 0.5s ease;
            }

            .loading-dots {
                display: flex;
                gap: 12px;
            }

            .dot {
                width: 16px;
                height: 16px;
                background: #fff;
                border-radius: 50%;
                animation: bounce 0.5s ease-in-out infinite;
            }

            .dot:nth-child(2) {
                animation-delay: 0.1s;
            }

            .dot:nth-child(3) {
                animation-delay: 0.2s;
            }

            @keyframes bounce {
                0%, 100% {
                    transform: translateY(0);
                }
                50% {
                    transform: translateY(-20px);
                }
            }

            .particles {
                opacity: 0;
                transition: opacity 1s ease;
            }
        `;
        document.head.appendChild(style);
    }

    // Initialize
    addLoaderStyles();
    initLoader();
})();
