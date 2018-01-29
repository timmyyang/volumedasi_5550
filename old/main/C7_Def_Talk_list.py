# -*- coding: UTF-8 -*-
import requests
word_mapping = {
    "DeviceMode" : 0,
    "IoTSmartHome" : 0,
    "SmartHome" : 0,
    "TurnOnTheLight" : 0,
    "TurnOnTheTv" : 1,
    "TurnOnTheFan" : 2,
    "TurnOnTheSoundMachine" : 3,
    "TurnOffTheLight" : 4,
    "TurnOffTheTv" : 5,
    "TurnOffTheFan" : 6,
    "TurnOffTheSoundMachine" : 7,
    "TurnOnAllTheDevices" : 8,
    "TurnOffAllTheDevices" : 9,
    "PhoneCalls" : 10,
    "CallMyDad" : 10,
    "CallMyMom" : 11,
    "CallMyHome" : 12,
    "TakeTheCall" : 13,
    "PickUpTheCall" : 13,
    "TurnOnAnnouncementMode" : 14,
    "AnnouncementMode" : 14,
    "AnnouncementModeOff" : 15,
    "TurnOnPartyMode" : 16,
    "PartyMode" : 16,
    "PartyModeOff" : 17,
    "GoAlexa" : 18,
    "goiris" : 19,
    "TurnUpTheVolume" : 20,
    "TurnTheVolumeUp" : 20,
    "TurnDownTheVolume" : 21,
    "TurnTheVolumeDown" : 21,
    "MaxVolume" : 22,
    "MinVolume" : 23,
    "VolumeMute" : 24,
    "PlayTheMusic" : 25,
    "StopTheMusic" : 26,
    "SearchTheIris" : 27,
    "TimeToEat" : 29,
    "WifiUp" : 30,
    "SingTheSong" : 31,
    "PushWps" : 32,
    "HelpConnect" : 33,
    "ToneTuning" : 34,
    "TurnOnRemoteControlMode" : 35,
    "RemoteControlMode" : 35,
    "TurnOnTheInternetRadio" : 36,
    "TurnTheInternetRadioOn" : 36,
    "ConnectToTheSetTopBox" :37,
    "SetTopBoxMode" :37,
    "IsTheLightOn" :38,
    "IsTheTvOn" :39,
    "IsTheFanOn" :40,
    "IsTheSoundMachineOn" :41,
    "TurnOnTheInternetRadioInOneMinute" : 42,
    "StandByMode" : 98,
    "GoIris" : 99,
    #"GoodBye" : 100,
    "SeeYouLater" : 100,
    "SuperTrouperBeams" : 101,
    "Lumos" : 901,
    "Stupefy" : 902,
    "Fight" : 903
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

word_device_redetect = {
    0 :"TurnOnTheLight" ,
    1 :"TurnOnTheTv" ,
    2 :"TurnOnTheFan" ,
    3 :"TurnOnTheSoundMachine" ,
    4 :"TurnOffTheLight" ,
    5 :"TurnOffTheTv" ,
    6 :"TurnOffTheFan" ,
    7 :"TurnOffTheSoundMachine" 
    #8 :"TurnOnAllTheDevices" ,
    #9 :"TurnOffAllTheDevices" 
}

word_device_redetect_get_number = {
    "TurnOnTheLight" : 0,
    "TurnOnTheTv" : 1,
    "TurnOnTheFan" : 2,
    "TurnOnTheSoundMachine" : 3,
    "TurnOffTheLight" : 0,
    "TurnOffTheTv" : 1,
    "TurnOffTheFan" : 2,
    "TurnOffTheSoundMachine" : 3,
    "TurnOnAllTheDevices" : 4,
    "TurnOffAllTheDevices" : 4
}

word_device_redetect_change = {
    0 :"TurnOffTheLight" ,
    1 :"TurnOffTheTv" ,
    2 :"TurnOffTheFan" ,
    3 :"TurnOffTheSoundMachine" ,
    4 :"TurnOnTheLight" ,
    5 :"TurnOnTheTv" ,
    6 :"TurnOnTheFan" ,
    7 :"TurnOnTheSoundMachine" ,
    8 :"TurnOffAllTheDevices" ,
    9 :"TurnOnAllTheDevices" 
}

word_mapping_de = {
    "Mach dasLichtAn" : 0,
    "Mach denFernseherAn" : 1,
    "Mach denVentilatorAn" : 2,
    "Mach dieTonmaschineAn" : 3,
    "Mach dasLichtAus" : 4,
    "Mach denFernseherAus" : 5,
    "Mach denVentilatorAus" : 6,
    "Mach dieTonmaschineAus" : 7,
    "Mach alleGerateAn" : 8,
    "Mach alleGerateAus" : 9,
    "Ruf meinenPapaAn" : 10,
    "Ruf meinenMamaAn" : 11,
    "Ruf meinenHauseAn" : 12,
    "Nimm den Anruf an" : 13,
    "Durchsage Modus an" : 14,
    "Durchsage Modus aus" : 15,
    "party modus an" : 16,
    "party modus aus" : 17,
    "Auf geht's Alexa" : 18,
    "Auf geht's Iris" : 19,
    "Lauter" : 20,
    "Leiser" : 21,
    "Maximale Lautstarke" : 22,
    "Minimale Lautstarke" : 23,
    "Stumm" : 24,
    "Mach dieMusikAn" : 25,
    "Mach dieMusikAus" : 26,
    "Such mal nach Iris" : 27,
    "Zeit zum Essen" : 29,
    "Ich brauche WLAN" : 30,
    "Sing mal" : 31,
    "Beide WLAN-Gerate vrerbinden" : 32,
    "Internet verbinden" : 33,
    "Hallo Iris" : 99,
    "Auf Wiedersehen" : 100,
    "SuperTrouperBeams" : 101
}
def angle_calc(angle ,angle_degree):
    calc_final = abs( float (angle_degree) - float ( angle ) )  / 20.0 
    if  calc_final <=  1.0  or  calc_final >= 17.0 :
        return 1
    else :
        return 0
        


def iris_mapping(lan , angle):
    try:
        f = open('/tmp/file/clisten', 'r').read().strip()
        f_tmp = f
        #print ("clisten = " , f)
        
        if lan == "EN":
            '''
            word_check = 0
            while word_check < len(word_detct_check):
                info = f_tmp.find(word_detct_check[word_check])
                if info >= 0:
                    f = word_reorganization[word_detct_check[word_check]]
                    break
                word_check = word_check + 1
            '''
            '''
            word_check = 0       
            while word_check < len(word_device_redetect):      
                info = f_tmp.find(word_device_redetect[word_check])
                if info == 0:
                    f_number = word_device_redetect_get_number[f]
                    try:
                        r = requests.get('http://192.168.1.150/volume/user_file/1600_device.txt',timeout=2)
                        device = r.text
                    except Exception as exc:
                        device = open('/tmp/file/device','r').read().strip() 
                    if device[f_number] == '1' and f.find('On') > 0 or device[f_number] == '0' and f.find('Off') > 0:
                        f = word_device_redetect_change[word_check]
                        break
                word_check = word_check + 1  
            '''       
            try:
                angle_degree = open('/tmp/file/angle','r').read().strip()
                angle_final = angle_calc(angle ,angle_degree)
                #if angle_final == 1:
                if angle_final != 100  :
                    word_id = word_mapping[f]
                else :
                    if f != '0':
                        word_id = 1000
                    else:   
                        word_id = 999
            except Exception as exc:
                if f != '0':
                    word_id = 1000
                else:   
                    word_id = 999
        elif lan == "DE":
            try:
                word_id = word_mapping_de[f]
            except Exception as exc:
                if f != '0':
                    word_id = 1000
                else:
                    word_id = 999
    except Exception as exc:
        word_id = 999
    return word_id
    
def iris_mapping_no_angle(lan):
    f = open('/tmp/file/clisten', 'r').read().strip()
    try:
        word_id = word_mapping[f]
    except Exception as exc:
        if f != '0':
            word_id = 1000
        else:   
            word_id = 999
    return word_id
