#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = [] 
    
    def learn(self, knowledge_item):
        self.knowledge.append(knowledge_item)
    
    def show_knowledge(self):
        return self.knowledge  # Return the knowledge list    
        