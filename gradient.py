# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 20:13:30 2015

@author: Ekta
"""
import matplotlib.pyplot as plt
import pylab
import csv

def gradient_descent(alpha, data, epsilon, max_iter):
    
    #variable for checking of the values have converged or not
    isconverge = 0
    
    #variable for counting the number of iterations
    iter_num = 0
    
    #number of samples
    m = len(data)
    
    t0 = 0
    t1 = 0
    
    #cost function
    J = 0;
    
    for i in range(0,m):
        J = J + pow((t0 + t1*data[i][0] - data[i][1]),2)
    
    #Multiplying with 1/2m will give us the cost, we can instead minimise the mean squared error
    J = J*(1/(2*m))
    print('Initial cost is ' + str(J))
    
    #Apply the gradient descent algorithm
    
    while( isconverge == 0):
        
        #Calculate the gradients
        g0 = 0;
        g1 = 0;
        
        #find partial derivative w.r.t theta0, get the sum over all training samples
        for i in range(0,m): 
            g0 = g0+ (t0+t1*data[i][0] - data[i][1])
            
        g0= g0*(1/m);
        
        #find partial derivative w.r.t theta1, get the sum over all training samples
        for i in range(0,m):
            g1 = g1 +(t0+t1*data[i][0] - data[i][1])*data[i][0]
            
        g1 = g1*(1/m);
        
        #new values for theta0 and theta1
        temp0 = t0 - alpha*g0
        temp1 = t1 - alpha*g1
        
        t0 = temp0
        t1 = temp1
        
        #calculate the error again
        error = 0
        for i in range(0,m):
            error = error + pow((t0 + t1*data[i][0] - data[i][1]),2)
        
        #Multiplying with 1/2m will give us the cost
        #error = error*(1/(2*m))
        
        er = error * (1/(2*m));
        
        #for debugging, check that th cost at every step decreases. As we move towards the minimum in every iteration, it can't increase.
        
        #print('Cost for this iteration ' + str(iter_num) + ' is ' + str(er))
       
            
        if abs(J-error) <= epsilon :
            print("Converged")
            isconverge = 1
            
        J = error
        iter_num += 1
        
        if(iter_num == max_iter):
           # print("Maximum iterations reached")
            isconverge = 1
            
    return t0,t1

#Let training samples be in file data.txt where each training sample is of the form (x,y)
with open('ex1data1.txt', 'r') as csvfile:
    lines = csv.reader(csvfile)
    d= list(lines)
        
    data = []
    
    for i in range(0,len(d)):
        data.append(d[i])
            
    #learning rate
    alpha= 0.01
    
    #convergence criteria
    epsilon = 0.0001
    
    #maximum no. of iterations
    max_iter = 1500
    
    for i in range(0,len(data)):
        data[i][0] = float(data[i][0])
        data[i][1] = float(data[i][1])
        x = data[i][0]
        y = data[i][1]
        plt.scatter(x,y)
   
    #plt.show()
    
    theta0,theta1 = gradient_descent(alpha,data,epsilon,max_iter)
    
    print("The optimal values of theta0 = : " + str(theta0))
    print("The optimal values of theta1 = : " + str(theta1))
    
    
    for i in range(0,len(data)-1):
        x = data[i][0];
        y = theta0 + theta1*x
        pylab.scatter(x,y, c= 'r')
        
    print("In the below graph, red marks show the predicted values as per the gradient descent algorithm and blue marks show the initial profit")
    