// ShellX Website — Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    initSmoothScrolling();
    initCodeCopy();
    initTerminalAnimation();
});

    if (!input || !gate) return;

    if (input.value === ACCESS_CODE) {
        // Grant access
        sessionStorage.setItem(STORAGE_KEY, 'true');
        gate.style.opacity = '0';
        gate.style.transition = 'opacity 0.5s ease';

        setTimeout(() => {
            gate.classList.add('hidden');
        }, 500);

        // Success feedback
        showNotification('Access granted. Welcome to ShellX.', 'success');
    } else {
        // Deny access
        input.style.borderColor = '#ef4444';
        input.style.animation = 'shake 0.5s';
        showNotification('Invalid access code. Try again.', 'error');

        setTimeout(() => {
            input.style.animation = '';
        }, 500);
    }
}

// Allow Enter key to submit password
document.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && document.getElementById('gate-password') === document.activeElement) {
        checkPassword();
    }
});

// Smooth Scrolling for Anchor Links
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Code Copy Functionality
function initCodeCopy() {
    const codeBlocks = document.querySelectorAll('pre code');

    codeBlocks.forEach(block => {
        const pre = block.parentElement;
        const button = document.createElement('button');
        button.className = 'copy-btn';
        button.innerHTML = '📋 Copy';
        button.style.cssText = `
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            padding: 0.25rem 0.75rem;
            border-radius: 4px;
            font-size: 0.8rem;
            cursor: pointer;
            opacity: 0;
            transition: all 0.3s ease;
        `;

        pre.style.position = 'relative';
        pre.appendChild(button);

        pre.addEventListener('mouseenter', () => button.style.opacity = '1');
        pre.addEventListener('mouseleave', () => button.style.opacity = '0');

        button.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(block.textContent);
                button.innerHTML = '✓ Copied!';
                button.style.color = 'var(--terminal-green)';

                setTimeout(() => {
                    button.innerHTML = '📋 Copy';
                    button.style.color = 'var(--text-secondary)';
                }, 2000);
            } catch (err) {
                showNotification('Failed to copy code', 'error');
            }
        });
    });
}

// Terminal Typing Animation
function initTerminalAnimation() {
    const terminals = document.querySelectorAll('.terminal');

    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                entry.target.style.transition = 'all 0.6s ease';

                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);

                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    terminals.forEach(terminal => {
        terminal.style.opacity = '0';
        observer.observe(terminal);
    });
}

// Notification System
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 2rem;
        right: 2rem;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        font-weight: 500;
        z-index: 10000;
        animation: slideIn 0.3s ease;
        backdrop-filter: blur(10px);
    `;

    if (type === 'success') {
        notification.style.background = 'rgba(34, 197, 94, 0.9)';
        notification.style.color = 'white';
    } else if (type === 'error') {
        notification.style.background = 'rgba(239, 68, 68, 0.9)';
        notification.style.color = 'white';
    } else {
        notification.style.background = 'rgba(0, 212, 255, 0.9)';
        notification.style.color = 'black';
    }

    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add shake animation
const style = document.createElement('style');
style.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        75% { transform: translateX(10px); }
    }

    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 1); }
    }
`;
document.head.appendChild(style);

// Console Easter Egg
console.log('%c⚡ ShellX', 'font-size: 24px; font-weight: bold; color: #00d4ff;');
console.log('%cCognitive Developer Engine', 'font-size: 14px; color: #94a3b8;');
console.log('%cPrivate documentation site — Authorized access only.', 'font-size: 12px; color: #64748b;');
