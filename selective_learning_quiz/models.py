from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from selective_learning_quiz.slQuiz import PayoffQuiz
import random
import math

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'selective_learning_quiz'
    players_per_group = None
    num_rounds = 3
    num_rows = 9
    low_limit = PayoffQuiz.lower_limit
    high_limit = PayoffQuiz.upper_limit
    tot_no_of_q = PayoffQuiz.no_of_cell_q + PayoffQuiz.no_of_avg_q


class Subsession(BaseSubsession):

    def creating_session(self):
        for player in self.get_players():
            random_questions = [0]*(Constants.tot_no_of_q)
            random_answers = [0]*(Constants.tot_no_of_q)
            question_types = [0]*(Constants.tot_no_of_q)
            index_list = [i for i in range(Constants.tot_no_of_q)]
            random_question = 0
            random_answer = 0
            question_type = 0
            correct_answer = False
            tot_correct_answer = 0
            player.participant.vars["random_questions"] = random_questions
            player.participant.vars["random_answers"] = random_answers
            player.participant.vars["question_types"] = question_types
            player.participant.vars["random_question"] = random_question
            player.participant.vars["random_answer"] = random_answer
            player.participant.vars["question_type"] = question_type
            player.participant.vars["index_list"] = index_list
            player.participant.vars["correct_answer"] = correct_answer
            player.participant.vars["tot_correct_answer"] = tot_correct_answer



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    solution = models.IntegerField(blank=True, min = 0, max = 9 )
