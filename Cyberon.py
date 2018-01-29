# -*- coding: UTF-8 -*-

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
return 1 = range in +-20

return 0 = range out +-20
"""    

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