#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 19:38:38 2022

@author: kanchantiwari
"""

import emp
import pickle

def addEmp(dict):
    name = input("Name: ")
    id_number = int(input("Id Number: "))
    department = input("Department: ")
    job_title = input("Job Title: ")

    employee = emp.Employee(name,id_number,department,job_title)
    dict[id_number] = employee
    print("Employee added to dictionary\n")

def lookup(dict):
    flag = False
    name = input("Enter the name to search: ")
    for items in dict:
        if name == dict[items].get_name():
            print(dict[items])
            flag = True
    if flag == False:
        print("Not found in dictionary")
        print()

def editEmp(dict):
    flag = False
    name = input("Enter employee name to edit: ")
    for items in dict:
        if name == dict[items].get_name():
            new_name = input("Enter new name: ")
            dept = input("Enter new department: ")
            job = input("Enter new job title: ")
            dict[items].set_name(new_name)
            dict[items].set_department(dept)
            dict[items].set_jobtitle(job)
            print("Employee details updated.\n")
            flag = True
    if flag == False:
        print("Employee not found.\n")

def delEmp(dict):
    name = input("Enter employee name to delete: ")
    flag = False
    id = 0
    for items in dict:
        if name == dict[items].get_name():
            id = items
            flag = True
    if flag == True:
        del dict[id]
        print("Employee deleted.\n")
    else:
        print("Employee not found.\n")


dict = {}
try:
    input_file = open('employee_dictionary.dat','rb')
    dict = pickle.load(input_file)
    input_file.close()
    print("Dictionary loaded from file.")
except:
    print("File not found. Using empty dictionary")
finally:
    choice = 0
    while(choice != 5):
        print("1. Look up an employee\n2. Add a new employee\n3. Edit employee details\n4. Delete an employee\n5. Quit\n")
        choice = int(input("Enter an option number between 1 to 5: "))
        print()
        if choice == 1:
            lookup(dict)
        elif choice == 2:
            addEmp(dict)
        elif choice == 3:
            editEmp(dict)
        elif choice == 4:
            delEmp(dict)
        elif choice == 5:
            output_file = open('employee_dictionary.dat','wb')
            pickle.dump(dict,output_file)
            output_file.close()
