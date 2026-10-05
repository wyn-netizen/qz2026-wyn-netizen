import json
import os

class UserManager:
    def __init__ (self):
        self.users = []
        self.id = 0
    def add_user(self,name:str, age:int) -> dict:
        self.id +=1
        new_user = {"id":self.id,"name":name,"age":,age}
        self.users.append(new_user)
        return new_user
      
