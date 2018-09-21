#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 11:18:33 2018

@author: ghkim
"""

import os, subprocess, sys
import pandas as pd
from pandas import DataFrame

class bookDB():
    def __init__(self):
        os.chdir('/home/ghkim/Desktop/books')
        pd.set_option('display.expand_frame_repr', False)
        self.data = pd.read_csv('book_list.csv')
    def print_list(self):
        print(self.data)
    def search(self, searchType, value):
        find = []
        temp = self.data[searchType]
        for i in temp.index:
            if value.lower() in temp[i].lower():
                find.append(i)
        print(self.data.loc[find])
    def open_book(self, serial):
        filename = '{}.pdf'.format(serial)
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

db = bookDB()

