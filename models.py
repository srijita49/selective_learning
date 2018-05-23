import random
import math
import time

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
    num_rounds = 2
    num_rows = PayoffMatrix.n
    num_cells = PayoffMatrix.N
    num_choices = 2


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    problem = models.IntegerField(min=0, max= Constants.num_cells, blank= True)
    row_problem = models.IntegerField(min = 0, max = Constants.num_rows, blank= True )
    col_problem = models.IntegerField(min = 0, max = Constants.num_rows, blank= True )
    solution = models.FloatField(blank=True)
    cont_learning = models.BooleanField( initial = True)
    row_choice= models.IntegerField(
                choices=[[0, 'average row'],
                        [1,'Row 1'],
                        [2,'Row 2']])
    column_choice= models.IntegerField(
                choices=[[0, 'average column' ],
                        [1,'Column 1'],
                        [2,'Column 2']])
