// Navbar scroll effect
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    navbar.classList.add("scrolled");
  } else {
    navbar.classList.remove("scrolled");
  }
});

// Mobile menu toggle
document.querySelector(".menu-toggle").addEventListener("click", function () {
  this.classList.toggle("active");
  // Add mobile menu functionality here
});

// Scroll animations
const observerOptions = {
  root: null,
  rootMargin: "0px",
  threshold: 0.1,
};

const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      if (entry.target.classList.contains("section-subtitle")) {
        entry.target.style.animation = "fadeInUp 0.8s forwards";
      } else if (entry.target.classList.contains("section-title")) {
        entry.target.style.animation = "fadeInUp 0.8s forwards 0.2s";
      } else if (entry.target.classList.contains("section-description")) {
        entry.target.style.animation = "fadeInUp 0.8s forwards 0.4s";
      } else if (entry.target.classList.contains("about-image-container")) {
        entry.target.style.animation = "fadeInLeft 0.8s forwards";
      } else if (entry.target.classList.contains("about-text")) {
        entry.target.style.animation = "fadeInRight 0.8s forwards";
      } else if (entry.target.classList.contains("timeline-item")) {
        entry.target.style.animation = "fadeInUp 0.8s forwards";
      } else if (entry.target.classList.contains("goal-card")) {
        entry.target.style.animation = "fadeInUp 0.8s forwards";
      } else if (entry.target.classList.contains("contact-info")) {
        entry.target.style.animation = "fadeInLeft 0.8s forwards";
      } else if (entry.target.classList.contains("contact-form")) {
        entry.target.style.animation = "fadeInRight 0.8s forwards";
      }
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observe elements
document
  .querySelectorAll(
    ".section-subtitle, .section-title, .section-description, .about-image-container, .about-text, .timeline-item, .goal-card, .contact-info, .contact-form"
  )
  .forEach((el) => {
    observer.observe(el);
  });

// Create particles
function createParticles() {
  const particlesContainer = document.getElementById("particles");
  const particleCount = 20;

  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement("div");
    particle.classList.add("particle");

    // Random size
    const size = Math.random() * 10 + 5;
    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;

    // Random position
    const posX = Math.random() * 100;
    const posY = Math.random() * 100;
    particle.style.left = `${posX}%`;
    particle.style.top = `${posY}%`;

    // Random color
    const colors = [
      "rgba(110, 86, 207, 0.3)",
      "rgba(255, 123, 146, 0.3)",
      "rgba(255, 255, 255, 0.3)",
    ];
    particle.style.backgroundColor =
      colors[Math.floor(Math.random() * colors.length)];

    // Random animation duration and delay
    const duration = Math.random() * 20 + 10;
    const delay = Math.random() * 5;
    particle.style.animationDuration = `${duration}s`;
    particle.style.animationDelay = `${delay}s`;

    particlesContainer.appendChild(particle);
  }
}

// Initialize particles
createParticles();

// Form submission
document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  // Add form submission logic here
  alert("Thank you for your message! I will get back to you soon.");
  this.reset();
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const targetId = this.getAttribute("href");
    const targetElement = document.querySelector(targetId);

    if (targetElement) {
      window.scrollTo({
        top: targetElement.offsetTop - 80,
        behavior: "smooth",
      });
    }
  });
});
