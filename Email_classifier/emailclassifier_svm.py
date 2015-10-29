# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:55:13 2015

@author: Ekta
@email-id: ektagoel04@gmail.com

"""
import os
import operator
import numpy as np
from sklearn import svm

frequent_words = {}
k = 10 # 10 most frequent occurring words
num_of_training_examples = 23
numstring = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numwords = ["zero", "one" , "two" , "three", "four", "five" , "six", "seven", "eight", "nine"]

def processemail(filename):

    data = ""    
    
    with open(filename, 'r+') as file :

        for line in file :
            line = line.lower();
            if "subject" not in line and "cc :" not in line and "sent by" not in line and "forwarded by" not in line and "to" not in line and "from" not in line : 
                data = data + line
        
    fp = open(filename , 'w' )
    fp.write(data)
    
    fp.close()
    
    fp = open(filename , 'r')
    lines = fp.readlines()

    words = []    
    
    for line in lines :
        words = words + line.split(" ")
        
    final = []
    
    for i in range(0,len(words)):
        
        if "http" in words[i] :
            words[i] = words[i].replace("http", "httpaddr")
        elif "$" in words[i] :
            words[i] = words[i].replace("$", "dollar")
        elif "@" in words[i] :
            words[i] = words[i].replace("@", "emailaddr")
        
        for j in range(0,len(numstring)):
            if numstring[j] in words[i] :
                words[i] = words[i].replace(numstring[j], numwords[j])
        
        
        if ( len(words[i]) >=3 ):
            final.append(words[i])
                        
    #print(final)
    
    return final

if __name__ == '__main__':


    list_of_words = []    
    
    folderham = r'C:/Users/Eku/Documents/Python Scripts/corpus/ham'

    for mails in os.listdir(folderham) :
        #print(mails)

        mailpath = folderham + "/" + mails        
        #print(mailpath)
        temp = processemail(mailpath)
    
        list_of_words = list_of_words + temp
    
    #print(list_of_words)
    
    folderspam = r'C:/Users/Eku/Documents/Python Scripts/corpus/spam'
    
    for mails in os.listdir(folderspam) :
        #print(mails)

        mailpath = folderspam + "/" + mails        
        #print(mailpath)
        temp = processemail(mailpath)
    
        list_of_words = list_of_words + temp
    
    for i in range(0,len(list_of_words)) :
            
        if list_of_words[i] in frequent_words:
            frequent_words[list_of_words[i]] += 1
        else:
            frequent_words[list_of_words[i]] = 1
    
    #print("The vocab is ")
    #print(frequent_words.items())
    
    #print("Sorted by key")
    frequent_words = sorted(frequent_words.items(), key=operator.itemgetter(1), reverse = True)
    
    X = np.zeros((num_of_training_examples,k))
    y = np.zeros((num_of_training_examples))

    cnt = 0
    num_mail = 0

    for mails in os.listdir(folderham) :
        
        cnt=0
        
        mailpath = folderham + "/" + mails        
        #print(mailpath)
        temp = processemail(mailpath)
        
        for key,value in frequent_words:
    
            if ( cnt >= k ) :
                break
            
            #print(key,value)
            
            if key in temp :
                X[num_mail][cnt] = 1
            cnt += 1
            
        y[num_mail] = 1 # 1 for ham
        num_mail += 1      
    
    for mails in os.listdir(folderspam) :
        
        cnt=0
        
        mailpath = folderspam + "/" + mails        
        #print(mailpath)
        temp = processemail(mailpath)
        
        for key,value in frequent_words:
    
            if ( cnt >= k ) :
                break
            
            #print(key,value)
            
            if key in temp :
                X[num_mail][cnt] = 1
            cnt += 1
            
        y[num_mail] = 0 # 1 for spam
        num_mail += 1   
        
    #print(X)
    
        
    clf = svm.SVC(gamma = 0.00, C = 100)
    clf.fit(X,y)
    
    for i in range(0,num_mail):
        res = clf.predict(X[i][:])
        print("prediction for i = : " + str(i) + "th mail is " + str(res))