#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:50:21 2018

@author: chris_poskitt
"""

from libdw import sm

class UpAndDown(sm.SM):
    start_state = 0
    
    def get_next_values(self, state, inp):
        assert(inp == 'up' or inp == 'down')
        assert(0 <= state)
        
        if inp == 'up':
            next_state = state + 1
            output = next_state
        elif inp == 'down':
            next_state = state - 1
            output = next_state
            
        return next_state, output

s = UpAndDown()
s.start()
print(s.transduce(['up', 'down', 'up', 'up', 'down']))
print(s.transduce(['up', 'up', 'up', 'down', 'down', 'up']))

