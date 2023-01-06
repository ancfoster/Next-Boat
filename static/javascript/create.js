// Init variables
const excerptField = document.getElementById("id_listing_excerpt");
const descriptionField = document.getElementById("id_listing_description");

const descriptionLengthDiv = document.getElementById("description-length");
const excerptLengthDiv = document.getElementById("excerpt-length");

// These two functions count & display how many characters have been inputted into the excerpt & description form fields
excerptField.addEventListener('input', updateExcerptLength);
function updateExcerptLength(e) {
    excerptLengthDiv.textContent = `${e.target.value.length} / 66`;
}
descriptionField.addEventListener('input', updateDescriptionLength);
function updateDescriptionLength(e) {
    descriptionLengthDiv.textContent = `${e.target.value.length} / 3500`;
}