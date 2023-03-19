#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 10:06:50 2022

@author: kanchantiwari
"""

import os

def add():
    f = open("contacts.txt","a")
    print("Enter the following contact details:")
    name = input("Name: ")
    email = input("Email id: ")
    phone = input("Phone number: ")
    f.write(name+","+email+","+phone)
    f.write("\n")
    f.close()

def show():
    f = open("contacts.txt","r")
    count = 0
    for line in f:
        count+=1
        contact = line.split(",")
        print("Contact #",count)
        print("\n")
        print("Name = ",contact[0])
        print("Email = ",contact[1])
        print("Phone = ",contact[2])
        print("---------------------------------------")
    f.close()

def search(name):
    f = open("contacts.txt","r")
    for line in f:
        if name in line:
            f.close()
            return line
    return "NF"

def update(name):
    s = search(name)
    if s == "NF":
        print("\n")
        print("Name not Found")
    else:
        og = open("contacts.txt","r")
        tmp = open("tmp.txt","w")
        for line in og:
            if name in line:
                print("\n")
                email = input("Enter updated email id: ")
                phone = input("Enter updated phone number: ")
                name = line.split(",")[0]
                tmp.write(name+","+email+","+phone)
                tmp.write("\n")
            else:
                tmp.write(line)
        og.close()
        tmp.close()
        os.remove("contacts.txt")
        os.rename("tmp.txt","contacts.txt")
        print("Contact updated")

def delete(name):
    s = search(name)
    if s == "NF":
        print("\n")
        print("Name not Found")
    else:
        og = open("contacts.txt","r")
        tmp = open("tmp.txt","w")
        for line in og:
            if name in line:
                continue
            else:
                tmp.write(line)
        og.close()
        tmp.close()
        os.remove("contacts.txt")
        os.rename("tmp.txt","contacts.txt")
        print("Contact deleted")



choice = 0
while(choice != 6):
    print("CHOICE MENU:")
    print("1. Add a contact")
    print("2. Show the list of contancts")
    print("3. Search for a name in the list")
    print("4. Modify a contact")
    print("5. Delete a contact from the list")
    print("6. Quit")
    choice = int(input("Enter the choice = "))
    if(choice == 1):
        add()
    elif(choice == 2):
        show()
    elif(choice == 3):
        name = input("Enter a name to search: ")
        found = search(name)
        if found != "NF":
            contact = found.split(",")
            print("\n")
            print("Name = ",contact[0])
            print("Email = ",contact[1])
            print("Phone = ",contact[2])
            print("---------------------------------------")
        else:
            print("name not found")
    elif(choice == 4):
        name = input("Enter name to search for update: ")
        update(name)
    elif(choice == 5):
        name = input("Enter name to delete: ")
        delete(name)
    else:
        print("Plase enter a choice between 1 to 6")