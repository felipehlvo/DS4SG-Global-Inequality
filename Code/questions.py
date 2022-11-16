import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
from pywebio.platform import *

# import visualizations
from Code.visualizations import *

def make_question_checkbox(prompt, options, correct, explanation, graph = False, next_question = None):
    # Clears the page
    clear()

    # Creates a checkbox prompt
    answer = checkbox(prompt, options = options)

    # Checks if the answer is correct
    if answer[0] == options[correct-1]:
        put_text("That's right!")
    else:
        put_text("Not quite")

    if graph:
        put_html(graph())

    put_text(explanation)

def make_question_input(prompt, options, correct, explanation, graph = False, next_question = None):
    # Clears the page
    clear()

    # Creates a checkbox prompt
    answer = input(prompt, type=options)

    # Checks if the answer is correct
    if abs(answer-correct) <= 5 :
        put_text("Good guess!, You are so close by ",abs(answer - correct), "points!")
    else:
        put_text("Not quite, Your answer is ", abs(answer - correct), "points away.")

    if graph:
        put_html(graph())

    put_text(explanation)


question_dict = {
    "question1": {
        "prompt": "Has GDP per capita increased or decreased in Brazil?",
        "options": ["Increased", "Decreased", "Stayed the same"],
        "correct": 1,
        "explanation": "As you can see in this graph, although there were some fluctutions, Brazil's GDP per capita has increased over time.",
        "graph": brazil_gdp
    },

    "question2": {
        "prompt": "Is inequality big in Brazil?",
        "options": ["Yes", "No"],
        "correct": 1,
        "explanation": "As you can see in this graph, inequality is big in Brazil.",
        "graph": None
    },

    "question3":{
        "prompt": "Hong Kong and Central African Republic has the highest and lowest life expectancy at birth respectively. What is the difference in life expectancy between the two countries? ",
        "options": ["15 years", "20 years", "25 years", "30 years"],
        "correct": 4,
        "explanation": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "graph": life_expectancy
    },

    "question4":{
        "prompt": "How many percentage of children in Zimbabue completed the birth registration and had legal proof of idenity in 2019? ",
        "options": NUMBER,
        "correct": 48.7,
        "explanation": "Nahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh I am working on it",
        "graph": None
    }
    
    ## Add more questions here
}


def question1():
    make_question_checkbox(**question_dict["question1"])
    put_buttons(["Next"], onclick=[question2])

def question2():
    make_question_checkbox(**question_dict["question2"])
    put_buttons(["Next"], onclick=[question3])

def question3():
    make_question_checkbox(**question_dict["question3"])
    put_buttons(["Next"], onclick=[question4])

def question4():
    make_question_input(**question_dict["question4"])
    put_buttons(["Next"], onclick=[question5])

def question5():
    #make_question(**question_dict["question3"])
    clear()
    put_text("In Development")