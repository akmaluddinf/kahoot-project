from flask import Flask, request, json, jsonify, g
import os

from . import router, quizzesFileLocation, questionsFileLocation
from ..utils.file import readFile, writeFile
from ..utils.authorization import verifyLogin

# bikin kuis baru
@router.route('/quizzes', methods=['POST'])
# @verifyLogin
def createQuiz():
    body = request.json
    # print("usernamenya adalah", g.username)

    quizData = {
        "total-quiz-available": 0,
        "quizzes": []
    }

    if os.path.exists(quizzesFileLocation):
        quizData = readFile(quizzesFileLocation)

    quizData["total-quiz-available"] += 1
    quizData["quizzes"].append(body)

    writeFile(quizzesFileLocation, quizData)

    return jsonify(quizData)

# meminta data kuis dan soalnya
@router.route('/quizzes/<quizId>') #kalau gaada methodnya itu defaulnya ["GET"]
def getQuiz(quizId):
    # nyari quiznya
    quizzesData = readFile(quizzesFileLocation)

    for quiz in quizzesData["quizzes"]:
        if quiz["quiz-id"] == int(quizId):
            quizData = quiz
            break

    # nyari soalnya
    questionsData = readFile(questionsFileLocation)

    for question in questionsData["questions"]:
        # question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)

#update dan delete quiz
@router.route('/quizzes/<quizId>', methods=["PUT", "DELETE"])
def updateDeleteQuiz(quizId):
    if request.method == "DELETE":
        return deleteQuiz(quizId)
    elif request.method == "PUT":
        return updateQuiz(quizId)

def deleteQuiz(quizId):
    
    quizzesData = readFile(quizzesFileLocation)

    for i in range(len(quizzesData["quizzes"])):
        if quizzesData["quizzes"][i]["quiz-id"] == int(quizId):
            quizzesData["quizzes"].pop(i)
            quizzesData["total-quiz-available"] -= 1
            break


    writeFile(questionsFileLocation, quizzesData)

    return jsonify(quizzesData)

def updateQuiz(quizId):
    body = request.json
    
    quizzesData = readFile(quizzesFileLocation)

    for i in range(len(quizzesData["quizzes"])):
        if quizzesData["quizzes"][i]["quiz-id"] == int(quizId):
            quizzesData["quizzes"][i]["quiz-category"] = body["quiz-category"]
            quizzesData["quizzes"][i]["quiz-name"] = body["quiz-name"]
            break

    writeFile(questionsFileLocation, quizzesData)

    return jsonify(quizzesData)