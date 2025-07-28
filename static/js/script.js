document.addEventListener('DOMContentLoaded', function() {
    const themeButtons = document.querySelectorAll('.theme-button');

    themeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const theme = this.dataset.theme;
            document.body.classList.remove('default-theme', 'dark-theme', 'light-theme');
            document.body.classList.add(theme + '-theme');
        });
    });
});