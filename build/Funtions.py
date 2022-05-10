import os
import json
import hashlib
import re
from tkinter import *
from pathlib import Path
from cs50 import *



db = SQL("sqlite:///Users.db")

path_to_file = "Data.json"

with open(path_to_file) as file:
    data = json.load(file)

ID = int(data[0]['ID'])


def registerUser(name,password):
    if len(db.execute("SELECT name FROM users WHERE name = ?;",name)) == 1 and len(name) > 1:
            return -2
    else:
        if  isPasswordStrong(password) == 1:
            # All good
            ID =+ 1
            salt = os.urandom(32) # A new salt for this user
            key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
            # Store the salt and key
            db.execute("INSERT INTO Users (id,name,key,salt) VALUES (?,?,?,?);",ID,name,key,salt)
            data = [
                    {
                            "ID" : ID
                    }
                ]

            path_to_file = "Data.json"

            with open(path_to_file,"w") as file:
                json.dump(data, file)
            return 1
                    
        else:    
            return -1
        
        
            




def checkLogin(name,password):
    if len(db.execute("SELECT name FROM users WHERE name = ?;",name)) == 1 :
        key = db.execute("SELECT key FROM users WHERE name = ?;",name)
        key = key[0]['key']
        salt = db.execute("SELECT salt FROM users WHERE name = ?;",name)
        salt = salt[0]['salt']
        new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        if key == new_key:
            return 1
        else:
            return 0
    else:
        return -1



def isPasswordStrong(v):
    if(len(v)>=8):
        if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
            return 1
        elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
            return 1
        else:
            return 0



# Sakuna = v+B:\7)aGyhd6c]*
# Admin = ea}S>`'"4^-ETy~C



