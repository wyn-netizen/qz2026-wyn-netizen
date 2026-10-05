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
    def get_user(self,user_id:int):
        for user in self.user:
            if user["id"] == user_id:
                return user_id
        return None
    def change_age(self,user_id:int,new_age:int) ->bool:
        user = self.get_user(user_id)
        if user is not None:
            user["age"] = new_age
            return True
        return False
        
