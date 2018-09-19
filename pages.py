import random
import math
import time

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

from selective_learning1.payoffmatrix import PayoffMatrix

class TimerPage(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + Constants.time_limit*60

class InstructionTwoPage(Page):
    def before_next_page(self):
        for player in self.subsession.get_players():
            solution_list=[-1]*PayoffMatrix.N
            row_solution_list =[-1]*Constants.num_rows
            col_solution_list =[-1]*Constants.num_rows
            problem_type = []
            row_options= [i for i in range (0, Constants.num_rows+2) ]
            column_options=[i for i in range (0, Constants.num_rows+2) ]
            row_choices = []
            column_choices = []
            choice_list = [0]*(Constants.num_cells + 1)
            row_choice_list = [0]*Constants.num_rows
            column_choice_list = [0]*Constants.num_rows
            pay_list_round = []
            problem_no = ''
            reveal_cell_no = 0
            reveal_avg_no = 0
            reveal_both_no = 0
            treatment_random = random.uniform(0,1)
            if (treatment_random > 0.75) & (self.player.participant.vars['reveal_cell_round'] <= Constants.cell_total_round) & (self.round_number > 1):
                treatment_type = 1
                self.player.participant.vars['reveal_cell_round'] = self.player.participant.vars['reveal_cell_round'] + 1
            elif (treatment_random > 0.5) & (treatment_random <= 0.75) & (self.player.participant.vars['reveal_avg_round'] <= Constants.avg_total_round) & (self.round_number >1):
                treatment_type = 2
                self.player.participant.vars['reveal_avg_round'] = self.player.participant.vars['reveal_avg_round'] + 1
            elif (treatment_random > 0.25) & (treatment_random <= 0.5) & (self.player.participant.vars['reveal_both_round'] <= Constants.both_total_round) & (self.round_number >1):
                treatment_type = 3
                self.player.participant.vars['reveal_both_round'] = self.player.participant.vars['reveal_both_round'] + 1
            else :
                treatment_type = 0

            player.participant.vars.update(PayoffMatrix.PayoffList(self))
            player.participant.vars['solution_list'] = solution_list
            player.participant.vars['row_solution_list'] = row_solution_list
            player.participant.vars['col_solution_list'] = col_solution_list
            player.participant.vars['problem_type'] = problem_type
            player.participant.vars['row_options'] = row_options
            player.participant.vars['column_options'] = column_options
            player.participant.vars['row_choices'] = row_choices
            player.participant.vars['column_choices'] = column_choices
            player.participant.vars['choice_list'] = choice_list
            player.participant.vars['row_choice_list'] = row_choice_list
            player.participant.vars['column_choice_list'] = column_choice_list
            player.participant.vars['pay_list_round'] = pay_list_round
            player.participant.vars['problem_no'] = problem_no
            player.participant.vars['treatment_type'] = treatment_type
            player.participant.vars['reveal_cell_no'] = reveal_cell_no
            player.participant.vars['reveal_avg_no'] = reveal_avg_no
            player.participant.vars['reveal_both_no'] = reveal_both_no



    def vars_for_template(self):
        if self.round_number == 1:
            payoff = 0
        else:
             payoff =  self.player.in_round(self.round_number-1).payoff
        return{ 'finalpayoff' : payoff,
                'totalpayoff': self.participant.payoff}

    timer_text = 'Time left to finish this round:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry']-time.time()>3

class PriorPage(Page):
    def vars_for_template(self):
        return{'prior_type': self.participant.vars['prior_type'],
                'zeros': self.participant.vars['zeros']}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry']-time.time()>3

class TreatmentTypePage(Page):
    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry'] - time.time()>3) and (self.participant.vars['treatment_type'] != 0)

    def vars_for_template(self):
        return{'treat_type': self.player.participant.vars["treatment_type"]}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

class SelectProblemPage(Page):
    form_model = 'player'
    form_fields = ['problem','row_problem','col_problem', 'no_learning']

    def vars_for_template(self):
        return {'zeros': self.player.participant.vars['zeros'],
            'cutoff': self.player.participant.vars['random_cutoff']}

    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry'] - time.time()>3)

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()


class ChooseToSolvePage(Page):
    form_model ='player'
    form_fields = ['solution', 'reveal_cell', 'reveal_avg', 'reveal_both']

    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry'] - time.time()>3) and (self.player.no_learning != 1)

    def vars_for_template(self):
        pid = self.player.problem
        pid_row = self.player.row_problem
        pid_col = self.player.col_problem
        if pid != None:
            pid_row= -1
            pid_col= -1
            self.player.participant.vars['problem_no'] = "P"+str(self.player.problem + 1)
            self.player.participant.vars['solution_list'][pid] = self.player.solution
            self.player.participant.vars['problem_type'].append(0)
        elif pid_row != None:
            pid = -1
            pid_col= -1
            self.player.participant.vars['problem_no'] = "R"+str(self.player.row_problem + 1)
            self.player.participant.vars['row_solution_list'][pid_row] = self.player.solution
            self.player.participant.vars['problem_type'].append(1)
        elif pid_col != None:
            pid = -1
            pid_row= -1
            self.player.participant.vars['problem_no'] = "C"+str(self.player.col_problem + 1)
            self.player.participant.vars['col_solution_list'][pid_col] = self.player.solution
            self.player.participant.vars['problem_type'].append(1)
        return {'prob' : self.player.participant.vars['problem_list'][pid],
                'row_avg': self.player.participant.vars['row_average'][pid_row],
                'col_avg': self.player.participant.vars['column_average'][pid_col],
                'prob_type':self.player.participant.vars['problem_type'],
                'rand_cutoff': self.player.participant.vars['random_cutoff'],
                'zeros': self.player.participant.vars['zeros'],
                'problem_no': self.player.participant.vars['problem_no'],
                'treat_type': self.player.participant.vars["treatment_type"],
                'reveal_cell_no': self.player.participant.vars['reveal_cell_no'],
                'reveal_cell_round': self.player.participant.vars['reveal_cell_round'],
                'reveal_avg_no': self.player.participant.vars['reveal_avg_no'],
                'reveal_avg_round': self.player.participant.vars['reveal_avg_round'],
                'reveal_both_no': self.player.participant.vars['reveal_both_no'],
                'reveal_both_round': self.player.participant.vars['reveal_both_round']}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

    def before_next_page(self):
        if len(self.player.participant.vars['problem_type'])> 0 :
            if self.player.participant.vars['problem_type'][len(self.player.participant.vars['problem_type'])-1] == 1 & self.player.participant.vars['problem_type'][len(self.player.participant.vars['problem_type'])-2] == 0:
                self.player.ca_switch = self.player.ca_switch + 1
            else if self.player.participant.vars['problem_type'][len(self.player.participant.vars['problem_type'])-1] == 0 & self.player.participant.vars['problem_type'][len(self.player.participant.vars['problem_type'])-2] == 1:
                self.player.ac_switch = self.player.ac_switch + 1



class CellOnlyRevealPage(Page):
    form_model ='player'
    form_fields = ['solution']

    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry'] - time.time()>3) and (self.player.reveal_cell == 1)

    def vars_for_template(self):
        self.player.participant.vars['reveal_cell_no'] = self.player.participant.vars['reveal_cell_no'] + self.player.reveal_cell
        self.player.reveal_cell = 0
        return{'reveal_cell_no': self.player.participant.vars['reveal_cell_no'],
                'problem_no': self.player.participant.vars['problem_no'],
                'rand_cutoff': self.player.participant.vars['random_cutoff'],
                'check_payoff': self.player.participant.vars['check_payoff'][self.player.problem],
                'payoff_cell': self.player.participant.vars['payoff_matrix'][self.player.problem//Constants.num_rows][self.player.problem % Constants.num_rows]}

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

class AvgOnlyRevealPage(Page):
    form_model ='player'
    form_fields = ['solution']

    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry'] - time.time()>3) and (self.player.reveal_avg == 1)

    def vars_for_template(self):
        self.player.participant.vars['reveal_avg_no'] = self.player.participant.vars['reveal_avg_no'] + self.player.reveal_avg
        self.player.reveal_avg = 0
        if self.player.row_problem != None:
            one_row_index = self.player.row_problem
        else:
            one_row_index = -1
        if self.player.col_problem != None:
            one_col_index = self.player.col_problem
        else:
            one_col_index = -1
        return{'reveal_avg_no': self.player.participant.vars['reveal_avg_no'],
                'problem_no': self.player.participant.vars['problem_no'],
                'one_row': self.player.participant.vars['ones_row'][one_row_index],
                'one_col': self.player.participant.vars['ones_column'][one_col_index]
                }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()

class BothRevealPage(Page):
    form_model ='player'
    form_fields = ['solution']

    def is_displayed(self):
        return self.player.cont_learning and (self.participant.vars['expiry'] - time.time()>3) and (self.player.reveal_both == 1)

    def vars_for_template(self):
        self.player.participant.vars['reveal_both_no'] = self.player.participant.vars['reveal_both_no'] + self.player.reveal_both
        self.player.reveal_both = 0
        if self.player.problem != None:
            prob_index = self.player.problem
        else :
            prob_index = 0
        if self.player.row_problem != None:
            one_row_index = self.player.row_problem
        else:
            one_row_index = -1
        if self.player.col_problem != None:
            one_col_index = self.player.col_problem
        else:
            one_col_index = -1
        return{'reveal_both_no': self.player.participant.vars['reveal_both_no'],
                'problem_no': self.player.participant.vars['problem_no'],
                'rand_cutoff': self.player.participant.vars['random_cutoff'],
                'payoff_cell': self.player.participant.vars['payoff_matrix'][prob_index//Constants.num_rows][prob_index % Constants.num_rows],
                'one_row': self.player.participant.vars['ones_row'][one_row_index],
                'one_col': self.player.participant.vars['ones_column'][one_col_index]
                }


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

    def row_choice_choices(self):
        choices = [[0, 'Average Row'],
                [1,'Square'],
                [2,'Triangle'],
                [3, 'Circle'],
                [4, 'Diamond'],
                [5, 'Pentagon'],
                [6, 'Spade'],
                [7, 'Heart'],
                [8, 'Rectangle'],
                [9, 'Ellipse'] ]
        random.shuffle(choices)
        return choices

    def column_choice_choices(self):
        choices=[[0, 'Average Column'],
                [1, 'Red'],
                [2, 'Blue'],
                [3, 'Orange'],
                [4, 'Purple'],
                [5, 'Pink'],
                [6, 'Green'],
                [7, 'Gray'],
                [8, 'Brown'],
                [9, 'Violet'] ]
        random.shuffle(choices)
        return choices

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
        if self.player.row_choice == 0 & self.player.column_choice == 0 :
            self.player.payoff = 0
        else:
            rand_choice = random.randint(1, len(self.player.participant.vars['pay_list_round']))
            self.player.payoff = self.player.participant.vars['pay_list_round'][rand_choice-1]



num_of_tries= PayoffMatrix.N + 2*PayoffMatrix.n
learning_page_sequence = [SelectProblemPage, ChooseToSolvePage,  CellOnlyRevealPage, AvgOnlyRevealPage, BothRevealPage, ContinueLearningPage]*num_of_tries
choice_page_sequence = [FinalChoiceOnePage, FinalChoiceTwoPage]*Constants.num_choices
page_sequence = [TimerPage, InstructionTwoPage, PriorPage, TreatmentTypePage] + learning_page_sequence + choice_page_sequence
