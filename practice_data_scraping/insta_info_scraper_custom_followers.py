import requests
import csv
import pandas as pd
import re

insta = pd.read_csv('Instagram.csv')

username = []

bad_urls = []

# for lines in insta['Instagram'][0:250]:
for lines in insta:
    lines = lines.split("/")
    username.append(lines[3])

with open('insta_output.csv', 'w') as csvfile:
    t = csv.writer(csvfile, delimiter=',')     #   ----> COMMA Seperated
for user in username:
   try:
       url = 'https://www.instagram.com/'+ user
       r = requests.get(url)
       m = re.search(r'"followed_by":\{"count":([0-9]+)\}', str(r.content))
       num_followers = m.group(1)
       t.writerow([user,num_followers])    #  ----> Adding Rows
   except:
       bad_urls.append(url)

#  A script for practice
# import requests
# import re
#
# username_extract = 'selenagomez'
#
# url = 'https://www.instagram.com/'+ username_extract
# r = requests.get(url)
# m = re.search(r'"followed_by":\{"count":([0-9]+)\}', str(r.content))
# print(m)
