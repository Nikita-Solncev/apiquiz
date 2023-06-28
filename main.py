from flask import Flask, request
from flask_restful import Api, Resource
import json
import random

app = Flask(__name__)
api = Api()

with open("questions.json", "r", encoding="UTF-8") as file:
     questions = json.load(fp=file)

def get_random_question(difficulty):
      random_question, random_answers = random.choice(list(questions[difficulty].items()))
      return random_question, random_answers
    
class Main(Resource):
    def get(self):
         difficulty = request.args.get('difficulty')
         question, answers = get_random_question(difficulty)
         response = {}
         response[question] = answers
         return response


api.add_resource(Main, "/getquestion")
api.init_app(app)

if __name__ == "__main__":
    app.run()