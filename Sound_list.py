device_play_en = {
    0 :  "/root/audio/en/0_OK_Turn_On_The_Light.mp3",
    1 :  "/root/audio/en/1_OK_Turn_On_The_TV.mp3",
    2 :  "/root/audio/en/2_OK_Turn_On_The_Fan.mp3",
    3 :  "/root/audio/en/3_Turn_On_Sound_Machine.mp3",
    4 :  "/root/audio/en/4_OK_Turn_Off_The_light.mp3",
    5 :  "/root/audio/en/5_OK_Turn_Off_The_TV.mp3",
    6 :  "/root/audio/en/6_OK_Turn_Off_all_The_Fan.mp3",
    7 :  "/root/audio/en/7_OK_Turn_off_all_The_Machine.mp3",
    8 :  "/root/audio/en/8_OK_Turn_On_All_The_Devices.mp3",
    9 :  "/root/audio/en/9_OK_Turn_Off_All_The_Devices.mp3",
    10:  "/root/audio/en/10_hang_up.mp3",
    11 : "/root/audio/en/11_calling_mom.mp3",
    12 : "/root/audio/en/12_calling_home.mp3",
    13:  "/root/audio/en/13_OK_Take_The_Call.mp3",
    14:  "/root/audio/en/14_OK_Announcement_Mode_On.mp3",
    15:  "/root/audio/en/15_OK_Announcement_Mode_Off.mp3",
    16:  "/root/audio/en/16_OK_Party_Mode_On.mp3",
    17:  "/root/audio/en/17_OK_Party_Mode_Off.mp3",
    18:  "/root/audio/en/18_OK_GO_alexa.mp3",
    19:  "/root/audio/en/19_OK_GO_iris.mp3",
    20:  "/root/audio/en/20_OK_Turn_Volume_Up.mp3",
    21:  "/root/audio/en/21_OK_Turn_Volume_Down.mp3",
    22:  "/root/audio/en/22_OK",
    23:  "/root/audio/en/23_Ding.mp3", 
    24:  "/root/audio/en/24_Ding.mp3",     
    25:  "/root/audio/en/25_Play_the_Music.mp3",
    27:  "/root/audio/en/27_OK_Search_The_Iris.mp3",
    28:  "/root/audio/en/28_Iris_search_down.mp3",
    29:  "/root/audio/en/29_Time_To_Eat.mp3",
    30:  "/root/audio/en/30_Start_Wifi.mp3",
    31:  "/root/audio/en/31_Show_Your_Voice.mp3",
    32:  "/root/audio/en/32_Ok_Push_Wps.mp3",
    33:  "/root/audio/en/33_Ok_connect_the_iris.mp3",
    34:  "/root/audio/en/34_Ready_to_turning.mp3",
    35:  "/root/audio/en/35_Ir_turn_on.mp3",
    36:  "/root/audio/en/36_Radio_turn_on.mp3",
    37:  "/root/audio/en/37_Andromeda_turn_on.mp3"
}


def audio_play(pair_id,lan,skill):
    if lan=='EN':
        if skill=='device':
            playback = device_play_en[pair_id]
            return playback
        if skill=='radio':
            playback = audio_main_play_en[pair_id]
            return playback     
        
    if lan=='DE':
        if skill=='device':
            playback = audio_play_de[pair_id]
            return playback
        if skill=='radio':
            playback = audio_main_play_de[pair_id]
            return playback 