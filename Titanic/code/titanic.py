# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:46:21 2019

@author: gavam
"""

"""Data Prep"""

import pandas as pd
import numpy as np

#Data = open('titanic_data/train.csv','w') 
#print('all ok')
#vISU = pd.DataFrame(list(Data))


import csv

with open('titanic_data/train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            print (row)
        #        if line_count == 0:
#            print('Column names are', ", ".join(row))