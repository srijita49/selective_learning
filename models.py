import random
import math
import time
import itertools

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from selective_learning1.payoffmatrix import PayoffMatrix


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'selective_learning1'
    players_per_group = None
    num_rounds = 30
    num_rows = PayoffMatrix.n
    num_cells = PayoffMatrix.N
    num_choices = 9
    low_limit = PayoffMatrix.low_cutoff
    high_limit = PayoffMatrix.high_cutoff
    time_limit = 2
    cell_reveal = 9
    avg_reveal = 9
    both_reveal = 9
    cell_total_round = 1
    avg_total_round = 1
    both_total_round = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            reveal_cell_round = 0
            reveal_avg_round = 0
            reveal_both_round = 0
            player.participant.vars["reveal_cell_round"] = reveal_cell_round
            player.participant.vars["reveal_avg_round"] = reveal_avg_round
            player.participant.vars["reveal_both_round"] = reveal_both_round


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    problem = models.IntegerField(min=0, max= Constants.num_cells, blank= True)
    row_problem = models.IntegerField(min = 0, max = Constants.num_rows, blank= True )
    col_problem = models.IntegerField(min = 0, max = Constants.num_rows, blank= True )
    no_learning = models.IntegerField(initial = 0, blank = True)
    solution = models.FloatField(blank=True)
    cont_learning = models.BooleanField( initial = True)
    row_choice= models.IntegerField()
    column_choice= models.IntegerField()
    reveal_cell = models.IntegerField(initial = 0, blank = True)
    reveal_avg = models.IntegerField(initial = 0, blank = True)
    reveal_both = models.IntegerField(initial = 0, blank = True)

    prior = models.IntegerField()
    zeroes = models.IntegerField()
    cell_open = models.IntegerField(initial = 0)
    avg_open = models.IntegerField(initial = 0)
    ca_switch = models.IntegerField(initial= 0)
    ac_switch = models.IntegerField(intial = 0)

    treatment = models.IntegerField()
    reveal_no = models.IntegerField(initial = 0)

    row_choice_1= models.IntegerField()
    col_choice_1 = models.IntegerField()

    row_choice_2= models.IntegerField()
    col_choice_2 = models.IntegerField()

    row_choice_3= models.IntegerField()
    col_choice_3 = models.IntegerField()

    row_choice_4= models.IntegerField()
    col_choice_4 = models.IntegerField()

    row_choice_5= models.IntegerField()
    col_choice_5 = models.IntegerField()

    row_choice_6= models.IntegerField()
    col_choice_6 = models.IntegerField()

    row_choice_7= models.IntegerField()
    col_choice_7 = models.IntegerField()

    row_choice_8= models.IntegerField()
    col_choice_8 = models.IntegerField()

    row_choice_9= models.IntegerField()
    col_choice_9 = models.IntegerField()
