#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge="str is a data type in Python"):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]
    def teach(self):
        index = random.randint(0, len(self.knowledge)-1)
        lesson = self.knowledge[index]
        print(lesson)
        return lesson
        
t1 = Teacher("Sakib", "Rasul")
t2 = Teacher("Ben", "Cavins")
print("t1:", t1.teach())
print("t2:", t2.teach())
