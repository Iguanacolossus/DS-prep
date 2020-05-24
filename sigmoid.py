'''
THE SIGMOID FUNCTION:
the sigmoid function has a center point at zero. As x gets bigger it converges on one, 
and as x gets smaller (more negative) the function converges on zero. This function maps 
phenomina that start slow, raplidly increase, then top out over time. example where sigmoid 
functions are used is, atrficial neralnetworks, audio signal processing, and crop yeild modeling.

-------------------------------
   
    This script, defines sigmoid in a function and makes a distribution of it in a dictionary


'''
import math 
def sigmoid(x):
    ''' 
    returns value of sigmoid function at x
    ---------------------------------
    input: <int or float>
        x value
    output: float
    '''
    return 1 / (1 + (math.exp(-x)))

def sigmoid_dict(r):
    '''
    returns a dictionary with keys of a range of inputs of sigmoid (x values)
    and values as values of the sigmoid function at x
    --------------------------------
    input: < int > 
        r = a integer that determins the range of the x inputs -r to r 
    '''
    d = {}
    for i in range(-r, r):
        d[i] = sigmoid(i)
    return d


for k, v in sigmoid_dict(10).items():
    print(f'{k} : {v}')
    #print(f'{k}:  {"*" * int(10 * v)}')


#########  just for fun #####################################################
import matplotlib.pyplot as plt

def plot_from_dict( dict):
    x = []
    y = []
    for k,v in dict.items():
        x.append(k)
        y.append(v)

    plt.plot(x,y)
    plt.suptitle('Sigmoid Function')
    plt.xlabel('x')
    plt.vlines(0,colors='y',ymin = 0, ymax=1,linestyle='dashed')
    plt.text(-6,.9,s= "center at zero -->",color='y')

    m_at_center = (sigmoid(1)-sigmoid(-1))/ 2
    print(m_at_center)
    
    x_slope = list(range(-2,3))
    y_slope = []
    for i in x_slope:
        y_slope.append((m_at_center * i) + .5)
    
    plt.plot(x_slope,y_slope,linestyle=':',color='m')
    plt.text(.2,.5,s=f'slope at center {round(m_at_center,4)}',color='m')

    plt.show()

#plot_from_dict(sigmoid_dict(10))





