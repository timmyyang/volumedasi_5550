import mraa
import time
import os

def Write_State_One_LED(pin):
    try:
        f = open('/tmp/file/gpio/State_One_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
        
def Write_Alexa_LED(pin):
    try:
        f = open('/tmp/file/gpio/Alexa_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
        
def Write_Iris_LED(pin):
    try:
        f = open('/tmp/file/gpio/Iris_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
        
def Write_Power_LED(pin):
    try:
        f = open('/tmp/file/gpio/Power_LED','w')
        f.write(str(pin))
        f.close()
    except Exception as exc:
        pass
        
def Start_button_gpio_check():
    a = Start_Button.read()
    if a == 1 :
            d = State_One_LED.read()          
            if d == 1 :
                    State_One_LED.write(0)
                    Write_State_One_LED(0)
                    #print("State_LED_ON")
            if d == 0 :
                    State_One_LED.write(1)
                    Write_State_One_LED(1)
                    #print("State_LED_OFF") 

def config_volume(value):
    volume_r = open('/root/file/volume_set.txt', 'r').read().strip()
    if int(volume_r)>0 and int(volume_r)<11:
        volume_r = int(volume_r) + value
    os.popen("amixer cset numid=2,iface=MIXER,name='MaxxVolume Control' "+str(volume_r))
    volume_w = open('/root/file/volume_set.txt','w')
    volume_w.write(str(volume_r))
    volume_w.close()
    time.sleep(0.5)


#inital button
Start_Button = mraa.Gpio(13)
Volume_Down_Button = mraa.Gpio(12)
Volume_Up_Button = mraa.Gpio(45)
Start_Button.dir(mraa.DIR_IN)
Volume_Down_Button.dir(mraa.DIR_IN)
Volume_Up_Button.dir(mraa.DIR_IN)

#inital led
State_One_LED = mraa.Gpio(17)
Power_LED = mraa.Gpio(44)
Alexa_LED = mraa.Gpio(46)
Iris_LED = mraa.Gpio(16)
State_One_LED.dir(mraa.DIR_OUT)
Power_LED.dir(mraa.DIR_OUT)
Alexa_LED.dir(mraa.DIR_OUT)
Iris_LED.dir(mraa.DIR_OUT)
State_One_LED.write(1)
Power_LED.write(0)
Alexa_LED.write(1)
Iris_LED.write(1)

#inital led file
Write_State_One_LED(2)
Write_Alexa_LED(2)
Write_Iris_LED(2)
Write_Power_LED(2)

#get led file
Morse = open('/tmp/file/gpio/Power_LED','r').read().strip()
Iris_LED_file = open('/tmp/file/gpio/Iris_LED','r').read().strip()
Alexa_LED_file = open('/tmp/file/gpio/Alexa_LED','r').read().strip()
State_One_file = open('/tmp/file/gpio/State_One_LED','r').read().strip()
Morse_tmp = Morse
Iris_LED_file_tmp = Iris_LED_file
Alexa_LED_file_tmp = Alexa_LED_file
State_One_file_tmp = State_One_file

#wait main process start
while True:
    Morse = open('/tmp/file/gpio/Power_LED','r').read().strip()
    Iris_LED.write(0)
    time.sleep(0.3)
    Iris_LED.write(1)
    time.sleep(0.3)
    if Morse == '1':
        Power_LED.write(0)
        Write_Power_LED(0)
        break

while True:
    try:
        time.sleep(0.3)
        
        a = Start_Button.read()
        if a == 1 :
                d = State_One_LED.read()          
                if d == 1 :
                        State_One_LED.write(0)
                        Write_State_One_LED(0)
                        State_One_file_tmp = '0'
                        #print("State_LED_ON")
                if d == 0 :
                        State_One_LED.write(1)
                        Write_State_One_LED(1)
                        State_One_file_tmp = '1'
                        #print("State_LED_OFF")   
                        
                time.sleep(1) 
                
        b = Volume_Down_Button.read()
        if b == 1:
            config_volume(1)
        if c == 0:
            config_volume(-1)
            
        Morse = open('/tmp/file/gpio/Power_LED','r').read().strip()
        if Morse== '1':
            while True:
                Morse = open('/tmp/file/gpio/Power_LED','r').read().strip()
                Iris_LED.write(1)
                time.sleep(0.1)
                Iris_LED.write(0)
                time.sleep(0.1)
                if Morse == '0':
                    break
                    
        Iris_LED_file = open('/tmp/file/gpio/Iris_LED','r').read().strip()
        if Iris_LED_file == '0' and Iris_LED_file != Iris_LED_file_tmp:
            Iris_LED_file_tmp = Iris_LED_file
            Iris_LED.write(0)
        if Iris_LED_file == '1' and Iris_LED_file != Iris_LED_file_tmp:
            Iris_LED_file_tmp = Iris_LED_file
            Iris_LED.write(1)
        if Iris_LED_file == '2' and Iris_LED_file != Iris_LED_file_tmp:
            while True:
                Iris_LED_file = open('/tmp/file/gpio/Iris_LED','r').read().strip()
                Iris_LED.write(1)
                Start_button_gpio_check()
                time.sleep(0.5)
                Iris_LED.write(0)
                Start_button_gpio_check()
                time.sleep(0.5)
                if Iris_LED_file == '0':
                    Iris_LED_file_tmp = Iris_LED_file
                    State_One_LED.write(1)
                    State_One_file_tmp = '1'
                    break   
            
        #Alexa_LED_file = open('/tmp/file/gpio/Alexa_LED','r').read().strip()
                    
        State_One_file = open('/tmp/file/gpio/State_One_LED','r').read().strip()
        if State_One_file == '0' and State_One_file != State_One_file_tmp:
            State_One_file_tmp = State_One_file
            State_One_LED.write(0)
        if State_One_file == '1' and State_One_file != State_One_file_tmp:
            State_One_file_tmp = State_One_file
            State_One_LED.write(1)
    except Exception as exc:
        time.sleep(1)
        pass
            
                
