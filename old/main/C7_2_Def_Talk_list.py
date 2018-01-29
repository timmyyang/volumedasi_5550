# -*- coding: UTF-8 -*-
word_mapping = {
    "MonoChannel" : 0,
    "LeftChannel" : 1,
    "RightChannel" : 2,
    "GoodByeSkill" : 3,
    "Fight" : 903,
    "Expelliarmus" : 904
}

word_mapping_de = {
    "Mach dasLichtAn" : 0,
    "Mach denFernseherAn" : 1
}


def iris_mapping(lan):
    try:   
        f = open('/tmp/file/clisten', 'r').read().strip()
        #print ("clisten = " , f)
        word_id = 999
        if lan == "EN":                   
                word_id = word_mapping[f]
        if lan == "DE":
                word_id = word_mapping_de[f]
    except Exception as exc:
        word_id = 999
        pass
    return word_id
    
