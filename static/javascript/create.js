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
// Feature list variables
let featureArray = [];
const addFeatureField = document.getElementById('add_feature_text');
const addfeatureButton = document.getElementById('add_feature_button');
const featureFlex = document.getElementById('feature-flex-list');

featureFlex.addEventListener('click', e => {
    if(e.target.classList.contains('delete_list_item')) {
        let itemDivToDelete = e.target.parentElement;
        featureFlexNode = itemDivToDelete.parentNode;
        let itemIndex = Array.from(featureFlexNode.children).indexOf(itemDivToDelete);
        deleteFeature(itemIndex);
        itemDivToDelete.remove();
    }
})

function deleteFeature(itemIndex) {
    updatedItemIndex = itemIndex - 1;
    featureArray.pop(updatedItemIndex)
    tempFeatureList = '';
    if(featureArray.length === 0) {
        featureFlex.innerHTML = `
        <span id="add-feature-text">Begin by adding a feature.</span>`;
        idBoatFeatureList.value = '';
    } else {
    for(i=0; i < featureArray.length; i++) {
        if(i < featureArray.length) {
            tempFeatureList = tempFeatureList + featureArray[i] + '^*';
        } else {
            tempFeatureList = tempFeatureList + featureArray[i];
        }
    }
    idBoatFeatureList.value = tempFeatureList;
    }
}
// Adds a new feature item to the DOM and idBoatFeatureList hidden form field
addfeatureButton.addEventListener('click', () => {
    newItem = addFeatureField.value;
    if( featureArray.length === 0) {
        featureArray.push(newItem);
        featureFlex.innerHTML = `
        <div class="feature-item">
        <span>${newItem}</span><div class="delete_list_item" role="button">
        </div>
    </div>`;
        addFeatureField.value = '';
        idBoatFeatureList.value = newItem;    
    }
    else {
        featureArray.push(newItem);
        featureFlex.innerHTML = featureFlex.innerHTML + `
        <div class="feature-item">
        <span>${newItem}</span><div class="delete_list_item" role="button">
        </div>
    </div>`;
        addFeatureField.value = '';
        idBoatFeatureList.value = idBoatFeatureList.value + "^%" + newItem;
    }
} )

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
            break;
    }
}