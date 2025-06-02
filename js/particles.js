class Particle {
    constructor(canvas, options = {}) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.x = options.x || Math.random() * canvas.width;
        this.y = options.y || Math.random() * canvas.height;
        this.size = Math.random() * 3 + 1;
        this.speedX = Math.random() * 3 - 1.5;
        this.speedY = Math.random() * 3 - 1.5;
        this.color = options.color || '#ffffff';
        this.opacity = Math.random() * 0.5 + 0.2;
    }

    update() {
        this.x += this.speedX;
        this.y += this.speedY;

        if (this.x > this.canvas.width) {
            this.x = 0;
        } else if (this.x < 0) {
            this.x = this.canvas.width;
        }

        if (this.y > this.canvas.height) {
            this.y = 0;
        } else if (this.y < 0) {
            this.y = this.canvas.height;
        }
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        this.ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
        this.ctx.fill();
    }
}

class ParticleNetwork {
    constructor(canvasId, options = {}) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.options = {
            particleCount: options.particleCount || 50,
            color: options.color || '#ffffff',
            maxDistance: options.maxDistance || 100,
            connectParticles: options.connectParticles !== false
        };

        this.init();
        this.animate();
        this.handleResize();
    }

    init() {
        // Set canvas size
        this.setCanvasSize();

        // Create particles
        for (let i = 0; i < this.options.particleCount; i++) {
            this.particles.push(new Particle(this.canvas, {
                color: this.options.color
            }));
        }
    }

    setCanvasSize() {
        this.canvas.width = this.canvas.offsetWidth;
        this.canvas.height = this.canvas.offsetHeight;
    }

    handleResize() {
        window.addEventListener('resize', () => {
            this.setCanvasSize();
        });
    }

    connectParticles() {
        const { particles, ctx, options } = this;
        
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < options.maxDistance) {
                    const opacity = 1 - (distance / options.maxDistance);
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(255, 255, 255, ${opacity * 0.2})`;
                    ctx.lineWidth = 1;
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }
    }

    animate() {
        const animate = () => {
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

            // Update and draw particles
            this.particles.forEach(particle => {
                particle.update();
                particle.draw();
            });

            // Connect particles if enabled
            if (this.options.connectParticles) {
                this.connectParticles();
            }

            requestAnimationFrame(animate);
        };

        animate();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const particleCanvas = document.createElement('canvas');
    particleCanvas.id = 'particle-canvas';
    particleCanvas.className = 'particles';
    
    // Add canvas to the intro section
    const introSection = document.getElementById('text-carousel-intro-section');
    if (introSection) {
        introSection.appendChild(particleCanvas);
        
        // Initialize particle network
        new ParticleNetwork('particle-canvas', {
            particleCount: 50,
            connectParticles: true,
            maxDistance: 150
        });
    }
});
