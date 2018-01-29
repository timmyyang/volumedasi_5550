import subprocess
import time
import C6_Def_Sound_list,C1_Def_File
import select

def strat_cyberon(lan,main,sub):    
    #subprocess.Popen('/usr/bin/CSpotterDemo_x86 /usr/bin/Trigger.bin', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    file = C1_Def_File.cyberon_file(lan,main,sub)
    if main == 0:
        #subprocess.Popen('/usr/bin/CSpotterDemo_x86 /usr/bin/Trigger.bin', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        subprocess.Popen(['/usr/bin/CSpotterDemo_x86' ,file])
    else :
        subprocess.Popen(['/usr/bin/CListenerDemo_x86', lan ,file, '0'])
        
def strat_cyberon_loop(lan,main,sub): 
    file = C1_Def_File.cyberon_file(lan,main,sub)
    subprocess.Popen(['/usr/bin/CListenerDemo_loop', lan ,file, '0'])
    
def strat_cyberon_clistener():
    #subprocess.Popen('/usr/bin/CSpotterDemo_x86 /usr/bin/Trigger.bin', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    subprocess.Popen(['/usr/bin/CListenerDemo_x86', 'TW' ,'/usr/bin/Command_0404', '0'])
    
def strat_cyberon_clistener_for_party_mode():    
    subprocess.Popen('/usr/bin/CSpotterDemo_x86 /usr/bin/Trigger.bin', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #subprocess.Popen(['/usr/bin/CListenerDemo_x86', 'TW' ,'/usr/bin/part_mode', '0'])
    
def kill_cyberon_cspotter():
    subprocess.Popen('killall -9 CSpotterDemo_x86', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    C1_Def_File.clear_cyberon()
    
def kill_cyberon_clistener():
    subprocess.Popen('killall -9 CListenerDemo_x86', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    C1_Def_File.clear_cyberon()
    
def kill_cyberon_clistener_loop():
    subprocess.Popen('killall -9 CListenerDemo_loop', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    C1_Def_File.clear_cyberon()

def start_program(command):
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
def kill_program(command):
    subprocess.Popen(['killall' ,'-9' ,command]).wait()
    
def play_music(set_id,lan,child):
    party_mode_pause(1)
    sound = C6_Def_Sound_list.iris_play(set_id,lan,child)
    command = 'madplay ' + sound + ' -o wave:- - | aplay -M'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    
def play_music_no_wait(set_id,lan,child):
    party_mode_pause(1)
    sound = C6_Def_Sound_list.iris_play(set_id,lan,child)
    command = 'madplay ' + sound + ' -o wave:- - | aplay -M'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
def play_music_file(file):
    command = 'madplay ' + file + ' -o wave:- - | aplay -M'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    
def play_music_keep(set_id,lan,child):
    sound = C6_Def_Sound_list.iris_play(set_id,lan,child)
    command = 'madplay ' + sound + ' -r -o wave:- - | aplay -M'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
def play_music_url(url):
    command = 'wget -q -O - ' + url + '   | madplay - -o wave:- | aplay -M&'
    r = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return r
    
def play_music_file_no_music_start(file):
    time.sleep(1)
    command = 'madplay ' + file + ' -o wave:- - | aplay -M'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(1)
    
def play_music_file_keep_no_music_start(file):
    party_mode_pause(1)
    command = 'madplay ' + file + ' -r -o wave:- - | aplay -M'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(1)
    
def kill_play():
    subprocess.Popen(["killall" ,"-9" , "madplay" ,"aplay"]).wait()
    
def kill_play_stream():
    subprocess.Popen(["killall" ,"-9" , "wget" ,"aplay"]).wait()
    
def selete_avoid_stop(r,time_out):
    poll_obj = select.poll()
    poll_obj.register(r.stdout, select.POLLIN)
    result = 0 ;count = 0
    for i in range(0 , time_out , 1):
        poll_result = poll_obj.poll(0)
        if poll_result:
            result_stream = r.stdout.readline()
            count += 1
            if count == 2:
                try:
                    if result_stream[0] == 'w':
                        return 1 #process done
                    else:
                        return 0
                except Exception as exc:
                    return 0
                    
        time.sleep(1)
    return 1
    
    
def control_volume(n):
    #subprocess.Popen(["amixer" ,"cset" ,"numid=2,iface=MIXER,name='MaxxVolume Control'" ,str(n)]).wait()
    command = "amixer cset numid=1,iface=MIXER,name='MaxxVolume Control' "  + str(n)
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    
def file_reset():
    f = open('/tmp/file/stream_check','w')
    f.write('0')
    f.close()
    f = open('/tmp/file/snapclient','w')
    f.write('1')
    f.close()
    
def button_trigger_reset(n):
    if n == '1':
        party_mode_off()
        file_reset()
    if n == '3':
        Announcement_Mode_Off()
        file_reset()  
    if n == '5':
        Ktv_off()
        file_reset()      
        
def party_mode_on():
    time.sleep(1)
    stream_ip = C1_Def_File.Get_stream_ip()

    command = "killall -9 snapclient_AIR"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    
    #####TMP##########
    command = 'amixer -c0 cset name="Channel Control" "1"'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    #####TMP##########
    
    command = "snapclient_AIR -d -h " + stream_ip
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    file_reset()
        
    
def party_mode_off():
    command = "killall -9 snapclient_AIR"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    
    #####TMP##########
    command = 'amixer -c0 cset name="Channel Control" "0"'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    #####TMP##########
    
    command = "/etc/init.d/snapclient start"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    file_reset()
    
def Announcement_Mode_On():
    time.sleep(1)
    stream_ip = C1_Def_File.Get_stream_ip()
    volume = 3
    control_volume(volume)
    command = "wget -q -O - http://" + stream_ip + ":8090/test1.wav | aplay&"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    file_reset()
    
def Announcement_Mode_Off():
    command = "killall -9 wget aplay"
    volume = C1_Def_File.get_iris_conf('volume_set')
    control_volume(volume)
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    file_reset()

def check_party_mode_music_time_out():
    f = open('/tmp/file/snapclient', 'r').read().strip()
    if f == '2':
        #print '*************party mod time out************'
        party_mode_off()
        return 0
    if f != '2':
        return 1
        
def inital_device():
    #print '*************inital_device************'

    #volume = C1_Def_File.get_iris_conf('volume_set')
    #subprocess.Popen("amixer cset numid=2,iface=MIXER,name='MaxxVolume Control' "+volume, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    C1_Def_File.choice_file_set('/tmp/file/cspotter', '0')
    C1_Def_File.choice_file_set('/tmp/file/clisten', '0')
    C1_Def_File.choice_file_set('/tmp/file/stream_check', '0')
    #C1_Def_File.choice_file_set('/tmp/file/sound_busy_check', '0')
    C1_Def_File.choice_file_set('/tmp/file/device', '00000')
    C1_Def_File.choice_file_set('//tmp/file/answer', '00000')
    master_quantenna_mac = C1_Def_File.get_iris_conf('master_quantenna_mac')
    C1_Def_File.choice_file_set('/tmp/file/master_quantenna_mac', master_quantenna_mac)
    command = "echo '192.168.1.246' > /tmp/file/search_iris"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    command = "echo '192.168.1.247' > /tmp/file/search_quantenna"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    default_quantenna_ip = C1_Def_File.get_iris_conf('default_quantenna_ip')
    C1_Def_File.choice_file_set('/tmp/file/default_quantenna_ip', default_quantenna_ip)
    C1_Def_File.set_iris_conf('radio3',1)
    command = ("ffserver /etc/ffserver.conf&")
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    #command = ("host_demo_iris -u&")
    #subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    #kill_play()
    
def tmp_I():
    command = 'amixer -c0 cset name="Channel Control" "2"'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    
def tmp_II():
    command = 'amixer -c0 cset name="Channel Control" "0"'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 

#start linux cmd
def start_command(cmd):
    command = cmd
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    
#pause the party mode music
def party_mode_pause(value):
    C1_Def_File.music_pause()
    time.sleep(value)
    
#pause the party mode music then start
def party_mode_pause_then_start(value):
    time.sleep(value)
    C1_Def_File.music_start() 
    
    

    
        
