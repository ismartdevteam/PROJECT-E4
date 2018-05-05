# Learning Management System (LMS) - E4 Project
## ESIEE PARIS IMC 2017

## Requirements:
- [Django2] 
- [Python] >= 3.5
- [pip]

## Introduction
Learning management System (LMS) is a software application for the administration, documentation, tracking, reporting and delivery of educational courses. It helps the instructor deliver course material to the students, administer tests and other assignments, track student progress, and manage record-keeping. Proposed LMS in this project is mainly focused on online tests delivery but support a range of other uses; it will act as a platform for fully online exercises evaluation system.
This project is expected to deliver a flexible, easy to use and secure online portal that will act as a dashboard for several types of users including students and teachers.
The new LMS will facilitate professors with dynamic graphical reports of student evaluation in form of charts, interactive illustrations and will allow students to attempt exercises through a user friendly platform and communicate with professors by easy to use messaging system which are lacking in the currently available systems.  


##### The Django2 main project directory is :

    /PROJECT-E4/tree/master/_Project/LMS
##### To run the Django2 project go to main directory and run this command:
    
    python manage.py runserver



Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```


### Programming
#####	Work done
So far, in Django, we have managed to handle to logging in of the user, creation of a student dashboard as well as a teacher dashboard. This required programming multiple python files in the project. Details about the coding will be found in the code documentation. In addition to programing the views and models for the applications, the D3.js visual library was used inside the project to display the graphs through SVG. 
We created 3 applications that were used in the presentation. The “login” app which is responsible for handling the login requests. The “student” app, responsible for handling requests by users who are of type students. The “teacher” app, responsible for handling requests by users who are of type students.

#####	Work to be done
More users are to be implemented in the project. Missing users according to the project requirements are: “Creator”, “Didactician” and “Institutional Head” 


License
----

ESIEE

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Django2]: <https://www.djangoproject.com/download/>
   [Python]: <https://www.python.org/downloads/>
   [pip]: <https://pip.pypa.io/en/stable/installing/>
   [Gulp]: <http://gulpjs.com>

