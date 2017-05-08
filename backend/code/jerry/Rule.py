#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Gerardo Fang
@created 04-18 T
@lastmod 05-07 U
"""
import Filter
import Action

class Rule():
    filters = [] #Expression: contains the expression for this Filter
    actions = []
    """Contract 20 Manage Rule"""

    #@requires:
    #@ensures: 
    def createRule(self,flt: Filter):
        """"Creates the structure by which it builds the Rule with a Filter for some set of Actions"""
        self.filters = self.filters.append(self.actions)
        
    #@requires:
    #@ensures: Appends to the list of Filters in the Rule structure
    def addFilter(self, flt: Filter):
        """Adds a Filter for a set of Actions"""
        try: self.filters.append(flt)
        except ValueError:
            pass #handle if not in list (if needed)
        except AttributeError:
            pass #handle if list not a list (if needed)
        
    """Contract 21 Manage Rule’s Actions"""

    def deleteFilter(self):
        """Deletes the last Filter added to this Rule"""
        try: del self.filters[-1]
        except ValueError:
            pass #handle if not in list (if needed)
        except AttributeError:
            pass #handle if list not a list (if needed)

    
    #@requires:
    #@ensures: Appends to the list of Actions in the Rule structure
    def addAction(self, action: Action):  
        """Receives an Action and adds it to the Rule in the last Filter.""" 
        try: self.filters[-1] = self.filters[-1].append(self.action)
        except ValueError:
            pass #handle if not in list (if needed)
        except AttributeError:
            pass #handle if list not a list (if needed)
        
    #@requires: The Action is the last added Action to the Rule.
    #@ensures:
    def deleteAction(self):
        """Deletes the last action added to this set of Actions for the Rule """
        try: del self.actions[-1]
        except ValueError:
            pass #handle if not in list (if needed)
        except AttributeError:
            pass #handle if list not a list (if needed)
