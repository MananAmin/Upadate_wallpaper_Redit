import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import time
import datetime

def fun(url,inn,names,six):
  
  Scorecard = requests.get(url).text

  Soup = BeautifulSoup(Scorecard,"html.parser")
  # print soup
  match_name = Soup.find('h1',class_="cb-nav-hdr cb-font-18 line-ht24").get_text()
  match_name = match_name[:match_name.find('- Live Cricket Score, Commentary')].strip()

  
  if inn ==1:

	  Inning1 = Soup.find_all('div',id="innings_1")[0]
	  Inning1_batting = Inning1.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
	  Inning1_batting = Inning1_batting.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms")
	  
	  Score = Inning1.find_all('span',class_="pull-right")
	  score = Score[0].get_text()
	  if '-' in score:
	    score = score[:score.find('-')]
	  team_name = Inning1.find('span').get_text()
	  if 'Innings' in team_name:
	    team_name = team_name[:team_name.find(' Innings')]
	  


	  # Inning 1 Start

	  Inning1_batting_info = []
	  count =0
	  for b in Inning1_batting:
	    # pprint(b)
	    batsman = {}
	    name = b.find('a',class_="cb-text-link")
	    if name:
	      pid = name['href'][10:]
	      batsman['pid'] = str(pid[:pid.find('/')])
	      batsman['name'] = str(name.get_text()).strip()
	      if '(' in batsman['name']:
	        batsman['name'] = batsman['name'][:batsman['name'].find('(')].strip()
	    out_by = b.find('span',class_="text-gray")
	    if out_by:
	      batsman['out_by'] = str(out_by.get_text()).strip()
	    runs = b.find('div',class_="cb-col cb-col-8 text-right text-bold")
	    if runs:
	      batsman['runs'] = str(runs.get_text()).strip()
	    all_others = b.find_all('div',class_="cb-col cb-col-8 text-right")
	    if len(all_others)>0:
	      batsman['balls'] = str(all_others[0].get_text()).strip()
	      batsman['fours'] = str(all_others[1].get_text()).strip()
	      batsman['sixes'] = str(all_others[2].get_text()).strip()
	      batsman['sr'] = str(all_others[3].get_text()).strip()
	   ##   dic[str(batsman['name'])]=  int(batsman['sixes'])
	      names[count] = str(batsman['name'])
	      six[count] =  int(batsman['sixes'])
	      count+=1
	    # print all_other
	    if len(batsman) > 0:
	      Inning1_batting_info.append(batsman)



  # Inning 2 Start

  else:
	  Inning2 = Soup.find_all('div',id="innings_2")[0]
	  Inning2_batting = Inning2.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[0]
	  Inning2_bowling = Inning2.find_all('div',class_="cb-col cb-col-100 cb-ltst-wgt-hdr")[1]
	  Inning2_batting = Inning2_batting.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms")
	  Inning2_bowling = Inning2_bowling.find_all('div',class_="cb-col cb-col-100 cb-scrd-itms ")
	  Score = Inning2.find_all('span',class_="pull-right")
	  score = Score[0].get_text()
	  if '-' in score:
	    score = score[:score.find('-')]
	  team_name = Inning2.find('span').get_text()
	  if 'Innings' in team_name:
	    team_name = team_name[:team_name.find(' Innings')]
	  





	  co = 0  
	  Inning2_batting_info = []
	  for b in Inning2_batting:
	    # pprint(b)
	    batsman = {}
	    name = b.find('a',class_="cb-text-link")
	    if name:
	      pid = name['href'][10:]
	      batsman['pid'] = str(pid[:pid.find('/')])
	      batsman['name'] = str(name.get_text()).strip()
	      if '(' in batsman['name']:
	        batsman['name'] = batsman['name'][:batsman['name'].find('(')].strip()
	    out_by = b.find('span',class_="text-gray")
	    if out_by:
	      batsman['out_by'] = str(out_by.get_text()).strip()
	    runs = b.find('div',class_="cb-col cb-col-8 text-right text-bold")
	    if runs:
	      batsman['runs'] = str(runs.get_text()).strip()
	    all_others = b.find_all('div',class_="cb-col cb-col-8 text-right")
	    if len(all_others)>0:
	      batsman['balls'] = str(all_others[0].get_text()).strip()
	      batsman['fours'] = str(all_others[1].get_text()).strip()
	      batsman['sixes'] = str(all_others[2].get_text()).strip()
	      names[co] = str(batsman['name'])
	      six[co]  = int(batsman['sixes'])
 	      co+=1
	      batsman['sr'] = str(all_others[3].get_text()).strip()

	    # print all_other
	    if len(batsman) > 0:
	      Inning2_batting_info.append(batsman)
  return 




url = "https://www.cricbuzz.com/live-cricket-scorecard/22479/csk-vs-mi-44th-match-indian-premier-league-2019"
inn = 2

names = []
six = []
temp =[]
flag =0
for x in xrange(0,10):
	names.append(' ')
	six.append(0)
	temp.append(0)

while True:
  for x1 in xrange(0,10):
  ##	print '  ',names[x1]
  ##	print '  ',six[x1]
  	temp[x1] = six[x1]
  fun(url,inn,names,six)

  if flag !=0:
	  for x in xrange(0,10):
	  	if temp[x] != six[x] :
	  		print 'heeeeeeeyyy six by ',names[x],'at time Now You can use "Swiggy6"  code  till 6 min from',datetime.datetime.now().time() 
  flag =1  		
  time.sleep(10)
