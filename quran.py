import requests,bs4,os,json,sys,time
from difflib import get_close_matches
ayt=True
ind=True
art=True
surah=[u'al-fatihah', u'al-baqarah', u'ali-imran', u'an-nisa', u'al-maidah', u'al-anam', u'al-araf', u'al-anfal', u'at-taubah', u'yunus', u'hud', u'yusuf', u'ar-rad', u'ibrahim', u'al-hijr', u'an-nahl', u'al-isra', u'al-kahfi', u'maryam', u'taha', u'al-anbiya', u'al-hajj', u'al-muminun', u'an-nur', u'al-furqan', u'asy-syuara', u'an-naml', u'al-qasas', u'al-ankabut', u'ar-rum', u'luqman', u'as-sajdah', u'al-ahzab', u'saba', u'fatir', u'yasin', u'as-saffat', u'sad', u'az-zumar', u'gafir', u'fussilat', u'asy-syura', u'az-zukhruf', u'ad-dukhan', u'al-jasiyah', u'al-ahqaf', u'muhammad', u'al-fath', u'al-hujurat', u'qaf', u'az-zariyat', u'at-tur', u'an-najm', u'al-qamar', u'ar-rahman', u'al-waqiah', u'al-hadid', u'al-mujadilah', u'al-hasyr', u'al-mumtahanah', u'as-saff', u'al-jumuah', u'al-munafiqun', u'at-tagabun', u'at-talaq', u'at-tahrim', u'al-mulk', u'al-qalam', u'al-haqqah', u'al-maarij', u'nuh', u'al-jinn', u'al-muzzammil', u'al-muddassir', u'al-qiyamah', u'al-insan', u'al-mursalat', u'an-naba', u'an-naziat', u'abasa', u'at-takwir', u'al-infitar', u'al-mutaffifin', u'al-insyiqaq', u'al-buruj', u'at-tariq', u'al-ala', u'al-gasyiyah', u'al-fajr', u'al-balad', u'asy-syams', u'al-lail', u'ad-duha', u'asy-syarh', u'at-tin', u'al-alaq', u'al-qadr', u'al-bayyinah', u'al-zalzalah', u'al-adiyat', u'al-qariah', u'at-takasur', u'al-asr', u'al-humazah', u'al-fil', u'quraisy', u'al-maun', u'al-kausar', u'al-kafirun', u'an-nasr', u'al-lahab', u'al-ikhlas', u'al-falaq', u'an-nas']
url="https://litequran.net/"

def get_surah(key):
    return "".join(get_close_matches(key,surah,n=1,cutoff=0))

def get_arab(surat):
    if off[surat] != {}:
       return off[surat]["arb"].split("<>")

    req=requests.get(url+surat).text
    pr=bs4.BeautifulSoup(req,"html.parser")
    rt=pr.find_all("span",class_="ayat")
    rs=[]
    for i in rt:
        rs.append(i.text[::-1])
    return rs

def get_indo(surat):
    if off[surat] != {}:
       return off[surat]["indo"].split("<>")
    req=requests.get(url+surat).text
    pr=bs4.BeautifulSoup(req,"html.parser")
    rt=pr.find_all("span",class_="bacaan")
    rs=[]
    for i in rt:
        rs.append(i.text)
    return rs

def get_arti(surat):
    if off[surat] != {}:
       return off[surat]["ar"].split("<>")

    req=requests.get(url+surat).text
    pr=bs4.BeautifulSoup(req,"html.parser")
    rt=pr.find_all("span",class_="arti")
    rs=[]
    for i in rt:
        rs.append(i.text)
    return rs

while True:
    try:
       off=json.loads(open("quran.txt").read())
    except IOError:
       pd={}
       for i in surah:
           pd[i] = {}
       open("quran.txt","w").write(json.dumps(pd))
       off=json.loads(open("quran.txt").read())
    except ValueError:
       off=open("quran.txt").read()
       off=ast.literal_eval(json.loads(json.dumps(off)))

    os.system("clear")
    menud = """\x1b[1;37m
    Semoga mendapat pahala .amminn
    By : Mr.Wedus//Error404
    
[AR] > Arab  > {}
[L]  > Latin > {}
[A]  > Arti  > {}

[H]  > Help

[D]  > Daftar Surah
[B]  > Baca Surah
[DO] > Download All Surah Offline
""".format(ayt,ind,art)
    print menud
    menu = raw_input("Pilihan > ")
    if menu.lower() == "ar":
       if ayt == False:
	  ayt = True
       else:
	  ayt = False
    elif menu.lower() == "l":
       if ind == False:
          ind = True
       else:
	  art = False
    elif menu.lower() == "a":
       if art == False:
          art = True
       else:
          art = False
    elif menu.lower() == "b":
       su = get_surah(raw_input("Nama Surah : "))
       if raw_input ("\nIngin Menampilkan Surah "+su+" (y/n) ? ").lower() == "n":
	  break
       os.system("clear")
       try:
        arb = get_arab(su)
        indo = get_indo(su)
        ar = get_arti(su)
       except:
	print ("Surah Ini Tidak Tersedia Offline :( ")
	break

       dikt = {"arb":"<>".join(arb),"indo":"<>".join(indo),"ar":"<>".join(ar)}
       if off[su] != "":
	  off[su] = dikt
	  open("quran.txt","w").write(json.dumps(off))
       for n,i in enumerate(arb):
	   if n == 70 or n == 140 or n == 210 or n == 280:
              raw_input("Tekan Apapun Untuk Lanjut Membaca")
	      os.system("clear")
           else:
	      pass
           print "[{}]".format(n+1)
           if ayt == True:
	      print ("Arab  : \x1b[1;34m"+i+"\x1b[1;37m")
	   if ind == True:
	      print ("Latin : \x1b[1;32m"+indo[n]+"\x1b[1;37m")
	   if art == True:
	      print ("Arti  : \x1b[1;36m"+ar[n]+"\x1b[1;37m")
           print
       print ("\n\n")
       raw_input("Enter To Clear")
    elif menu.lower() == "d":
       for n,i in enumerate(surah):
	   if off[i] != {}:
              print ("[{}] . {} (\x1b[1;32moffline\x1b[1;30m)".format(n+1,i))
           else:
	      print ("[{}] . {} ".format(n+1,i))
       raw_input("Enter To Clear")
    elif menu.lower() == "do":
       for sr in surah:
         if off[sr] == {}:
	    try:
	      arb = get_arab(sr)
              indo = get_indo(sr)
              ar = get_arti(sr)
	    except:
	      print ("Tidak Ada Jaringan :( ")
	      break
	    dikt = {"arb":"<>".join(arb),"indo":"<>".join(indo),"ar":"<>".join(ar)}
            if off[sr] != "":
	          off[sr] = dikt
	          open("quran.txt","w").write(json.dumps(off))
	    sys.stdout.write("\rDownloading : "+sr+"            \b")
	    sys.stdout.flush()
	    time.sleep(.1)
       print 
       raw_input("Semua Surah Sudah Tersedia Offline :) ")
    elif menu.lower() == "h":
       os.system("clear")
       print("""
(AR,L,A) : Merupakan Fitur untuk mengaktifkan & menonaktifkan print,jika di nonaktifkan
           Tidak Akan Menampilkan Bagian Itu

(D)      : Untuk Menampilkan Daftar Surah

(B)      : Untuk Membaca Surah, Ketikkan saja surah yang kamu inginkan,
           contoh : al baqoroh,albaqoroh,al bakoroh
	   akan tetap membuka surah al-baqarah

(DO)     : Untuk Mendownload Semua Surah Agar Offline,
           Ukurannya tidak terlalu besar,hanya 5 mb

Author        : Mr.Wedus//Error404
thanks to     : Allah SWT,My Parents,Litequran.net, And You :)
""")
       raw_input()