# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 20:32:22 2020

@author: Aditya
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())