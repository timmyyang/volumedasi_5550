#device,...
audio_play_device_en = {
    103 :  "./audio/en/device/103_OK_Turn_On_The_Light.mp3",
    104 :  "./audio/en/device/104_OK_Turn_On_The_TV.mp3",
    105 :  "./audio/en/device/105_OK_Turn_On_The_Fan.mp3",
    106 :  "./audio/en/device/106_OK_Turn_On_Sound_Machine.mp3",
    107 :  "./audio/en/device/107_OK_Turn_Off_The_light.mp3",
    108 :  "./audio/en/device/108_OK_Turn_Off_The_TV.mp3",
    109 :  "./audio/en/device/109_OK_Turn_Off_all_The_Fan.mp3",
    110 :  "./audio/en/device/110_OK_Turn_off_all_The_Machine.mp3",
    111 :  "./audio/en/device/111_OK_Turn_On_All_The_Devices.mp3",
    112 :  "./audio/en/device/112_OK_Turn_Off_All_The_Devices.mp3",
	201 :  "./audio/en/device/153_Light_is_on.mp3",
    202 :  "./audio/en/device/154_Light_is_off.mp3",
    203 :  "./audio/en/device/155_Tv_is_on.mp3",
    204 :  "./audio/en/device/156_Tv_is_off.mp3",
    205 :  "./audio/en/device/157_Fan_is_on.mp3",
    206 :  "./audio/en/device/158_Fan_is_off.mp3",
    207 :  "./audio/en/device/159_Soundmachine_is_on.mp3",
    208 :  "./audio/en/device/160_Soundmachine_is_off.mp3",
	500 :  "./audio/en/public/Please_check_net.mp3"
}


def iris_play(pair_id,lan,skill):
    if lan=='EN':
        if skill=='device':
            playback = audio_play_device_en[pair_id]
        
    if lan=='DE':
        if skill=='device':
            playback = audio_play_de[pair_id]
            
    return playback