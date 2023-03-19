#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:31:23 2022

@author: kanchantiwari
"""

def determine_grade(test_score):
    if(test_score>=90 and test_score<=100):
        return 'A'
    elif(test_score>=80 and test_score<=89):
        return 'B'
    elif(test_score>=70 and test_score<=79):
        return 'C'
    elif(test_score>=60 and test_score<=69):
        return 'D'
    elif(test_score<60):
        return 'F'

def calc_averaqge(t1,t2,t3,t4,t5):
    average = (t1+t2+t3+t4+t5)/5
    return average

if __name__ == '__main__':
    ts1 = int(input("Enter test score 1: "))
    result = determine_grade(ts1)
    print("Grade for test score 1 is = ",result)
    ts2 = int(input("Enter test score 2: "))
    result = determine_grade(ts2)
    print("Grade for test score 2 is = ",result)
    ts3 = int(input("Enter test score 3: "))
    result = determine_grade(ts3)
    print("Grade for test score 3 is = ",result)
    ts4 = int(input("Enter test score 4: "))
    result = determine_grade(ts4)
    print("Grade for test score 4 is = ",result)
    ts5 = int(input("Enter test score 5: "))
    result = determine_grade(ts5)
    print("Grade for test score 5 is = ",result)
    avg = calc_averaqge(ts1,ts2,ts3,ts4,ts5)
    print("Average of scores = ",avg)