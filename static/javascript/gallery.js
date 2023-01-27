/* jshint esversion: 11 */
// Init variables
let allImagesCont = document.getElementById('all-images-cont');
let galleryLaunchButton = document.getElementById('gallery-launch-button');
let galleryStatus = 0;

// This function opens and collapses the gallery of all the pictures
galleryLaunchButton.addEventListener("click", () => {
    if (galleryStatus === 0) {
        galleryStatus += 1;
        allImagesCont.style.display = 'grid';
        galleryLaunchButton.innerHTML = `
        <img alt="" class="gallery-icon" src="https://nextboat-ci-static.s3.eu-west-2.amazonaws.com/static/images/gallery_icon.svg">
            <span>
                Hide Pictures
            </span>
        `;
    } else {
        galleryStatus = 0;
        allImagesCont.style.display = 'none';
        galleryLaunchButton.innerHTML = `
        <img alt="" class="gallery-icon" src="https://nextboat-ci-static.s3.eu-west-2.amazonaws.com/static/images/gallery_icon.svg">
            <span>
                All Pictures
            </span>
        `;
    }
});