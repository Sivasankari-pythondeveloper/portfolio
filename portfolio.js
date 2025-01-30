<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
import 'boxicons'


    // Toggle navbar on mobile view
    let menuIcon = document.querySelector('#icons');
    let navbar = document.querySelector('.navbar');

    // Scroll to top button
    let toTop = document.querySelector('.footer-iconTop a');

    window.onscroll = () => {
        if (window.scrollY > 500) {
            toTop.style.display = 'block';
        } else {
            toTop.style.display = 'none';
        }
        highlightActiveLink();
    };

    // Smooth scrolling for navbar links
    document.querySelectorAll('.navbar-nav a').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').slice(1);
            smoothScroll(targetId);
        });
    });

    // Smooth scroll function
    function smoothScroll(targetId) {
        const target = document.getElementById(targetId);
        const topOffset = target.getBoundingClientRect().top + window.scrollY;
        const startPosition = window.scrollY;
        const distance = topOffset - startPosition;
        const duration = 800; // duration in ms
        let startTime = null;

        function animation(currentTime) {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const progress = Math.min(timeElapsed / duration, 1);
            const ease = easeInOutQuad(progress);
            window.scrollTo(0, startPosition + distance * ease);

            if (timeElapsed < duration) {
                requestAnimationFrame(animation);
            }
        }

        requestAnimationFrame(animation);
    }

    // Easing function (easeInOutQuad)
    function easeInOutQuad(t) {
        return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
    }

    // Highlight active navbar link on scroll
    function highlightActiveLink() {
        const sections = document.querySelectorAll('section');
        const scrollPos = window.scrollY;

        sections.forEach(section => {
            const top = section.offsetTop - 100;
            const bottom = top + section.offsetHeight;
            const navLink = document.querySelector(`.navbar-nav a[href*=${section.id}]`);

            if (scrollPos >= top && scrollPos < bottom) {
                navLink.classList.add('active');
            } else {
                navLink.classList.remove('active');
            }
        });
    }