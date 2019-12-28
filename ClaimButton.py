# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 23:45:33 2019

@author: Justin Corcuera
"""

from tkinter import * 
from ConfigUtility import ConfigUtility

servant = ""
util = None

class ClaimButton():
    
    servant = " "
    
    def __init__(self, root):
        
        #Creating background Label
        self.label = Label(borderwidth = 1, relief = "raised", bg = "#CBCACA")      
        self.label.place(height = 70, width = 160, x = 50, y = 320)
        
        #Creating Claim Button
        self.button = Button(root, text = "Claim", command = lambda: self.claim())
        self.button.place(height = 50, width = 140, x = 60, y = 330)

    def current_name(self, name, utility):
        global servant
        global util
        
        #sets current Servant and current instance of the ConfigUtility   
        util = utility
        servant = name

    def claim(self):
        global servant
        claim_dict = util.claimed()
        
        if servant != "" and claim_dict[servant] == False:  
            claim_dict[servant] = True
            util.update_config()