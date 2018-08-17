import unittest
import json
from app import create_app, json
 
class stackoverflow_apiTestCase(unnitest.stackoverflow_apiTestCase)
     """This class represents the stackoverflow_api testcase"""


    def setUp(self):
    	"""Define test variables and initialize the app."""
    	self.app=create_app(config_name="testing")
    	self.client=self.app.test_client
    	self.stackoverflow_api={"questions": "questions"}

    	#binds the app to the current context


    def test_stackoverflow_api_can_show _all_questions(self):
    	""Test API can show all questions(GET)""
    	res= self.client().get('/stackoverflow_api',data=self.stackoverflow_api)
    	self.assertEqual(res.status_code, 200)
        self.assertIn("what is flask?",str(res.data))

     def test_stackoverflow_api_can_get_a_ question(self):
    	""Test API can show a question(GET)""
    	res= self.client().get('/stackoverflow_api',data=self.stackoverflow_api)
    	self.assertEqual(res.status_code, 200)
        self.assertIn("what is flask?",str(res.data))

    def test_stackoverflow_api_can_add_a_question(self):
        """Test API can create a question (POST question)"""
        res = self.client().post('/stackoverflow_api/', data=self.stackoverflow_api)
        self.assertEqual(res.status_code, 201)
        self.assertIn('What is flask?', str(res.data))

    def test_stackoverflow_api_can_add_an_answer_to_a_question(self):
        """Test API can create an answer to a question (POST answer)"""
        res = self.client().post('/stackoverflow_api/', data=self.stackoverflow_api)
        self.assertEqual(res.status_code, 201)
        self.assertIn('What is flask?', str(res.data))