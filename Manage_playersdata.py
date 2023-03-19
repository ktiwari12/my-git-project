#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 10:51:13 2022

@author: kanchantiwari
"""
import sqlite3


def createDatabase():
    conn = sqlite3.connect('players_Data.db')
    cur = conn.cursor()

    sql = '''CREATE TABLE if not exists Player
    (
        name TEXT not null,
        wins INTEGER not null,
        losses INTEGER not null,
        ties INTEGER not null
    )
    '''
    cur.execute(sql)

    conn.commit()
    conn.close()

def addplayer():
    name = input("Name: ")
    wins = input("Wins: ")
    losses = input("Losses: ")
    ties = input("Ties: ")

    conn = sqlite3.connect('players_Data.db')
    cur = conn.cursor()

    sql = '''INSERT into Player values(?,?,?,?)'''

    cur.execute(sql,(name,wins,losses,ties))

    print(name+" was added to databse.\n")

    conn.commit()
    conn.close()
 
def viewplayers():
    conn = sqlite3.connect('players_Data.db')
    cur = conn.cursor()

    sql = '''SELECT name,wins,losses,ties, (wins+losses+ties) as Games from Player order by wins desc'''

    cur.execute(sql)
    result = cur.fetchall()

    print(f'{"Name":34} {"Wins":6} {"Losses":6} {"Ties":6} {"Games":6}')
    print("---------------------------------------------------------------")

    for row in result:
        print(f'{row[0]:30} {row[1]:6} {row[2]:6} {row[3]:6} {row[4]:6}')

    print()
    conn.commit()
    conn.close()   

def updateplayer():
    conn = sqlite3.connect('players_Data.db')
    cur = conn.cursor()
    name = input("Name: ")
    wins = input("Wins: ")
    losses = input("Losses: ")
    ties = input("Ties: ")

    sql = '''Update Player set wins = ?,losses = ?,ties = ? where name == ?'''
    cur.execute(sql,(wins,losses,ties,name))    

    print(name+"'s details have been updated.\n")
    conn.commit()
    conn.close()


def deleteplayer():
    name = input("Name: ")

    conn = sqlite3.connect('players_Data.db')
    cur = conn.cursor()

    sql = '''Delete from Player where name == ?'''

    cur.execute(sql,(name,))

    print(name+" was deleted from databse.\n")


    conn.commit()
    conn.close()



createDatabase()
print("Player Manager\n")
print("COMMAND MENU\nview - View players\nadd - Add player\nupdate - Update player details\ndel - Delete a player\nexit - Exit program\n")
cmd = ""
while(cmd.lower() != 'exit'):
    cmd = input("Command: ")
    if cmd.lower() == 'view':
        viewplayers()
    elif cmd.lower() == 'add':
        addplayer()
    elif cmd.lower() == 'update':
        updateplayer()
    elif cmd.lower() == 'del':
        deleteplayer()
    elif cmd.lower() == 'exit':
        print("Bye!")
        break
    else:
        print("Enter a valid command")    




