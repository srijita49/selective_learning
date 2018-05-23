import random
import math
import time

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from selective_learning1.payoffmatrix import PayoffMatrix


class InstructionPage(Page):
    def is_displayed(self):
        return self.round_number==1

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + 5*60

class InstructionTwoPage(Page):
    def before_next_page(self):
        for player in self.subsession.get_players():
            solution_list=[-1]*PayoffMatrix.N
            row_solution_list =[-1]*Constants.num_rows
            col_solution_list =[-1]*Constants.num_rows
            row_options= [i for i in range (0, Constants.num_rows+2) ]
            column_options=[i for i in range (0, Constants.num_rows+2) ]
            row_choices = []
            column_choices = []
            choice_list = [0]*(Constants.num_cells + 1)
            row_choice_list = [0]*Constants.num_rows
            column_choice_list = [0]*Constants.num_rows
            pay_list_round = []
            player.participant.vars.update(PayoffMatrix.PayoffList(self))
            player.participant.vars['solution_list'] = solution_list
            player.participant.vars['row_solution_list'] = row_solution_list
            player.participant.vars['col_solution_list'] = col_solution_list
            player.participant.vars['row_options'] = row_options
            player.participant.vars['column_options'] = column_options
            player.participant.vars['row_choices'] = row_choices
            player.participant.vars['column_choices'] = column_choices
            player.participant.vars['choice_list'] = choice_list
            player.participant.vars['row_choice_list'] = row_choice_list
            player.participant.vars['column_choice_list'] = column_choice_list
            player.participant.vars['pay_list_round'] = pay_list_round

    timer_text = 'Time left to finish this round:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry']-time.time()>3

class InformationPage(Page):
    def vars_for_template(self):
        return {'zeros': self.player.participant.vars['zeros'],
            'cutoff': self.player.participant.vars['random_cutoff'],
            'pay_list' : self.player.participant.vars['payoff_list'],
            'prob_list': self.player.participant.vars['problem_list'],
            'one_row': self.player.participant.vars['ones_row'],
            'one_col': self.player.participant.vars['ones_column'],
            'pay_matrix': self.player.participant.vars['payoff_matrix'],
            'row_avg': self.player.participant.vars['row_average'],
            'col_avg': self.player.participant.vars['column_average']}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry']-time.time()>3


class SelectProblemPage(Page):
    form_model = 'player'
    form_fields = ['problem','row_problem','col_problem']

    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry'] - time.time()>3)

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()


class ChooseToSolvePage(Page):
    form_model ='player'
    form_fields = ['solution']

    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry'] - time.time()>3)

    def vars_for_template(self):
        pid = self.player.problem
        pid_row = self.player.row_problem
        pid_col = self.player.col_problem
        if pid != None:
            pid_row= -1
            pid_col= -1
            self.player.participant.vars['solution_list'][pid] = self.player.solution
        elif pid_row != None:
            pid = -1
            pid_col= -1
            self.player.participant.vars['row_solution_list'][pid_row] = self.player.solution
        elif pid_col != None:
            pid = -1
            pid_row= -1
            self.player.participant.vars['col_solution_list'][pid_col] = self.player.solution
        return {'prob' : self.player.participant.vars['problem_list'][pid],
                'row_avg': self.player.participant.vars['row_average'][pid_row],
                'col_avg': self.player.participant.vars['column_average'][pid_col],
                'rand_cutoff': self.player.participant.vars['random_cutoff'],
                'zeros': self.player.participant.vars['zeros']}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

class ContinueLearningPage(Page):
    form_model ='player'
    form_fields = ['cont_learning']

    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry']-time.time()>3)

    def vars_for_template(self):
        pid = self.player.problem
        pid_row = self.player.row_problem
        pid_col = self.player.col_problem
        if pid != None:
            pid_row= -1
            pid_col= -1
            self.player.participant.vars['solution_list'][pid] = self.player.solution
        elif pid_row != None:
            pid = -1
            pid_col= -1
            self.player.participant.vars['row_solution_list'][pid_row] = self.player.solution
        elif pid_col != None:
            pid = -1
            pid_row= -1
            self.player.participant.vars['col_solution_list'][pid_col] = self.player.solution
        return{'sol_list' : self.player.participant.vars['solution_list'],
                'row_sol_list': self.player.participant.vars['row_solution_list'],
                'col_sol_list':self.player.participant.vars['col_solution_list']}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()




class FinalChoiceOnePage(Page):
    form_model = 'player'
    form_fields = ['row_choice', 'column_choice']

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry']-time.time()>3



class FinalChoiceTwoPage(Page):
    def vars_for_template(self):
        rid = self.player.row_choice
        cid = self.player.column_choice
        payoff_row =[]
        if rid != 0 and cid != 0:
            self.player.participant.vars['choice_list'][(rid-1)*Constants.num_rows + (cid-1)] = 1
        elif rid == 0 and cid != 0:
            self.player.participant.vars['column_choice_list'][cid-1] = 1
        elif rid!=0 and cid == 0:
            self.player.participant.vars['row_choice_list'][rid-1] = 1
        else:
            self.player.participant.vars['choice_list'][-1] = 1
        for i in range(Constants.num_cells):
            if self.player.participant.vars['choice_list'][i] == 1:
                self.player.participant.vars['pay_list_round'].append(self.player.participant.vars['check_payoff'][i])
        for i in range(Constants.num_rows):
            if  self.player.participant.vars['row_choice_list'][i] == 1:
                payoff_row = self.player.participant.vars['check_payoff'][i*Constants.num_rows : (i+1)*Constants.num_rows]
                rand_row= random.randint(1, len(payoff_row))
                self.player.participant.vars['pay_list_round'].append(payoff_row[rand_row-1])
        for i in range(Constants.num_rows):
            if self.player.participant.vars['column_choice_list'][i] == 1:
                payoff_col = self.player.participant.vars['check_payoff'][i: Constants.num_rows*(Constants.num_rows -1) + i+1: Constants.num_rows]
                rand_col = random.randint(1, len(payoff_col))
                self.player.participant.vars['pay_list_round'].append(payoff_col[rand_col-1])
        if rid == 0:
            self.player.participant.vars['row_choices'].append('average row')
        else:
            self.player.participant.vars['row_choices'].append( 'row '+ str(self.player.participant.vars['row_options'][rid]))
        if cid == 0:
            self.player.participant.vars['column_choices'].append('average column')
        else:
            self.player.participant.vars['column_choices'].append('column '+ str(self.player.participant.vars['column_options'][cid]))

        return {'row_choices': self.player.participant.vars['row_choices'],
                'column_choices': self.player.participant.vars['column_choices'],
                'choice_list': self.player.participant.vars['choice_list'],
                'row_choice_list': self.player.participant.vars['row_choice_list'],
                'column_choice_list': self.player.participant.vars['column_choice_list'],
                'pay_list_round' : self.player.participant.vars['pay_list_round']}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry']-time.time()>3

    def before_next_page(self):
        rand_choice = random.randint(1, len(self.player.participant.vars['pay_list_round']))
        self.player.payoff = self.player.participant.vars['pay_list_round'][rand_choice-1]



class ResultsPage(Page):
    def vars_for_template(self):
        return {'finalpayoff': self.player.payoff,
                'totalpayoff': self.player.participant.payoff}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.participant.vars['expiry']-time.time()>3


num_of_tries= PayoffMatrix.N + 2*PayoffMatrix.n
learning_page_sequence = [SelectProblemPage, ChooseToSolvePage,ContinueLearningPage]*num_of_tries
choice_page_sequence = [FinalChoiceOnePage, FinalChoiceTwoPage]*Constants.num_choices
page_sequence = [ InstructionPage, InstructionTwoPage] + learning_page_sequence + choice_page_sequence + [ResultsPage]
