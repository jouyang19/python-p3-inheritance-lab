#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, knowledge=""):
        super().__init__(first_name, last_name)
        self.knowledge = []
    def learn(self, lesson):
        if isinstance(lesson, str):
            self._knowledge = self.knowledge.append(lesson)