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

### PEP8 Python Validation

- Listings App

|File|Screenshot|
|---|---|
|admin.py|![](testing_assets/pep8/listings_admin.png)|
|models.py|![](testing_assets/pep8/listings_models.png)|
|urls.py|![](testing_assets/pep8/listings_urls.png)|
|views.py|![](testing_assets/pep8/listings_views.png)|
|forms.py|![](testing_assets/pep8/listings_forms.png)|

- Conversations

|File|Screenshot|
|---|---|
|admin.py|![](testing_assets/pep8/conversations_admin.png)|
|models.py|![](testing_assets/pep8/conversations_models.png)|
|urls.py|![](testing_assets/pep8/conversations_urls.png)|
|views.py|![](testing_assets/pep8/conversations_views.png)|
|forms.py|![](testing_assets/pep8/conversations_forms.png)|

- Favourites App

|File|Screenshot|
|---|---|
|admin.py|![](testing_assets/pep8/favourites_admin.png)|
|models.py|![](testing_assets/pep8/favourites_models.png)|
|urls.py|![](testing_assets/pep8/favourites_urls.png)|
|views.py|![](testing_assets/pep8/favourites_views.png)|

### HTML Validation

As many pages require a user to be logged in validation was carried out by copying the source code from the browser and pasting it into the W3 Nu HTML Validator.

Django forms generated HTML that did not pass validation in `create_listing_form.html` and `listing_edit.html`, the `required` attribute is not allowed on element `input`. As Django generated this I am unable to fix it.

All other HTML validation tests were successful. 

|File|Screenshot|
|---|---|
|index.html|![](testing_assets/html_validation/index_nu.jpeg)|
|favourites.html|![](testing_assets/html_validation/favourites_nu.png)|
|favourites_delete.html|![](testing_assets/html_validation/favourite_delete_nu.png)|
|conversations.html|![](testing_assets/html_validation/conversations_nu.jpeg)|
|display_conversations.html|![](testing_assets/html_validation/display_conversation_nu.jpeg)|
|listings.html|![](testing_assets/html_validation/listings_nu.jpeg)|
|listing_delete.html|![](testing_assets/html_validation/listing_delete.png)|
|listing_edit_images.html|![](testing_assets/html_validation/listing_edit_images.png)|
|my_listings.html|![](testing_assets/html_validation/my_listings_nu%20.jpeg)|
|listing_create_form.html|![](testing_assets/html_validation/listing_create_form_nu.jpeg)|
|listing_edit.html|![](testing_assets/html_validation/listing_edit.jpeg)|


## Browser Compatibility Testing

Pages were tested in Chrome & Firefox to test for compatiblity between different browsers.
Chrome and Firefox use different rendering engines, unlike Edge/Brave which also use Chromium.

- conversations.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/conversations_chrome.png)|
|![Firefox](testing_assets/firefox.png)|![](testing_assets/browser_screenshots/conversations_firefox.png)|

- display_conversations.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/display_conversation_chrome.png)|
|![Firefox](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/display_conversations_firefox.png)|

- favourites.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/favourites_chrome.png)|
|![Firefox](testing_assets/firefox.png)|![](testing_assets/browser_screenshots/favourites_firefox.png)|

- index.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/index_chrome.png)|
|![Firefox](testing_assets/firefox.png)|![](testing_assets/browser_screenshots/index_firefox.png)|

- listing_details.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/listing_details_chrome.png)|
|![Firefox](testing_assets/firefox.png)|![](testing_assets/browser_screenshots/display_conversations_firefox.png)|

- listing_edit.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/listing_edit_chrome.png)|
|![Firefox](testing_assets/firefox.png)|![](testing_assets/browser_screenshots/listing_edit_firefox.png)|

- listings.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/listings_chrome.png)|
|![Firefox](testing_assets/firefox.png)|![](testing_assets/browser_screenshots/listings_firefox.png)|

- my_listings.html

| Browser| Screenshot |
|---|---|
|![Chrome](testing_assets/chrome.png)|![](testing_assets/browser_screenshots/my_listings_chrome.png)|
|![Firefox](testing_assets/firefox.png)|![](testing_assets/browser_screenshots/my_listings_firefox.png)|


## Responsiveness

| **Feature** | **iPhone** | **Desktop** |
|---|---|---|
| Home Page | ![](testing_assets/responsive/iphone_index.png) | ![Home Page](readme_assets/features/feature_homepage.jpeg) |
| Listings | ![](testing_assets/responsive/iphone_listings.png)| ![Listings](readme_assets/features/feature_listings.jpeg) |
| Listings Detail View | ![](testing_assets/responsive/iphone_listings_details.png) | ![Listings Detail View](readme_assets/features/feature_listings_details.jpeg) |
| Create listing | ![](testing_assets/responsive/iphone_create_listing.png)  | ![Create listing](readme_assets/features/feature_create_listing.jpeg) |
| My Listings | ![](testing_assets/responsive/iphone_my_listings.png) |
| Delete listing | ![](testing_assets/responsive/delete_iphone.png) | ![Delete listing](readme_assets/features/feature-delete_listing.jpeg) |
| Messages List | ![](testing_assets/responsive/iphone_conversations.png)  | ![messages list](readme_assets/features/feature_messages.jpeg) |
| Favourites List | ![](testing_assets/responsive/iphone_favourites.png) | ![favourite list](readme_assets/features/feature_favourites_list.jpeg) |


## Manual Testing

| Action | Expected Result | Actual Result |
|---|---|---|
| Create Account | Account created, redirected to home page | Account created, redirected to home page |
| Click on 'Buy' | Site listings are presented | Site listings are presented |
| Click on first listing | Taken to the detail view of that listing | Taken to the detail view of that listings |
| Click on favorite icon | Icon turns red, indicating favorite created | Icon turns red, indicating favorite created |
| Click again on favorite icon | Icon turns grey, indicating favorite has been deleted | Icon turns grey, indicating favorite has been deleted |
| Click contact seller button | Taken to new conversation view | New conversation was created & message sent successfully |
| Click contact seller button once a chat has been created | Taken to conversation view | Internal Server Error (500). A bug has been discovered. Instead of a PK, CreateConversation is returning an object as a string. I have spoken to tutor support and no ne has been able to understand why this is happening. COnversation can still be reached through the main messages interface. |
| View conversations, by going to 'Messages' from the profile menu | List of conversations is shown | List of conversations was shown |
| Click on a conversation | Conversation with its messages loaded | Conversation with its messages loaded |
| Send a new message from conversation view | Upon writing and submitting a new message it will be added to the conversation | New message was added |
| Create a listing | A new listing with all of the user inputs and file uploads is created | A new listing with all of the user inputs and file uploads is created |
| Edit Listing, make a change to a field | The edit listing page appears, with pre-populated fields, when one of the values of these fields is changed and the form submitted, the change will be saved | Change to listing was saved on edit form submission |
| Delete image form listing | A prompt is given, once confirmed, the image is deleted | Prompt was given, image was then deleted |
| Add extra images to existing listing | Images will upload and appear in both the edit images view and on the listing details | Images uploaded correctly and were displayed |
| Delete listing | When delete action button is pressed a confirmation form will show, then the listing will be deleted and the user redirected back to My Listings | Redirected back to My Listings and the desired listing was deleted successfully.  |
| Logout | Asked to confirm log out, then taken to home page | Taken to home page after confirming that I want to log out |