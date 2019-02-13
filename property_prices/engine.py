#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:24:14 2019

@author: harriet
"""

from config import app_id, api_key

from bs4 import BeautifulSoup
import requests
import csv
import time



endpoint = f"https://api.adzuna.com:443/v1/api/property/gb/search/1?app_id={app_id}&app_key={api_key}&where=London&category=for-sale&sort_by=date&beds=1&price_min=200000&price_max=400000"

response = get(endpoint)

data = response.json()

print(data)


