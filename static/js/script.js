document.addEventListener('DOMContentLoaded', function() {
    // Get theme buttons
    const themeButtons = document.querySelectorAll('.theme-button');
    
    // Check if there's a saved theme preference in localStorage
    const savedTheme = localStorage.getItem('webstoreTheme') || 'dark';
    
    // Remove any existing theme classes
    document.body.classList.remove('dark-theme', 'light-theme');
    
    // Apply the saved theme
    document.body.classList.add(savedTheme + '-theme');
    
    // Theme switching functionality
    themeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const theme = this.dataset.theme;
            
            // Remove all theme classes
            document.body.classList.remove('dark-theme', 'light-theme');
            
            // Add the selected theme class
            document.body.classList.add(theme + '-theme');
            
            // Save the preference to localStorage
            localStorage.setItem('webstoreTheme', theme);
        });
    });
});