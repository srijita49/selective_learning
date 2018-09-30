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
    name_in_url = 'selective_learning2'
    players_per_group = None
    num_rounds = 30
    num_rows = PayoffMatrix.n
    num_cells = PayoffMatrix.N
    num_choices = 9
    low_limit = PayoffMatrix.low_cutoff
    high_limit = PayoffMatrix.high_cutoff
    time_limit = 5
    cell_reveal = 9
    avg_reveal = 9
    both_reveal = 9
    cell_reveal_limit = 1
    avg_reveal_limit = 1
    both_reveal_limit = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        treatment_group = itertools.cycle([1,2]) # cell type and 2 average type
        for player in self.get_players():
            player.treat_group = next(treatment_group)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    problem = models.IntegerField(min=0, max= Constants.num_cells, blank= True) # selected cell to be opened
    row_problem = models.IntegerField(min = 0, max = Constants.num_rows, blank= True ) # selected column average to be opened
    col_problem = models.IntegerField(min = 0, max = Constants.num_rows, blank= True ) # selected row average to be opened
    no_learning = models.IntegerField(initial = 0, blank = True) # chosen Pass

    solution = models.FloatField(blank=True) # solution calculated by the subject

    cont_learning = models.BooleanField( initial = True)

    reveal_cell = models.IntegerField(initial = 0, blank = True) # container for whether a cell is revealed, treatment 1
    reveal_avg = models.IntegerField(initial = 0, blank = True) # container for whether an average is revealed, treatment 2
    reveal_both = models.IntegerField(initial = 0, blank = True) # container for whether a cell OR average is revealed, treatment 3


    prior = models.IntegerField() # prior: type 1 - all three equally likely, type 2 - 54 with 50% chance, type 3 - no 54 case
    zeroes = models.IntegerField() # eealized number of zeroes


    cell_open = models.IntegerField(initial = 0) # Number of cells opened
    avg_open = models.IntegerField(initial = 0) # number of averages opened

    ca_switch = models.IntegerField(initial= 0) # number of times swiched from cell to average, should be 0
    ac_switch = models.IntegerField(initial= 0) # number of times switched from average to cell

    info_first = models.IntegerField(initial = -1) # cell 0 average 1
    info_last = models.IntegerField(initial = -1)

    treat_group = models.IntegerField(initial = 0) # group 1 : cell + both, group 2 : average + both
    treat_type = models.IntegerField(initial =0) # 1: cells, 2: averages, 3: both

    reveal_cell_total = models.IntegerField(initial = 0) # number of cells revealed
    reveal_avg_total = models.IntegerField(initial = 0) # number of averages revealed
    reveal_both_total = models.IntegerField(initial =0) # number of cells of averages revealed in treatment 3
    reveal_cell_total_in_both = models.IntegerField(initial = 0) # number of cells revealed in treatment 3
    reveal_avg_total_in_both = models.IntegerField(initial = 0) # number of averages revealed in treatment 3

    cell_reveal_round = models.IntegerField(initial = 0) # Number of times treatment 1 has been chosen
    avg_reveal_round = models.IntegerField(initial = 0)
    both_reveal_round = models.IntegerField(initial = 0 )

    # Final row and column choices and payoff
    row_choice_1= models.IntegerField()
    col_choice_1 = models.IntegerField()
    payoff_choice_1 = models.IntegerField()


    row_choice_2= models.IntegerField()
    col_choice_2 = models.IntegerField()
    payoff_choice_2 = models.IntegerField()

    row_choice_3= models.IntegerField()
    col_choice_3 = models.IntegerField()
    payoff_choice_3 = models.IntegerField()

    row_choice_4= models.IntegerField()
    col_choice_4 = models.IntegerField()
    payoff_choice_4 = models.IntegerField()

    row_choice_5= models.IntegerField()
    col_choice_5 = models.IntegerField()
    payoff_choice_5 = models.IntegerField()

    row_choice_6= models.IntegerField()
    col_choice_6 = models.IntegerField()
    payoff_choice_6 = models.IntegerField()

    row_choice_7= models.IntegerField()
    col_choice_7 = models.IntegerField()
    payoff_choice_7 = models.IntegerField()

    row_choice_8= models.IntegerField()
    col_choice_8 = models.IntegerField()
    payoff_choice_8 = models.IntegerField()

    row_choice_9= models.IntegerField()
    col_choice_9 = models.IntegerField()
    payoff_choice_9 = models.IntegerField()
