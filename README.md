# Next-Boat

NextBoat is a classifieds listing website that connect buyers and sellers of boats. The wbeiste allows seller to create listings and then for potential buyers to browse these listings. The website also includes an in-built messaging app, allowing buyers to contact sellers in a secure way without having to give out personal information.

![NextBoat responsive image](readme_assets/responsive_mockup.png)

## Design Process

### UX Design & Agile

- In Agile software development, user stories are used to capture the requirements for a particular feature or piece of work. They are typically written from the perspective of an end user using the format:
    - As a ** role ** I can ** capability ** so that ** benefit **

- For this project I used GitHub's built in Projects feature, to organise the Agile devlopment process. A Kanban board was created which featured three columns, Todo, In Progress & Done. 

- New User stories were created as Issues and placed in the Todo column. A user story being developed was placed in the 'In Progress' column, whilst completed user stories were placed in the 'Done' column. 

- User stories were labelled, 'must have', 'should have', 'could have'.

#### User Stories

** Implemented user stories ** | All user stories labelled as 'must have' or 'should have' were completed.

- As a user I can browse boat listings so that I can see if there is a boat on NextBoat that I am interested in
- 

** Implemented user stories not implemented **
As part of the agile process, user stories were 

### UI Design

## Features

### Current features


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

- HTML - hypertext markup language is the standard language for designing files to be displayed in a web browser like Chrome or Safari. 

- CSS - cascading style sheets is a language used for styling a file written in a markup language like HTML.

- JavaScript (ES11) is a scripting language and one of the main technologies of web development. In this project it was used on the client side for webpage behavior.


- [Django](https://www.djangoproject.com/) an open-source, Python-based web framework that follows the model–template–views (MTV) architectural pattern.

- [PostgreSQL](https://www.postgresql.org/) is an open-source relational database management system (RDBMS)

- [Python](https://www.python.org/) is a high-level, general-purpose programming language and was used for the backend. The use of Django as the selected framework dictated the use of Python.

- [Heroku](https://heroku.com/) is a cloud platform as a service (PaaS) supporting several programming languages and database. Heroku is used to host the deployed application and PostgreSQL database.

- [AWS S3](http://aws.amazon.com/s3/) was used for hosting the Django static files and user uploaded media. Amazon Simple Storage Service is a service offered by Amazon Web Services (AWS) that provides object storage through a web service interface.


## Tools Used

- For writing the project code, [GitPod](https://gitpod.io) a cloud based version of Visual Studio code was used,

- [GitHub](https://github.com]) was used for hosting the online repository, it provides an online version of Git, a source code management tool. 

- [GitHub](https://github.com) was also used as the agile project management tool. GitHub contains a Projects feature that allows for the creation of Kanban boards.

- Adobe Illustrator was used to make site graphics. 

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