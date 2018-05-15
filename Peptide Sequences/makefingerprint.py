# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:26:18 2018

@author: jtfl2
"""
import numpy as np
filename = '12lengthpeptides.csv'
f = open(filename,'r')
f.readline()

def find_base_structure(seq):
    structure = np.zeros((3,3))
    consecutive = 0
    placement = 0
    for amino in seq:
        if amino in 'IMVAL' and consecutive <= 5:
            structure[0, placement] = 1
            consecutive = consecutive + 1
            if consecutive > 5:
                placement = placement + 1
                
        if amino in 'RHKDESTNQG' and consecutive <= 10:
            structure[1, placement] = 1
            consecutive = consecutive + 1
            if consecutive > 10:
                placement = placement + 1
                
        if amino in 'YWFRHKDESTNQG' and consecutive <= 13:
            structure[2, placement] = 1
            consecutive = consecutive + 1
            if consecutive > 13:
                placement = placement + 1

        