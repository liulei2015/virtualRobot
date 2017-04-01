# /usr/bin/python
from selenium import webdriver
import django

print(django.VERSION)


brower = webdriver.Chrome()

brower.get('http://localhost:8000')

assert 'Django' in brower.title
