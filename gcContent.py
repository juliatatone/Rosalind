#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:59:45 2018

@author: juliatatone
"""

f = open('rosalind_gc.txt', 'r')
i = 2
while i < len(text):
    if not text[i].startswith('>') and not text[i-1].startswith('>'):
        text[i-1] += text[i]
        del text [i]
        i -= 1
    i += 1
bestID = text[0]
bestGC = float((text[1].count('G') + text[1].count('C'))) / len(text[1]) * 100
for i in range(2,len(text),2):
    gc = float((text[i+1].count('G') + text[i+1].count('C'))) / len(text[i+1]) *100
    if gc > bestGC:
        bestGC = gc
        bestID = text[i]
print(bestID[1:] + '\n' + str(bestGC))