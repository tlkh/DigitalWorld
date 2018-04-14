#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:39:41 2018

@author: chris_poskitt
"""

from libdw import sm

class TorchLight(sm.SM):
    start_state = 0
    
    def get_next_values(self, state, inp):
        assert(inp == 'push')
        assert(0 <= state <= 1)
        
        if state == 0:
            next_state = 1
            output = 'on'
        elif state == 1:
            next_state = 0
            output = 'off'
            
        return next_state, output

# do this in the kernel

s = TorchLight()
s.start()
s.step('push')
s.step('push')
s.step('push')

s = TorchLight()
s.start()
print(s.transduce(['push'] * 7))