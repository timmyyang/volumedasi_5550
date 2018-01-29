import C3_Def_link ,C5_Def_Program ,C1_Def_File ,C9_Power_command ,C4_Def_Gpio,C7_Def_Talk_list,C7_1_Def_Talk_list,D2_Iris_talk
import time
import random
import json

def Center_need_to_inital_iris():
    C5_Def_Program.inital_device()    

def Center_need_to_Brocast_iris():
    C3_Def_link.brocast_iris_ip()
    
def Center_need_to_check_quan_link(wifi_count,lan):
    wifi_count , state  = C3_Def_link.check_quan_link(wifi_count)
    if lan == 'EN':
        file = "/root/audio/en/quantenna/master_connect_wifi_"+ str(wifi_count) +".mp3"
    if lan == 'DE':
        file = "/root/audio/de/quantenna/master_connect_wifi_"+ str(wifi_count) +".mp3"
    if state == 1 :
        C5_Def_Program.play_music_file(file)
    return wifi_count
    
def Center_need_to_start_command(cmd):
    C5_Def_Program.start_command(cmd)

def Center_need_to_play(set_id,lan,child):
    C5_Def_Program.play_music(set_id,lan,child) 
    
def Center_need_to_play_music_no_wait(set_id,lan,child):
    C5_Def_Program.play_music_no_wait(set_id,lan,child) 
    
def Center_need_to_play_file(file):
    C5_Def_Program.play_music_file(file)
    
def Center_need_to_play_file_keep(file):
    play_music_file_keep_no_music_start(file)
    
def Center_need_to_start_cyberon(lan,main,sub):
    C5_Def_Program.strat_cyberon(lan,main,sub)

def Center_need_to_start_cyberon_loop(lan,main,sub):
    C5_Def_Program.strat_cyberon_loop(lan,main,sub)
    
def Center_need_to_kill_cyberon_cspoter():
    C5_Def_Program.kill_cyberon_cspotter()
    
def Center_need_to_kill_cyberon_clistener():
    C5_Def_Program.kill_cyberon_clistener()
    
def Center_need_to_kill_cyberon_clistener_loop():
    C5_Def_Program.kill_cyberon_clistener_loop()
    
def Center_need_to_start_program(command):
    C5_Def_Program.start_program(command)
    
def Center_need_to_control_volume(n):
    C5_Def_Program.control_volume(n)
    
def Center_need_to_party_mode():
    C3_Def_link.call_to_party_mode_on()
    C5_Def_Program.tmp_I()
    
def Center_need_to_party_mode_off():
    C3_Def_link.call_to_party_mode_off()
    C5_Def_Program.tmp_II()
    
def Center_need_to_party_mode_time_out():
    C5_Def_Program.check_party_mode_music_time_out()

def Center_need_to_Announcement_Mode_On():
    C3_Def_link.Announcement_Mode_On()
    
def Center_need_to_Announcement_Mode_Off():
    C3_Def_link.Announcement_Mode_Off()
    
def Center_need_to_find_iris(line,lan):
    tmp_line = line
    line = C1_Def_File.choice_file_length('/tmp/file/search_iris')
    if tmp_line != line:
        C5_Def_Program.party_mode_pause(1)
        C5_Def_Program.play_music(21,lan,2)
        C5_Def_Program.party_mode_pause_then_start(1)
    return line
    
def Center_need_to_rand_init(start,end):
    return random.randint(start,end)
    
def Center_need_to_unicast(key_word):
    line = C3_Def_link.Get_all_iris_ip_length()
    #print ('length =',line)
    if line >= 2:
        unicast_ip = C3_Def_link.Get_all_iris_ip(random.randint(2,line))
        #print ('unicast_ip =',unicast_ip)
        C3_Def_link.unicast_iris_ip(unicast_ip,key_word)
    
def call_group_iris_check(stream_state_busy):
    stream_state = C1_Def_File.Get_stream_state()
    if stream_state != '0':
    
        if stream_state == '1':
            #print '***********party mode on now***************'
            C5_Def_Program.party_mode_on()
            stream_state_busy = 1
        if stream_state == '2':
            #print '***********party mode off now***************'
            C5_Def_Program.party_mode_off()
            stream_state_busy = 0
        if stream_state == '3':
            #print '***********AnnouncementModeOn now***************'
            C5_Def_Program.Announcement_Mode_On()
            stream_state_busy = 2
        if stream_state == '4':
            #print '***********AnnouncementModeOff now***************'
            C5_Def_Program.Announcement_Mode_Off()
            stream_state_busy = 0
        if stream_state == '5':
            #print '***********ktv on now***************'
            C5_Def_Program.Ktv_on()
            stream_state_busy = 0
        if stream_state == '6':
            #print '***********ktv off now***************'
            C5_Def_Program.Ktv_off()
            stream_state_busy = 0
            
    return stream_state_busy  
    
def Center_want_to_talk():
    value = Center_need_to_rand_init(1,want_to_talk_length_check()) 
    if value < 10:
        value = '00' + str(value)
    elif value < 100:
        value = '0' + str(value)
    elif value < 1000:
        value = str(value)
    value = str(value) + str(Center_need_to_rand_init(1,want_to_talk_sub_length_check(value))) 

    need_brocast ,stat_rand_time ,end_rand_time = D2_Iris_talk.which_one_i_want_to_talk(value)
    talk = Center_need_to_rand_init(stat_rand_time,end_rand_time)
    Center_need_to_play_file('/tmp/file/answer.mp3')
    
    if need_brocast == 1 :
        Center_need_to_unicast(value)
        
    return talk
 
def Center_need_to_answer(value):
    need_brocast ,stat_rand_time ,end_rand_time,value =  D2_Iris_talk.which_one_i_need_answer(value)
    talk = Center_need_to_rand_init(stat_rand_time,end_rand_time)
    Center_need_to_play_file('/tmp/file/answer.mp3')
    C1_Def_File.choice_file_set('//tmp/file/answer', '00000')
    
    if need_brocast == 1 :
        Center_need_to_unicast(value)
        
    return talk   
    
def skill_inital(set_id,lan,music_choice,main_music,bmp_name,clisten_file):
    C4_Def_Gpio.Write_Iris_LED(2)
    C1_Def_File.clear_cyberon()
    C5_Def_Program.play_music(music_choice,lan,main_music) 
    C1_Def_File.bmp_file_set(bmp_name)
    C5_Def_Program.strat_cyberon(lan,1,clisten_file)
    C4_Def_Gpio.Write_Iris_LED(1) 
    
def main_trigger(lan , subcount , bmp_name , clisten_file , clisten_check ,angle):
    f = C1_Def_File.cyberon_get()
    set_id = C7_1_Def_Talk_list.iris_mapping(lan,clisten_check,angle)     
    State_led_check = C4_Def_Gpio.Check_State_One_LED()
    #if subcount == 101 or set_id == 1000:
    if subcount == 101:
        volume = C1_Def_File.get_iris_conf('volume_set')
        if int(volume)>0 and int(volume) < 10:
            C5_Def_Program.control_volume(volume)  
        
        C5_Def_Program.kill_cyberon_clistener() 
        #C5_Def_Program.kill_cyberon_clistener_loop()
        C1_Def_File.clear_cyberon()
        C1_Def_File.music_start() 
        C4_Def_Gpio.Write_Iris_LED(0)
        C1_Def_File.bmp_file_set(bmp_name)
        #C5_Def_Program.strat_cyberon(lan,0,0)
        subcount = 101
    elif f == "Go Iris" or f == "Iris" :
        angle = C1_Def_File.angle_get()
        volume = C1_Def_File.get_iris_conf('volume_set')
        if int(volume)>0 and int(volume) < 10:
            C5_Def_Program.control_volume(10)  
        
        #C5_Def_Program.kill_cyberon_cspotter()
        if clisten_check != 'radio':
            C5_Def_Program.play_music_no_wait(60,lan,2)
        C1_Def_File.clear_cyberon_cspotter()
        C5_Def_Program.strat_cyberon(lan,1,clisten_file)
        #C5_Def_Program.strat_cyberon_loop(lan,1,clisten_file)
        C1_Def_File.bmp_file_set('listen')
        C4_Def_Gpio.Write_Iris_LED(1)
        subcount = 0
            
    return set_id , State_led_check ,subcount ,angle
        
    

#######radio###########

def get_user_choice(i):
    str=C1_Def_File.get_iris_conf('radio%1d'%(i))
    return str[0:len(str)-1]
     
def radio_url_get(start_step,step_num):
    global decodejson ;global user_choice_id
    i=start_step
    for i in range(step_num):
        if i>=1:
            #print "query step",i
            user_choice_id[i]=get_user_choice(i)#raw_input("id=")#=get_from_ui_api()
            #print user_choice_id[i]
        if i==2:
            step3start=0
            step3len=100
        #elif i==3:
        #    searchstr='radio'
        #    page=1
        if i<=1:
            payload = {'uuid': 1, 'tkx': 'TTiSMC1030DevKey', 'id': user_choice_id[i]}
        elif i==2:
            payload = {'uuid': 1, 'tkx': 'TTiSMC1030DevKey', 'id': user_choice_id[i],'start':step3start,'len':step3len}
            #elif i==3:
        #    params = urllib.urlencode({'uuid': 1, 'tkx': 'TTiSMC1030DevKey','s':searchstr,'p':page})
        try:
            if i==0:
                #r=requests.get("http://Andromeda.tti.tv/SMC1030/API/v1/Genre/QueryFirst",params=payload,timeout=0.5)
                r=C3_Def_link.requests_command_payload("http://Andromeda.tti.tv/SMC1030/API/v1/Genre/QueryFirst",payload,1)
            elif i==1:
                #r=requests.get("http://Andromeda.tti.tv/SMC1030/API/v1/Genre/QuerySecond",params=payload,timeout=0.5)
                r=C3_Def_link.requests_command_payload("http://Andromeda.tti.tv/SMC1030/API/v1/Genre/QuerySecond",payload,1)
            elif i==2:
                #r=requests.get("http://Andromeda.tti.tv/SMC1030/API/v1/Station/Query" ,params=payload,timeout=0.5)
                r=C3_Def_link.requests_command_payload("http://Andromeda.tti.tv/SMC1030/API/v1/Station/Query",payload,1)
                #elif i==3:
                #    query1 = urllib.urlopen("http://Andromeda.tti.tv/SMC1030/API/v1/Station/SearchAll?%s" % params)
        except:
            #print 'requests.get Andromeda.tti.tv/SMC1030/API/v1/... failed'
            return False
        sStr1= r.text#query1.read()   
        decodejson[i]=json.loads(sStr1)#(1)(3)(5)send to user interface
        if decodejson[i]['status'] != '200':
            #print 'query action is not 200 ok'
            return False
        sStr = '['   
        startPos = sStr1.index(sStr)   
        sStr = ']'
        endPos = sStr1.index(sStr)
        subStr= sStr1[startPos:endPos+1] 
        decodejson[i] =  json.loads(subStr)#(1)(3)(5)send to user interface
        #print 'len(decodejson[',i,'])=',len(decodejson[i])
        '''
        if i<=1:
            for j in range(len(decodejson[i])):
                print 'i=',i,'id=',decodejson[i][j]['id'],'title=', decodejson[i][j]['title']
        elif i==2:
            for j in range(len(decodejson[i])):
                try:
                    print 'i=',i,'ID=',decodejson[i][j]['ID'],',name=', decodejson[i][j]['Name'],',url=',decodejson[i][j]['StreamUrl']
                except Exception as exc:
                    print 'i=',i,'ID=',decodejson[i][j]['ID'],',name=', 'something error',',url=',decodejson[i][j]['StreamUrl']
                    
                ''' 
def radio_choice(radio_tmp, len_mp3 , lan , play ,subcount , bmp_word ,set_id):
    try: 
        radio_now=int(C1_Def_File.get_iris_conf('radio3')) 
    except Exception as exc:
        radio_now=1
    if radio_tmp== 999:
        radio_tmp = radio_now
        radio_play(radio_now-1 ,lan)
        
    if set_id < 999: 
        C4_Def_Gpio.Write_Iris_LED(2)
        subcount = 100
        #play
        if set_id == 6 and play ==1:
            radio_tmp = radio_now
            radio_play(radio_now-1 ,lan)
            play=0 
            
        #pause
        elif set_id == 7 and play==0:
            C1_Def_File.bmp_file_set('pause')
            bmp_word = 'pause'
            C5_Def_Program.kill_play_stream() 
            play=1
            
        #volume up down
        elif set_id == 9:
            volume = C1_Def_File.get_iris_conf('volume_set')
            if int(volume)>0 and int(volume) <= 10 :
                volume = int(volume) - 1
                C1_Def_File.bmp_file_set('volume%i'%(volume))
                C1_Def_File.set_iris_conf('volume_set',volume)
                C5_Def_Program.control_volume(volume) 
                bmp_word = C1_Def_File.bmp_file_get()
                
        elif set_id == 10:
            #C5_Def_Program.play_music(27,lan,2)     
            volume = C1_Def_File.get_iris_conf('volume_set')
            if int(volume)>=0 and int(volume) < 10 :
                volume = int(volume) + 1
                C1_Def_File.bmp_file_set('volume%i'%(volume))
                C1_Def_File.set_iris_conf('volume_set',volume)
                C5_Def_Program.control_volume(volume) 
                bmp_word = C1_Def_File.bmp_file_get()
                C1_Def_File.bmp_file_set(bmp_word)                
                
        #volume lowest      
        elif set_id == 17:
            #C5_Def_Program.play_music(27,lan,2)     
            volume = C1_Def_File.get_iris_conf('volume_set')
            if int(volume)>=0 and int(volume) < 10 :
                volume = 10
                C1_Def_File.bmp_file_set('volume%i'%(volume))
                C1_Def_File.set_iris_conf('volume_set',volume)
                C5_Def_Program.control_volume(volume)  
                time.sleep(1)
                bmp_word = C1_Def_File.bmp_file_get()
                C1_Def_File.bmp_file_set(bmp_word)
                
        #next        
        elif set_id == 11 and radio_now < len_mp3 :
            C1_Def_File.bmp_file_set('processing')
            bmp_word = 'processing'             
            radio_now += 1
        #back    
        elif set_id == 8 and radio_now > 1:
            C1_Def_File.bmp_file_set('processing')
            bmp_word = 'processing'   
            radio_now -= 1
            
        elif set_id == 13 and radio_now < len_mp3 :
            C5_Def_Program.kill_play_stream() 
            C1_Def_File.set_iris_conf('radio1','212.')
            C1_Def_File.set_iris_conf('radio2','218.')
            play=3
            
        elif set_id == 14 and radio_now < len_mp3 :
            C5_Def_Program.kill_play_stream()    
            C1_Def_File.set_iris_conf('radio1','220.')
            C1_Def_File.set_iris_conf('radio2','230.')
            play=3
           
        elif set_id == 15 and radio_now < len_mp3 :
            C5_Def_Program.kill_play_stream()     
            C1_Def_File.set_iris_conf('radio1','163.')
            C1_Def_File.set_iris_conf('radio2','170.')
            play=3
            
        if radio_now != radio_tmp:
            radio_tmp = radio_now
            play=radio_play(radio_now-1 ,lan)
            C1_Def_File.set_iris_conf('radio3',radio_now)
                
        C1_Def_File.clear_cyberon()
        
    subcount += 1
    return radio_tmp , play  , subcount , bmp_word 
                
def radio_play(radio_now ,lan):    
    C5_Def_Program.kill_play_stream()
    command = "'" + mp3_site[radio_now] + "'"
    #print ("command=",command)
    r = C5_Def_Program.play_music_url(command)
    r = C5_Def_Program.selete_avoid_stop(r,10)#r=return command , %d=time_out
    #print r
    if r == 1:
        C5_Def_Program.play_music(31,lan,2)
        C5_Def_Program.kill_play_stream()
        play = 1
        return play
    else :
        C1_Def_File.bmp_file_set('playing')
        bmp_word = 'playing'
        play = 0
        return play
    
##################
    
########voip#########
def Center_need_to_voip(lan ,voip_now): 
    subcount = 101 ;
    
    C5_Def_Program.kill_cyberon_clistener_loop()
    C5_Def_Program.strat_cyberon_loop(lan,1,6)
    C1_Def_File.clear_cyberon()
    while True:
        f = C1_Def_File.cyberon_get()    
        State_led_check = C4_Def_Gpio.Check_State_One_LED()
        voip_talk_check = open('/tmp/file/sound_busy_check', 'r').read().strip()
        set_id = C7_1_Def_Talk_list.iris_mapping(lan,'voip' ,'720')  
        '''
        if f == "Go Iris" or f == "Iris" :
        
            volume = 10
            C5_Def_Program.control_volume(volume)  
            
            C5_Def_Program.kill_cyberon_cspotter()
            C1_Def_File.bmp_file_set('listen')
            C1_Def_File.clear_cyberon_cspotter()
            C5_Def_Program.strat_cyberon_loop(lan,1,6)
            C4_Def_Gpio.Write_Iris_LED(1)
            subcount = 0
            
        elif subcount == 101:
            volume = C1_Def_File.get_iris_conf('volume_set')
            if int(volume)>0 and int(volume) < 10:
                C5_Def_Program.control_volume(volume)  
                
            #C5_Def_Program.kill_cyberon_clistener() 
            C5_Def_Program.kill_cyberon_clistener_loop()
            C1_Def_File.clear_cyberon()
            C1_Def_File.music_start() 
            C4_Def_Gpio.Write_Iris_LED(0)
            C1_Def_File.bmp_file_set('voip')
            C5_Def_Program.strat_cyberon(lan,0,0)
            subcount = 101
        '''
        if set_id == 1 and voip_now == 0 and voip_talk_check == '4':
            C5_Def_Program.kill_cyberon_clistener_loop()
            C5_Def_Program.start_program('killall -9 madplay aplay')
            C5_Def_Program.start_program('echo a | telnet localhost 5555')
            volume = C1_Def_File.get_iris_conf('volume_set')
            C5_Def_Program.control_volume(volume)  
            voip_now = 1
        
        elif State_led_check == 1 or voip_talk_check=='9' or set_id == 0:
            C5_Def_Program.kill_cyberon_clistener_loop()
            #C5_Def_Program.kill_cyberon_cspotter()
            C5_Def_Program.start_program('killall -9 madplay aplay')
            C5_Def_Program.start_program('echo b | telnet localhost 5555')
            volume = C1_Def_File.get_iris_conf('volume_set')
            C5_Def_Program.control_volume(volume)  
            C4_Def_Gpio.Write_Voip(0)
            time.sleep(1)            
            C5_Def_Program.play_music(10,lan,1) 
            C5_Def_Program.kill_cyberon_clistener() 
            break

        subcount = subcount + 1   
        time.sleep(0.1)   
        
    C1_Def_File.clear_cyberon()    
    C5_Def_Program.kill_cyberon_clistener_loop()
        
#######################

def Choice_skill(set_id,lan,party_mode_now,angle):

    if set_id == 0 : 
        skill_inital(set_id,lan,58,2,'device',5)
        subcount = 0
        while True:
            set_id , State_led_check ,subcount ,angle= main_trigger(lan , subcount , 'device' , 5 , 'device' , angle)
            if set_id == 100 or State_led_check == 1:
                break 
            elif set_id < 999: 
                C4_Def_Gpio.Write_Iris_LED(2)
                subcount = 100
                try:
                    #r=requests.get("http://192.168.1.150/volume/user_file/1600.txt",timeout=2)
                    url = "http://192.168.1.150/volume/user_file/1600.txt"
                    r = C3_Def_link.requests_command(url,3) 
                    pos=r.text.index('results') 
                    integer=r.text[(pos+7):len(r.text)].strip('":} \r\n')
                    if set_id < 10 :
                        C5_Def_Program.play_music(set_id,lan,1)   
                        C1_Def_File.device_save(set_id)      
                        url = C9_Power_command.power_command(1,set_id)
                        r = C3_Def_link.requests_command(url,3)   
                    elif set_id == 10 :
                        if integer[0] == '1':
                            C5_Def_Program.play_music(32,lan,2)
                        else :
                            C5_Def_Program.play_music(33,lan,2)
                    elif set_id == 11 :
                        if integer[1] == '1':
                            C5_Def_Program.play_music(34,lan,2)
                        else :
                            C5_Def_Program.play_music(35,lan,2)
                    elif set_id == 12 :
                        if integer[2] == '1':
                            C5_Def_Program.play_music(36,lan,2)
                        else :
                            C5_Def_Program.play_music(37,lan,2)
                    elif set_id == 13 :
                        if integer[3] == '1':
                            C5_Def_Program.play_music(38,lan,2)
                        else :
                            C5_Def_Program.play_music(39,lan,2)
                            
                except Exception as exc:
                    C5_Def_Program.play_music(31,lan,2)
                    
                C1_Def_File.clear_cyberon()

            time.sleep(0.1)
            subcount = subcount + 1   
    
        C4_Def_Gpio.Write_Iris_LED(2)       
        C5_Def_Program.play_music(5,lan,2)
        
    if set_id == 10:
        skill_inital(set_id,lan,59,2,'phone',6)
        subcount = 0
        while True:
            set_id , State_led_check ,subcount ,angle = main_trigger(lan , subcount , 'phone' , 6 , 'phone' , angle)
            if set_id == 100 or State_led_check == 1:
                C4_Def_Gpio.Write_Iris_LED(2)       
                C5_Def_Program.play_music(5,lan,2)
                break 
            elif set_id < 999: 
                subcount = 100 
                if set_id == 1:
                    C5_Def_Program.play_music(11,lan,1)
                elif set_id == 2:
                    C5_Def_Program.play_music(12,lan,1)
                if set_id == 1 or set_id == 2:
                    recall = 0
                    C4_Def_Gpio.Write_Iris_LED(2)
                    C1_Def_File.bmp_file_set('calling')
                    command = 'echo b | telnet localhost 5555'
                    while True:
                        voip_talk_check = open('/tmp/file/sound_busy_check', 'r').read().strip()
                        State_led_check = C4_Def_Gpio.Check_State_One_LED()
                        if voip_talk_check == '9':
                            if set_id == 1:
                                command = 'echo d 2011 | telnet localhost 5555'
                                C5_Def_Program.start_program(command)
                            elif set_id == 2:
                                command = 'echo d 2011 | telnet localhost 5555'
                                C5_Def_Program.start_program(command)
                            time.sleep(1)
                        if voip_talk_check == '1':
                            C5_Def_Program.kill_cyberon_clistener_loop()
                            Center_need_to_voip(lan ,1)
                            break
  
                        elif recall >= 5:
                            command = 'echo b | telnet localhost 5555'
                            C5_Def_Program.start_program(command)
                            C5_Def_Program.play_music(31,lan,2)
                            break
                            
                        elif State_led_check == 1:
                            command = 'echo b | telnet localhost 5555'
                            break
                            
                        recall += 1          
                    break
        
            time.sleep(0.1)
            subcount = subcount + 1   
    


    if set_id == 20:
        C4_Def_Gpio.Write_Iris_LED(2)
        volume = C1_Def_File.get_iris_conf('volume_set')
        if int(volume)>0 and int(volume) <= 10:
            volume = int(volume) - 1
            C1_Def_File.bmp_file_set('volume%i'%(volume))
            C1_Def_File.set_iris_conf('volume_set',volume)
            C5_Def_Program.control_volume(volume)  
            C5_Def_Program.play_music(20,lan,1)
            C1_Def_File.bmp_file_set('iris_now')
        
        #print '*************volume up************' 
    if set_id == 21:
        C4_Def_Gpio.Write_Iris_LED(2)
        volume = C1_Def_File.get_iris_conf('volume_set')
        if int(volume)>=0 and int(volume)<10:
            volume = int(volume) + 1
            C1_Def_File.bmp_file_set('volume%i'%(volume))
            C1_Def_File.set_iris_conf('volume_set',volume)
            C5_Def_Program.control_volume(volume)  
            C5_Def_Program.play_music(21,lan,1)
            C1_Def_File.bmp_file_set('iris_now')
        
        #print '*************volume down************' 
    if set_id == 220:
        volume = 2
        C1_Def_File.set_iris_conf('volume_set',volume)
        C5_Def_Program.control_volume(volume)  
        C5_Def_Program.play_music(22,lan,1)
        
        #print '*************Max volume************'     
    if set_id == 230:
        volume = 10
        C1_Def_File.set_iris_conf('volume_set',volume)
        C5_Def_Program.control_volume(volume) 
        C5_Def_Program.play_music(22,lan,1)
                
        #print '*************min volume************'            
    if set_id == 240:
        volume = 11
        C1_Def_File.volume_set(volume)
        C5_Def_Program.control_volume(volume)  
        C5_Def_Program.play_music(22,lan,1)
        
        #print '*************Mute************'              
    
    
    #search iris
    if set_id == 270:
        C4_Def_Gpio.Write_Iris_LED(2) 
        #print '*************search iris************' 
        C5_Def_Program.play_music(set_id,lan,1) 
        Net_state = C3_Def_link.call_to_search_ip()
        if Net_state == 1 :
            C5_Def_Program.play_music_keep(9,lan,2) 
            C3_Def_link.search_iris_quan()
            C5_Def_Program.kill_play()
            C5_Def_Program.play_music(28,lan,1)  
        C4_Def_Gpio.Write_Iris_LED(4) 
        
    #wifi down               
    if set_id == 290:
        C4_Def_Gpio.Write_Iris_LED(2) 
        C5_Def_Program.play_music(set_id,lan,1) 
        #print '*************wifi down************' 
        C3_Def_link.quantenna_wifi_down()    
        C4_Def_Gpio.Write_Iris_LED(4)

    #wifi up   
    if set_id == 300:
        C4_Def_Gpio.Write_Iris_LED(2) 
        C5_Def_Program.play_music(set_id,lan,1) 
        #print '*************wifi up************' 
        C3_Def_link.quantenna_wifi_up()               
        C4_Def_Gpio.Write_Iris_LED(4) 
        
    #push wps                   
    if set_id == 320:  
        C4_Def_Gpio.Write_Iris_LED(2) 
        C5_Def_Program.play_music(set_id,lan,1)
        Wps_state = C3_Def_link.check_quan_wps()
        #print '*************push wps************' 
        if Wps_state == 1:
            C5_Def_Program.play_music_keep(6,lan,2)         
            Wps_state = C3_Def_link.call_to_push_wps() 
            C5_Def_Program.kill_play()
            if Wps_state == '2':
                C5_Def_Program.play_music(7,lan,2)   
            if Wps_state == '4':
                C5_Def_Program.play_music(8,lan,2)          
        C4_Def_Gpio.Write_Iris_LED(4)
        
    #connect_the_iris
    if set_id == 330:
        C4_Def_Gpio.Write_Iris_LED(2) 
        C5_Def_Program.play_music(set_id,lan,1)
        #print '*************connect_the_iris************' 
        Net_state = C3_Def_link.quantenna_connect_iris()
        if Net_state == 1 :
            C5_Def_Program.play_music(10,lan,2)
        if Net_state == 0 :
            C5_Def_Program.play_music(11,lan,2)
        C4_Def_Gpio.Write_Iris_LED(4)   
        
    #ir controller
    if set_id == 35:
        skill_inital(set_id,lan,set_id,1,'controller',1)
        subcount = 0
        while True:
            set_id , State_led_check ,subcount ,angle = main_trigger(lan , subcount , 'controller' , 1 , 'controller' , angle)
            if set_id == 100 or State_led_check == 1:
                break 
            elif set_id < 999: 
                C4_Def_Gpio.Write_Iris_LED(2)
                subcount = 100
                if set_id == 0:
                    C1_Def_File.ir_file_set('power')
                    C5_Def_Program.play_music(49,lan,2)    
                elif set_id == 26:
                    C1_Def_File.ir_file_set('power')
                    C5_Def_Program.play_music(57,lan,2)    
                elif set_id == 1:
                    C1_Def_File.ir_file_set('up')
                elif set_id == 2:
                    C1_Def_File.ir_file_set('left')
                elif set_id == 3:
                    C1_Def_File.ir_file_set('ok')
                elif set_id == 4:
                    C1_Def_File.ir_file_set('right')
                elif set_id == 5:
                    C1_Def_File.ir_file_set('down')
                elif set_id == 6:
                    C1_Def_File.ir_file_set('play')
                elif set_id == 7:
                    C1_Def_File.ir_file_set('back')
                elif set_id == 8:
                    C1_Def_File.ir_file_set('volumeadd')
                elif set_id == 9:
                    C1_Def_File.ir_file_set('volumedown')
                elif set_id == 10:
                    C1_Def_File.ir_file_set('programadd')
                elif set_id == 11:
                    C1_Def_File.ir_file_set('programdown')
                elif set_id == 12:
                    C1_Def_File.ir_file_set('0')
                elif set_id == 13:
                    C1_Def_File.ir_file_set('1')
                elif set_id == 14:
                    C1_Def_File.ir_file_set('2')
                elif set_id == 15:
                    C1_Def_File.ir_file_set('3')
                elif set_id == 16:
                    C1_Def_File.ir_file_set('4')
                elif set_id == 17:
                    C1_Def_File.ir_file_set('5')
                elif set_id == 18:
                    C1_Def_File.ir_file_set('6')
                elif set_id == 19:
                    C1_Def_File.ir_file_set('7')
                elif set_id == 20:
                    C1_Def_File.ir_file_set('8')
                elif set_id == 21:
                    C1_Def_File.ir_file_set('9')
                elif set_id == 22:
                    C1_Def_File.ir_file_set('3')
                    C5_Def_Program.play_music(50,lan,2)  
                elif set_id == 23:
                    C1_Def_File.ir_file_set('49')
                    C5_Def_Program.play_music(51,lan,2)  
                elif set_id == 24:
                    C1_Def_File.ir_file_set('50')
                    C5_Def_Program.play_music(52,lan,2)  
                elif set_id == 25:
                    C1_Def_File.ir_file_set('volumemute')
                    C5_Def_Program.play_music(53,lan,2)  
                            
                C1_Def_File.clear_cyberon()

            time.sleep(0.1)
            subcount = subcount + 1   
    
        C4_Def_Gpio.Write_Iris_LED(2)       
        C5_Def_Program.play_music(5,lan,2)
        
    # radio 
    if set_id == 36 or set_id == 42:
        # radio wait time
        if set_id == 42:
            skill_inital(set_id,lan,40,1,'processing',2)
            C4_Def_Gpio.Write_Iris_LED(2) 
            time_count = 0 ; subcount = 0;
            while True:
                set_id , subcount  , angle = main_trigger(lan , subcount , 'radio' , 1 , 'radio' , angle)
                if time_count == 60 :
                    set_id = 36
                    break 
                time_count += 1 
                time.sleep(1)  
                
        if set_id == 36:                
            skill_inital(set_id,lan,set_id,1,'processing',2)
            while True:
                C1_Def_File.bmp_file_set('processing')
                global decodejson;global mp3_site;global user_choice_id
                decodejson=[[]]*3;mp3_site=[];user_choice_id=['1','','']  
                try:
                    r = C3_Def_link.requests_command("http://Andromeda.tti.tv",0.5)
                except Exception as exc:
                    C5_Def_Program.play_music(31,lan,2)
                    break
                '''
                if r.status_code!=200:
                    print 'requests.get \"Andromeda.tti.tv\" failed'
                '''
                return_bool_value=radio_url_get(0,3)
                if return_bool_value==False:
                    print 'return_bool_value error'
                i=0;j=0
                
                radio_tmp = 999 ; play=0 ;call_iris =0 ; subcount = 101 ; bmp_word = 'processing' ;
                '''
                for i in range(len(decodejson[2])):
                    print 'request.get:'+decodejson[2][i]['StreamUrl']
                    try:
                        r = C3_Def_link.requests_command_stream(decodejson[2][i]['StreamUrl'], 0.5)#200,503,403,only connected message
                    except:
                        print 'requests.get \"'+decodejson[2][i]['StreamUrl']+'\" failed'
                        continue
                    print r.status_code
                    aac=2
                    if r.status_code==200:
                        print r.headers['content-type']
                        if 'aac' in r.headers['content-type']:
                            aac=1
                        else:
                            aac=0
                    if aac==0:
                        #print 'aac=0'
                        mp3_site.append(decodejson[2][i]['StreamUrl'])
                        print len(mp3_site)
                        radio_tmp , play , subcount  = radio_choice(radio_tmp,len(mp3_site),lan ,play,subcount )
                        if play == 2 or play == 3:
                            C1_Def_File.set_iris_conf('radio3',1)
                            break 
                print ('mp3 site count=',len(mp3_site))
                '''
                # tmp
                for i in range(len(decodejson[2])):
                    mp3_site.append(decodejson[2][i]['StreamUrl'])    
                #print ('mp3 site count=',len(mp3_site))    
                    
                if len(mp3_site)>0:
                    while True:            
                        set_id , State_led_check ,subcount , angle= main_trigger(lan , subcount , 'radio' , 2 , 'radio' , angle)    
                        if set_id == 100 or State_led_check == 1 or play == 3:
                            C1_Def_File.set_iris_conf('radio3',1)
                            break
                        radio_tmp , play , subcount , bmp_word  = radio_choice(radio_tmp,len(mp3_site),lan , play , subcount , bmp_word ,set_id)
                        time.sleep(0.1)
                if set_id == 100 or State_led_check == 1:
                    C5_Def_Program.kill_play_stream() 
                    break
            #tmp
            C1_Def_File.set_iris_conf('radio3',1)
            
        C4_Def_Gpio.Write_Iris_LED(2)       
        C5_Def_Program.play_music(5,lan,2)
            


    if set_id == 37:
        skill_inital(set_id,lan,set_id,1,'Andromeda',3)
        subcount = 0; app = '0' ; ip = 'http://192.168.1.150:7070/'
        Andromeda_ID  = C1_Def_File.get_iris_conf('Andromeda_ID')
        #ip = 'http://211.75.14.235:7070/'
        while True:
            set_id , State_led_check ,subcount ,angle= main_trigger(lan , subcount , 'Andromeda' , 3 , 'Andromeda' ,angle)
            if set_id == 100 or State_led_check == 1:
                break 
            elif set_id < 999: 
                try:
                    C4_Def_Gpio.Write_Iris_LED(2)
                    subcount = 100
                    
                    if set_id == 0:
                        C5_Def_Program.play_music(45,lan,2)
                        payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'open', 'uri':''}
                        r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        app = 'LiveTV'
                        
                    elif set_id == 1:
                        C5_Def_Program.play_music(46,lan,2)
                        payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'open', 'uri':''}
                        r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        app = 'MediaStore'  
                        
                    #elif set_id == 2:
                    #    C1_Def_File.ir_file_set('back')
                        
                    elif app == 'LiveTV':  
                        if set_id == 16:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'close', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                            app = '0'
                        elif set_id == 2:
                            C1_Def_File.ir_file_set('back')
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'close', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                            app = '0'
                        elif set_id == 10:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'change to channel 3', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 11:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'change to channel 49', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 12:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'change to channel 50', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)  
                            
                    elif app == 'MediaStore' :   
                        if set_id == 2:
                            C1_Def_File.ir_file_set('back')
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'back', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                            app = '0'
                        elif set_id == 3:
                            C5_Def_Program.play_music(47,lan,2)
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'video', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 4:
                            C5_Def_Program.play_music(48,lan,2)
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'audio', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 5:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'stop', 'uri':''}
                            r=r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 6:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'play', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 7:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'pause', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 13:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'play wonderland', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 14:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'play snowboard', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 15:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'play redbull', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                        elif set_id == 16:
                            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'close', 'uri':''}
                            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                            app = '0'
                                
                except Exception as exc:
                    C5_Def_Program.play_music(31,lan,2)
                    
                C1_Def_File.clear_cyberon()
            
            time.sleep(0.1)
            subcount = subcount + 1 
            
        C4_Def_Gpio.Write_Iris_LED(2)       
        C5_Def_Program.play_music(5,lan,2)
        
        
                

                                
        


        
