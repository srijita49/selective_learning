import random
import math

# Create a class PayoffMatrix with the following class variable

class PayoffMatrix:
    """Create a n-by-n payoff matrix."""

    N=4
    n=int(math.sqrt(N))
    low_cutoff=.24
    high_cutoff=.25

    def __init__(self,zeros, low_values=[], high_values=[], payoff_list=[], problem_list=[]):
        #super(, self).__init__()
        self.model_number = random.randint(1,2)
        self.zeros=zeros
        self.rand_cutoff=random.uniform(.24,.25)
        self.low_scale= self.rand_cutoff-low_cutoff
        self.high_scale=high_cutoff-self.rand_cutoff
        self.low_values=low_values
        self.high_values=high_values
        self.payoff_list=payoff_list
        self.problem_list=problem_list
        self.problem_choice=random.randint(1,2)
        self.num1=[]
        self.num2=[]
        self.num3=[]
        self.num3_raw=[]
        self.problem=problem

    def No_of_zeros (self):
        if PayoffMatrix.model_number==1:
            zeros=1
        else:
            zeros=3
        return zeros

    def HighValues(self):
        for zero in range(PayoffMatrix.N-PayoffMatrix.zeros):
            high_values=random.uniform(PayoffMatrix.rand_cutoff, PayoffMatrix.high_cutoff)

    def LowValues(self):
        for zero in range(PayoffMatrix.zeros):
            low_values=random.uniform(PayoffMatrix.low_cutoff, PayoffMatrix.rand_cutoff)

    def PayoffList(self):
        payoff_list.append(high_values)
        payoff_list.append(low_values)
        random.shuffle(payoff_list)
        return payoff_list

    def ProblemList(self):
        if PayoffMatrix.problem_choice== 1:
            for cell in payoff_list:
                PayoffMatrix.num1= random.uniform(1,2)*PayoffMatrix.payoff_list[cell]
                PayoffMatrix.num2= random.uniform(PayoffMatrix.low_cutoff, PayoffMatrix.high_cutoff)
                PayoffMatrix.num3_raw= PayoffMatrix.payoff_list[cell]-num1 +num2
                PayoffMatrix.num3=abs(num3_raw)
                if num3_raw<0:
                    sign='-'
                else:
                    sign='+'
                PayoffMatrix.problem=str(num1)+'-'+str(num2)+sign+str(num3)
                PayoffMatrix.problem_list.append(problem)
        else:
            for cell in payoff_list:
                num1= random.uniform(0,1)*PayoffMatrix.payoff_list[cell]
                num2= random.uniform(PayoffMatrix.low_cutoff, PayoffMatrix.high_cutoff)
                num3_raw= PayoffMatrix.payoff_list[cell]-num1 -num2
                num3=abs(num3_raw)
                if num3_raw<0:
                    sign='-'
                else:
                    sign='+'
                PayoffMatrix.problem=str(num1)+'+'+str(num2)+sign+str(num3)
                PayoffMatrix.problem_list.append(problem)
        return problem_list




# N: total number of cells
# n: total number of rows
# And instance variables
# model number,
# number of zeros (function of model number)
# low cutoff (empty list),
# high cutoff
# random cutoff value (random number),
# low scale (function of cutoff value and low value),
# high scale (function of cutoff value and low value),
# low values (empty list)
# high values (empty list),
# list of random number using cutoffs (for problem matrix),
#
# Define a function to generate high values depending on the model number
# This function would take number of zeros as input
#
# Define a function to generate low values depending on the model number
# This function would also take number of zeros as input
#
# Define a function to create the final payoff matrix:
# Two inputs: high values and low values
# This would do two things, one join the two lists and shuffle it using random.shuffle
#
#
# Define a function to rearrage the array in the n-by n format
#
# Define a function to generate the problem matrix with the following input:
# payoff list generated from class PayoffMatrix
# number 1 is multiplied by another random number based on a random draw using iterator
# number 3 is residually computed using iterator
# finally a string with proper signs
