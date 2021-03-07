import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''

  @app.route('/categories', methods=['GET'])
  def get_categories():
    try:
      categories = Category.query.all()
    
      categories_dic = {}

      for count, category in enumerate(categories,1):
        categories_dic[count] = category.type     
    
      return jsonify({
        'success': True,
        'categories':categories_dic
      })
    except:
      abort(405)

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions', methods=['GET'])
  def get_questions():
    try:
      questions = Question.query.all()
      categories = Category.query.all()
      page = request.args.get('page',1,type=int)
    
      start = (page - 1) * 10
      end = start + 10

      formatted_questions = [question.format() for question in questions]
      list_of_questions = formatted_questions[start:end]

      if(len(list_of_questions) == 0):
        abort(404)

      categories_dic = {}

      for count, category in enumerate(categories,1):
        categories_dic[count] = category.type     


      
      
      return jsonify({
        'success': True,
        'questions': list_of_questions,
        'total_questions':len(questions),
        'categories':categories_dic,
        'currentCategory':None,

      }) 
    except:
      abort(404) 
  

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = {}
    error= False
    try:
      question = Question.query.filter(Question.id == question_id).first()

      if question is None:
        abort(404)
      question.delete()
    except:
      error = True
      db.session.rollback()
    finally:
      db.session.close()

    if error:
      abort(422)
    else: return jsonify({'success': True})
      

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()
    



    error = False
    try:
      question = body['question']
      category = body['category']
      answer = body['answer']
      diff = body['difficulty']
      question = Question(question=question, category=category, answer=answer,difficulty=diff)
      print(question)
      question.insert()
    except:
      error = True
      db.session.rollback()
    finally:
      db.session.close()
    
    if error:
      abort(422)
    else:return jsonify({'success':True})


  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/searchQuestions', methods=['POST'])
  def search_questions():
    search_obj = request.get_json()
    search_term = search_obj['searchTerm']


    questions = Question.query.filter(Question.question.ilike("%" + search_term + "%")).all()

    if search_term == '':
      question = Question.query.all()
    formatted_questions = [question.format() for question in questions]

    print(formatted_questions)

    return jsonify({
      'success': True,
      'questions': formatted_questions,
      'total_questions':len(questions),
      'current_category':None
    }) 
    

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 
  @
  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<question_category>/questions')
  def categorical_questions(question_category, methods=['GET']):

    try:

      questions = Question.query.filter(Question.category == question_category).all()
      category = Category.query.filter(Category.id == question_category).first()

      formatted_questions = [question.format() for question in questions]
      current_category = category.format()

      return jsonify({
        'success': True,
        'questions': formatted_questions,
        'total_questions':len(questions),
        'current_category':current_category
      })
    except:
      abort(422)  


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def playQuiz():
    try:
      body = request.get_json()
      previous_questions = body.get('previous_questions')
      quiz_category = body.get('quiz_category')


      questions = []

      if not quiz_category['id'] == 0:
        questions = Question.query.filter(Question.category == quiz_category['id']).all()
      else: 
        questions = Question.query.all()

      next_question = random.choice(questions)


      flag = True

      while flag:
        if next_question.id in previous_questions:
          next_question = random.choice(questions)
        else:
          flag = False

      next_question = next_question.format()
      print(next_question)
      

      return jsonify({
        'success': True,
        'question': next_question
      })
    except:
      abort(400)
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success':False,
      'error':404,
      'message':'Resource Not Found'
    }), 404
  
  @app.errorhandler(422)
  def unable_to_process(error):
    return jsonify({
      'success':False,
      'error':422,
      'message':'Could not processs'
    }), 422
          
  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success':False,
      'error':405,
      'message':'Method not allowed'
    }), 405
  
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success':False,
      'error':400,
      'message':'Bad Request'
    }), 400
  
  return app

    