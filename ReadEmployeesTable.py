#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:04:44 2020

@author: ton
"""


import pandas as pd

#df = pd.read_excel(file, sheetname='Elected presidents')

file_path = "/Users/ton/documents/github/data/EmployeesSheet.xlsx"

employees = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=1)


#pd.read_excel?

type(employees)