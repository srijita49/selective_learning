from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.round_number == 1:
            yield (pages.TimerPage)
        yield (pages.InstructionTwoPage)
        yield (pages.PriorPage)
        if self.player.participant.vars['treatment_type'] != 0:
            yield (pages.TreatmentTypePage)
        yield (pages.SelectProblemPage, {'problem': 15})
        if self.player.participant.vars['treatment_type'] == 0:
            yield (pages.ChooseToSolvePage, {'solution': 1})
        elif self.player.participant.vars['treatment_type'] == 1:
            yield (pages.ChooseToSolvePage, {'reveal_cell':1})
        elif self.player.participant.vars['treatment_type'] == 2:
            yield (pages.ChooseToSolvePage, {'reveal_avg': 1})
        else:
            yield (pages.ChooseToSolvePage, {'reveal_both':1})
        if self.player.reveal_cell == 1 :
            yield (pages.CellOnlyRevealPage, {'solution': 1})
        if self.player.reveal_avg == 1 :
            yield (pages.AvgOnlyRevealPage, {'solution': 1})
        if self.player.reveal_both == 1 :
            yield (pages.BothRevealPage, {'solution': 1})
        yield (pages.ContinueLearningPage, {'cont_learning': False })
        yield (pages.FinalChoiceOne1Page, {'row_choice_1': 1, 'col_choice_1': 1})
        yield (pages.FinalChoiceTwo1Page)
        yield (pages.FinalChoiceOne2Page, {'row_choice_2': 2, 'col_choice_2': 1})
        yield (pages.FinalChoiceTwo2Page)
        yield (pages.FinalChoiceOne3Page, {'row_choice_3': 1, 'col_choice_3': 6})
        yield (pages.FinalChoiceTwo3Page)
        yield (pages.FinalChoiceOne4Page, {'row_choice_4': 5, 'col_choice_4': 2})
        yield (pages.FinalChoiceTwo4Page)
        yield (pages.FinalChoiceOne5Page, {'row_choice_5': 8, 'col_choice_5': 1})
        yield (pages.FinalChoiceTwo5Page)
        yield (pages.FinalChoiceOne6Page, {'row_choice_6': 1, 'col_choice_6': 6})
        yield (pages.FinalChoiceTwo6Page)
        yield (pages.FinalChoiceOne7Page, {'row_choice_7': 5, 'col_choice_7': 1})
        yield (pages.FinalChoiceTwo7Page)
        yield (pages.FinalChoiceOne8Page, {'row_choice_8': 3, 'col_choice_8': 1})
        yield (pages.FinalChoiceTwo8Page)
        yield (pages.FinalChoiceOne9Page, {'row_choice_9': 1, 'col_choice_9': 4})
        yield (pages.FinalChoiceTwo9Page)
        yield (pages.PayoffInfoPage)
