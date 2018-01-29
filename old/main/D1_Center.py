# -*- coding: UTF-8 -*-
import time
import C1_Def_File,C4_Def_Gpio,C8_Def_Skill,C7_Def_Talk_list,C7_1_Def_Talk_list

def check_language(lan):
    language = C1_Def_File.get_iris_conf(lan)
    #C8_Def_Skill.Center_need_to_start_cyberon(language,1,0) #inital cyberon because first start it is too slow
    return language

def All_file_program_reset(lan):
    C4_Def_Gpio.Write_Power_LED(0)
    C8_Def_Skill.Center_need_to_inital_iris()
    C8_Def_Skill.Center_need_to_play(3,lan,2)
    C1_Def_File.bmp_file_set('hello')

def Brocast_iris_ip():
    C8_Def_Skill.Center_need_to_Brocast_iris()
    #C8_Def_Skill.Center_need_to_kill_cyberon_cspoter() #inital cyberon because first start it is too slow
    
def check_state_led():
    State_led_check = C4_Def_Gpio.Check_State_One_LED()
    return State_led_check
    
def call_group_iris(stream_state_busy): 
    stream_state_busy = C8_Def_Skill.call_group_iris_check(stream_state_busy)
    if stream_state_busy == 1 :
        C8_Def_Skill.Center_need_to_party_mode_time_out()
    return stream_state_busy
    
def check_voip_state():
    return C1_Def_File.Get_voip_state()
    
def answer_check():
    return C1_Def_File.choice_file_get('/tmp/file/answer')
    
def want_to_talk():
    talk = C8_Def_Skill.Center_want_to_talk()
    return talk

def need_to_answer(value):
    talk = C8_Def_Skill.Center_need_to_answer(value)
    return talk
    
def call_music_pause():
    C1_Def_File.music_pause()

def call_music_start():
    C1_Def_File.music_start()  
    
def check_quan_link(wifi_count,lan):
    wifi_count = C8_Def_Skill.Center_need_to_check_quan_link(wifi_count,lan)
    return wifi_count

def random_init(start,end):
    return C8_Def_Skill.Center_need_to_rand_init(start,end)
    
def Find_Other_Iris(line,lan):
    line = C8_Def_Skill.Center_need_to_find_iris(line,lan)
    return line
    
def main_cspotter(lan):
    C8_Def_Skill.Center_need_to_start_cyberon(lan,0,0)
    
def clistener_voip(lan ,voip_now): 
    C8_Def_Skill.Center_need_to_voip(lan ,voip_now)  
    
def main_cspotter_check(lan):
    State_led_check = C4_Def_Gpio.Check_State_One_LED()
    f = C1_Def_File.cyberon_get()
    if f == "Go Iris" or f == "Iris":
        #C8_Def_Skill.Center_need_to_kill_cyberon_cspoter()
        C1_Def_File.clear_cyberon_cspotter()
        angle = C1_Def_File.angle_get()
        return 2 , angle
        
    elif State_led_check==1:
        C4_Def_Gpio.Write_State_One_LED(0)
        angle = 720
        return 2 , angle
    angle = 0
    return 0 , angle
    

        
def clistener(lan , party_mode_now , angle): 
    #C8_Def_Skill.Center_need_to_kill_cyberon_cspoter()
    C1_Def_File.clear_cyberon()
    C8_Def_Skill.Center_need_to_play_music_no_wait(60,lan,2)
    C8_Def_Skill.Center_need_to_start_cyberon(lan,1,0)
    #C8_Def_Skill.Center_need_to_start_cyberon_loop(lan,1,0)
    C1_Def_File.bmp_file_set('iris_now')
    C4_Def_Gpio.Write_Iris_LED(1)
    #print '*************clistener up************'
    Count = 1;iris_state = 0;
    
    if party_mode_now == 1:
        volume = 10
        C8_Def_Skill.Center_need_to_control_volume(volume)     
    
    while True:   
        State_led_check = C4_Def_Gpio.Check_State_One_LED()
        voip_talk_check = open('/tmp/file/sound_busy_check', 'r').read().strip()
        
        if voip_talk_check != '9' or Count == 10:
            break
            
        if voip_talk_check == '9':
            
            if angle !=720:
                set_id = C7_Def_Talk_list.iris_mapping(lan , angle)   
            else:
                set_id = C7_Def_Talk_list.iris_mapping_no_angle(lan)  
            #button to down
            if State_led_check == 1 or set_id == 1000:
                #C1_Def_File.music_pause()
                break
                  
              
            #print set_id
            if set_id < 999 and State_led_check == 0:
                C8_Def_Skill.Center_need_to_kill_cyberon_clistener_loop()
                C1_Def_File.clear_cyberon() 
                if set_id == 100:
                    C4_Def_Gpio.Write_Iris_LED(2)     
                
                    if party_mode_now == 1:  
                        C8_Def_Skill.Center_need_to_party_mode_off()
                        
                    C8_Def_Skill.Center_need_to_kill_cyberon_clistener() 
                    C8_Def_Skill.Center_need_to_play(5,lan,2) 
                    C4_Def_Gpio.Write_Iris_LED(0)           
                
                elif set_id == 14 or set_id == 15: 
                    C4_Def_Gpio.Write_Iris_LED(2) 
                    C1_Def_File.bmp_file_set('annocement')                  
                    C8_Def_Skill.Center_need_to_play(14,lan,1)                     
                    C8_Def_Skill.Center_need_to_Announcement_Mode_On()
                    C1_Def_File.clear_cyberon()
                    C8_Def_Skill.Center_need_to_start_cyberon_loop(lan,1,0)
                    C4_Def_Gpio.Write_Iris_LED(1) 
                    Announcement_count=0
                    while True:
                        time.sleep(1)
                        set_id = C7_Def_Talk_list.iris_mapping_no_angle(lan)
                        State_led_check = C4_Def_Gpio.Check_State_One_LED()
                        if State_led_check == 1 or Announcement_count == 40 or set_id == 14 or set_id == 15: 
                            C8_Def_Skill.Center_need_to_Announcement_Mode_Off()
                            break
                            
                        Announcement_count=Announcement_count+1

                    C8_Def_Skill.Center_need_to_kill_cyberon_clistener_loop()
                    C4_Def_Gpio.Write_Iris_LED(2)                            
                    C8_Def_Skill.Center_need_to_play(15,lan,1) 
            
                elif set_id == 16 or  set_id == 17: 
                    C4_Def_Gpio.Write_Iris_LED(2) 
                    if party_mode_now == 0:
                        C1_Def_File.bmp_file_set('partymodenow')
                        C8_Def_Skill.Center_need_to_play(16,lan,1)
                        C8_Def_Skill.Center_need_to_party_mode()   
                        party_mode_now=1
                    elif party_mode_now == 1: 
                        C8_Def_Skill.Center_need_to_party_mode_off()
                        C8_Def_Skill.Center_need_to_play(17,lan,1)  
                        party_mode_now=0
                        
                elif set_id == 18 :
                    C1_Def_File.bmp_file_set('alexa_now')
                    C4_Def_Gpio.Write_Alexa_LED(1)
                    f = C1_Def_File.alexa_control_get()
                    if f == '0' :
                        #print '*************alexa up************'
                        C8_Def_Skill.Center_need_to_kill_cyberon_clistener_loop()
                        C1_Def_File.alexa_control_set()
                        while True:
                            State_led_check = C4_Def_Gpio.Check_State_One_LED()
                            alexa_control = C1_Def_File.alexa_control_get()
                            if alexa_control == '0' :
                                break
                            if State_led_check==1 :
                                C1_Def_File.button_alexa_to_reset()
                                break
                                
                            time.sleep(1)

                        #C8_Def_Skill.Center_need_to_start_cyberon(lan,0,0)
                        
                    elif f != '0' :  
                        #print '*************alexa error************'
                        C8_Def_Skill.Center_need_to_play(1,lan,2)
                        
                    C4_Def_Gpio.Write_Alexa_LED(0)
                    C1_Def_File.clear_cyberon()
                    
                else:           
                    C8_Def_Skill.Choice_skill(set_id , lan,party_mode_now , angle)   
                    

                            
                    break
                
            Count += 1
            time.sleep(1)
            
    C8_Def_Skill.Center_need_to_kill_cyberon_clistener()
    #C8_Def_Skill.Center_need_to_kill_cyberon_clistener_loop()
    C1_Def_File.clear_cyberon() 
    C4_Def_Gpio.Write_Iris_LED(0)
    C4_Def_Gpio.Write_State_One_LED(0)
    if party_mode_now == 0:
        C1_Def_File.bmp_file_set('hello')
    else :
        C1_Def_File.bmp_file_set('partymodenow')
        
    if party_mode_now == 1:
        volume = C1_Def_File.get_iris_conf('volume_set')
        C8_Def_Skill.Center_need_to_control_volume(volume)   

    C1_Def_File.music_start() 
    return party_mode_now
            

'''
def cspotter(lan , party_mode_now):
    C8_Def_Skill.Center_need_to_kill_cyberon_cspoter()
    C1_Def_File.clear_cyberon()
    C1_Def_File.bmp_file_set('second')
    C8_Def_Skill.Center_need_to_start_cyberon(lan,1,4)
    Count = 0
    
    if party_mode_now == 1:
        volume = 10
        C8_Def_Skill.Center_need_to_control_volume(volume)   
        
    while True :
        f = C1_Def_File.clisten_get()
        voip_talk_check = open('/tmp/file/sound_busy_check', 'r').read().strip()
        State_led_check = C4_Def_Gpio.Check_State_One_LED()
        if voip_talk_check != '9':
            break
            
        elif voip_talk_check == '9':
            if f == "Go Alexa" and  party_mode_now==0 :
                C1_Def_File.bmp_file_set('alexa_now')
                C4_Def_Gpio.Write_State_One_LED(0)
                C4_Def_Gpio.Write_Alexa_LED(1)
                f = C1_Def_File.alexa_control_get()
                if f == '0' :
                    #print '*************alexa up************'
                    C8_Def_Skill.Center_need_to_kill_cyberon_clistener()
                    C1_Def_File.alexa_control_set()
                    while True:
                        State_led_check = C4_Def_Gpio.Check_State_One_LED()
                        alexa_control = C1_Def_File.alexa_control_get()
                        if alexa_control == '0' :
                            break
                        if State_led_check==1 :
                            C1_Def_File.button_alexa_to_reset()
                            break
                            
                        time.sleep(1)

                    C4_Def_Gpio.Write_Alexa_LED(0)
                    
                elif f != '0' :  
                    #print '*************alexa error************'
                    C8_Def_Skill.Center_need_to_play(1,lan,2)

                break

            elif f == "Go Iris" :
                C8_Def_Skill.Center_need_to_kill_cyberon_clistener()
                C4_Def_Gpio.Write_State_One_LED(0)
                return 2                
            
            elif f == "SeeYouLater":
                C8_Def_Skill.Center_need_to_play(2,lan,2)
                break
            elif State_led_check == 0 or Count == 10 :
                break
                

            elif f == "Auf geht's Iris" :
                C8_Def_Skill.Center_need_to_kill_cyberon_cspoter()
                C4_Def_Gpio.Write_State_One_LED(0)
                return 3

            
            Count = Count + 1  
            time.sleep(1)
            
    C8_Def_Skill.Center_need_to_kill_cyberon_clistener()
    C4_Def_Gpio.Write_State_One_LED(0)
    if party_mode_now == 0:
        C1_Def_File.bmp_file_set('hello')
    else :
        C1_Def_File.bmp_file_set('partymodenow')
        
    if party_mode_now == 1:
        volume = C1_Def_File.get_iris_conf('volume_set')
        C8_Def_Skill.Center_need_to_control_volume(volume)   
        
    C1_Def_File.music_start()       
    return 0    
'''    
