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

    // Search suggestions functionality
    const searchInput = document.querySelector('.navbar-search-input');
    const suggestionsContainer = document.querySelector('.search-suggestions');
    
    if (searchInput && suggestionsContainer) {
        let debounceTimer;
        
        // Function to fetch and display suggestions
        const fetchSuggestions = (query) => {
            if (query.length < 3) {
                suggestionsContainer.classList.remove('show');
                suggestionsContainer.innerHTML = '';
                return;
            }
            
            fetch(`/api/search-suggestions?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(suggestions => {
                    suggestionsContainer.innerHTML = '';
                    
                    if (suggestions.length > 0) {
                        suggestions.forEach(suggestion => {
                            const item = document.createElement('div');
                            item.classList.add('suggestion-item');
                            item.textContent = suggestion;
                            
                            item.addEventListener('click', () => {
                                searchInput.value = suggestion;
                                suggestionsContainer.classList.remove('show');
                                // Submit the form when a suggestion is clicked
                                searchInput.closest('form').submit();
                            });
                            
                            suggestionsContainer.appendChild(item);
                        });
                        
                        suggestionsContainer.classList.add('show');
                    } else {
                        suggestionsContainer.classList.remove('show');
                    }
                })
                .catch(error => {
                    console.error('Error fetching suggestions:', error);
                    suggestionsContainer.classList.remove('show');
                });
        };
        
        // Input event with debounce
        searchInput.addEventListener('input', function() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(() => {
                fetchSuggestions(this.value);
            }, 300);
        });
        
        // Hide suggestions when clicking outside
        document.addEventListener('click', function(event) {
            if (!searchInput.contains(event.target) && !suggestionsContainer.contains(event.target)) {
                suggestionsContainer.classList.remove('show');
            }
        });
        
        // Focus event - show suggestions again if input has value
        searchInput.addEventListener('focus', function() {
            if (this.value.length >= 3) {
                fetchSuggestions(this.value);
            }
        });
    }
});