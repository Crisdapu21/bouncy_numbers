#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Menu:
    # Display a menu and respond to choices when run.
    def __init__(self):
        self.choices = {
            1: self.info,
            2: self.calculate,
            3: self.quit
        }

    def display_menu(self):
        print(
            '\nWELCOME TO PROPORTION BOUNCY NUMBER CALCULATOR\n'
            '--------------------------------------\n\n'
            '1. ¿ What are the Bouncy Numbers ?\n'
            '2. Calculate Proportion Bouncy Numbers\n'
            '3. Exit\n'
        )

    # Display the menu and respond to choices.
    def run(self):
        while True:
            self.display_menu()
            choice = input('Enter an option : ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print('\n{} is not a valid Option'.format(choice))
    
    def info(self):
        print(
            '\n-- BOUNCY NUMBERS :\n'
            '   They are positive integers, that if we read from left to\n'
            '   right, we realize that they are not increasing or decreasing.\n\n'
            '   Example : 155349, 154830'
        )
     
     # Function that determines if a number is Bouncy
    def is_Bouncy(self, number):
        increase = False
        decrease = False
        num_list = [int (x) for x in str (number)]
        for i in range (1, len (num_list)):
            if (num_list [i-1] < num_list [i]):
                increase = True
            elif (num_list [i-1] > num_list [i]):
               decrease = True
            if (increase and decrease):
                return True
        return False
    
    # Function that determines proportion for limit 
    def proportion_Bouncy(self, limit):
        percentage = 0
        count = 0 
        n = 99
        while True:
            # If percentage is == the limit finish the cycle
            if percentage == float(limit):
                break
            else: 
                n = n + 1
                # If is bouncy number increase the counter
                if self.is_Bouncy(n):
                    count = count + 1
                percentage = (count *100.0) / n
        print '\n ---> Least number for which the proportion of bouncy numbers is exactly {}% is : {} <---'.format(limit, n)
            
    def calculate(self):
        print(
            '\n-- PROPORTION BOUNCY NUMBERS :\n'
        )
        numero = raw_input("Enter an percentage limit to proportion :  ")
        self.proportion_Bouncy(numero)     
         
    def quit(self):
        print('\nThank you for using PROPORTION BOUNCY NUMBER CALCULATOR\n')
        sys.exit(0)
                
if __name__ == "__main__":
    Menu().run()   
       
