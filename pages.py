from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Information(Page):
    form_model=player
    form_fields= [c11, c12, c21, c22, ca1, ca2, ra1, ra2, row, column]

class MyWaitPage(Page):
    timeout_seconds=5

class Results(Page):
    form_model=player
    form_fields=[row_choice, column_choice]


page_sequence = [
    Instructions,
    Information,
    Choice,
    MyWaitPage,
    Choice,
    ]
