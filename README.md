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

The application is run on http://127.0.0.1:5000/

### Frontend

From the frontend folder, run the following commands to start the client:

npm install  *run this once to install dependencies*

npm start

The app should then start at localhost:3000

## Test

In order to run tests navigate to the backend folder and run these commands.

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py

:exclamation: The first time you run the tests, omit the dropdb command :exclamation:

## API Reference

 ### Getting Started
 - Authentication: This application does require any authentication for user keys.
 - This app can only run locally and is not hosted anywhere. The backend app is hosted at the default http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.

## Error Handling

Errors are returned as JSON objects in the following format:

```
{
    'success':False,
    'error':404,
    'message':'Resource Not Found'
}
```

The API will return four error types when requsts fial:

- 404 Resource Not Found
- 422 Not Processable
- 405 Method Not Allowed
- 400 Bad Request

## EndPoints

# GET /questions

- Returns a list of question, a dictonary of cateogories, the number of total questions
- Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample ```curl http://127.0.0.1:5000/questions```

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": null,
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": "5",
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "6",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "6",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": "4",
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "3",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "3",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 18
}
```
# GET /categories/<question_category>/questions
- Sample ```curl http://127.0.0.1:5000/categories/1/questions```
- Returns a list of questions,current category, and total number of questions based on the category number passed in the URL.
- Results are paginated in groups of 10. Include a category argument to choose a category.
```
{
  "current_category": {
    "id": 1,
    "type": "Science"
  },
  "questions": [
    {
      "answer": "The Liver",
      "category": "1",
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": "1",
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
  ],
  "success": true,
  "total_questions": 9
}
```

# GET /categories
- Sample ```curl http://127.0.0.1:5000/categories```
- Returns a dictonary of available categories.

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```
# DELETE /questions/<question_id>
- Sample ```curl -X "DELETE" http://127.0.0.1:5000/questions/1```
- Returns a success message following a successful deletions of question.

```
{
  "success": true
}
```
# POST /questions
- Sample ```curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d "{\"question\":\"who is evil\",\"category\":\"1\",\"difficulty\":\"2\",\"answer\":\"amazon\"}"```
- Returns a success message after a question has been added to the database. .
  The above curl request would output the following:
```
{
  "success": true
}
```

# POST /searchTerm
- Sample ```curl -X POST http://127.0.0.1:5000/searchQuestions -H "Content-Type:application/json" -d "{\"searchTerm\":\"what\"}"```
- Returns a list of questions that have that search term passed in as a json object by the client.
  The above curl request would output the following:
```
{
{
  "current_category": null,
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": "4",
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": "5",
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": "5",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "5",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Lake Victoria",
      "category": "3",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "Mona Lisa",
      "category": "2",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "The Liver",
      "category": "1",
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Blood",
      "category": "1",
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 8
}
}
```
# POST /quizzes
- Sample ```curl -X POST curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [],"quiz_category":{"type": "Science", "id": "1"}}'```
- Returns the next question that will be given to the client to the user can answer.
  The above curl request would output the following:
  ```
  {
  "question": {
    "answer": "amazon",
    "category": "1",
    "difficulty": 2,
    "id": 32,
    "question": "who is evil"
  },
  "success": true
}
  ```


## Deployment N/A

## Authors

Cesar Gomez AKA zootechdrum