# -*- coding: UTF-8 -*-
word_device = {
    "TurnOnTheLight" : 103,
    "TurnTheLightOn" : 103,
    "SwitchOnTheLight" : 103,
    "SwitchTheLightOn" : 103,
    "TurnOnTheTv" : 104,
    "TurnTheTVOn" : 104,
    "SwitchOnTheTV" : 104,
    "SwitchTheTVOn" : 104,
    "TurnOnTheFan" : 105,
    "TurnTheFanOn" : 105,
    "SwitchOnTheFan" : 105,
    "SwitchTheFanOn" : 105,
    "TurnOnTheSoundMachine" : 106,
    "TurnTheSoundMachineOn" : 106,
    "SwitchOnTheSoundMachine" : 106,
    "SwitchTheSoundMachineOn" : 106,
    "TurnOffTheLight" : 107,
    "TurnTheLightOff" : 107,
    "SwitchOffTheLight" : 107,
    "SwitchTheLightOff" : 107,
    "TurnOffTheTv" : 108,
    "TurnTheTvOff" : 108,
    "SwitchOffTheTv" : 108,
    "SwitchTheTvOff" : 108,
    "TurnOffTheFan" : 109,
    "TurnTheFanOff" : 109,
    "SwitchOffTheFan" : 109,
    "SwitchTheFanOff" : 109,
    "TurnOffTheSoundMachine" : 110,
    "TurnTheSoundMachineOff" : 110,
    "SwitchOffTheSoundMachine" : 110,
    "SwitchTheSoundMachineOff" : 110,
    "TurnOnAllTheDevices" : 111,
    "TurnAllTheDevicesOn" : 111,
    "SwitchOnAllTheDevices" : 111,
    "SwitchAllTheDevicesOn" : 111,
    "TurnOffAllTheDevices" : 112,
    "TurnAllTheDevicesOff" : 112,
    "SwitchOffAllTheDevices" : 112,
    "SwitchAllTheDevicesOff" : 112,
    #reserve 113~152 for new devices
	"IsTheLightOn" :201,
    "CanYouTellMeIfTheLightIsOn" :201,
    "IsTheLightTurnOn" :201,
    "IsTheLightSwitchOn" :201,
    "IsTheTvOn" :203,
    "CanYouTellMeIfTheTVIsOn" :203,
    "IsTheTVTurnOn" :203,
    "IsTheTVSwitchOn" :203,
    "IsTheFanOn" :205,
    "CanYouTellMeIfTheFanIsOn" :205,
    "IsTheFanTurnOn" :205,
    "IsTheFanSwitchOn" :205,
    "IsTheSoundMachineOn" :207,
    "CanYouTellMeIfSoundMachineIsOn" :207,
    "IsTheSoundMachineTurnOn" :207,
    "IstheSoundMachineSwitchOn" :207,
    "GoodBye" : 500 ,
    "SeeYouLater" : 500
    
}

word_detct_check = {
    0 : "OffTheTheFan" ,  
    1 : "OffTheFan",
    2 : "OnTheTv",
    3 : "OnTheSoundMachine",
    4 : "OffTheTv",
    5 : "OffTheSoundMachine",
    6 : "PlayTheIris",
    7 : "SeeYouIris",
    8 : "Iris",
    9 : "OnTheLight",
    10 : "OffTheLight",
    11 : "OffTheLight",
    12 : "PartyModeSong",
    13 : "PartyMode",
    14 : "AnnouncementModeSong",
    15 : "TheInternetRadio",
    16 : "OnInternetRadio",
    17 : "OffInternetRadio",
    18 : "TheController",
    19 : "OnControllero",
    20 : "OffController",
    21 : "TheAndromeda",
    22 : "OnAndromeda",
    23 : "OffAndromeda"
}

word_reorganization = {
    "OffTheTheFan" : "TurnOffTTheFan" ,  
    "OffTheFan" : "TurnOffTheFan" ,
    "OnTheTv" : "TurnOnTheTv" ,
    "OnTheSoundMachine" : "TurnOnTheSoundMachine" ,
    "OffTheTv" : "TurnOffTheTv" ,
    "OffTheSoundMachine" : "TurnOffTheSoundMachine" ,
    "PlayTheIris" : "Iris" ,
    "Iris" : "Iris" ,
    "OnTheLight" : "TurnOnTheLight" ,
    "OffTheLight" : "TurnOffTheLight",
    "SeeYouIris" : "SeeYouIris",
    "PartyModeSong" :"PartyModeOn",
    "PartyMode" : "PartyModeOn",
    "AnnouncementModeSong" : "AnnouncementModeOn",
    "TheInternetRadio" : "TurnTheInternetRadio",
    "OnInternetRadio" : "TurnOnInternetRadio",
    "OffInternetRadio" : "TurnOffInternetRadio",
    "TheController" : "TurnTheController",
    "OnController" : "TurnOnController",
    "OffController" : "TurnOffController",
    "TheAndromeda" : "TurnTheAndromeda",
    "OnAndromeda" : "TurnOnAndromeda",
    "OffAndromeda" : "TurnOffAndromeda"
    
}

def device_mapping()
    f = open('/tmp/file/clisten', 'r').read().strip()
    f_tmp = f
    word_check = 0
    while word_check < len(word_detct_check):
        info = f_tmp.find(word_detct_check[word_check])
        if info >= 0:
            f = word_reorganization[word_detct_check[word_check]]
            break
        word_check = word_check + 1
   pair_id = main_speech_pair.word_device[f]
   return pair_id
    
