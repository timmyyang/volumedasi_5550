import Library

def Get_stream_ip():
    f = open('/tmp/file/stream_check')
    f = f.readlines()[1]
    f = f.strip()
    return f
    
def Get_stream_state():
    f = open('/tmp/file/stream_check')
    f = f.readlines()[0]
    f = f.strip()
    return f
    
def file_reset():
    Library.file_set('/tmp/file/stream_check','0')
    Library.file_set('/tmp/file/snapclient','1')
    
def party_mode_on():
    stream_ip = Get_stream_ip()
    Library.kill_program('snapclient_AIR')
    command = "snapclient_AIR -d -h " + stream_ip
    Library.start_program_wait(command)
    file_reset()
        
    
def party_mode_off():
    stream_ip = Get_stream_ip()
    Library.kill_program('snapclient_AIR')
    command = "/etc/init.d/snapclient start"
    Library.start_program_wait(command)
    file_reset()
    
def Announcement_Mode_On(stream_volume):
    stream_ip = Get_stream_ip()
    volume = Announcement_volume
    Library.control_volume(volume)
    command = "wget -q -O - http://" + stream_ip + ":8090/test1.wav | aplay&"
    Library.start_program_wait(command) 
    file_reset()
    
def Announcement_Mode_Off():
    command = "killall -9 wget aplay"
    volume = Library.get_iris_conf('volume_set')
    control_volume(volume)
    Library.start_program_wait(command) 
    file_reset()

    
"""
stream_state_busy = tell machine you are going to play now
"""
def stream_check(stream_state_busy , stream_volume):

    stream_state = Get_stream_state
    if stream_state != '0':
    
        if stream_state == '1':
            #print '***********party mode on now***************'
            party_mode_on()
            stream_state_busy = 1
        elif stream_state == '2':
            #print '***********party mode off now***************'
            party_mode_off()
            stream_state_busy = 0
        elif stream_state == '3':
            #print '***********AnnouncementModeOn now***************'
            Announcement_Mode_On()
            stream_state_busy = 2
        elif stream_state == '4':
            #print '***********AnnouncementModeOff now***************'
            Announcement_Mode_Off()
            stream_state_busy = 0
            
    return stream_state_busy  