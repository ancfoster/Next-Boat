// Init variables
const excerptField = document.getElementById("id_listing_excerpt");
const descriptionField = document.getElementById("id_listing_description");
const createForm = document.getElementById("create-form");
const descriptionLengthDiv = document.getElementById("description-length");
const excerptLengthDiv = document.getElementById("excerpt-length");
// Hidden field variables
const idCondition = document.getElementById('id_condition')
const idBoatFeatureList = document.getElementById('id_boat_feature_list')
const idCategory = document.getElementById('id_category')
const idType = document.getElementById('id_type')
const idTaxPaid = document.getElementById('id_tax_paid')

// These two functions count & display how many characters have been inputted into the excerpt & description form fields
excerptField.addEventListener('input', updateExcerptLength);
function updateExcerptLength(e) {
    excerptLengthDiv.textContent = `${e.target.value.length} / 66`;
}
descriptionField.addEventListener('input', updateDescriptionLength);
function updateDescriptionLength(e) {
    descriptionLengthDiv.textContent = `${e.target.value.length} / 3500`;
}

// Check if clicked form item item is an INPUT
// If it is pass it and its value to relayButtonValue function
createForm.addEventListener('click', e => {
    if (e.target.tagName == 'INPUT') {
        eValue = e.target.value;
        eId = e.target.id;
        relayRadioButtonValue(eId, eValue)
    }
})
// Checks if clicked form item is radio button, if so take value and assign to corresponding hidden form field
function relayRadioButtonValue(fieldId, fieldValue) {
    switch (fieldId)
    {
        case "power-radio":
            idType.value = fieldValue;
            break;
        case "sail-radio":
            idType.value = fieldValue;
            break;
        case "used-radio":
            idCondition.value = fieldValue;
            break;
        case "new-radio":
            idCondition.value = fieldValue;
            break;
        case "paid-radio":
            idTaxPaid.value = fieldValue;
            break;
        case "unpaid-radio":
            idTaxPaid.value = fieldValue;
            break;
        default:
            console.log("Error assigning clicked form input to hidden form field");
    }

}