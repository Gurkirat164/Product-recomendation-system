document.addEventListener('DOMContentLoaded', function() {
    // Get theme buttons
    const themeButtons = document.querySelectorAll('.theme-button');
    
    // Add default 'dark-theme' class to body when page loads
    document.body.classList.add('dark-theme');
    
    // Theme switching functionality
    themeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const theme = this.dataset.theme;
            
            // Remove all theme classes
            document.body.classList.remove('dark-theme', 'light-theme');
            
            // If light theme is selected, add light-theme class
            // Otherwise, the default (dark) theme will be applied
            if (theme === 'light') {
                document.body.classList.add('light-theme');
            } else {
                document.body.classList.add('dark-theme');
            }
        });
    });
});