import requests
import socket
import fcntl
import struct
import time

def requests_command(url,time):
    r = requests.get(url,timeout=time)
    return r
    
def requests_payload_command(url,payload,time):
    r = requests.get(url,params=payload,timeout=time)
    return r
        
def requests_stream_command(url,streaming,time):
    r = requests.get(url, stream=streaming,timeout=time)    
    return r
        
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
    
def Get_default_quan_ip():
    f = open('/tmp/file/default_quantenna_ip').read().strip()
    return f
    
def Get_request(host):
    r = requests.get(host,timeout=3)
    r = r.text
    r = r.strip()
    return r
    
def call_to_search_ip():
    my_ip = Get_my_ip()

    if my_ip.strip() == '192.168.1.247':
        return 0
    if my_ip.strip() != '':
        return 1
        
def search_iris_quan():

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
    #print default_ip

    f = open('/tmp/file/search_iris.tmp','w')
    f.truncate()
    f.close()
    f = open('/tmp/file/search_quantenna.tmp','w')
    f.truncate()
    f.close()
    search_ip=1
    while search_ip != 255:
        check_ip=default_ip+str(search_ip)
        try:
            r = requests.get('http://'+check_ip+'/search_ip',timeout=0.5).text.strip()
            if r=='1':
                f = open('/tmp/file/search_iris.tmp','a')
                f.write(check_ip)
                f.write('\n')
                f.close()
                #print ("get iris ip: ",check_ip)
            if r=='2':
                f = open('/tmp/file/search_iris.tmp','a')
                f.write(check_ip)
                f.write('\n')
                f.close()
                #print ("get quan ip: ",check_ip)
        except Exception as exc:
            pass
        time.sleep (loop_time)
        search_ip = search_ip+1
    try:    
        f_tmp = open('/tmp/file/search_iris.tmp', 'r')
        f_tmp = f.readlines()[2]
        f = open('/tmp/file/search_iris.tmp', 'r').read().strip()
        f_q = open('/tmp/file/search_iris', 'w')
        f_q.write(f)
        f_q.close()
    except Exception as exc:
        pass
        
    try: 
        f_tmp = open('/tmp/file/search_quantenna.tmp', 'r')
        f_tmp = f.readlines()[2]
        f = open('/tmp/file/search_quantenna.tmp', 'r').read().strip()
        f_q = open('/tmp/file/search_quantenna', 'w')
        f_q.write(f)
        f_q.close()
       
    except Exception as exc:
        pass
        
def check_quan_wps():
    f = Get_quan_mac()
    wps_quantenna_ip=Get_default_quan_ip()
    wps_quantenna_request="http://"+wps_quantenna_ip+"/iris.php?iris_need_wps=1&iris_need_check_mac="+f
    #print wps_quantenna_request
    try:
        r = Get_request(wps_quantenna_request)
        return 1
    except Exception as exc:
        return 0
        
def call_to_push_wps():

    f = Get_quan_mac()
    wps_quantenna_ip=Get_default_quan_ip()
    wps_quantenna_request="http://"+wps_quantenna_ip+"/iris.php?iris_need_wps=1&iris_need_check_mac="+f
    #print wps_quantenna_request
    try:
        r = Get_request(wps_quantenna_request)
        if r == '1' :
            i_wps = 0
            while i_wps < 60:
                wps_quantenna_ip_state="http://"+wps_quantenna_ip+"/iris.php?iris_need_wps_state=1&iris_need_check_mac="+f
                #print wps_quantenna_ip_state
                try:
                    r_state = Get_request(wps_quantenna_ip_state)
                    #print r_state
                except Exception as exc:
                    #print 'can not link quan wps state'
                    pass

                if r_state == '2':
                    #print '***get wps**'
                    i_wps = 60
                    
                if r_state == '4':
                    #print '***no wps**'
                    i_wps = 60
              
                i_wps=i_wps+1

            #i=99
        if r != '1' :
            os.popen('madplay /root/audio/de/32_Error_mac_address.mp3 -o wave:- | aplay')
            #print 'mac address error'
    except Exception as exc:
        os.popen('madplay /root/audio/de/32_Can_not_find_my_wps.mp3 -o wave:- | aplay')
        #print 'can not link quan wps'
        #i=i+1
        
def check_quan_link(master_wifi_count):
    f = Get_quan_mac()
    state=0
    try:
        master_quantenna_ip=Get_default_quan_ip()
        master_quantenna_ip="http://"+master_quantenna_ip+"/iris.php?iris_need_count_assoc=1&iris_need_check_mac="+f+"&iris_need_check_ip="+master_quantenna_ip
        #print master_quantenna_ip
        r = requests.get(master_quantenna_ip,timeout=1)
        r = r.text
        r = r.strip()
        
        if master_wifi_count != r[1] and r[0] == 'm':
            r = r[1]
            master_wifi_count=r
            state=1
            return master_wifi_count ,state

    except Exception as exc:
        #print ("can not link this quan ip " ,master_quantenna_ip)
        pass
        
    return master_wifi_count ,state

def check_quan_wifi_connect(master_wifi_connect_state):
    f = Get_quan_mac()

    try:
        quantenna_ip=Get_default_quan_ip()
        quantenna_ip="http://"+quantenna_ip+"/iris.php?iris_need_connect_iris_state=1&iris_need_check_mac="+f
        #print quantenna_ip
        r = requests.get(quantenna_ip,timeout=1)
        r = r.text
        r = r.strip()
        
        if master_wifi_connect_state != r[0]  and r[0] == 'A':
            master_wifi_connect_state = r[0]
            os.popen("madplay /root/audio/de/33_The_connection_is_complete.mp3 -o wave:- | aplay")  
            return master_wifi_connect_state
            
        if master_wifi_connect_state != r[0]  and r[0] == 'N':
            master_wifi_connect_state = r[0]
            os.popen("madplay /root/audio/de/33_Leave_wifi.mp3 -o wave:- | aplay") 
            return master_wifi_connect_state
            
    except Exception as exc:
        #print ("can not link this quan ip " ,quantenna_ip)
        pass          

    return master_wifi_connect_state
    
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
        
def unicast_iris_ip(unicast_ip,key_word):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        PORT = 1060
        ip = 'd' + key_word + unicast_ip
        s.sendto( ip.encode('utf-8'), (unicast_ip, PORT))
    except Exception as exc:
        pass
        
def quantenna_connect_iris():

    f = Get_quan_mac()
    try:
        quantenna_ip=Get_default_quan_ip()
        quantenna_ip_connect_wifi="http://"+quantenna_ip+"/iris.php?iris_need_connect_iris=1&iris_need_check_mac="+f
        #print quantenna_ip_connect_wifi
        r = requests.get(quantenna_ip_connect_wifi,timeout=10)
        r = r.text
        r = r.strip()
        if r == '1':
            #print 'link quan wifi'  
            return 1 
        if r != '1':  
            #print 'can not link quan wifi' 
            return 0
    except Exception as exc:
        #print 'can not link quan wifi' 
        return 0
def call_to_party_mode_on():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    PORT = 1060
    ip = 'po' + Get_my_ip()
    brocast_ip = Get_brocast_ip()
    #network = '<broadcast>'
    s.sendto( ip.encode('utf-8'), (brocast_ip, PORT))
    

def call_to_party_mode_off():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    PORT = 1060
    ip = 'pf' + Get_my_ip()
    brocast_ip = Get_brocast_ip()
    #network = '<broadcast>'
    s.sendto( ip.encode('utf-8'), (brocast_ip, PORT))

        
def Announcement_Mode_On():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    PORT = 1060
    ip = 'ao' + Get_my_ip()
    brocast_ip = Get_brocast_ip()
    #network = '<broadcast>'
    s.sendto( ip.encode('utf-8'), (brocast_ip, PORT))

def Announcement_Mode_Off():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    PORT = 1060
    ip = 'af' + Get_my_ip()
    brocast_ip = Get_brocast_ip()
    #network = '<broadcast>'
    s.sendto( ip.encode('utf-8'), (brocast_ip, PORT))
        
def quantenna_wifi_down():

    ip_line_length=Get_all_quan_ip_length()
    i = 1 
    f = Get_quan_mac()
    while i <=  ip_line_length:
        try:
            quantenna_ip_tmp=Get_all_quan_ip(i)
            #print quantenna_ip_tmp
            quantenna_ip="http://"+quantenna_ip_tmp+"/iris.php?iris_need_black_assoc=1&iris_need_assoc_number="+str(i)+"&iris_need_check_mac="+f
            #print quantenna_ip
            r = int(Get_request(quantenna_ip))
            while  r > 0:
                quantenna_ip="http://"+quantenna_ip_tmp+"/iris.php?iris_need_black_assoc=1&iris_need_assoc_mac="+str(r)+"&iris_need_check_mac="+f
                #print quantenna_ip
                r_tmp = (Get_request(quantenna_ip))
                #print ('****Deal black***',r_tmp)
                j = 1
                while j <=  ip_line_length:
                    try:
                        quantenna_ip=Get_all_quan_ip(j)
                        quantenna_ip="http://"+quantenna_ip+"/iris.php?iris_need_black_assoc=1&iris_need_assoc_black="+r_tmp+"&iris_need_check_mac="+f
                        Get_request(quantenna_ip)
                        #print quantenna_ip

                    except Exception as exc:
                        pass
                        #print '******Some ip error*******'
                    j=j+1
                r=r-1
        except Exception as exc:
            #print '******Some ip error*******'
            pass
        i=i+1  

def quantenna_wifi_up():

    ip_line_length=Get_all_quan_ip_length()
    i = 1 
    f = Get_quan_mac()
    while i <=  ip_line_length:
        try:
            quantenna_ip=Get_all_quan_ip(i)
            quantenna_ip="http://"+quantenna_ip+"/iris.php?iris_need_white_assoc=1&iris_need_check_mac="+f
            #print quantenna_ip
            r = requests.get(quantenna_ip,timeout=5) 
        except Exception as exc:
            #print i
            pass
        i=i+1   

        

    

        
