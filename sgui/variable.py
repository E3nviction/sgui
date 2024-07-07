"""
Sgui Variable Module 1.0.0
"""

variables = {}

import pygame

class var():
    """
    Class for variables.
    """
    def vset(name:str,value):
        """
        Sets a new value for a given variable in the global variables dictionary.

        name (str): The name of the variable to be set.
        value (any): The value to set for the variable.
        """
        global variables
        variables[name] = value
    def vget(name:str):
        """
        Retrieve the value associated with the given name from the global variables dictionary.

        name (str): The name of the variable to retrieve.
        """
        global variables
        return variables.get(name)