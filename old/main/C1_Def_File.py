# -*- coding: UTF-8 -*-

csport_mapping = {
    0 : "/usr/bin/Trigger.bin",
    1 : "TurnOnTheTv"
}

csport_mapping_de = {
    0 : "/usr/bin/Trigger.bin",
    1 : "TurnOnTheTv"
}

clistener_mapping = {
    0 : "/usr/bin/main",
    1 : "/usr/bin/controller",
    2 : "/usr/bin/radio",
    3 : "/usr/bin/Andromeda",
    4 : "/usr/bin/go_alexa_go_iris" ,
    5 : "/usr/bin/device",
    6 : "/usr/bin/phone"
}

clistener_mapping_de = {
    0 : "/usr/bin/Command_0407",
    1 : "/usr/bin/Command_0407"
}

device_list = {
    0 : 0 ,
    1 : 1 ,
    2 : 2 ,
    3 : 3 ,
    4 : 0 ,
    5 : 1 ,
    6 : 2 ,
    7 : 3 ,
    8 : 4 ,
    9 : 4 
}

def cyberon_file(lan,main,sub):
    if lan == 'EN':
        if main == 0:
            return csport_mapping[sub]
        if main == 1:
            return clistener_mapping[sub]
            
    if lan == 'DE':
        if main == 0:
            return csport_mapping_de[sub]
        if main == 1:
            return clistener_mapping_de[sub]

def get_iris_conf(key):
    f = open('/root/file/iris.conf', 'r')
    f = f.read().strip().split('\n')
    if key == 'language':
        value=f[0].split('=')
    if key == 'volume_set':
        value=f[1].split('=')
    if key == 'master_quantenna_mac':
        value=f[2].split('=')
    if key == 'default_quantenna_ip':
        value=f[3].split('=')
    if key == 'search_quantenna':
        value=f[4].split('=')
    if key == 'time':
        value=f[5].split('=')
    if key == 'snapclient':
        value=f[6].split('=')
    if key == 'radio1':
        value=f[7].split('=')
    if key == 'radio2':
        value=f[8].split('=')
    if key == 'radio3':
        value=f[9].split('=')
    if key == 'Andromeda_ID':
        value=f[10].split('=')
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
    f_1 = open('/root/file/iris.conf','w')
    for i in range(0,len(f)):
        f_1.write(str(f[i])+'\n')
            
def choice_file_get(file):
    f = open(file, 'r').read().strip()
    return f
            
def choice_file_set(file,word):
    f = open(file,'w')
    f.write(word)
    f.close()    
    
def choice_file_copy(tmp_file,file):
    f = open(tmp_file, 'r').read().strip()
    f_q = open(file, 'w')
    f_q.write(f)
    f_q.close()
    
def choice_file_length(file):  
    myfile = open(file) 
    lines = len(myfile.readlines()) 
    return lines      

###############取得CYBERON之值####################

def cyberon_get():
    f = open('/tmp/file/cspotter', 'r').read().strip()
    return f

def clisten_get():
    f = open('/tmp/file/clisten', 'r').read().strip()
    return f
###############取得ALEXA狀態####################
def alexa_control_get():
    f = open('/tmp/file/alexa_control', 'r').read().strip()
    return f   

def alexa_control_set():
    f = open('/tmp/file/alexa_control','w')
    f.write('1')
    f.close()     
    
def button_alexa_to_reset():
    f = open('/tmp/file/alexa_control','w')
    f.write('0')
    f.close()     
    
###############取得音樂大小#######################
def volume_get():
    f = open('/root/file/volume_set', 'r')
    f = f.read()
    f = f.strip()
    return f

###############儲存音樂大小#######################    
def volume_set(q):
    q = str(q)
    f = open('/root/file/volume_set','w')
    f.write(q)
    f.close()

###############清除cyberon#######################        
def clear_cyberon():
    f = open('/tmp/file/clisten','w')
    f.write('0')
    f.close()
    
def clear_cyberon_cspotter():
    f = open('/tmp/file/cspotter','w')
    f.write('0')
    f.close()

###############音樂暫停##########################      
def music_pause():
    f = open('/tmp/file/snapclient','w')
    f.write('0')
    f.close()

###############音樂開始##########################
def music_start():
    f = open('/tmp/file/snapclient','w')
    f.write('1')
    f.close()
    
###############偵測設備##########################
def device_state():
    f = open('/tmp/file/device','r').read().strip()
    return f
    
def device_save(set_id):
    f_tmp = open('/tmp/file/device','r').read().strip()
    if set_id <4 :
        f_tmp = list(f_tmp)
        f_tmp[device_list[set_id]]= '1'
        f_tmp = ''.join(f_tmp)
    if set_id >=4 and set_id <8:
        f_tmp = list(f_tmp)
        f_tmp[device_list[set_id]]= '0'
        f_tmp = ''.join(f_tmp)
    #if set_id ==8 :
    #    f_tmp = '11111'
    #if set_id ==9:
    #    f_tmp = '00000'
        
    f = open('/tmp/file/device','w')
    f.write(f_tmp)
    f.close()
    

###############取得STREAM IP##########################    
def Get_stream_ip():
    f = open('/tmp/file/stream_check')
    f = f.readlines()[1]
    f = f.strip()
    return f
    
def Get_stream_state():
    f = open('/tmp/file/stream_check')
    f = f.readlines()[0]
    f = f.strip()
    return f
    
###############get voip##########################  
def Get_voip_state():
    f = open('/tmp/file/sound_busy_check', 'r').read().strip()
    return f
    
###########set bmp word value#####################
def bmp_file_set(value):
    f = open('/tmp/file/bmp_set','w')
    f.write(str(value))
    f.close() 
    
def bmp_file_get():
    f = open('/tmp/file/bmp_set','r').read().strip()
    return f

###########ir file set#####################
def ir_file_set(value):
    f = open('/tmp/file/ir_set','w')
    f.write(str(value))
    f.close()
    
###########angle get#####################   
def angle_get():
    f = open('/tmp/file/angle','r').read().strip()
    return f
    
