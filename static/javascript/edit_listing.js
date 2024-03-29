/* jshint esversion: 11 */
// Init variables
const excerptField = document.getElementById("id_listing_excerpt");
const descriptionField = document.getElementById("id_listing_description");
const editForm = document.getElementById("edit-form");
const descriptionLengthDiv = document.getElementById("description-length");
const excerptLengthDiv = document.getElementById("excerpt-length");
// Hidden field variables
const idCondition = document.getElementById('id_condition');
const idBoatFeatureList = document.getElementById('id_boat_feature_list');
const idCategory = document.getElementById('id_category');
const idType = document.getElementById('id_type');
const idTaxPaid = document.getElementById('id_tax_paid');
// Feature list variables
let featureArray = [];
const addFeatureField = document.getElementById('add_feature_text');
const addfeatureButton = document.getElementById('add_feature_button');
const featureFlex = document.getElementById('feature-flex-list');

// Category Constants
const categoryListPower = document.getElementById('category_list_power');
const categoryListSail = document.getElementById('category_list_sail');
const categoryListPowerLabel = document.getElementById('clp');
const categoryListSailLabel = document.getElementById('cls');

window.addEventListener("load", loadState);

// This function takes the information from hidden fields and then adjusts the UI (e.g radio buttons) based on the values
function loadState(){
    if (idCondition.value == 'N') {
        document.getElementById('new-radio').checked = true;
    }
    if (idTaxPaid.value == 'N') {
        document.getElementById('unpaid-radio').checked = true;
    }
    boatCategoryLoad();
    if (idBoatFeatureList.value !== '') {
        let idBoatFeatureListString = idBoatFeatureList.value;
        featureArray = idBoatFeatureListString.split('^^');
        featureFlex.innerHTML = '';
        for(let i = 0; i < featureArray.length; i++){
            featureFlex.innerHTML = featureFlex.innerHTML + `
            <div class="feature-item">
            <span>${featureArray[i]}</span><div class="delete_list_item" role="button">
            </div>
            </div>`;
        }
    }
}
// Assigns the value of the category drop down field
function boatCategoryLoad(){
    if(idType.value == "P") {
        categoryListPowerLabel.style.display = 'block';
        categoryListPower.style.display = 'block';
    } else {
        categoryListSailLabel.style.display = 'block';
        categoryListSail.style.display = 'block';
      document.getElementById('sail-radio').checked = true;
    }
    switch (idCategory.value)
    {
        case 'C':
            categoryListSail.value = 'C';
            break;
        case 'DS':
            categoryListSail.value = 'DS';
            break;
        case 'DI':
            categoryListSail.value = 'DI';
            break;
        case 'RA':
            categoryListSail.value = 'RA';
            break;
        case 'PC':
            categoryListPower.value = 'PC';
            break;
        case 'DC':
            categoryListPower.value = 'DC';
            break;
        case 'S':
            categoryListPower.value = 'S';
            break;
        case 'F':
            categoryListPower.value = 'F';
            break;
        case 'RT':
            categoryListPower.value = 'RT';
            break;
        case 'NC':
            categoryListPower.value = 'NC';
            break;
    }
}

// When an option from either power or sail category lists is selected, the value is forwarded to the hidden from field
categoryListPower.addEventListener('change', function() {
    idCategory.value = categoryListPower.value;
});
categoryListSail.addEventListener('change', function() {
    idCategory.value = categoryListSail.value;
});

// If add feature field is less than two characters in length add button is disabled
addFeatureField.addEventListener('input', checkFeatureField);
function checkFeatureField(e) {
    if(addFeatureField.value.length > 2) {
        addfeatureButton.disabled = false;
    }
}

// Create event listener for when delete icons are clicked by user, then calculate child item of list item and call delete function
featureFlex.addEventListener('click', e => {
    if(e.target.classList.contains('delete_list_item')) {
        let itemDivToDelete = e.target.parentElement;
        let featureFlexNode = itemDivToDelete.parentNode;
        let itemIndex = Array.from(featureFlexNode.children).indexOf(itemDivToDelete);
        deleteFeature(itemIndex);
        itemDivToDelete.remove();
    }
});

// This function deletes selected boat feature and updates the hidden form field.
function deleteFeature(itemIndex) {
    let updatedItemIndex = itemIndex - 1;
    featureArray.pop(updatedItemIndex);
    let tempFeatureList = '';
    if(featureArray.length === 0) {
        featureFlex.innerHTML = `
        <span id="add-feature-text">Begin by adding a feature.</span>`;
        idBoatFeatureList.value = '';
    } else {
    for(let i=0; i < featureArray.length; i++) {
        if(i < featureArray.length - 1) {
            tempFeatureList = tempFeatureList + featureArray[i] + '^^';
        } else {
            tempFeatureList = tempFeatureList + featureArray[i];
        }
    }
    idBoatFeatureList.value = tempFeatureList;
    }
}

// Adds a new feature item to the DOM and idBoatFeatureList hidden form field
addfeatureButton.addEventListener('click', () => {
    let newItem = addFeatureField.value;
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
        featureFlex.innerHTML += `
        <div class="feature-item">
        <span>${newItem}</span><div class="delete_list_item" role="button">
        </div>
    </div>`;
        addFeatureField.value = '';
        idBoatFeatureList.value = idBoatFeatureList.value + "^^" + newItem;
    }
    addfeatureButton.disabled = true;
});

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
editForm.addEventListener('click', e => {
    if (e.target.tagName == 'INPUT') {
        let eValue = e.target.value;
        let eId = e.target.id;
        relayRadioButtonValue(eId, eValue);
    }
});
// Checks if clicked form item is radio button, if so take value and assign to corresponding hidden form field
function relayRadioButtonValue(fieldId, fieldValue) {
    switch (fieldId)
    {
        case "power-radio":
            if (idType.value == 'S') {
                categoryListPower.style.display = 'block';
                categoryListPowerLabel.style.display = 'block';
                categoryListSailLabel.style.display = 'none';
                categoryListSail.style.display = 'none';
                idCategory.value = 'PC';
            }
            idType.value = fieldValue;
            break;
        case "sail-radio":
            if (idType.value == 'P') {
                categoryListPower.style.display = 'none';
                categoryListPowerLabel.style.display = 'none';
                categoryListSailLabel.style.display = 'block';
                categoryListSail.style.display = 'block';
                idCategory.value = 'C';
            }
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