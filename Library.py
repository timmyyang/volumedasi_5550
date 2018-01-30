import requests
import subprocess
import select
import random
import json
import socket
import fcntl
import struct

#######################network########################

"""
like import requests
you have to add try and except 
"""
def requests_command(url,time):
    r = requests.get(url,timeout=time)
    return r
    
def requests_payload_command(url,payload,time):
    r = requests.get(url,params=payload,timeout=time)
    return r
    
def requests_stream_command(url,streaming,time): #streaming = True or False
    r = requests.get(url, stream=streaming,timeout=time)    
    return r

"""
Default use Get_my_ip() return br-lan ip
"""
def get_interface_ip(ifname):
    get_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(get_s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])

def get_lan_ip():
    interfaces = ["br-lan","eth0", "eth1", "eth2", "wlan0", "wlan1", "wifi0", "ath0", "ath1", "ppp0",]
    for ifname in interfaces:
        try:
            ip = get_interface_ip(ifname)
            break
        except IOError:
            ip = ''
            pass

    return ip
    
def Get_my_ip():
    my_ip = get_lan_ip()
    my_ip = my_ip.strip()
    return my_ip
    
    
"""
get ip and change to 255 ex 192.168.1.1 > 192.168.1.255
"""

def Get_brocast_ip():
    my_ip_exec_check=0
    while my_ip_exec_check == 0:
        my_ip = Get_my_ip()
        try:
            #print my_ip[0]
            my_ip_exec_check=1
        except Exception as exc:
            my_ip_exec_check=0    

    j=0
    default_ip_count=0
    default_ip=''
    while default_ip_count < 3:

        if my_ip[j] == '.' and default_ip_count < 3:
            default_ip_count=default_ip_count+1

        default_ip += str(my_ip[j])
        j=j+1
    default_ip = default_ip + '255'
    #print default_ip
    return default_ip
    
"""
port = network port
word = which word you want to sendto
ip = 255 or unicast ip
"""

def brocast_iris_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        PORT = 1060
        ip = 'c' + Get_my_ip()
        brocast_ip = Get_brocast_ip()
        #network = '<broadcast>'
        s.sendto( ip.encode('utf-8'), (brocast_ip, PORT))
    except Exception as exc:
        #print ("Network is unreachable")
        pass

def brocast_to_ip(port,word,ip):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    #PORT = 1060
    PORT = port
    #word = 'pf' + Get_my_ip()
    word = word
    #brocast_ip = Get_brocast_ip()
    brocast_ip = ip
    #network = '<broadcast>'
    s.sendto( word.encode('utf-8'), (brocast_ip, PORT))
    
#######################process########################

"""
start_program() no wait so process may pass 
start_program_wait() wait process start then go 
kill_program() killall process that you want to kill
"""

def start_program(command):
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
def start_program_wait(command):
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    
def kill_program(command):
    command = 'killall -9 ' + command
    bprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    
"""
play_music_keep() add -r 
"""
def play_music_file(file):
    command = 'madplay ' + file + ' -o wave:- - | aplay -M&'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
def play_music_file_wait(file):
    command = 'madplay ' + file + ' -o wave:- - | aplay -M'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    
def play_music_keep(file):
    command = 'madplay ' + file + ' -r -o wave:- - | aplay -M&'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
def play_music_url(url):
    command = 'wget -q -O - ' + url + '   | madplay - -o wave:- | aplay -M&'
    r = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return r
    
"""
control_volume() range 0-10
"""
def control_volume(value):
    #subprocess.Popen(["amixer" ,"cset" ,"numid=2,iface=MIXER,name='MaxxVolume Control'" ,str(n)]).wait()
    command = "amixer cset numid=1,iface=MIXER,name='MaxxVolume Control' "  + str(value)
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 

"""
/root/file/iris.conf

language=EN
volume_set=10
master_quantenna_mac=000000
default_quantenna_ip=192.168.1.246
search_quantenna=192.168.1.247
time=30000
snapclient=1
radio1=163.
radio2=170.
radio3=1
Andromeda_ID=0b38076dff1bde83
Andromeda_IP=http://192.168.1.150:7070/

"""
#######################file########################
def get_iris_conf(key):
    f = open('/root/file/iris.conf', 'r')
    f = f.read().strip().split('\n')
    if key == 'language':
        value=f[0].split('=')
    elif key == 'volume_set':
        value=f[1].split('=')
    elif key == 'master_quantenna_mac':
        value=f[2].split('=')
    elif key == 'default_quantenna_ip':
        value=f[3].split('=')
    elif key == 'search_quantenna':
        value=f[4].split('=')
    elif key == 'time':
        value=f[5].split('=')
    elif key == 'snapclient':
        value=f[6].split('=')
    elif key == 'radio1':
        value=f[7].split('=')
    elif key == 'radio2':
        value=f[8].split('=')
    elif key == 'radio3':
        value=f[9].split('=')
    elif key == 'Andromeda_ID':
        value=f[10].split('=')
    elif key == 'Andromeda_IP':
        value=f[11].split('=')
    return value[1]
    
def set_iris_conf(key,value):
    f = open('/root/file/iris.conf','r')
    f = f.read().strip().split('\n')
    if key == 'language':
        f[0]='language='+str(value)
    if key == 'volume_set':
        f[1]='volume_set='+str(value)
    if key == 'master_quantenna_mac':
        f[2]='master_quantenna_mac='+str(value)
    if key == 'default_quantenna_ip':
        f[3]='default_quantenna_ip='+str(value)
    if key == 'search_quantenna':
        f[4]='search_quantenna='+str(value)
    if key == 'time':
        f[5]='time='+str(value)
    if key == 'snapclient':
        f[6]='snapclient='+str(value)
    if key == 'radio1':
        f[7]='radio1='+str(value)
    if key == 'radio2':
        f[8]='radio2='+str(value)
    if key == 'radio3':
        f[9]='radio3='+str(value)
    if key == 'Andromeda_ID':
        f[10]='Andromeda_ID='+str(value)
    if key == 'Andromeda_IP':
        f[10]='Andromeda_IP='+str(value)
    f_1 = open('/root/file/iris.conf','w')
    for i in range(0,len(f)):
        f_1.write(str(f[i])+'\n')
    
def file_get(file):
    f = open(file, 'r').read().strip()
    return f
            
def file_set(file,word):
    f = open(file,'w')
    f.write(str(word))
    f.close()    
    
def file_copy(tmp_file,file):
    f = open(tmp_file, 'r').read().strip()
    f_q = open(file, 'w')
    f_q.write(f)
    f_q.close()
    
def file_length(file):  
    myfile = open(file) 
    lines = len(myfile.readlines()) 
    return lines   

    
"""
decode json
"""
def decode_json(load_json)
    decodejson = json.loads(load_json)
    return decodejson

#######################GPIO LED BUTTON########################
"""
use file talk 
pin = 1 or 0
"""
def Check_State_LED():
    try:
        State_LED = open('/tmp/file/gpio/State_LED','r').read().strip()
    except Exception as exc:
        State_LED = 2
    State_LED = int(State_LED)
    return State_LED
    
def Write_State_LED(pin):
    try:
        f = open('/tmp/file/gpio/State_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
    
def Check_Alexa_LED():
    try:
        Alexa_LED = open('/tmp/file/gpio/Alexa_LED','r').read().strip()
    except Exception as exc:
        Alexa_LED = 2
    Alexa_LED = int(Alexa_LED)
    return Alexa_LED
    
def Write_Alexa_LED(pin):
    try:
        f = open('/tmp/file/gpio/Alexa_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
    
def Check_Iris_LED():
    try:
        Iris_LED = open('/tmp/file/gpio/Iris_LED','r').read().strip()
    except Exception as exc:
        Iris_LED = 2
    Iris_LED = int(Iris_LED)
    return Iris_LED
    
def Write_Iris_LED(pin):
    try:
        f = open('/tmp/file/gpio/Iris_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass

    
def Check_Power_LED():
    try:
        Power_LED = open('/tmp/file/gpio/Power_LED','r').read().strip()
    except Exception as exc:
        Power_LED = 2
    Power_LED = int(Power_LED)
    return Power_LED
    
def Write_Power_LED(pin):
    try:
        f = open('/tmp/file/gpio/Power_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass

def Start_Button_check():
    try:
        Start_Button = open('/tmp/file/gpio/Start_Button','r').read().strip()
    except Exception as exc:
        Start_Button = 2
    Start_Butto = int(Start_Button)
    return Start_Button
    
def Write_Voip(pin):
    try:
        f = open('/tmp/file/sound_busy_check','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
        
def Write_VOIP_LED(pin):
    try:
        f = open('/tmp/file/gpio/VOIP_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
    
def Read_VOIP_LED():
    return open('/tmp/file/gpio/VOIP_LED','r').read().strip()