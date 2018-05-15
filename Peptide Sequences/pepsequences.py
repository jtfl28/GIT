# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 13:38:09 2018

@author: jtfl2
"""
import itertools as it
import pc_self as pcs



aromatic = {}
hydrophobic = {}
hydrophilic = {}
per = {}
ranges = [[],[],[],[],[]]

hydrophobic['3'] = it.product('IMVAL', repeat=3)
hydrophilic['5'] = it.product('TSGNQ', repeat=5)
aromatic['4'] = it.product('YWF','HRKDETSGNQYWF','HRKDETSGNQYWF','HRKDETSGNQYWF')
    
per['12'] = it.product(hydrophobic['3'],hydrophilic['5'],aromatic['4'], repeat = 1)

f = open('12lengthpeptides.csv', 'w')
f.write("Sequence,Mass,Isoelectric Point (pI),Net Charge,Hydrophobicity,Extinction coefficient 1,Extinction coefficient2" + "\n")
p = ""
for p in per['12']:
    seq = "".join(p[0] + p[1] + p[2])
    Info = pcs.calcProp(seq,ranges)
    ranges = Info[7]
    f.write(Info[0] + ',' + str(Info[1])+ ','+ str(Info[2])+ ','+ str(Info[3])+ ','+ str(Info[4])+ ','+ str(Info[5])+ ','+ str(Info[6])   + "\n")
f.close()