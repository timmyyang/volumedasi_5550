
import subprocess
import socket
import fcntl
import struct
import time

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
    
def Get_quan_mac():
    f = open('/tmp/file/master_quantenna_mac', 'r').read().strip()
    return f
    
def Get_all_iris_ip_length():  
    filename = "/tmp/file/search_iris" 
    myfile = open(filename) 
    lines = len(myfile.readlines()) 
    return lines 

def Get_all_quan_ip_length():  
    filename = "/tmp/file/search_quantenna" 
    myfile = open(filename) 
    lines = len(myfile.readlines()) 
    return lines      
    
def Get_all_iris_ip(number):
    f = open('/tmp/file/search_iris')
    f = f.readlines()[number-1].strip()
    return f
    
def Get_all_quan_ip(number):
    f = open('/tmp/file/search_quantenna')
    f = f.readlines()[number-1].strip()
    return f
    
def brocast_iris_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        PORT = 1060
        ip = 'b' + Get_my_ip()
        brocast_ip = Get_brocast_ip()
        #network = '<broadcast>'
        s.sendto( ip.encode('utf-8'), (brocast_ip, PORT))
    except Exception as exc:
        #print ("Network is unreachable")
        pass

        
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

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        PORT = 1060

        s.bind(('', PORT))
        #print('Listening for broadcast at ', s.getsockname())

        while True:
            data, address = s.recvfrom(65535)
            #print('Server received from {}:{}'.format(address, data.decode('utf-8')))

            r = format(data.decode('utf-8'))
            #print r
            brocast_ip = r.strip('apofqtcbd')
            my_ip = Get_my_ip()
            if brocast_ip != my_ip:
                if r[0]=='c':
                    brocast_iris_ip()
                    r = r.strip('c')
                    ip_line_length=Get_all_iris_ip_length()
                    i = 1
                    repeat_ip = 0
                    while i <=  ip_line_length:
                        check_ip= Get_all_iris_ip(i)
                        if r == check_ip:
                            repeat_ip = 1
                            i = ip_line_length + 1
                            break
                        i = i + 1
                        
                    if repeat_ip == 0:
                        subprocess.Popen('echo '+r+'>> /tmp/file/search_iris', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
                        
                        #print ("get iris ip: ",r)
                if r[0]=='b':
                    r = r.strip('b')
                    ip_line_length=Get_all_iris_ip_length()
                    i = 1
                    repeat_ip = 0
                    while i <=  ip_line_length:
                        check_ip= Get_all_iris_ip(i)
                        if r == check_ip:
                            repeat_ip = 1
                            i = ip_line_length + 1
                            break
                        i = i + 1
                        
                    if repeat_ip == 0:
                        subprocess.Popen('echo '+r+'>> /tmp/file/search_iris', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
                        #print ("get iris ip: ",r)
                        
                if r[0]=='a':
                    if r[1]=='o':
                        r = r.strip('ao')
                        subprocess.Popen('echo 3 > /tmp/file/stream_check', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
                        subprocess.Popen('echo '+r+'>> /tmp/file/stream_check', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
                        #print ("brocast Announcement_Mode_On")
                        
                    if r[1]=='f':
                        r = r.strip('af')
                        subprocess.Popen('echo 4 > /tmp/file/stream_check', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        #print ("brocast Announcement_Mode_Off")
                        
                if r[0]=='p':
                    if r[1]=='o':
                        r = r.strip('po')
                        
                        subprocess.Popen('echo 1 > /tmp/file/stream_check', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
                        subprocess.Popen('echo '+r+'>> /tmp/file/stream_check', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
                        #print ("brocast party_Mode_On ,ip=",r)
                        
                    if r[1]=='f':
                        r = r.strip('pf')
			subprocess.Popen('echo 2 > /tmp/file/stream_check', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
                        #print ("brocast party_Mode_Off")
                        
                if r[0]=='q':
                        if r[1]=='t':
                            f = Get_quan_mac()
                            r = r.strip('qt')

                            ip_line_length=Get_all_quan_ip_length()
                            i = 1
                            repeat_ip = 0
                            while i <=  ip_line_length:
                                check_ip= Get_all_quan_ip(i)      
                                if r[6:] == check_ip:
                                    repeat_ip = 1
                                    i = ip_line_length + 1
                                    break
                                i = i + 1
                                
                            if repeat_ip == 0:
                                if (r[:6]==f):
                                    #print ("get master quan ip: ",r[6:])
                                    subprocess.Popen('echo '+r[6:]+' > /tmp/file/default_quantenna_ip', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()  
                                    
                                subprocess.Popen('echo '+r[6:]+'>> /tmp/file/search_quantenna', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
                                #print ("get other iris's quantenna ip: ",r[6:])
                                
                if r[0]=='d':
                    f = open('/tmp/file/answer','w')
                    f.write(r[1:6])
                    f.close()

    except Exception as exc:
        #print ("socket error")
        pass
        
    time.sleep(0.5)
        
    
