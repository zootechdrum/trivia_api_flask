# Udacity Trivia Flask App
 A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game. As a part of the FullStack Nanodegree, it serves as a practice module for lessons on API Development and Documentation. By completing this project I will apply the skills I learned about formatting API endpoints that leverage knowledge of HTTP and API development best practices. 

 [All backend code follows PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/)

 ## Pre-requisites and Local Development
 Developers using this project should already have Python3, pip and node installed on their local machines. 

 ### Backend
 From the backend folder rup pip3 install requirements.txt. All the required packages are included in the txt file. 

 To run the backend server, run the following commands:

export FLASK_APP=flaskr        
export FLASK_ENV=development
flask run

These commands put the application in development and directs our application to use <mark>__init__.py</mark> file in our flaskr folder. One of the advantages of working in dev mode is that the server will restart whenever you have made changes and saved changes to your application. 

The application is run on <mark>http://127.0.0.1:5000/<mark>

### Frontend

From the frontend folder, run the following commands to start the client:

npm install // run this once to install dependencies

npm start

The app should then start at localhost:3000

## Test

In order to run tests navigate to the backend folder and run these commands.

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

<mark>The first time you run the tests, omit the dropdb command</mark>


## Deployment N/A

## Authors

Cesar Gomez AKA zootechdrum