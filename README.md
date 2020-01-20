# Hood411
A web application that allows you to be in the loop about everything happening in your neighborhood.

## Author and contact details
* Jacques Kiruma
Email: jayruma@yahoo.com

# Project Description
A user of the application should be able to:

1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the hospital and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.

A search functionality is implemented where one can search for the different businesses and their images.

# SetUp and installation requirements
You need to have the following installed:
* Python3+
* Pip
* Virtual ```$ python3.6 -m venv virtual```
* Activate the virtual environment ```source virtual/bin/activate```
* Django==1.11 ```(virtual)$ pip install django==1.11```
* Install all requirements

### Setting up the database
The database in use for this project is Postgres
* Ensure postgress is installed. ``` $ sudo apt-get update```
* Step 2 ```sudo apt-get install postgresql postgresql-contrib```

### Run migrations
``` $ python manage.py makemigrations ```
``` $ python manage.py migrate ```


### Running the server
```python manage.py runserver```

# Behaviour Driven Development
Some of the behaviours in this application include;

| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Launch the site | User has to login or sign up before using the application | User is updated |
| Login | User is directed to create profile page | user is logged in |
| Create profile | Profile is updated and hood updated | users details are stored. |
| User can view their hood details | User can change hood detaols in the app | Hood details are displayed|
| Add business | User can add business in different neighbourhoods | Business is added and displayed on homepage|
| Post a notice | Notice displayed can only be viewed by the users of that neighbourhood | neighbours are updated in the neighbourhood|

## Technologies used
* Django a python frame-work
* Html
* Bootstrap

# Development
It would be so great to have your contributions! Just follow the instructions below.

* Clone the repo in your machine but ensure you have all the necessary modules.(You can find them in the set up instructions above)
* Create a new branch git branch contributions
* Edit your changes in your branch
* Run the application
* Push your changes so we can have a view!

# Live development
Currently the app is deployed to heroku. You can find it [here](https://hood411.herokuapp.com/)

## Known Bugs
User cannot register their own community, The admin has to set one up.

### LICENSE
MIT License

 Copyright (c) 2019 Jacques Kiruma III

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
