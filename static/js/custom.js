// Custom JavaScript for The Wedding Company Management System

document.addEventListener('DOMContentLoaded', function() {
    const body = document.body;

    // Theme toggle
    const themeToggle = document.getElementById('themeToggle');
    const storedTheme = localStorage.getItem('twc-theme') || '';
    if (storedTheme) {
        body.setAttribute('data-theme', storedTheme);
        updateThemeToggleIcon(themeToggle, storedTheme);
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const current = body.getAttribute('data-theme');
            const next = current === 'dark' ? '' : 'dark';
            body.setAttribute('data-theme', next);
            localStorage.setItem('twc-theme', next);
            updateThemeToggleIcon(themeToggle, next);
        });
    }

    // Scroll to top button
    const scrollBtn = document.getElementById('scrollTopBtn');
    if (scrollBtn) {
        window.addEventListener('scroll', function() {
            scrollBtn.style.display = window.scrollY > 180 ? 'flex' : 'none';
        });
        scrollBtn.addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(function(card, index) {
        card.style.animationDelay = (index * 0.1) + 's';
        card.classList.add('fade-in');
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
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

    // Form validation and submission handling
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        const submitButton = form.querySelector('button[type="submit"]');
        let isSubmitting = false;
        
        // Handle form submission
        form.addEventListener('submit', function(e) {
            // If already submitting, prevent double submission
            if (isSubmitting) {
                e.preventDefault();
                return false;
            }
            
            // Check HTML5 validation
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
                form.classList.add('was-validated');
                return false;
            }
            
            // Form is valid - show loading state and allow submission
            if (submitButton && !isSubmitting) {
                isSubmitting = true;
                const originalHTML = submitButton.innerHTML;
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Saving...';
                submitButton.disabled = true;
                
                // Store original HTML for potential restoration
                submitButton.dataset.originalHTML = originalHTML;
                
                // Form will submit normally - don't prevent default
                // If submission fails (network error, etc.), restore button after timeout
                setTimeout(function() {
                    if (isSubmitting) {
                        // If still marked as submitting after 15 seconds, restore button
                        submitButton.innerHTML = originalHTML;
                        submitButton.disabled = false;
                        isSubmitting = false;
                        alert('Submission is taking longer than expected. Please check your connection and try again.');
                    }
                }, 15000);
            }
            
            form.classList.add('was-validated');
            // Allow form to submit normally to server
        });
    });

    // Tooltip initialization
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Popover initialization
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.btn-danger, [data-action="delete"]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });

    // Auto-calculate remaining amount in booking form
    const totalAmountInput = document.getElementById('id_total_amount');
    const advancePaidInput = document.getElementById('id_advance_paid');
    
    if (totalAmountInput && advancePaidInput) {
        function calculateRemaining() {
            const total = parseFloat(totalAmountInput.value) || 0;
            const advance = parseFloat(advancePaidInput.value) || 0;
            const remaining = total - advance;
            
            // Update remaining amount display if exists
            const remainingDisplay = document.getElementById('remaining-amount');
            if (remainingDisplay) {
                remainingDisplay.textContent = '₹' + remaining.toLocaleString('en-IN', {maximumFractionDigits: 0});
                if (remaining < 0) {
                    remainingDisplay.classList.add('text-danger');
                } else {
                    remainingDisplay.classList.remove('text-danger');
                }
            }
        }
        
        totalAmountInput.addEventListener('input', calculateRemaining);
        advancePaidInput.addEventListener('input', calculateRemaining);
        calculateRemaining();
    }

    // Add animation to stat cards
    const statCards = document.querySelectorAll('.stat-card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    statCards.forEach(function(card) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });

    // Search functionality enhancement
    const searchInputs = document.querySelectorAll('input[type="search"], input[name="search"]');
    searchInputs.forEach(function(input) {
        let searchTimeout;
        input.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(function() {
                // Add visual feedback
                input.style.borderColor = '#28a745';
                setTimeout(function() {
                    input.style.borderColor = '';
                }, 300);
            }, 500);
        });
    });
});

// Utility function for formatting currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        maximumFractionDigits: 0
    }).format(amount);
}

// Utility function for formatting dates
function formatDate(dateString) {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(date);
}

function updateThemeToggleIcon(button, theme) {
    if (!button) return;
    const icon = button.querySelector('i');
    if (theme === 'dark') {
        icon.className = 'bi bi-brightness-high';
        button.querySelector('span') && (button.querySelector('span').textContent = 'Light mode');
    } else {
        icon.className = 'bi bi-moon-stars';
        button.querySelector('span') && (button.querySelector('span').textContent = 'Dark mode');
    }
}

