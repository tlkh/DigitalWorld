#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:47:08 2018

@author: chris_poskitt
"""

from libdw import sm

class LanguageAcceptor(sm.SM):
    start_state = 0
    
    def get_next_values(self, state, inp):
        assert(inp in 'abc' and len(inp) == 1)
        assert(0 <= state <= 3)
        
        if state == 0 and inp == 'a':
            next_state = 1
            output = True
        elif state == 1 and inp == 'b':
            next_state = 2
            output = True
        elif state == 2 and inp == 'c':
            next_state = 0
            output = True
        else:
            next_state = 3
            output = False
            
        return next_state, output

s = LanguageAcceptor()
s.start()
print(s.transduce(list('abcabcabcabc')))
print(s.transduce(list('abcccccc')))
print(s.transduce(list('cabcabc')))
