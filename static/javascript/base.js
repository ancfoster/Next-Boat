let menuStatus = 0

const menuButton = document.getElementById('menu-button');
const menuUserIcon = document.getElementById('menu-button-icon');
const menuCloseIcon = document.getElementById('menu-button-icon-close')
const menuContainer = document.getElementById('menu-container');

menuButton.addEventListener("click", () => {
    if (menuStatus === 0) {
        menuUserIcon.style.opacity = "0";
        menuCloseIcon.style.opacity = "1.0"
        menuStatus = 1
        menuContainer.style.cssText = `padding: 16px; height: auto; display: flex;`
    }
    else {
        menuCloseIcon.style.opacity = "0.0"
        menuUserIcon.style.opacity = "1.0";
        menuStatus = 0
        menuContainer.style.cssText = `padding: 0px; height: 0px; display: hidden;`
    }
});
