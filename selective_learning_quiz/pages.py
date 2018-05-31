from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from selective_learning_quiz.slQuiz import PayoffQuiz
import random
import math

class InstructionPage(Page):
    def is_displayed(self):
        poor_performance = False
        if self.round_number>1:
            if self.player.participant.vars["tot_correct_answer"] < 4:
                poor_performance = True
        return self.round_number == 1 or poor_performance

    def before_next_page(self):
        self.player.participant.vars.update(PayoffQuiz.CellQuestion(self))
        self.player.participant.vars.update(PayoffQuiz.AverageQuestion(self))
        random_index = [i for i in range(Constants.tot_no_of_q)]
        random.shuffle(random_index)
        all_questions = self.player.participant.vars["cell_questions"] + self.player.participant.vars["avg_questions"]
        all_answers = self.player.participant.vars["correct_payoff"] + self.player.participant.vars["true_num_list"]
        all_qtype = self.player.participant.vars["cutoff"] + [0]*(PayoffQuiz.no_of_avg_q)
        counter = 0
        for i in range(len(random_index)):
            self.player.participant.vars["random_questions"][i] = all_questions[random_index[i]]
            self.player.participant.vars["random_answers"][i] = all_answers[random_index[i]]
            self.player.participant.vars["question_types"][i] = all_qtype[random_index[i]]
        self.player.participant.vars["counter"] = counter


class QuizPage(Page):
    form_model = 'player'
    form_fields = ['solution']

    def vars_for_template(self):
        self.player.participant.vars["random_question"] =  self.player.participant.vars["random_questions"][self.player.participant.vars["counter"]]
        self.player.participant.vars["random_answer"] =  self.player.participant.vars["random_answers"][self.player.participant.vars["counter"]]
        self.player.participant.vars["question_type"] =  self.player.participant.vars["question_types"][self.player.participant.vars["counter"]]
        self.player.participant.vars["counter"] += 1

        return {"cell_questions": self.player.participant.vars["cell_questions"],
                "avg_questions": self.player.participant.vars["avg_questions"],
                "correct_payoff": self.player.participant.vars["correct_payoff"],
                "true_num_list": self.player.participant.vars["true_num_list"],
                "random_question": self.player.participant.vars["random_question"],
                "random_answer": self.player.participant.vars["random_answer"],
                "question_type": self.player.participant.vars["question_type"],
                "index_list": self.player.participant.vars["index_list"],
                "correct_answer" : self.player.participant.vars["correct_answer"]}


class Results(Page):
    def vars_for_template(self):
        if self.player.solution == self.player.participant.vars['random_answer']:
            self.player.participant.vars["correct_answer"] = True
            self.player.participant.vars["tot_correct_answer"] += 1
        else:
            self.player.participant.vars["correct_answer"] = False

        return {"correct_answer": self.player.participant.vars["correct_answer"],
                "tot_correct_answer": self.player.participant.vars["tot_correct_answer"]}


quiz_page_sequence = [QuizPage, Results]*(Constants.tot_no_of_q)
page_sequence = [InstructionPage ] + quiz_page_sequence
