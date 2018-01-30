# -*- coding: UTF-8 -*-
word_main_mapping = {
    "TurnUpTheVolume" : 1,
    "TurnTheVolumeUp" : 1,
    "TurnDownTheVolume" : 2,
    "TurnTheVolumeDown" : 2,
    "MaxVolume" : 3,
    "MinVolume" : 4,
    "VolumeMute" : 5,
    "TurnOnAnnouncementMode" : 51,
    "AnnouncementMode" : 51,
    "TurnOffAnnouncementMode" : 52,
    "AnnouncementModeOff" : 52,
    "TurnOnPartyMode" : 71,
    "PartyMode" : 71,
    "TurnOffPartyMode" : 72,
    "PartyModeOff" : 72,
    "DeviceMode" : 101,
    "IoTSmartHome" : 101,
    "SmartHome" : 101,
    "SmartHomeOff" : 102,
    "PhoneCalls" : 10,
    "TurnOnRemoteControlMode" : 501,
    "RemoteControlMode" : 501,
    "ConnectToTheSetTopBox" :1001,
    "SetTopBoxMode" :1001,
    "TurnOnTheInternetRadio" : 1501,
    "TurnTheInternetRadioOn" : 1501,
    "GoodBye" : 50,
    "SeeYouLater" : 50
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

def main_mapping()
    f = open('/tmp/file/clisten', 'r').read().strip()
    f_tmp = f
    word_check = 0
    while word_check < len(word_detct_check):
        info = f_tmp.find(word_detct_check[word_check])
        if info >= 0:
            f = word_reorganization[word_detct_check[word_check]]
            break
        word_check = word_check + 1
   pair_id = main_speech_pair.word_main_mapping[f]
   return pair_id
    
