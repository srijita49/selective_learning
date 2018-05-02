from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import PayoffMatrix as pm


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'selective_learning1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    c11=models.FloatField(blank=True)
    c12=models.FloatField(blank=True)
    c21=models.FloatField(blank=True)
    c22=models.FloatField(blank=True)
    ca1=models.FloatField(blank=True)
    ca2=models.FloatField(blank=True)
    ra1=models.FloatField(blank=True)
    ra2=models.FloatField(blank=True)

    self.Row1=[c11, c12, ca1]
    self.Row2=[c21, c22, ca2]
    self.ARow=[ra1,ra2]

    row=models.IntegerField(
        choices=[
                [0, 'Average'],
                [1,'Red'],
                [2, 'Blue'],
                ]
            )
    column=models.IntegerField(
        choices=[
                [0, 'Average'],
                [1, 'Square'],
                [2, 'Circle'],
                ]
            )
    row_choice=models.IntegerField(
        choices=[
                [0, 'Average'],
                [1,'Red'],
                [2, 'Blue'],
                ]
            )
    column_choice=models.IntegerField(
        choices=[
                [0, 'Average'],
                [1, 'Square'],
                [2, 'Circle'],
                ]
            )
