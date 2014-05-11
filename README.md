django-twoscoops-project
========================

A personalized project template for Django 1.6 using postgres for development and production. Ready to deploy on Heroku.

To use this project follow these steps:

1. Create the new project using the django-two-scoops template
2. Create dev and prod virtual environments
3. Install dependences for both dev and prod
4. Create postgres database for dev
5. Create .env file for prod
6. Run the project in dev
7. Run the project in prod
8. Deploy to Heroku

*note: these instructions show creation of a project called "icecream". You
should replace this name with the actual name of your project.*

Create your project
===================

*Prerequisites: python, pip, django*

To create a new Django project called '**icecream**' using django-twoscoops-project, run the following command:

    $ django-admin.py startproject --template=https://github.com/imkevinxu/django-twoscoops-project/archive/master.zip --extension=py,md,bat,html --name=Procfile,Makefile icecream

Virtual Environments
====================

*Prerequisites: virtualenv, virtualenvwrapper*

    $ cd icecream
    $ mkvirtualenv icecream-dev && add2virtualenv `pwd` && deactivate
    $ mkvirtualenv icecream-prod && add2virtualenv `pwd` && deactivate

Install Dependencies
====================

For development:

    $ deactivate && workon icecream-dev
    $ pip install -r requirements/local.txt

For production:

    $ deactivate && workon icecream-prod
    $ pip install -r requirements.txt

*note: We install production requirements this way because many Platforms as a
Services expect a requirements.txt file in the root of projects.*

Local Postgres Database
=======================

*Prerequisites: Postgres*

Install Postgres for your OS [here](http://www.postgresql.org/download/). For Max OSX the easiest option is to download and run [Postgres.app](http://postgresapp.com/).

    $ createdb icecream

Set .env variable for prod
==========================

The SECRET_KEY for production is not version controlled so the first person to create this project needs to create a .env file for Foreman and Heroku to read into the environment. Hacky use of `date | md5` to generate a pseudo-random string.

.env is not version controlled so future collaboraters need to email the creator for it.

    $ echo "SECRET_KEY=`date | md5`" >> .env

Run project in dev
==================

Be in the same directory as `manage.py`.

    $ deactivate && workon icecream-dev
    $ python manage.py runserver

Run project in prod
===================

*Prerequisites: Heroku Toolbelt*

Be in the same directory as `Procfile`.

    $ deactivate && workon icecream-prod
    $ cd icecream && python manage.py collectstatic --noinput && cd ..
    $ foreman start

Deploy to Heroku
================

*Prerequisites: heroku-config*

    $ git init
    $ git add .
    $ git commit -m "ready for heroku deploy"
    $ heroku create
    $ heroku config:push
    $ git push heroku master
    $ heroku ps:scale web=1
    $ heroku open

TODO
====

- Syncdb instructions
- Database migration instructions

Follow Best Practices
=====================

![Two Scoops of Django](http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png "Two Scoops Logo")

This project follows best practices as espoused in [Two Scoops of Django: Best Practices for Django 1.6](http://twoscoopspress.org/products/two-scoops-of-django-1-6).

Acknowledgements
================

- Many thanks to Randall Degges for the inspiration to write the book and django-skel.
- All of the [contributors](https://github.com/twoscoops/django-twoscoops-project/blob/master/CONTRIBUTORS.txt) to this project.
