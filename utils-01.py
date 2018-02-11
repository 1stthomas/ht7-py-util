# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:20:46 2018

@author: 1stthomas
"""

def module_exists(module_name):
    """
    Checks if the submitted Module is installed. This Function prints
    the Result of the check.
    
    Parameters
    ----------
    module_name : The name of the module to be checked.
    
    Returns
    -------
    is_installed : boolean
      True if the submitted module is installed
    
    Example
    -------
    >>> module_exists("csv")
    true
    """
    try:
        __import__(module_name)
    except ImportError:
        print("Module \"" + module_name + "\" is NOT installed")
        return False
    else:
        print("Module \"" + module_name + "\" is installed")
        return True


module_exists("csv")