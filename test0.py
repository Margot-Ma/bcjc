# -*- coding: utf-8 -*-
"""
Created on Sat May 29 09:37:08 2021

@author: ASUS
"""

class my_robot(object):
    
    def __init__(self, name):
        self.name = name
        self.chat_history = []
    
    def __str__(self):
        return 'Ha,your chat robot %s comes'%self.name
    
    def chat(self):
        print('Hi there, let\'s talk. Input "quit" to stop.')