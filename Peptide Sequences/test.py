# -*- coding: utf-8 -*-
"""
Created on Wed May  9 15:14:34 2018

@author: jtfl2
"""

import pc_self as pcs
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def register_extension(id, extension): Image.EXTENSION[extension.lower()] = id.upper()
Image.register_extension = register_extension
def register_extensions(id, extensions): 
  for extension in extensions: register_extension(id, extension)
Image.register_extensions = register_extensions

seq = 'IVTESSDYSSY'
ranges = [[2.84, 12.79], [-3, 3], [-1.19, 16.0], [1490.0, 17990.0], [1490, 17990]]
info = pcs.calcProp(seq,ranges)
[binary,prop] = pcs.make_barcodes(info)
print(binary)
#binary = np.tile(binary, [100, 1])
#result = Image.fromarray(s,mode = 'L')
#result.save('test.bmp')
binary=np.asarray(binary)
binary = np.tile(binary,(256,1))
result = Image.fromarray(binary,mode='L')
result.save('seq1.png')
result.show()