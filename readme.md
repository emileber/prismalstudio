# Getting started #

## The virtual environment ##

You first need a Python virtual environment (venv). Get that running and then browse to the `venv/Scripts` directory using the command prompt and execute `activate.bat`.

Then you should see that the command prompt has changed from:

	c:\venv\Scripts>
to:

	(venv) c:\venv\Scripts>

Then browse to the django project root directory using that same command prompt window. Always keep it open or make you a script to get it open at first so you can skip the previous step each time you want to start to develop.

## Wampserver ##

You want to start wamp beforehand and if not already done, create a database for the website. No need to create table or other stuff, Django deal alone with all the SQL script and database validation.

## Versioning with Git ##

Use SourceTree.

Or, do it manually with the already open command prompt window.

	git add .
	git commit -m "your commit message"

# Hosting on Heroku #

See [Getting Started with Heroku](https://devcenter.heroku.com/articles/quickstart "Quickstart with Heroku").

Download the toolbelt, then log you in using the cmd:

	heroku login

other usefull heroku commands:

	// open the current app in browser
	heroku open
	heroku logs
	// for a django test shell
	heroku run python manage.py shell

## Pushing to Heroku ##

	git push heroku master