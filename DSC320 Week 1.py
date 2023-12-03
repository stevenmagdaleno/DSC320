'''DSC320 Week 1
Steven Magdaleno'''

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math as math

################################### 1. RMSE #####################################
#loading the data as a data frame
#importing as a pandas data frame to make the data easy to work with, 
#the try block is to help the user out, if they just enter the file path
#it'll grab the housing_data.csv file from the path provided, or if they
#enter the filepath and the file name, it'll take that too.

try:
    df = pd.read_csv('housing_data.csv')
except:
    file_path = input('Enter your file path for housing_data.csv:')  
    try:
        df = pd.read_csv(f'{file_path}')
    except:
        df = pd.read_csv(f'{file_path}\housing_data.csv')

#creating an array for the sale price
sale_price = df['sale_price'].to_numpy()
print(f'sale price array {sale_price}')

#creating an array for the predicted sale price
sale_price_pred = df['sale_price_pred'].to_numpy()
print(f'sale price pred array {sale_price_pred}')

#setting the n variable
n = len(sale_price)
print(f'n = {n}')

#the function takes the three inputs, n, array 2, and array 1
def _RMSE(n, array2, array1):
    f = 0 #an arbitrary variable to start my sum at 0
    for yhat, y in zip(array2, array1): #zipping the two arrays to iterate through both of them
        x = abs(yhat-y) #the (yhatn-yn) math
        x = x**2 #squared
        f = f+x #adding each x
    a = 1/n*f #a = the first part of the rmse equation, this could also just go straight into the sqrt func, but I wanted to show the steps
    answer = math.sqrt(a) #the sqrt of a
    return(answer) #returning the answer

############################ 2. MAE ######################################
#this function is almost exactly the same, it just doesn't square/sqrt
def _MAE(n, sale_price_pred, sale_price):
    f = 0
    for yhat, y in zip(sale_price_pred, sale_price):
        x = abs(yhat-y)
        f = f+x
    answer = 1/n*f
    return(answer)

#below are the actual values, then the rounded values (since its a dollar amount)
RMSE_actual = _RMSE(n, sale_price_pred, sale_price) 
RMSE_rounded = round(RMSE_actual,2)

MAE_actual = _MAE(n, sale_price_pred, sale_price) 
MAE_rounded = round(MAE_actual,2)

#and finally the output is printed for the user
print(f'The RMSE is {RMSE_rounded}')
print(f'The MAE is {MAE_rounded}')

######################################## 3. Binary Target ###################################################

try:
    df = pd.read_csv('mushroom_data.csv')
except:
    file_path = input('Enter your file path for the mushroom_data.csv file:')
    try:
        df = pd.read_csv(f'{file_path}')
    except:
        df = pd.read_csv(f'{file_path}\mushroom_data.csv')

#i put these in lists instead of putting them in arrays since they're not numbers
mush_actual = df['actual'].to_list()
mush_predicted = df['predicted'].to_list()
n = len(mush_actual)

#the function checks if the values are the same, then counts the correct predictions, and divides by the total predictions.
def _bool_accuracy(n, array2, array1):
    f=0
    for x,y in zip(array2, array1):
        if x == y: #are the values the same?
            f=f+1 #if they are, add one to the counter
        else:
            pass #if not, skip to the next value
    answer = f/n*100 #answer *100 to give a readable %
    return(answer) #return the answer

#the actual answer and the rounded answer
mush_accuracy_actual = _bool_accuracy(n, mush_predicted, mush_actual)
mush_accuracy_rounded = round(mush_accuracy_actual,4)

print(f'The predictions are {mush_accuracy_rounded}% accurate.')

########################################### 4. plotting #################################################
num_range = []
num_start = 16.75
for i in range(5000):
    num_range.append(num_start)
    num_start = num_start+0.0001
x = np.array(num_range)
y = 0.005*x**6-0.27*x**5+5.998*x**4-69.919**3+449.17*x**2-1499.7*x+2028

plt.plot(x,y)
plt.grid(True)
plt.show()

#the estimated value of p that minimizes the error using the graph is about 16.95
#the estimated minimum error is 0

#below is a qc I did to check if my answers were at least pretty close the answers 
#I got were 16.954 and -2.31, if i increased the step to 100,000 at 0.000001 increment 
#i could approach 0 further, but thats completely unnecessary in this instance.

x=16.5
numbers=[]
xlist=[]
for i in range(10000):
    xlist.append(x)
    y = 0.005*x**6-0.27*x**5+5.998*x**4-69.919**3+449.17*x**2-1499.7*x+2028
    x=float(x)+0.0001
    numbers.append(y)

n = min(numbers, key=abs)
print(f'error is {n}')
index = numbers.index(n)
print(f'at p value {xlist[index]}')