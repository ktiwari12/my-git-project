#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 19:38:29 2022

@author: kanchantiwari
"""

class Employee:
    def __init__(self,name,id_number,department,job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title
    
    def set_name(self,name):
        self.name = name
    
    def set_id(self,id_number):
        self.id_number = id_number

    def set_department(self,department):
        self.department = department
    
    def set_jobtitle(self,job_title):
        self.job_title = job_title

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id_number
    
    def get_department(self):
        return self.department
    
    def get_jobtitle(self):
        return self.job_title
    
    def __str__(self):
        return "Name = "+self.name+"\nId Number = "+str(self.id_number)+"\nDepartment = "+self.department+"\nJob Title = "+self.job_title+"\n"


