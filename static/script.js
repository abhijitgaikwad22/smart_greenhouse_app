// Modern JavaScript for Greenhouse Application

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
            }
        });
    });

    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    // Export PDF functionality
    const exportPdfBtn = document.getElementById('exportPdf');
    if (exportPdfBtn) {
        exportPdfBtn.addEventListener('click', exportToPdf);
    }

    // Real-time validation for detection form
    const detectionForm = document.getElementById('detectionForm');
    if (detectionForm) {
        const inputs = detectionForm.querySelectorAll('input[type="number"]');
        inputs.forEach(input => {
            input.addEventListener('input', function() {
                validateInput(this);
            });
        });
    }
});

// Form validation
function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input[required], select[required]');
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            showError(input, 'This field is required');
            isValid = false;
        } else {
            clearError(input);
        }
        
        // Number validation
        if (input.type === 'number') {
            const value = parseFloat(input.value);
            const min = parseFloat(input.min);
            const max = parseFloat(input.max);
            
            if (value < min || value > max) {
                showError(input, `Value must be between ${min} and ${max}`);
                isValid = false;
            }
        }
    });
    
    return isValid;
}

// Show error message
function showError(input, message) {
    const formGroup = input.closest('.form-group');
    let errorDiv = formGroup.querySelector('.error-message');
    
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.className = 'error-message alert alert-danger';
        formGroup.appendChild(errorDiv);
    }
    
    errorDiv.textContent = message;
    input.classList.add('error');
}

// Clear error message
function clearError(input) {
    const formGroup = input.closest('.form-group');
    const errorDiv = formGroup.querySelector('.error-message');
    if (errorDiv) {
        errorDiv.remove();
    }
    input.classList.remove('error');
}

// Validate individual input
function validateInput(input) {
    const value = parseFloat(input.value);
    const min = parseFloat(input.min);
    const max = parseFloat(input.max);
    
    if (!Number.isFinite(value) || !Number.isFinite(min) || !Number.isFinite(max)) {
        clearError(input);
        return;
    }

    if (value < min || value > max) {
        showError(input, `Value must be between ${min} and ${max}`);
    } else {
        clearError(input);
    }
}

// Export to PDF
async function exportToPdf() {
    const btn = document.getElementById('exportPdf');
    const originalText = btn.textContent;
    
    try {
        btn.textContent = 'Generating PDF...';
        btn.disabled = true;
        
        // Collect data from the page
        const formData = {
            crop: document.getElementById('crop')?.value || '',
            temperature: document.getElementById('temperature')?.value || '',
            humidity: document.getElementById('humidity')?.value || '',
            soil_moisture: document.getElementById('soil_moisture')?.value || '',
            light: document.getElementById('light')?.value || '',
            result: {
                status: document.querySelector('.status-badge')?.textContent || '',
                score: document.querySelector('.score-value')?.textContent || '',
                health_indicator: document.querySelector('.health-indicator')?.textContent || '',
                alerts: getAlerts(),
                recommendations: getRecommendations()
            }
        };
        
        // Send to server
        const response = await fetch('/export/pdf', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) throw new Error('PDF generation failed');
        
        // Download PDF
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `greenhouse_report_${new Date().toISOString().slice(0,10)}.pdf`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
        
        showNotification('PDF exported successfully!', 'success');
    } catch (error) {
        console.error('PDF export error:', error);
        showNotification('Failed to export PDF. Please try again.', 'error');
    } finally {
        btn.textContent = originalText;
        btn.disabled = false;
    }
}

// Get alerts from page
function getAlerts() {
    const alerts = [];
    document.querySelectorAll('.alert-item').forEach(item => {
        alerts.push(item.textContent);
    });
    return alerts;
}

// Get recommendations from page
function getRecommendations() {
    const recommendations = [];
    document.querySelectorAll('.recommendation-item').forEach(item => {
        recommendations.push(item.textContent);
    });
    return recommendations;
}

// Show notification
function showNotification(message, type) {
    const normalizedType = String(type || '').toLowerCase();
    const mappedType =
        normalizedType === 'error' ? 'danger'
        : normalizedType === 'warn' ? 'warning'
        : normalizedType === 'warning' ? 'warning'
        : normalizedType === 'info' ? 'info'
        : 'success';

    const notification = document.createElement('div');
    notification.className = `alert alert-${mappedType}`;
    notification.style.position = 'fixed';
    notification.style.top = '20px';
    notification.style.right = '20px';
    notification.style.zIndex = '9999';
    notification.style.maxWidth = 'calc(100vw - 40px)';
    notification.style.minWidth = 'min(360px, calc(100vw - 40px))';
    notification.style.opacity = '0';
    notification.style.transform = 'translateX(16px)';
    notification.style.transition = 'opacity 200ms ease, transform 200ms ease';
    notification.textContent = message;
    
    document.body.appendChild(notification);
    requestAnimationFrame(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
    });
    
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(16px)';
        notification.addEventListener('transitionend', () => notification.remove(), { once: true });
    }, 3000);
}
