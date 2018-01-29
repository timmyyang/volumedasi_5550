# -*- coding: utf-8 -*
import serial
import time
import os
import A3_1_PRINT

ser = serial.Serial("/dev/ttyS1", 115200)

#-----state led-----------
def MCU_Write_State_One_LED(pin):
    count_led=0
    
    if pin==1:
        while count_led<1:
            r=0;g=250;b=5
            if count_led == 1:
                r = 250 ;g = -10 ;b = -10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(0))
                time.sleep(0.02)#0.15  
            
            count_led += 1

    if pin==0:
        while count_led<1:
            r=250;g=-10;b=-10
            if count_led == 1:
                r = 0 ;g = 250 ;b = 10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(0))
                time.sleep(0.02)  
                         
            count_led += 1
            
    time.sleep(0.1)
    
def Write_State_One_LED(pin):
    try:
        f = open('/tmp/file/gpio/State_One_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
        
def Read_State_One_LED():
    return open('/tmp/file/gpio/State_One_LED','r').read().strip()

#-----alexa led-----------
def MCU_Write_Alexa_LED(pin):
    count_led=0
    
    if pin==1:
        while count_led<1:
            r=0;g=250;b=10
            if count_led == 1:
                r = 250 ;g = -10 ;b = -10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(0))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(loop_r))
                time.sleep(0.02)#0.15 
            
            count_led += 1
                
    if pin==0:
        while count_led<1:
            r=250;g=-10;b=-10
            if count_led == 1:
                r = 0 ;g = 250 ;b = 10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(0))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(loop_r))
                time.sleep(0.02)#0.15 
            
            count_led += 1
            
    time.sleep(0.1)
            
def MCU_Write_Alexa_LED_Flash():
    b=0;r=0;g=0
    for r in range(250,-25,-25):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(0))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r))
        time.sleep(0.03)
        
    for r in range(0,250,25):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(0))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r))
        time.sleep(0.03)#0.15 
        
    time.sleep(0.1)
    
def Write_Alexa_LED(pin):
    try:
        f = open('/tmp/file/gpio/Alexa_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
        
def Read_Alexa_LED():
    return open('/tmp/file/gpio/Alexa_LED','r').read().strip()
    
#-----iris led-----------

def MCU_Write_Iris_LED(pin):
    count_led=0
    
    if pin==1:
        while count_led<1:
            r=0;g=250;b=10
            if count_led == 1:
                r = 250 ;g = -10 ;b = -10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(loop_r/5))
                time.sleep(0.02)#0.15 
            
            count_led += 1
                
    if pin==0:
        while count_led<1:
            r=250;g=-10;b=-10
            if count_led == 1:
                r = 0 ;g = 250 ;b = 10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(loop_r/5))
                time.sleep(0.02)#0.15 
            
            count_led += 1
            
    time.sleep(0.1)
            
def MCU_Write_Iris_LED_Flash():
    b=0;r=0;g=0
    for r in range(250,-25,-25):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r/5))
        time.sleep(0.03)
        
    for r in range(0,250,25):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r/5))
        time.sleep(0.03)#0.15 
        
    time.sleep(0.1)
        
def MCU_Write_Iris_LED_Party_Mode():
    count_led=0
    while count_led<1:
        r=0;g=250;b=5
        if count_led == 1:
            r = 250 ;g = -5 ;b = -5;
        for loop_r in range(r,g,b):
            ser.write(chr(0x4C))#L
            ser.write('\x08')
            ser.write(chr(0x52))#R
            ser.write(chr(loop_r))
            ser.write(chr(0x47))#G
            ser.write(chr(0))
            ser.write(chr(0x42))#B
            ser.write(chr(0))
            time.sleep(0.02)#0.15 
        count_led += 1
        
    time.sleep(0.1)
        

def MCU_Write_Iris_LED_WAIT():
    b=0;r=0;g=0
    for r in range(250,-10,-10):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r/5))
        time.sleep(0.03)
    '''    
    for r in range(0,250,10):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r/5))
        if b>=1:
            b-=1
        time.sleep(0.03)#0.15 
    '''    
    time.sleep(0.1)
    
def MCU_Write_Iris_LED_IR():
    b=0;r=0;g=0
    for r in range(250,-50,-50):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r/5))
        time.sleep(0.03)
        
    for r in range(0,250,50):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r/5))
        time.sleep(0.03)#0.15 
        
    for r in range(250,-50,-50):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r/5))
        time.sleep(0.03)
        
    for r in range(0,250,50):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(0))
        ser.write(chr(0x42))#B
        ser.write(chr(r/5))
        time.sleep(0.03)#0.15 
        
    time.sleep(0.1)
        
def Write_Iris_LED(pin):
    try:
        f = open('/tmp/file/gpio/Iris_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
        
def Read_Iris_LED():
    return open('/tmp/file/gpio/Iris_LED','r').read().strip()

#-----power led-----------
def MCU_Write_Power_LED(pin):
    count_led=0
    
    if pin==3:
        while count_led<2:
            r=250;g=-25;b=-25
            if count_led == 1:
                r = 0 ;g = 250 ;b = 25;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(0))
                time.sleep(0.02)#0.15 
            
            count_led += 1     
            
        time.sleep(0.1)
    
    if pin==2:
        while count_led<1:
            r=0;g=250;b=10
            if count_led == 1:
                r = 250 ;g = -10 ;b = -10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(0))
                time.sleep(0.02)#0.15 
            
            count_led += 1     
            
        time.sleep(0.1)
    
    if pin==1:
        while count_led<2:
            r=0;g=250;b=10
            if count_led == 1:
                r = 250 ;g = -10 ;b = -10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(0))
                time.sleep(0.02)#0.15 
            
            count_led += 1     
            
        time.sleep(0.1)
                
    if pin==0:
        while count_led<1:
            r=250;g=-10;b=-10
            if count_led == 1:
                r = 0 ;g = 250 ;b = 10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(0))
                ser.write(chr(0x42))#B
                ser.write(chr(0))
                time.sleep(0.02)#0.15 
            
            count_led += 1  
            
        time.sleep(0.1)
    
def Write_Power_LED(pin):
    try:
        f = open('/tmp/file/gpio/Power_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass

def Read_Power_LED():
    return open('/tmp/file/gpio/Power_LED','r').read().strip()

#-----voip check-----------    
def Write_voip_state(value):
    try:
        f = open('/tmp/file/sound_busy_check','w')
        f.write(str(value))
        f.close()
    except Exception as exc:
        pass

def Read_voip_state():
    return open('/tmp/file/sound_busy_check','r').read().strip()
    
def Write_VOIP_LED(pin):
    try:
        f = open('/tmp/file/gpio/VOIP_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
    
def Read_VOIP_LED():
    return open('/tmp/file/gpio/VOIP_LED','r').read().strip()
    
def MCU_Write_VOIP_LED(pin):
    count_led=0
    
    if pin==1:
        while count_led<1:
            r=0;g=250;b=10
            if count_led == 1:
                r = 250 ;g = -10 ;b = -10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(loop_r))
                ser.write(chr(0x42))#B
                ser.write(chr(loop_r))
                time.sleep(0.02)#0.15 
            
            count_led += 1     
            
        time.sleep(0.1)
                
    if pin==0:
        while count_led<1:
            r=250;g=-10;b=-10
            if count_led == 1:
                r = 0 ;g = 250 ;b = 10;
            for loop_r in range(r,g,b):
                ser.write(chr(0x4C))#L
                ser.write('\x08')
                ser.write(chr(0x52))#R
                ser.write(chr(loop_r))
                ser.write(chr(0x47))#G
                ser.write(chr(loop_r))
                ser.write(chr(0x42))#B
                ser.write(chr(loop_r))
                time.sleep(0.02)#0.15 
            
            count_led += 1  
            
        time.sleep(0.1)
        
def MCU_Write_VOIP_LED_Flash():
    b=0;r=0;g=0
    
    for r in range(0,250,25):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(r))
        ser.write(chr(0x42))#B
        ser.write(chr(r))
        time.sleep(0.03)#0.15 
        
    for r in range(250,-25,-25):
        ser.write(chr(0x4C))#L
        ser.write('\x08')
        ser.write(chr(0x52))#R
        ser.write(chr(r))
        ser.write(chr(0x47))#G
        ser.write(chr(r))
        ser.write(chr(0x42))#B
        ser.write(chr(r))
        time.sleep(0.03)
        

        
    time.sleep(0.1)
    
def Write_VOIP_LED(pin):
    try:
        f = open('/tmp/file/gpio/VOIP_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass

def Read_VOIP_LED():
    return open('/tmp/file/gpio/VOIP_LED','r').read().strip()
                    
#-----volume check----------- 
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
    f_1 = open('/root/file/iris.conf','w')
    for i in range(0,len(f)):
        f_1.write(str(f[i])+'\n')
    
def config_volume(value,check):
    volume_r = get_iris_conf('volume_set')
    if int(volume_r)>=0 and int(volume_r)<10 and check==1:
        volume_r = int(volume_r) + value
    elif int(volume_r)>0 and int(volume_r)<=10 and check==0:
        volume_r = int(volume_r) - value
    os.popen("amixer cset numid=1,iface=MIXER,name='MaxxVolume Control' "+str(volume_r))
    volume_w = open('/root/file/volume_set','w')
    volume_w.write(str(volume_r))
    set_iris_conf('volume_set',volume_r)
    volume_w.close()
    return int(volume_r)

#-----phone----------- 
def voip(call_now):
    buffer = []
    location = 0 ; ser_time = 0 ; sound_kill=0;
    while True:
        count = ser.inWaiting()
        voip_talk_check = open('/tmp/file/sound_busy_check', 'r').read().strip()
        if count != 0 :
            recv = ser.read(count)
            if recv[0]=='T' and ser_time > 2:
                if sound_kill==0:
                    os.popen('killall -9 madplay aplay')
                    word_clean()
                    sound_kill=1
                if recv[3]=='1':
                    os.popen('madplay /root/audio/voip/voip2.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('1')
                elif recv[3]=='2':
                    os.popen('madplay /root/audio/voip/voip2.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('2')
                elif recv[3]=='3':
                    os.popen('madplay /root/audio/voip/voip2.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('3')
                elif recv[3]=='4':
                    os.popen('madplay /root/audio/voip/voip3.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('4')
                elif recv[3]=='5':
                    os.popen('madplay /root/audio/voip/voip3.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('5')
                elif recv[3]=='6':
                    os.popen('madplay /root/audio/voip/voip3.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('6')
                elif recv[3]=='7':
                    os.popen('madplay /root/audio/voip/voip4.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('7')
                elif recv[3]=='8':
                    os.popen('madplay /root/audio/voip/voip4.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('8') 
                elif recv[3]=='9':
                    os.popen('madplay /root/audio/voip/voip4.mp3 -o wave:- - | aplay -M &')
                    buffer.append(recv[3]) 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('9')
                elif recv[3]=='A':
                    MCU_Write_VOIP_LED(0)
                    os.popen('echo b | telnet localhost 5555')
                    os.popen('madplay /root/audio/voip/voip7.mp3 -o wave:- - | aplay -M &')
                    Write_voip_state(9)
                    word_clean()
                    time.sleep(1)
                    break
                elif recv[3]=='B':
                    os.popen('madplay /root/audio/voip/voip5.mp3 -o wave:- - | aplay -M &')
                    buffer.append('#') 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('#')
                elif recv[3]=='C':
                    os.popen('madplay /root/audio/voip/voip5.mp3 -o wave:- - | aplay -M &')
                    buffer.append('0') 
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('0')
                elif recv[3]=='D':
                    os.popen('madplay /root/audio/voip/voip5.mp3 -o wave:- - | aplay -M &')
                    buffer.append('*')  
                    ser.write(chr(0x4F))#O
                    ser.write('\x04')
                    ser.write(chr(location))
                    ser.write('*')
                elif recv[3]=='E' and location !=0 and call_now==0 and voip_talk_check !='3' :
                    MCU_Write_VOIP_LED_Flash()
                    bmp_set('calling')
                    os.popen('echo b | telnet localhost 5555')
                    time.sleep(1)
                    number = "".join(buffer)
                    number = 'echo d ' + number + ' | telnet localhost 5555'
                    os.popen(number)
                    call_now=1
                
                location += 1
                ser_time = 0
                
            if recv[0]=='B' and ser_time>2:
                if recv[3]=='1':
                    config_volume(1,1)
                if recv[3]=='3':
                    config_volume(1,0)
                ser_time = 0
                
        if voip_talk_check == '3' and call_now==1:
            Write_VOIP_LED(1)
            call_now=2
        if voip_talk_check == '0':
            os.popen('echo b | telnet localhost 5555')
            os.popen('madplay /root/audio/voip/voip7.mp3 -o wave:- - | aplay -M &')
            Write_VOIP_LED(0)
            Write_voip_state(9)
            word_clean()
            time.sleep(1)
            break

        time.sleep(0.02)
        ser_time += 1 
        
def bmp_file_get():
    bmp_word_value = open('/tmp/file/bmp_set', 'r').read().strip()
    return  bmp_word_value
    
def bmp_file_set(value):
    try:
        f = open('/tmp/file/bmp_set','w')
        f.write(str(value))
        f.close()
    except Exception as exc:
        pass    
    
def bmp_set(word):
    word_clean()
    try:
        bmp_word = A3_1_PRINT.Print_oled(word)
        if len(bmp_word) == 512 :
            ser.write(chr(0x6F))#o
            ser.write('\x83')#131
            ser.write('\x01')#column 1
            count = 0
            for count in range(0,128,1):
                ser.write(chr(bmp_word[count]))
                
            time.sleep(0.02)
            ser.write(chr(0x6F))#o
            ser.write('\x83')#131
            ser.write('\x02')#column 2
            for count in range(128,256,1):
                ser.write(chr(bmp_word[count]))

            time.sleep(0.02)
            ser.write(chr(0x6F))#o
            ser.write('\x83')#131
            ser.write('\x03')#column 3
            for count in range(256,384,1):
                ser.write(chr(bmp_word[count]))

            time.sleep(0.02)
            ser.write(chr(0x6F))#o
            ser.write('\x83')#131
            ser.write('\x04')#column 4
            for count in range(384,512,1):
                ser.write(chr(bmp_word[count]))
                
            time.sleep(0.1)
        
    except Exception as exc:
        pass   
        
def word_clean():
    ser.write(chr(0x4F))#O
    ser.write('\x03')
    ser.write(chr(0x63))#c
    time.sleep(0.1)
    
def touch_led(pin):
    if pin==1:
        ser.write(chr(0x6C))#l
        ser.write('\x0A')#10
        ser.write(chr(0x54))#T
        ser.write('\x01')#1
        ser.write(chr(0x57))#W
        ser.write('\x00')#0
        ser.write(chr(0x42))#B
        ser.write('\x00')#0
        ser.write(chr(0x41))#A
        ser.write('\x00')#0
        
    if pin==0:
        ser.write(chr(0x6C))#l
        ser.write('\x0A')#10
        ser.write(chr(0x54))#T
        ser.write('\x00')#0
        ser.write(chr(0x57))#W
        ser.write('\x00')#0
        ser.write(chr(0x42))#B
        ser.write('\x00')#0
        ser.write(chr(0x41))#A
        ser.write('\x00')#0
        
    time.sleep(0.1)
        
def ir_file_get():
    bmp_word_value = open('/tmp/file/ir_set', 'r').read().strip()
    return  bmp_word_value
    
def ir_file_set(value):
    try:
        f = open('/tmp/file/ir_set','w')
        f.write(str(value))
        f.close()
    except Exception as exc:
        pass 
        
def ir_set(value , toggle_bit_for_voice):
    ir_range=0 ; ser_time = 0 ; timer=0; toogle_bit = toggle_bit_for_voice ;push_count=5
    toogle_bit -= 1 
    toogle_bit = abs(toogle_bit)
    if value=='power':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x01))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='up':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x0E))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='left':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x10))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='ok':
        for ir_range in range(0,15,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x11))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='right':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x12))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='down':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x14))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='play':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x36))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='back':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x1B))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='volumeadd':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x16))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='volumedown':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x1A))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='volumemute':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x1A))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='programadd':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x19))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='programdown':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x1D))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='0':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x2B))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='1':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x1E))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='2':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x1F))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='3':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x20))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='4':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x22))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='5':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x23))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='6':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x24))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='7':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x26))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='8':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x27))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='9':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x28))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
    if value=='49':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x22))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
        time.sleep(0.1)
        toogle_bit -= 1 
        toogle_bit = abs(toogle_bit)
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x28))
            ser.write(str(toogle_bit))
            time.sleep(0.02)        
    if value=='50':
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x23))
            ser.write(str(toogle_bit))
            time.sleep(0.02)
        time.sleep(0.1)
        toogle_bit -= 1 
        toogle_bit = abs(toogle_bit)
        for ir_range in range(0,push_count,1):
            ser.write(chr(0x49))#I
            ser.write('\x04')
            ser.write(chr(0x2B))
            ser.write(str(toogle_bit))
            time.sleep(0.02)    

    
    time.sleep(0.1)
    return toogle_bit
    
def ir_set_touch():
    ir_range=0 ; ser_time = 0 ; timer=0; toogle_bit = 1 ;push_count=5
    while True:
        count = ser.inWaiting()
        if count != 0 :
            recv = ser.read(count)
            if recv[0]=='T' and ser_time > 2:
                '''
                for ir_range in range(0,10,1):
                    ser.write(chr(0x49))#I
                    ser.write('\x04')
                    ser.write(chr(0x00))
                    ser.write(str(toogle_bit))
                    time.sleep(0.02)
                toogle_bit = 1
                '''
                toogle_bit -= 1 
                toogle_bit = abs(toogle_bit)
                ir_range=0
                if recv[3]=='1': #power
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x01))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='2': #up
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x0E))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='3':
                        time.sleep(0.02)
                elif recv[3]=='4': #left
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x10))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='5': #ok
                    for ir_range in range(0,15,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x11))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='6': #right
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x12))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='7': #volume up
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x16))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='8': #down
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x14))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='9': #program add
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x19))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='A':
                        MCU_Write_Power_LED(0)
                        break
                elif recv[3]=='B': #program down
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x1D))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='C': # back
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x1B))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='D': #volume down
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x1A))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='E':
                        time.sleep(0.02)
                        
                MCU_Write_Power_LED(3)        
                timer = 0
                ser_time = 0
                
        elif timer==100:
            MCU_Write_Power_LED(0)
            word_clean()
            break
                        
        time.sleep(0.1)
        timer+=1
        ser_time += 1 
        
def ir_set_touch_2():
    ir_range=0 ; ser_time = 0 ; timer=0; toogle_bit = 1 ;push_count = 5
    while True:
        count = ser.inWaiting()
        if count != 0 :
            recv = ser.read(count)
            if recv[0]=='T' and ser_time > 2:
                '''
                for ir_range in range(0,10,1):
                    ser.write(chr(0x49))#I
                    ser.write('\x04')
                    ser.write(chr(0x00))
                    ser.write(str(toogle_bit))
                    time.sleep(0.02)
                toogle_bit = 1
                '''
                toogle_bit -= 1 
                toogle_bit = abs(toogle_bit)
                ir_range=0
                if recv[3]=='1': #1
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x1E))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='2': #2
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x1F))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='3':
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x20))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='4': #4
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x22))#I
                        ser.write('\x04')
                        ser.write(chr(0x22))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='5': #5
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x23))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='6': #6
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x24))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='7': #7
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x26))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='8': #8
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x27))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='9': #9
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x28))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='A':
                        MCU_Write_Power_LED(0)
                        break
                elif recv[3]=='B': #program down
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x12))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='C': # 0
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x1B))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='D': #left
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x10))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                elif recv[3]=='E': #OK
                    for ir_range in range(0,push_count,1):
                        ser.write(chr(0x49))#I
                        ser.write('\x04')
                        ser.write(chr(0x11))
                        ser.write(str(toogle_bit))
                        time.sleep(0.02)
                        
                MCU_Write_Power_LED(3)        
                timer = 0
                ser_time = 0
                
                
        elif timer==100:
            MCU_Write_Power_LED(0)
            word_clean()
            break
                        
        time.sleep(0.1)
        timer+=1
        ser_time += 1 

def main():
    #init gpio
    Write_State_One_LED(0)
    Write_Alexa_LED(0)
    Write_Iris_LED(0)
    Write_Power_LED(1)
    Write_VOIP_LED(0)
    bmp_set('tti')
    bmp_set('tti')
    #init voip
    Write_voip_state(9)
    Voip_bmp_tmp = 0
    #init volume
    volume = get_iris_conf('volume_set')
    os.popen("amixer cset numid=1,iface=MIXER,name='MaxxVolume Control' "+volume)
    #os.popen("madplay -r /root/audio/en/start_music.mp3 -o wave:- | aplay - M &")
    #init bmp_word
    bmp_file_set(0)
    
    #init ir
    ir_file_set(0)

    #get led file
    Morse = Read_Power_LED()
    Iris_LED_file = Read_Iris_LED()
    Alexa_LED_file = Read_Alexa_LED()
    State_One_file = Read_State_One_LED()
    VOIP_LED_file  = Read_VOIP_LED()
    Morse_tmp = Morse
    Iris_LED_file_tmp = Iris_LED_file
    Alexa_LED_file_tmp = Alexa_LED_file
    State_One_file_tmp = State_One_file
    VOIP_LED_file_tmp = VOIP_LED_file

    #wait main process start
    while True:
        Morse = Read_Power_LED()
        MCU_Write_Power_LED(1)
        if Morse == '0':
            Write_Power_LED(0)
            break

    main_time = 0;touch_led_time = 101;touch_count = 0;touch_location = 0;bmp_value_tmp = '0';toggle_bit_for_voice = 0;touch_bright = 0;
    touch_buffer = []
    while True:
            time.sleep(0.1)
            bmp_value = bmp_file_get()
            ir_value = ir_file_get()
            #---------voip----------
            voip_talk_check = open('/tmp/file/sound_busy_check', 'r').read().strip()
            if voip_talk_check == '4' and Voip_bmp_tmp == 0:
                Write_VOIP_LED(2)
                os.popen('madplay /root/audio/en/ring.mp3 -r -o wave:- - | aplay -M &')
                bmp_set('in_come_call')
                Voip_bmp_tmp = 1
                    
            elif voip_talk_check == '3':
                bmp_set('voip')
                os.popen('echo a | telnet localhost 5555')
                voip(1)
                Voip_bmp_tmp = 0
                bmp_value = bmp_file_get()
                if bmp_value != '0':
                    bmp_set(bmp_value)
                    
            if voip_talk_check == '0':
                Voip_bmp_tmp = 0
                Write_voip_state(9)
                
            #---------uart----------
            count = ser.inWaiting()
            if count != 0:
                recv = ser.read(count)
                if recv[0]=='B' and main_time > 2:
                    if recv[3]=='1' :
                            d = Read_State_One_LED()        
                            if d == '0' :
                                    Write_State_One_LED(1)
                            if d == '1' :
                                    Write_State_One_LED(0)
                            
                    if recv[3]=='2':
                        volume_r = config_volume(1,1)
                        bmp_set('volume%i'%(volume_r))
                        touch_led_time = 80
                    if recv[3]=='3':
                        volume_r = config_volume(1,0)
                        bmp_set('volume%i'%(volume_r))
                        touch_led_time = 80
                        
                    main_time = 0
                    
                #---------voip----------   
                if recv[0]=='T' and main_time > 2 :
                    touch_led(1)
                    if touch_bright == 0:
                        touch_bright = 1
                    elif touch_bright == 1:
                        touch_word = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'B', 'C' , 'D']
                        if recv[3] in touch_word :
                            if touch_location==0:
                                word_clean()
                            if touch_location==11:
                                touch_location=0
                                word_clean()
                            ser.write(chr(0x4F))#O
                            ser.write('\x04')
                            ser.write(chr(touch_location))
                            if recv[3] == 'B':
                                ser.write('#')
                            elif recv[3] == 'C':
                                ser.write('0')
                            elif recv[3] == 'D':
                                ser.write('*')
                            else:
                                ser.write(recv[3])
                            touch_location += 1
                            time.sleep(0.1)
                        
                        
                        if recv[3]=='E' and voip_talk_check == '9' and State_One_file_tmp == '0' and Iris_LED_file_tmp == '0':  
                            MCU_Write_VOIP_LED(1)
                            Write_voip_state(8)
                            os.popen('madplay -r /root/audio/voip/voip6.mp3 -o wave:- - | aplay -M &')
                            bmp_set('voip')
                            voip(0)
                            if bmp_value != '0':
                                bmp_set(bmp_value)
                        elif recv[3]=='E' and voip_talk_check == '4':
                            os.popen('killall -9 madplay aplay')
                            MCU_Write_VOIP_LED(1)
                            bmp_set('voip')
                            os.popen('echo a | telnet localhost 5555')
                            voip(1)
                            Voip_bmp_tmp = 0
                            if bmp_value != '0':
                                bmp_set(bmp_value)
                        elif recv[3]=='A' and voip_talk_check == '4':
                            os.popen('killall -9 madplay aplay')
                            os.popen('echo b | telnet localhost 5555')
                            Write_voip_state(9)
                            MCU_Write_VOIP_LED(0)
                            if bmp_value != '0':
                                bmp_set(bmp_value)
                                
                        elif recv[3]=='A' and voip_talk_check == '1':
                            os.popen('echo b | telnet localhost 5555')
                            Write_voip_state(9)
                            MCU_Write_VOIP_LED(0)
                            if bmp_value != '0':
                                bmp_set(bmp_value)
                                
                        elif recv[3]=='A' :
                            touch_location=0;touch_count = 0
                            if bmp_value != '0':
                                bmp_set(bmp_value)
                            
                        #---------IR---------- 
                        elif recv[3]=='B':
                            touch_count += 13
                        elif recv[3]=='1':
                            touch_count += 1 
                        elif recv[3]=='2':
                            touch_count += 2 
                        else:
                            touch_count = 0
                            
                        if touch_count==16:
                            bmp_set('controller')
                            MCU_Write_Power_LED(2)
                            ir_set_touch()
                            touch_location=0;touch_count = 0
                            if bmp_value != '0':
                                bmp_set(bmp_value)
                                
                        elif touch_count==17:
                            bmp_set('controller')
                            MCU_Write_Power_LED(2)
                            ir_set_touch_2()
                            touch_location=0;touch_count = 0
                            if bmp_value != '0':
                                bmp_set(bmp_value)  
                                
                    touch_led_time = 0        
                    main_time = 0 
                    
                    
            if bmp_value != '0' and bmp_value != bmp_value_tmp:
                bmp_set(bmp_value)
                bmp_value_tmp = bmp_value
                #bmp_file_set(0)
            
            if ir_value != '0':
                toggle_bit_for_voice = ir_set(ir_value , toggle_bit_for_voice)
                ir_file_set(0)
                    
            if touch_led_time == 100 or touch_led_time > 1000000:
                touch_led(0)
                touch_led_time = 101;touch_location = 0;touch_count = 0;touch_bright = 0;                
                if bmp_value != '0':
                    bmp_set(bmp_value)
                else :
                    word_clean()
                           
            main_time += 1   
            touch_led_time += 1
            #---------file----------
            
            Morse = Read_Power_LED()
            if Morse== '1':
                while True:
                    Morse = Read_Power_LED()
                    MCU_Write_Power_LED(1)
                    if Morse == '0':
                        MCU_Write_Power_LED(0)
                        break
                                          
            Iris_LED_file = Read_Iris_LED()
            if Iris_LED_file == '0' and Iris_LED_file != Iris_LED_file_tmp:
                Iris_LED_file_tmp = Iris_LED_file
                MCU_Write_Iris_LED(0)
            if Iris_LED_file == '1' and Iris_LED_file != Iris_LED_file_tmp and State_One_file == '0':
                Iris_LED_file_tmp = Iris_LED_file
                MCU_Write_Iris_LED(1)
            if Iris_LED_file == '2' :
                Iris_LED_file_tmp = Iris_LED_file
                MCU_Write_Iris_LED_Flash()
            if Iris_LED_file == '3' and Iris_LED_file != Iris_LED_file_tmp :
                Iris_LED_file_tmp = Iris_LED_file
                MCU_Write_Iris_LED_Party_Mode()
            if Iris_LED_file == '4' and Iris_LED_file != Iris_LED_file_tmp:
                Iris_LED_file_tmp = Iris_LED_file
                #MCU_Write_Iris_LED_WAIT()
            if Iris_LED_file == '5' and Iris_LED_file != Iris_LED_file_tmp:
                Iris_LED_file_tmp = Iris_LED_file  
                MCU_Write_Iris_LED_IR()

                
            Alexa_LED_file = Read_Alexa_LED()
            if Alexa_LED_file == '0' and Alexa_LED_file != Alexa_LED_file_tmp :
                Alexa_LED_file_tmp = Alexa_LED_file
                MCU_Write_Alexa_LED(0)
            if Alexa_LED_file == '1' and Alexa_LED_file != Alexa_LED_file_tmp and State_One_file == '0':
                Alexa_LED_file_tmp = Alexa_LED_file
                MCU_Write_Alexa_LED(1)
            if Alexa_LED_file == '2' :
                Alexa_LED_file_tmp = Alexa_LED_file
                MCU_Write_Alexa_LED_Flash()
                
            State_One_file = Read_State_One_LED()
            if State_One_file == '0' and State_One_file != State_One_file_tmp :
                State_One_file_tmp = State_One_file
                MCU_Write_State_One_LED(0)
            if State_One_file == '1' and State_One_file != State_One_file_tmp and Iris_LED_file == '0'  and Alexa_LED_file == '0':
                State_One_file_tmp = State_One_file
                MCU_Write_State_One_LED(1) 
                
            VOIP_LED_file = Read_VOIP_LED()
            if VOIP_LED_file == '0' and VOIP_LED_file!= VOIP_LED_file_tmp :
                VOIP_LED_file_tmp = VOIP_LED_file
                MCU_Write_VOIP_LED(0)
            if VOIP_LED_file == '1' and VOIP_LED_file!= VOIP_LED_file_tmp : 
                VOIP_LED_file_tmp = VOIP_LED_file
                MCU_Write_VOIP_LED(1)
            if VOIP_LED_file == '2' : 
                VOIP_LED_file_tmp = VOIP_LED_file
                MCU_Write_VOIP_LED_Flash()

        
if __name__ == '__main__':
    #try:
        main()
    #except KeyboardInterrupt:
    #    if ser != None:
    #        ser.close()
            
                
