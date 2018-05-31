import random
import math

class PayoffQuiz():
    """ Create a set of questions for selective learning experiment"""

    lower_limit = .24
    upper_limit = .25
    error = .00000001
    no_of_cell_q = 6
    no_of_avg_q = 4

    def __init__(self):
        self.random_cutoff = random_cutoff
        self.random_Cutoff = random_Cutoff
        self.random_payoff = random_payoff
        self.check_payoff = check_payoff
        self.correct_payoff = correct_payoff
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num3_abs = num3_abs
        self.sign = sign
        self.q_type = q_type
        self.cell_quiz_q = cell_quiz_q
        self.cell_questions = cell_questions
        self.avg_questions = avg_questions
        self.true_num = true_num
        self.true_num_list = true_num_list
        self.avg_quiz_q = avg_quiz_q
        self.avg_num_rand = avg_num_rand



    def CellQuestion(self):
        correct_payoff = []
        check_payoff = 0
        cell_questions = []
        random_Cutoff = []
        cell_quiz_q = ''
        for i in range(PayoffQuiz.no_of_cell_q):
            random_cutoff = round(random.uniform(PayoffQuiz.lower_limit, PayoffQuiz.upper_limit),6)
            random_Cutoff.append(random_cutoff)
            random_payoff = round(random.uniform(PayoffQuiz.lower_limit, PayoffQuiz.upper_limit),6)
            if random_payoff > random_cutoff - PayoffQuiz.error:
                check_payoff = 1
            correct_payoff.append(check_payoff)
            num1 = round(random.uniform(1,2)*random_payoff,8)
            num2 = round(random.uniform(PayoffQuiz.lower_limit, PayoffQuiz.upper_limit),8)
            num3 = round(random_payoff - num1 + num2,8)
            num3_abs = abs(num3)
            if num3>0:
                sign = '+'
            else:
                sign = '-'
            q_type = random.randint(1,2)
            if q_type == 1:
                cell_quiz_q = str(num1) + "-" + str(num2) + sign + str(num3_abs)
                cell_questions.append(cell_quiz_q)
            else:
                cell_quiz_q = str(num1) + sign + str(num3_abs) + "-" + str(num2)
                cell_questions.append(cell_quiz_q)
        return {"cutoff": random_Cutoff,
                "correct_payoff": correct_payoff,
                "cell_questions": cell_questions}

    def AverageQuestion(self):
        true_num_list = []
        avg_questions = []
        for i in range(PayoffQuiz.no_of_avg_q):
            avg_quiz_q = '.'
            true_num = random.randint (1,9)
            true_num_list.append(true_num)
            for j in range(6):
                avg_num_rand = random.randint(0,9)
                avg_quiz_q += str(avg_num_rand)
                j=j+1
            avg_quiz_q += (str(true_num))
            for j in range(4):
                avg_num_rand = random.randint(0,9)
                avg_quiz_q += str(avg_num_rand)
                j=j+1
            avg_questions.append(avg_quiz_q)
        return {"true_num_list": true_num_list,
                "avg_questions": avg_questions}
