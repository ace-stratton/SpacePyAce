# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 01:05:12 2024

@author: user
"""

import time, sys
import matplotlib.pyplot as plt
import numpy as np


from PDMInterface import PDMSetPower

sys.path.insert(0, 'C:/Users/user/Desktop/SpacePy_Ace')


output = PDMSetPower(3, "Power1")
print(output)