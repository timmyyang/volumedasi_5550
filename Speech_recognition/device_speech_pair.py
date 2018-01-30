# -*- coding: UTF-8 -*-
word_device = {
    "TurnOnTheLight" : 0,
    "TurnTheLightOn" : 0,
    "SwitchOnTheLight" : 0,
    "SwitchTheLightOn" : 0,
    "TurnOnTheTv" : 1,
    "TurnTheTVOn" : 1,
    "SwitchOnTheTV" : 1,
    "SwitchTheTVOn" : 1,
    "TurnOnTheFan" : 2,
    "TurnTheFanOn" : 2,
    "SwitchOnTheFan" : 2,
    "SwitchTheFanOn" : 2,
    "TurnOnTheSoundMachine" : 3,
    "TurnTheSoundMachineOn" : 3,
    "SwitchOnTheSoundMachine" : 3,
    "SwitchTheSoundMachineOn" : 3,
    "TurnOffTheLight" : 4,
    "TurnTheLightOff" : 4,
    "SwitchOffTheLight" : 4,
    "SwitchTheLightOff" : 4,
    "TurnOffTheTv" : 5,
    "TurnTheTvOff" : 5,
    "SwitchOffTheTv" : 5,
    "SwitchTheTvOff" : 5,
    "TurnOffTheFan" : 6,
    "TurnTheFanOff" : 6,
    "SwitchOffTheFan" : 6,
    "SwitchTheFanOff" : 6,
    "TurnOffTheSoundMachine" : 7,
    "TurnTheSoundMachineOff" : 7,
    "SwitchOffTheSoundMachine" : 7,
    "SwitchTheSoundMachineOff" : 7,
    "TurnOnAllTheDevices" : 8,
    "TurnAllTheDevicesOn" : 8,
    "SwitchOnAllTheDevices" : 8,
    "SwitchAllTheDevicesOn" : 8,
    "TurnOffAllTheDevices" : 9,
    "TurnAllTheDevicesOff" : 9,
    "SwitchOffAllTheDevices" : 9,
    "SwitchAllTheDevicesOff" : 9,
    "IsTheLightOn" :10,
    "CanYouTellMeIfTheLightIsOn" :10,
    "IsTheLightTurnOn" :10,
    "IsTheLightSwitchOn" :10,
    "IsTheTvOn" :11,
    "CanYouTellMeIfTheTVIsOn" :11,
    "IsTheTVTurnOn" :11,
    "IsTheTVSwitchOn" :11,
    "IsTheFanOn" :12,
    "CanYouTellMeIfTheFanIsOn" :12,
    "IsTheFanTurnOn" :12,
    "IsTheFanSwitchOn" :12,
    "IsTheSoundMachineOn" :13,
    "CanYouTellMeIfSoundMachineIsOn" :13,
    "IsTheSoundMachineTurnOn" :13,
    "IstheSoundMachineSwitchOn" :13,
    #"GoodBye" : 100 ,
    "SeeYouLater" : 100,
    "GoBackToSkills" : 100
    
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
    
