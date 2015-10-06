# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:11:53 2015

@author: Ekta
@email: ektagoel04@gmail.com
"""

#Implementing logistc regression
#The algorithm is based on supervised learning where we have with us the training data with the correct class to which a particular training example will belong.

import numpy as np
import scipy.optimize as op
import csv,math

num_labels = 0

#Function for computing the hypothesis

def sigmoid(var):

    h = []    
    
    for i in range(0,len(var)):
        v = var[i]
        hypothesis = 1.0 + math.exp(-v)
        hypothesis = 1/hypothesis
        h.append(hypothesis)
    
    h = np.array(h)
    
    return h
    
#Function for computing the cost

def get_cost(theta,X,y):
    
    m = X.shape[0]; # number of training examples

    pro = sigmoid(X.dot(theta))

    for i in range(0,len(pro)):
        v = pro[i]
        v = math.log(v)
        pro[i] = v
    
    J = (-np.transpose(y)).dot(pro)
    
    pro = sigmoid(X.dot(theta))

    for i in range(0,len(pro)):
        v = pro[i]
        v = math.log(1-v)
        pro[i] = v
    
    J = J - np.transpose(1-y).dot(pro)
    J = J/m;    

    return J
    
#compute gradients

def get_gradients(theta,X,y):
    
    grad = np.zeros((num_labels,1))  

    h = sigmoid(X.dot(theta))
    m = X.shape[0]
    
    delta = h-y

    grad = np.transpose(X).dot(delta)
        
    grad = grad/m
    
    return grad
    
# Predict the class of every training example
    
def predict(theta,X):

    m = X.shape[0]    
    
    p = np.zeros((m,1))     
    
    h = sigmoid(X.dot(theta))
    
    #Assuming threshold of 0.5
    for i in range(0,h.shape[0]):
        if h[i] >= 0.5:
            p[i][0] = 1
        else:
            p[i][0] = 0
            
    return p

with open('ex2data1.txt', 'r') as csvfile:
    lines = csv.reader(csvfile)
    
    d = list(lines)
        
    num_label = len(d[0])
    m = len(d)    
    
    features = num_label-1
    
    x = []
    ans = []
    
    for i in range(0,len(d)):
        t=[]
        
        t.append(float(1.0))
        
        for j in range(0,features):
           t.append(float(d[i][j]))
        
        ans.append(float(d[i][features]))
        
        x.append(t)
     
    X = np.array(x)
    #print(X)
    
    y  = np.array(ans)
    #print(y)

    theta = np.zeros((num_label,1))       
    
    print('The initial cost which has to be minimized is ' +  str(get_cost(theta,X,y)))
        
    get_gradients(theta,X,y)
    
    #Getting the optimum values of theta
    Result = op.minimize(fun = get_cost, x0 = theta, args = (X, y), method = 'TNC',
                                 jac = get_gradients);

    #Print the complete result to check all the parameters
    ar = Result.x
   
    for i in range(0,len(ar)):
        theta[i] = ar[i]
        
   # print(theta)
    
    res = predict(theta,X)

    cnt = 0    
    
    for i in range(0,m):
        p1 = res[i][0]
        p2 = y[i]
        #print('The first training example bby the algorithm belongs to class ' + (str(p1)))
        #print('By the given data it belongs to class ' + str(p2))
        
        if(p1==p2):
            cnt +=1
    
    print('Accuracy by training : ' + str((cnt/m)*100))
    print('The minimized cost is ' +  str(get_cost(theta,X,y)))