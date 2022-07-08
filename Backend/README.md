# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Managing Dependencies
After cloning the project, on your terminal navigate to project base folder (where requirements.txt is)
To install dependencies run the following command:

```
pip install -r requirements.txt
```

In case you add dependencies to the project, make sure you update requirements.txt by 
running the following command.

```
pip freeze > requirements.txt
```

### Seeding

```
python manage.py seed 
python manage.py seed --mode=fresh
```

### Running Migrations
Before you can run the project in development environment, you need to set up the 
migration. To create initial migrations run the following command:
```
python manage.py makemigrations
```

To sync your migration with the database use the following command:
```
python manage.py migrate
```

### Removing All Migrations Files
Sometimes in the course of development you find yourself at a point where you need to clear
migrations. You can use the following commands:

```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
```

```
find . -path "*/migrations/*.pyc"  -delete
```

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact