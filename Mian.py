# -*- coding: UTF-8 -*-
import Library
import Inital
import Sound_list
import time 


class IRIS():
    def start_initial(self):
        Inital.inital_device()
        Center_need_to_play(3,lan,2)
        Library.file_set('/tmp/file/bmp_set','hello') # oled set
        Library.Write_Power_LED(0)
        
    def start_recognition(self):
        lan = Library.get_iris_conf('language')
        stream_state = 0 ;brocast_time = 0 ;wifi_count = 0 ;quantenna_time = 0 ;Line = 1 ;choice = 0 ;talk = 0 ;tmp_voip = 0 ;party_mode = 0
        Library.start_program_wait("/usr/bin/CSpotterDemo_x86 /usr/bin/Trigger.bin&")
    
        while True:
            #step 1 : check iris
            choice , angle = cspotter_check(lan)
            #step 2 : check voip
            voip_state = Library.file_get('/tmp/file/sound_busy_check')
            #step 3 : check party mode or ann
            stream_state = D1_Center.call_group_iris(stream_state)
            
            


if __name__ == '__main__':
    e = IRIS()
    e.start_initial()
    e.start_recognition()
    