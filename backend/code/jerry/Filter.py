# -*- coding: utf-8 -*-
"""
@author Gerardo Fang
@created 04-18 T
@modified 05-07 U gfang, mafravi
"""
import Action 
import Expression
#Contains Expression(s) by which to visualize and modify the PDML capture


class Filter():
    expression = [] #Expression: contains the expression for this Filter
    action = [] #Actions: contains the actions for this Filter
    
    """ Contract 8: Manage Filter """
    
    # @requires the rule exists
    # @ensures 
    def addFilter(self,expr: Expression):
        self.expression = expr
        """ Receives a filter and adds the filter to the rule """
        
    
    # @requires the filter is the last added to the rule
    # @ensures 
    def deleteFilter(self):
        """ Deletes the filter """
        self.expression = []
    
    # @requires 
    # @ensures 
    def addAction(self,actn: Action):
        """ Appends this Action to the list of Actions for this Filter """
        self.action.append(actn)
        
    # @requires  List of Actions is not empty
    # @ensures
    def deleteAction(self):
        """Deletes the last Action added to this Filter"""
        del self.actions[-1]
    
    """ Contract 9: Manage Expression """
    
    # @requires The Expression is in the Berkeley Packet Filter (BPF) syntax.
    # @ensures The addition of a primitive to the Expression for this Filter.
    def addToExpression(self,expr):
        """Receives a primitive (composed from the string) and adds it to the Expression in this Filter"""
        try: self.expression.append(expr)
        except ValueError:
            pass #handle if not in list (if needed)
        except AttributeError:
            pass #handle if list not a list (if needed)

    # @requires
    # @ensures
    def deleteExpression(self, expr):
        """Deletes the specified Expression from this Filter"""
        try: self.expression.remove(expr)
        except ValueError:
            pass #handle if not in list (if needed)
        except AttributeError:
            pass #handle if list not a list (if needed)
        
    pass
