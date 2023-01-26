# Next-Boat

NextBoat is a classifieds listing website that connect buyers and sellers of boats. The wbeiste allows seller to create listings and then for potential buyers to browse these listings. The website also includes an in-built messaging app, allowing buyers to contact sellers in a secure way without having to give out personal information.

![NextBoat responsive image](readme_assets/responsive_mockup.png)

## Design Process

### UX Design & Agile

- In Agile software development, user stories are used to capture the requirements for a particular feature or piece of work. They are typically written from the perspective of an end user using the format:
    - As a **role** I can **functionality** so that **benefit**

- For this project I used GitHub's built in Projects feature, to organise the Agile devlopment process. A Kanban board was created which featured three columns, Todo, In Progress & Done. 
    - The project Kanban board can be viewed (here)[https://github.com/users/ancfoster/projects/2/views/1]

- New User stories were created as Issues and placed in the Todo column. A user story being developed was placed in the 'In Progress' column, whilst completed user stories were placed in the 'Done' column. 

- User stories were labelled, 'must have', 'should have', 'could have'.

### User Stories

**Implemented user stories** | All user stories labelled as 'must have' or 'should have' were completed.

- View Listings
    - As a user I can browse boat listings so that I can see if there is a boat on NextBoat that I am interested in

- View detailed information about a boat
    - As a user I can see a detailed view of a listing so that I can learn as much information about a boat and see a gallery of images of that boat

- Create a listing
    - As a user I can create a boat listing so that I can allow other users to see my boat is for sale and view the boat particulars, price and photos

- Edit Listing
    - As a user I can edit a listing so that I can update listing information and listing images

- Delete Listing
    - As a user I can delete a listing so that I can remove my boat from the site if I no longer wish it to be on there.

- Send a message
     - As a user I can initiate a message chat with a boat owner so that so that I can express interest in a boat on NextBoat and/or ask the owner questions about this boat
     - As a user I can respond to a potential buyer's message so that I can communicate with them

- View Messages
    - As a user I can view sent & received messages so that I can communicate with other NextBoat users and see past messages in a message exchange

- Favourite Listings
    - As a user I can **mark listings as a 'favorite' ** so that I can save boats I like the look of as I browse the site, so that I can then view them another time without having to find them in the listings again.

- Compress Uploaded Image Files
    - As a site owner the site will automatically compress and resize uploaded images so that I can reduce cloud storage and bandwidth costs
    - As a user the site will automatically compress and resize uploaded images so that pages will load quickly, improving the overall user experience.

**User stories not implemented**

- Filter Listings
    - As a user I can filter listings so that I can only see boat listings that meet my criteria

- Share Boat
    - As a user I can open a share modal so that share a boat listing on popular services like WhatsApp, Facebook and by email

These are stories, labelled as 'could have' that were not implemented in this iteration. As part of the agile process they will stay on the Kanban board for the next itertaion and their label reviewed as part of the iteratiob planning.

### Visual Design

#### Colours

![Colour swatch](readme_assets/colours.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

![CSS & Font root variables](readme_assets/css_vars.png)

#### Fonts

I've used CSS `:root` variables to easily update font-weights scheme by changing only one value, instead of everywhere in the CSS file.

The nextboat project makes use of Adobe Fonts.

Only one font (with multiple weights) is used in the project:

- [Proxima Nova](https://fonts.adobe.com/fonts/proxima-nova)

![Proxima Nova](readme_assets/font.png)

#### Icons

- [Google Font Icons](https://fonts.google.com/icons)

Icons were used throughout the site to improve the user interface.

- e.g My Listings - a trashcan icon is used to represent delete functionality, a pen to represent edit.

- e.g Favourites - on a listing a user can add and remove the listing to their favourites by using a heart icon as a toggle button.

- Icons are also used in the account dropdown menu.

## Features

## Database Schema 


### Features for future iterations/sprints

- Email integration
    - Email sent upon account creation
    - Password reset emails
    - Notification emails

- The site owners would eventually like to monetise the site. To do the following features need to be implemented.
    - Users will have to pay a small fee to list their boat on the site.
    - Users will be able to pay to boost their boat listing within the listing results.

- The site owners wish to attract businesses like yacht brokers and boat yards. To facilitate this the following features will need to be added:
    - Different account types, personal and business.
    - There will be a business dashboard for business users so that they can get detailed infromation about their listings. e.g Number of listing views
    - Integration with popular CRM solutions.

- To increase site traffic the site owners would also like dynamic integration with Google Ads, so that adverts for listings can be dynamically generated.

- An analytics system to track the listing prices of different kinds of boats over time. 

## Technologies Used

### Front-End

- HTML5 - hypertext markup language is the standard language for designing files to be displayed in a web browser like Chrome or Safari. 

- CSS3 - cascading style sheets is a language used for styling a file written in a markup language like HTML.

- JavaScript (ES11) is a scripting language and one of the main technologies of web development. In this project it was used on the client side for webpage behavior.

### Back-End

- [Django](https://www.djangoproject.com/) an open-source, Python-based web framework that follows the model–template–views (MTV) architectural pattern.

- [PostgreSQL](https://www.postgresql.org/) is an open-source relational database management system (RDBMS)

- [Python](https://www.python.org/) is a high-level, general-purpose programming language and was used for the backend. The use of Django as the selected framework dictated the use of Python.

- [Heroku](https://heroku.com/) is a cloud platform as a service (PaaS) supporting several programming languages and database. Heroku is used to host the deployed application and PostgreSQL database.

- [AWS S3](http://aws.amazon.com/s3/) was used for hosting the Django static files and user uploaded media. Amazon Simple Storage Service is a service offered by Amazon Web Services (AWS) that provides object storage through a web service interface.

### Packages Used

Further details on all Python packages used on this project can be found in the requirements.txt file.
| Package | Version | Description |
|---|---|---|
| asgiref | 3.5.2 | ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and positioned as an asynchronous successor to WSGI. |
| backports.zoneinfo | 0.2.1 | Backport of the standard library module zoneinfo |
| boto3 | 1.26.12 | Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2 |
| botocore | 1.29.12 | A low-level interface to a growing number of Amazon Web Services. The botocore package is the foundation for the AWS CLI  |
| dj-database-url | 1.0.0 | Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application. |
| Django | 3.2.16 | Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. |
| django-allauth | 0.51.0 | Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication. |
| django-multiupload | 0.6.1 | Simple drop-in multi file upload field for django forms using HTML5's multiple attribute. |
| django-storages | 1.13.1 | Adds support for storage backends in Django |
| gunicorn | 20.1.0 | A Python WSGI HTTP Server for UNIX. |
| jmespath | 1.0.1 | JSON Matching Expressions |
| oauthlib | 3.2.2 | A generic, spec-compliant, thorough implementation of the OAuth request-signing logic |
| Pillow | 9.3.0 | Python Imaging Library adds image processing capabilities |
| psycopg2-binary | 2.9.5 | PostgreSQL database adapter for the Python programming language |
| PyJWT | 2.6.0 | JSON Web Token implementation in Python |
| python3-open-id | 3.2.0 | A set of Python packages to support use of the OpenID decentralized identity system |
| pytz | 2022.7 | Accurate and cross platform timezone calculations |
| requests-oauthlib | 1.3.1 | Provides OAuth library support for requests |
| s3transfer | 0.6.0 | For managing Amazon S3 transfers |
| sqlparse | 0.4.3 | A non-validating SQL parser. |


## Tools Used

- For writing the project code, [GitPod](https://gitpod.io) a cloud based version of Visual Studio code was used,

- [GitHub](https://github.com]) was used for hosting the online repository, it provides an online version of Git, a source code management tool. 

- [GitHub](https://github.com) was also used as the agile project management tool. GitHub contains a Projects feature that allows for the creation of Kanban boards.

- Adobe Illustrator was used to site graphics. 

- [Figma](https://figma.com) was used to create wirefames, UX prototypes and mockups.

## Testing

- For all testing, please refer to the [TESTING.md](TESTING.md) file.


## Deployment

- The NextBoat application was deployed on [Heroku](https://heroku.com) a cloud platform as a service.

- [AWS S3](http://aws.amazon.com/s3/) was used for hosting the Django static files and user uploaded media. Amazon Simple Storage Service is a service offered by Amazon Web Services (AWS) that provides object storage through a web service interface.

### Heroku deployment steps


### AWS S3 configuration steps



### Local deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

`git clone https://github.com/ancfoster/Next-Boat.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in GitPod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ancfoster/Next-Boat)


## Credits

### Technical documentation and tutorials

- I followed a tutorial created by [Michael Herman](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) on how to configure a Django application to store static and media files on AWS S3.

- Extensive use was made of the [Django project documentation](https://docs.djangoproject.com/en/4.1/)

- Code snippet from Stackoverflow user [artem](https://stackoverflow.com/questions/8317537/django-templates-split-string-to-array) to convert a string into an array with a custom Django template filter

- [Code snippet](https://stackoverflow.com/questions/48248405/cannot-write-mode-rgba-as-jpeg) from Stackoverflow user [Prahlad Yeri](https://stackoverflow.com/users/849365/prahlad-yeri) Using PILLOW to convert an uploaded image if it is a PNG with alpha channel, which would otherwise cause an error when converting the upload file to .JPG format. 

### Acknowledgements
I would like to thank my Code Institute mentor Tim Nelson for providing invaluable guidance duirng the development of this project