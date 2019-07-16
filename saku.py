import requests,sys,time;from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError;import os
#--------Warna
i="\033[32m" #hijau
cg="\033[36m" #cyan gelap
k="\033[33;1m" #kuning
p="\033[0m" #putih
ba="\033[96;1m" #biruaqua
pu="\033[35m" # #purple
gr="\033[37m" #putih terang
pb="\033[47m" #putihbold
m="\033[31m" #merah
b="\033[34m" # Biru
#------------------#
banr = "\n         \x1b[34m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mAuthor   \x1b[37m: Sazxt\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mMy Team  \x1b[37m: Black Coder Crush\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mwhatsapp \x1b[37m: 083892081021\n           \x1b[31m\xe2\x8f\xa3 \x1b[32mCodeName \x1b[37m: \x1b[36mSakuraNime \x1b[0;1mv1.1\n         \x1b[34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n"
def ap(u):
	for s in u + "\n":
		sys.stdout.write(s)
		sys.stdout.flush()
		time.sleep(130. / 1000)
def ux():
    load = ['.   ', '..  ', '... ']
    for z in load:
        print '\r%s[%s+%s] %sMembuka %shttps://sakuranime.com%s'%(b,m,b,gr,i,cg) + z,
        sys.stdout.flush()
        time.sleep(1)
def on():
	os.system("clear")
	try:
		nx = '\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
		print banr
		print "\n"+gr+nx
		a = requests.get("https://sakuranime.com").text;link = []
		soup = BeautifulSoup(a,"html.parser");tit = []
		for s in soup.find_all("a"):
			tit.append(s.get("title"))
		for n in soup.find_all("a"):
			link.append(n.get("href"))
		print """
\033[34m[\033[37m1\033[34m] \033[37m{b}
\033[34m[\033[37m2\033[34m] \033[37m{a}
\033[34m[\033[37m3\033[34m] \033[37m{u}
\033[34m[\033[37m4\033[34m] \033[37m{pn}
\033[34m[\033[37m5\033[34m] \033[37m{flot}
\033[34m[\033[37m6\033[34m] \033[37m{bx}
\033[34m[\033[37m7\033[34m] \033[37m{ox}
\033[34m[\033[37m8\033[34m] \033[37m{lax}
\033[34m[\033[37m9\033[34m] \033[37m{pat}
\033[34m[\033[37m10\033[34m] \033[37m{flor}
\033[34m[\033[37m12\033[34m] \033[37mExit
		""".format(b=tit[12],a=tit[17],u=tit[22],pn=tit[27],flot=tit[32],bx=tit[37],ox=tit[42],lax=tit[47],pat=tit[52],flor=tit[57])
		print gr+nx
		lop = raw_input("%s[%s+%s] %sPilih Menu : %s"%(b,m,b,gr,i))
		if lop == "1":
			os.system("clear")
			print banr
			u = requests.get(link[9]).text
			xsoup = BeautifulSoup(u,"html.parser")
			print "\n"+gr+nx
			for s in xsoup.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "2":
			os.system("clear")
			print banr
			ba = requests.get(link[13]).text
			zn = BeautifulSoup(ba,"html.parser")
			print "\n"+gr+nx
			for s in zn.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "3":
			os.system("clear")
			print banr
			xu = requests.get(link[22]).text
			ab = BeautifulSoup(xu,"html.parser")
			print "\n"+gr+nx
			for s in ab.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "4":
			os.system("clear")
			print banr
			nu = requests.get(link[23]).text
			bi = BeautifulSoup(nu,"html.parser")
			print "\n"+gr+nx
			for s in bi.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "5":
			os.system("clear")
			print banr
			ox = requests.get(link[28]).text
			bo = BeautifulSoup(ox,"html.parser")
			print "\n"+gr+nx
			for s in bo.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "6":
			os.system("clear")
			print banr
			ol = requests.get(link[34]).text
			bm = BeautifulSoup(ol,"html.parser")
			print "\n"+gr+nx
			for s in bm.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "7":
			os.system("clear")
			print banr
			np = requests.get(link[38]).text
			no = BeautifulSoup(np,"html.parser")
			print "\n"+gr+nx
			for s in no.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "8":
			os.system("clear")
			print banr
			mo = requests.get(link[43]).text
			vo = BeautifulSoup(mo,"html.parser")
			print "\n"+gr+nx
			for s in vo.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "9":
			print "%s[%s!%s] %sPerbaikan Maaf !"%(b,m,b,gr)
#			os.system("clear")
#			print banr
#			bp = requests.get(link[48]).text
#			bl = BeautifulSoup(bp,"html.parser")
#			print "\n"+gr+nx
#			for s in bl.find_all("h3"):
#				print s.get_text()
#			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "10":
			os.system("clear")
			print banr
			bnp = requests.get(link[54]).text
			lox = BeautifulSoup(bnp,"html.parser")
			print "\n"+gr+nx
			for s in lox.find_all("h3"):
				print s.get_text()
			print gr+nx
			raw_input("%s[%s+%s] %sBack >> "%(b,m,b,gr))
			on()
		elif lop == "e" or lop == "E":
			sys.exit()
		else:
			print "\n%s[%s!%s] %sWrong Input !"%(b,m,b,gr)
			time.sleep(0.5)
			on()
	except requests.exceptions.ConnectionError:
		print "\n%s[%s!%s] %sConnection Closed !"%(b,m,b,gr)
	except KeyboardInterrupt:
		print "\n%s[%s!%s] %sPliss Ctr+D Out Program ! "%(b,m,b,gr)
		time.sleep(0.3)
		on()
	except EOFError:
		sys.exit()
if __name__ == "__main__":
	 on()