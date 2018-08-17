#!flask/bin/python
from flask import Flask,jsonify
from classes.questions import Questions
from answers.answers import Answers
app = Flask(__name__)
from app import app

@app.route('/questions',methods['GET'])
def show_all_questions():
    return jsonify('questions','questions'), 200

@app.route('/question/question_id>',methods['GET'])
def get_a_question(question_id):
	question=[question for question in questions if question['id']==question_id]
	if len(question)==0:
		abort(404)
	return jsonify('question','question[0]')
 
@app.route('/question',methods['POST'])
def create_a_question():
	if not request.json or not 'title' in request json:
		abort (400)
	question={
	        'id': questions[-1]['id']+1	
	        'title': request.json.['title'],
	        'description': request.json.get('description',""),
            'done':False
            }
    questions.append(question)
    return jsonify({'question':question}),201

@app.route('./answer/<answer_id>',methods['POST'])
def create_an_answer_to_a_question():
    return jsonify({"answers, answer"}, 201

if __name__ == '__main__':
    app.run(debug=True)