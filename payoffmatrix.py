import random
import math


# Create a class PayoffMatrix with the following class variable

class PayoffMatrix:
    """Create a n-by-n payoff matrix."""
# defining Class parameters
    N = 81
    n = int(math.sqrt(N))
    low_cutoff = .24
    high_cutoff = .25
    error = .00000001
# defining parameters for the Class object
    def __init__(self):
        #super(, self).__init__()
        self.model_number = model_number
        self.zeros = zeros
        self.rand_cutoff = rand_cutoff
        self.high_values= high_values
        self.low_values=low_values
        self.payoff_list = payoff_list
        self.problem_choice = problem_choice
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num3r = num3r
        self.problem = problem
        self.problem_list=problem_list
        self.payoff_matrix= payoff_matrix
        self.ones_row= ones_row
        self.ones_column= ones_column
        self.row_average= row_average
        self.column_average= column_average
        self.row_avg_comp=row_avg_comp
        self.col_avg_comp=col_avg_comp
        self.avg_num_rand_row = avg_num_rand_row
        self.avg_num_rand_col= avg_num_rand_col
        self.check_payoff = check_payoff


    def PayoffList(self):
#Choosing the prior
        prior_type = random.randint(1,3)
#Choosing the model
        if prior_type == 1:
            model_number= random.randint(1,3)
    # Defining no of zeros in the model
            if model_number == 1:
                zeros = 36
            elif model_number == 2:
                zeros = 54
            else:
                zeros = 72
        elif prior_type == 2:
            model_number= random.randint(1,4)
    # Defining no of zeros in the model
            if model_number == 1:
                zeros = 36
            elif model_number == 2:
                zeros = 72
            else:
                zeros = 54
        else :
            model_number= random.randint(1,2)
    # Defining no of zeros in the model
            if model_number == 1:
                zeros = 36
            else:
                zeros = 72
        for zero in range(zeros):

# Defining cutoff
            rand_cutoff= random.uniform(PayoffMatrix.low_cutoff,PayoffMatrix.high_cutoff)
    # Generating lists of payoff for the matrix
            payoff_list=[]
            for zero in range(PayoffMatrix.N-zeros):
                high_value=round(random.uniform(rand_cutoff, PayoffMatrix.high_cutoff), 6)
                payoff_list.append(high_value)
            for zero in range(zeros):
                low_value=round(random.uniform(PayoffMatrix.low_cutoff, rand_cutoff),6)
                payoff_list.append(low_value)
            random.shuffle(payoff_list)
    # Creating the list of problems
            problem_list = []
            problem = ''
            for cell in range(len(payoff_list)):
                problem_choice = random.randint(1,2)
                if problem_choice == 1 :
                    num1= round(random.uniform(1,2)*payoff_list[cell],8)
                    num2= round(random.uniform(PayoffMatrix.low_cutoff, PayoffMatrix.high_cutoff),8)
                    num3r= round(payoff_list[cell]-num1 +num2,8)
                    num3=abs(num3r)
                    if num3r<0:
                        sign='-'
                    else:
                        sign='+'
                    problem=str(num1)+'-'+str(num2)  + sign+str(num3)
                    problem_list.append(problem)
                else:
                    num1= round(random.uniform(0,1)*payoff_list[cell],8)
                    num2= round(random.uniform(PayoffMatrix.low_cutoff, PayoffMatrix.high_cutoff),8)
                    num3r= round(payoff_list[cell]- num1- num2,8)
                    num3=abs(num3r)
                    if num3r<0:
                        sign='-'
                    else:
                        sign='+'
                    problem=str(num1)+'+'+str(num2)+sign+str(num3)
                    problem_list.append(problem)
            final_problem= ''
            problem_list.append(final_problem)
    #Defining the matrix and calculating number of zeros in each row and column
            payoff_matrix = [payoff_list[i:i+PayoffMatrix.n] for i in range(0, len(payoff_list), PayoffMatrix.n)]
            ones_column = [0]*PayoffMatrix.n
            ones_row=[0]*PayoffMatrix.n
            for i in range(PayoffMatrix.n):
                for j in range(PayoffMatrix.n):
                    if payoff_matrix[i][j]>=rand_cutoff:
                        ones_column[i] += 1
            for i in range(PayoffMatrix.n):
                for j in range(PayoffMatrix.n):
                    if payoff_matrix[i][j]>=rand_cutoff:
                        ones_row[j] +=1
    # Creating the numbers in the average row/column, the second last digit represents the
    # number of ones in the row/column
            row_average= []
            for i in range(PayoffMatrix.n):
                row_avg_comp='.'
                for j in range(4):
                    avg_num_rand_row=random.randint(0,9)
                    row_avg_comp += str(avg_num_rand_row)
                    j=j+1
                row_avg_comp += (str(ones_row[i]))
                for j in range(6):
                    avg_num_rand_row=random.randint(0,9)
                    row_avg_comp += str(avg_num_rand_row)
                    j=j+1
                row_average.append(row_avg_comp)
            final_row_problem=''
            row_average.append(final_row_problem)
            column_average=[]
            for i in range(PayoffMatrix.n):
                col_avg_comp='.'
                for j in range(6):
                    avg_num_rand_col = random.randint(0,9)
                    col_avg_comp += str(avg_num_rand_col)
                    j=j+1
                col_avg_comp += (str(ones_column[i]))
                for j in range(4):
                    avg_num_rand_col = random.randint(0,9)
                    col_avg_comp += str(avg_num_rand_col)
                    j=j+1
                column_average.append(col_avg_comp)
            final_col_problem=''
            column_average.append(final_col_problem)
    # checking the values in a given rows
            check_payoff = [0]*PayoffMatrix.N
            for i in range(len(payoff_list)):
                if  payoff_list[i] > rand_cutoff-PayoffMatrix.error:
                    check_payoff[i] = 1
            return {'model_number': model_number,'zeros': zeros,
                 'random_cutoff': rand_cutoff, 'payoff_list': payoff_list,
                 'problem_list': problem_list,
                 'ones_row': ones_row, 'ones_column': ones_column,
                 'payoff_matrix': payoff_matrix,
                 'row_average': row_average,
                 'column_average': column_average,
                 'check_payoff': check_payoff,
                 'prior_type': prior_type }
