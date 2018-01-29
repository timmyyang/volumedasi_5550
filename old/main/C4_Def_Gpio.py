def Check_State_One_LED():
    try:
        State_One_LED = open('/tmp/file/gpio/State_One_LED','r').read().strip()
    except Exception as exc:
        State_One_LED = 2
    State_One_LED = int(State_One_LED)
    return State_One_LED
    
def Write_State_One_LED(pin):
    try:
        f = open('/tmp/file/gpio/State_One_LED','w')
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
  
                    
