
# Project Title
Hoodville
[![hoodlanding.png](https://i.postimg.cc/fT6nBkJ7/hoodlanding.png)](https://postimg.cc/9rtnfmPz)
## User story
#### -Sign in with the application to start using.
#### -Set up a profile about me and a general location and my neighborhood name.
#### -Find a list of different businesses in my neighborhood.
#### -Find Contact Information for the health department and Police authorities near my neighborhood.
#### -Create Posts that will be visible to everyone in my neighborhood.
#### -Change My neighborhood when I decide to move out.
#### -Only view details of a single neighborhood.
## Setup and installation
To get the project .......
### Cloning the repository:
https://github.com/Olliemint/Hood-101.git
### Navigate into the folder and install requirements
cd Hood
### Install and activate Virtual
- python3 -m venv virtual - source virtual/bin/activate
### Install Dependencies
pip install -r requirements.txt
### Setup Database
SetUp your database User,Password, Host then make migrate
### Migrate
python manage.py makemigrations hood
python manage.py migrate
### Run the application
python manage.py runserver
## Running the tests
* To run the tests for the class files:
        $ python3.8 manage.py tests
Open the application on your browser 127.0.0.1:8000.
## Deployment
For deployment to heroku,please follow instructions here (https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0)
### Technologies
* python3.8
* Django 
* Virtualenv
## Authors
* **Oliver Maiyo**
* **Valarie Rono**
## License
MIT Copyright (c) 2022 Oliver Maiyo,Valarie Rono
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.