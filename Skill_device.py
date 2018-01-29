'''
first_inital = 1 or 0 :
first use this skills

skill_need_keep = 1 or 0 : 
keep don't need to say iris 

pair_id :
voice text ,pair id 

lan:
user's language

'''
def Device_skill(first_inital,pair_id,lan): 
            #if pair_id == 100 or State_led_check == 1:
            #    break 
            #elif pair_id < 999: 
                C4_Def_Gpio.Write_Iris_LED(2)
                subcount = 100
                try:
                    #r=requests.get("http://192.168.1.150/volume/user_file/1600.txt",timeout=2)
                    url = "http://192.168.1.150/volume/user_file/1600.txt"
                    r = C3_Def_link.requests_command(url,3) 
                    pos=r.text.index('results') 
                    integer=r.text[(pos+7):len(r.text)].strip('":} \r\n')
                    if pair_id < 10 :
                        C5_Def_Program.play_music(pair_id,lan,1)   
                        C1_Def_File.device_save(pair_id)      
                        url = C9_Power_command.power_command(1,pair_id)
                        r = C3_Def_link.requests_command(url,3)   
                    elif pair_id == 10 :
                        if integer[0] == '1':
                            C5_Def_Program.play_music(32,lan,2)
                        else :
                            C5_Def_Program.play_music(33,lan,2)
                    elif pair_id == 11 :
                        if integer[1] == '1':
                            C5_Def_Program.play_music(34,lan,2)
                        else :
                            C5_Def_Program.play_music(35,lan,2)
                    elif pair_id == 12 :
                        if integer[2] == '1':
                            C5_Def_Program.play_music(36,lan,2)
                        else :
                            C5_Def_Program.play_music(37,lan,2)
                    elif pair_id == 13 :
                        if integer[3] == '1':
                            C5_Def_Program.play_music(38,lan,2)
                        else :
                            C5_Def_Program.play_music(39,lan,2)
                            
                except Exception as exc:
                    C5_Def_Program.play_music(31,lan,2)
                    
                C1_Def_File.clear_cyberon()

            #time.sleep(0.1)
            #subcount = subcount + 1   
    
        #C4_Def_Gpio.Write_Iris_LED(2)       
        #C5_Def_Program.play_music(5,lan,2)
        