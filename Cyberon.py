# -*- coding: UTF-8 -*-
import ./Speech_recognition/main_speech_pair
import ./Speech_recognition/device_speech_pair
import Library

clistener_mapping = {
    'main' : "/usr/bin/main",
    'device' : "/usr/bin/device",
    'controller' : "/usr/bin/controller",
    'STB' : "/usr/bin/STB",
    'radio' : "/usr/bin/radio",
    'voip' : "/usr/bin/voip"
}

clistener_mapping_de = {
    0 : "/usr/bin/Command_0407",
    1 : "/usr/bin/Command_0407"
}

"""

"""

def clistten(lan,skill,need_kill):
    if need_kill == 1:
        kill_program('CListenerDemo_x86')
        
    command = '/usr/bin/CListenerDemo_x86 TW' +  clistener_mapping[skill] + ' 0'    
    start_program_wait(command)
"""
return 1 = range in +-20

return 0 = range out +-20
"""

def angle_calc(angle ,angle_degree):
    calc_final = abs( float (angle_degree) - float ( angle ) )  / 20.0 
    if  calc_final <=  1.0  or  calc_final >= 17.0 :
        return 1
    else :
        return 0
        
"""
ex: when you say go iris , the angle = 350 degree ,then you say something , the other angle = +-20 degree ,you will mapping
"""    

def word_mapping(lan,skill,angle):
    try:
        angle_degree = file_get('/tmp/file/angle')
        angle_final = angle_calc(angle ,angle_degree)
        if angle_final == 1:
            if lan == "EN":
                if skill == 'main':
                    pair_id = main_speech_pair.word_main_mapping()
                elif skill == 'help':
                    pair_id = main_speech_pair.word_main_mapping()
                elif skill == 'device':
                    pair_id = device_speech_pair.word_main_mapping()
                elif skill == 'channel':
                    pair_id = word_mapping()
                elif skill == 'controller':
                    pair_id = word_controller()
                elif skill == 'STB':
                    pair_id = word_Andromeda()
                elif skill == 'radio':
                    pair_id = word_radio()
                elif skill == 'voip':
                    pair_id = word_voip() 
        else :
            pair_id = 9999
    except Exception as exc:
        pair_id = 9999
        
    return pair_id
    
def word_mapping_no_angle(lan,skill):

    try:
        if lan == "EN":
            if skill == 'main':
                pair_id = main_speech_pair.word_main_mapping()
            elif skill == 'help':
                pair_id = main_speech_pair.word_main_mapping()
            elif skill == 'device':
                pair_id = device_speech_pair.word_main_mapping()
            elif skill == 'channel':
                pair_id = word_mapping()
            elif skill == 'controller':
                pair_id = word_controller()
            elif skill == 'STB':
                pair_id = word_Andromeda()
            elif skill == 'radio':
                pair_id = word_radio()
            elif skill == 'voip':
                pair_id = word_voip() 

    except Exception as exc:
        pair_id = 9999
        
    return pair_id
    
def cspotter_check(lan):
    f = Library.file_get('/tmp/file/cspotter')
    if f == "Go Iris" or f == "Iris":
        Library.file_set('/tmp/file/cspotter','0')
        angle = C1_Def_File.angle_get()
        return 1 , angle
    else 
        return 0 , 0
        