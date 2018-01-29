import D1_Center
import time 

class IRIS():
    def start_initial(self):
        lan = D1_Center.check_language('language')
        D1_Center.All_file_program_reset(lan)
        D1_Center.Brocast_iris_ip()
        return lan
        
    def start_recognition(self,lan):
        stream_state_busy = 0 ;brocast_time = 0 ;wifi_count = 0 ;quantenna_time = 0 ;Line = 1 ;choice = 0 ;talk = 0 ;tmp_voip = 0 ;party_mode = 0;
        D1_Center.main_cspotter(lan)
        while True:
            #try : 
                #--------check start led--------
                #Start_led = D1_Center.check_state_led()
                
                #--------check voip------
                voip_state = D1_Center.check_voip_state()
                
                #check iris talk
                #answer = D1_Center.answer_check()
                choice , angle = D1_Center.main_cspotter_check(lan)
                if voip_state == '9':
                    stream_state_busy = D1_Center.call_group_iris(stream_state_busy)
                    Line = D1_Center.Find_Other_Iris(Line,lan)
                    #if Start_led == 1:
                    #    choice = D1_Center.cspotter(lan , party_mode)
                    
                    if choice == 2 and stream_state_busy == 0:
                        lan = 'EN'
                        party_mode = D1_Center.clistener(lan , party_mode , angle)
                        #D1_Center.main_cspotter(lan)
                        choice = 0 
                        
                    elif choice == 3 and stream_state_busy == 0:
                        lan = 'DE'
                        party_mode = D1_Center.clistener(lan , party_mode , angle)
                        #D1_Center.main_cspotter(lan)
                        choice = 0 


                #--------iris talk-----
                #if talk == 30: 
                #    talk = D1_Center.want_to_talk()
                    #D1_Center.random_init(1,20)
                
                #--------iris answer-----
                #if answer != '00000':
                #    talk = D1_Center.need_to_answer(answer)
                
                #--------voip now------
                elif voip_state != '9' and tmp_voip == 0:
                    D1_Center.call_music_pause()
                    D1_Center.clistener_voip(lan , 0)
                    D1_Center.call_music_start()
                    #D1_Center.main_cspotter(lan)
                    f = open('/tmp/file/bmp_set','w')
                    f.write('hello')
                    f.close() 

                    


                elif quantenna_time == 200 and voip_state == '9':   
                    wifi_count = D1_Center.check_quan_link(wifi_count,lan)  
                    quantenna_time = 0 
                elif  brocast_time == 600000:
                    D1_Center.Brocast_iris_ip()
                    brocast_time = 0 
                    

                quantenna_time += 1
                brocast_time += 1      
                #talk += 1
                time.sleep(0.1) 

            #except Exception as exc:
            #   pass
    
if __name__ == '__main__':
    e = IRIS()
    lan = e.start_initial()
    e.start_recognition(lan)
    
    