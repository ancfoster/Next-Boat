# Testing
 Click to return back to [README.md](README.md)

## Code Validation

### Javascript JSHint 
All JavaScript code was analysed with [JSHint](https://jshint.com)

| File | Screenshot |
|---|---|
|base.js|![base.js](testing_assets/base_js.png)|
|edit_listing.js|![edit_listing.js](testing_assets/edit_listing_js.png)|
|create.js|![create.js](testing_assets/create_js.png)|
|gallery.js|![gallery.js](testing_assets/gallery_js.jpeg)|
|message.js|![message.js](testing_assets/message_js.jpeg)|

### CSS Validation

CSS files were validated with the [W3C CSS Validation Service](https://jigsaw.w3.org/)

| File | Screenshot |
|---|---|
| account.css | ![account.css](testing_assets/css/account_css.png) |
| base.css | ![base.css](testing_assets/css/base_css.png) |
| conversarion.css | ![conversation.css](testing_assets/css/conversation_css.png) |
| create.css | ![create.css](testing_assets/css/create_css.png) |
| delete_listing.css | ![delete.css](testing_assets/css/delete_listing_css.png) |
| edit_delete_images.css | ![edit_delete.css](testing_assets/css/edit_delete_images_css.png) |
| favourites.css | ![favourites.css](testing_assets/css/favourites_css.png) |
| home.css | ![home.css](testing_assets/css/home_css.png) |
| listing_details.css | ![listing_details.css](testing_assets/css/listing_details_css_png.png) |
| listings.css | ![listings.css](testing_assets/css/listings_css.png) |
| messages.css | ![messages.css](testing_assets/css/messages_css.png) |
| my_listings.css | ![my_listings.css](testing_assets/css/my_listings_css.png) |


### HTML Validation

As many pages require a user to be logged in validation was carried out by copying the source code from the browser and pasting it into the W3 Nu HTML Validator.

Django forms generated HTML that did not pass validation. e.g `required` attribute not allowed on element `input`


### PEP8 Python Validation


## Browser Compatibility Testing

Pages were tested in Chrome & Firefox to test for compatiblity between different browsers.
Chrome and Firefox use different rendering engines, unlike Edge/Brave which also use Chromium.

- conversations.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/conversations_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/conversations_firefox.png)|

- display_conversations.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/display_conversation_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/display_conversations_firefox.png)|

- favourites.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/favourites_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/favourites_firefox.png)|

- index.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/index_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/index_firefox.png)|

- listing_details.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/listing_details_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/display_conversations_firefox.png)|

- listing_edit.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/listing_edit_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/listing_edit_firefox.png)|

- listings.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/listings_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/listings_firefox.png)|

- my_listings.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/my_listings_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/my_listings_firefox.png)|


## Responsiveness



## Manual Testing




## Automted Testing

Using the built in Django library unittest I wrote a number series of unit tests to test the operation of key functions and classes.