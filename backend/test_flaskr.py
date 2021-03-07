from models import setup_db, Question, Category
from flaskr import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import unittest
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        database_port = os.environ.get('database_port')
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.port = os.environ.get('database_port')
        self.database_name = os.environ.get('database_name')
        self.database_path = "postgres://{}/{}".format(
            self.port, self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful"""\
    """
    operation and for expected errors.
    """

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

    def test_get_categories_wrong_method(self):
        res = self.client().post('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertIs(type(data['total_questions']), int)
        self.assertIs(type(data['categories']), dict)

    def test_get_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    # def test_delete_question(self):
    #     res = self.client().delete('/questions/3')
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    def test_fail_delete_question(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)

    def test_add_question(self):
        res = self.client().post('/questions', json={
            'question': 'Why are you doing this?',
            'answer': 'Because of small sausage',
            'category': 1,
            'difficulty': '4'}
        )
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_fail_add_question(self):
        # Question was not provided
        res = self.client().post('/questions', json={
            'answer': 'Because of small sausage',
            'category': 1,
            'difficulty': '4'}
        )
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 422)

    def test_search_question(self):
        res = self.client().post('/searchQuestions', json={
            'searchTerm': 'Because of small sausage'}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIs(type(data['questions']), list)
        self.assertIs(type(data['total_questions']), int)
        self.assertEqual(data['current_category'], None)

    def test_question_by_categry(self):
        res = self.client().get('/categories/1/questions')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIs(type(data['questions']), list)
        self.assertIs(type(data['total_questions']), int)
        self.assertIs(type(data['current_category']), dict)

    def test_get_requesting_beyond_valid_page(self):
        res = self.client().get('/categories/100/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Could not processs")

    def test_quiz(self):
        res = self.client().post(
            '/quizzes',
            json={
                'previous_questions': [4],
                'quiz_category': {'type': 'Science', 'id': '1'}
            },
        )

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIs(type(data['question']), dict)

    def test_quiz_fail(self):
        res = self.client().post(
            '/quizzes',
            json={
                'previous_questions': [],
            },
        )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        # self.assertIs(type(data['question']),dict)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
