import Library
import Sound_list
'''
first_inital = 1 or 0 :
first use this skills

skill_need_keep = 1 or 0 : 
keep don't need to say iris 

pair_id :
voice text ,pair id 

lan:
user's language

'''
device_list = {
    103 : 0 ,
    104 : 1 ,
    105 : 2 ,
    106 : 3 ,
    107 : 0 ,
    108 : 1 ,
    109 : 2 ,
    110 : 3 ,
    111 : 4 ,
    112 : 4 
}
power_control_link = {
    0 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=1&WAP1600_VALUE_2=0&WAP1600_VALUE_3=0&WAP1600_VALUE_4=0&homepage=8",
    1 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=0&WAP1600_VALUE_2=1&WAP1600_VALUE_3=0&WAP1600_VALUE_4=0&homepage=8",
    2 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=0&WAP1600_VALUE_2=0&WAP1600_VALUE_3=1&WAP1600_VALUE_4=0&homepage=8",
    3 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=0&WAP1600_VALUE_2=0&WAP1600_VALUE_3=0&WAP1600_VALUE_4=1&homepage=8",
    4 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=0&WAP1600_VALUE_2=1&WAP1600_VALUE_3=1&WAP1600_VALUE_4=1&homepage=8",
    5 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=1&WAP1600_VALUE_2=0&WAP1600_VALUE_3=1&WAP1600_VALUE_4=1&homepage=8",
    6 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=1&WAP1600_VALUE_2=1&WAP1600_VALUE_3=0&WAP1600_VALUE_4=1&homepage=8",
    7 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=1&WAP1600_VALUE_2=1&WAP1600_VALUE_3=1&WAP1600_VALUE_4=0&homepage=8",
    8 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=1&WAP1600_VALUE_2=1&WAP1600_VALUE_3=1&WAP1600_VALUE_4=1&homepage=8",
    9 :  "http://192.168.1.150/WAP-1600.php?WAP1600_VALUE_1=0&WAP1600_VALUE_2=0&WAP1600_VALUE_3=0&WAP1600_VALUE_4=0&homepage=8"
}
def power_command(need_command , command_number):
    if need_command == 1:
        try :
            #print(power_control_link[command_number])
            a = power_control_link[command_number]
        except Exception as exc:
            a = 99
        return a

'''
def device_save(pair_id):
    f_tmp=file_get('/tmp/file/device')
    #f = open(file, 'r').read().strip()
    #return f#f_tmp = open('/tmp/file/device','r').read().strip()
    if pair_id <107 :
        f_tmp = list(f_tmp)
        f_tmp[device_list[pair_id]]= '1'
        f_tmp = ''.join(f_tmp)
    if pair_id >=107 and pair_id <111:
        f_tmp = list(f_tmp)
        f_tmp[device_list[pair_id]]= '0'
        f_tmp = ''.join(f_tmp)
    #if set_id ==8 :
    #    f_tmp = '11111'
    #if set_id ==9:
    #    f_tmp = '00000'
    file_set('/tmp/file/device',f_tmp)    
'''

def Device_skill(first_inital,pair_id,lan): 
             
    Write_Iris_LED(2)
    subcount = 100
    try:
        url = "http://192.168.1.150/volume/user_file/1600.txt"
        r = requests_command(url,3) 
        pos=r.text.index('results') 
        integer=r.text[(pos+7):len(r.text)].strip('":} \r\n')
        if pair_id < 113 :
			sound = Sound_list.iris_play(pair_id,lan,1)
	        play_music_file_wait(sound)
               
            #device_save(pair_id)      
            url = power_command(1,pair_id)
            r = requests_command(url,3)   
        elif pair_id == 201 :
            if integer[0] == '1':
                sound = Sound_list.iris_play(201,lan,'device')
	            play_music_file_wait(sound)
            else :
				sound = Sound_list.iris_play(202,lan,'device')
	            play_music_file_wait(sound)
        elif pair_id == 203 :
            if integer[1] == '1':
			    sound = Sound_list.iris_play(203,lan,'device')
	            play_music_file_wait(sound)
            else :
			    sound = Sound_list.iris_play(204,lan,'device')
	            play_music_file_wait(sound)
        elif pair_id == 205 :
            if integer[2] == '1':
                sound = Sound_list.iris_play(205,lan,'device')
	            play_music_file_wait(sound)
            else :
                sound = Sound_list.iris_play(206,lan,'device')
	            play_music_file_wait(sound)

        elif pair_id == 207 :
            if integer[3] == '1':
                sound = Sound_list.iris_play(207,lan,'device')
	            play_music_file_wait(sound)
            else :
                sound = Sound_list.iris_play(208,lan,'device')
	            play_music_file_wait(sound)
                            
    except Exception as exc:
        sound = Sound_list.iris_play(500,lan,2)
	    play_music_file_wait(sound)

        
    file_set('/tmp/file/clisten','0')

            
        