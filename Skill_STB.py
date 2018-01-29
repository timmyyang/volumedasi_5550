'''
first_inital = 1 or 0 :
first use this skills

pair_id :
voice text ,pair id 

lan:
user's language

'''
def Network_STB(first_inital,pair_id,lan) 
    app = '0' ; ip = 'http://192.168.1.150:7070/'
    Andromeda_ID  = C1_Def_File.get_iris_conf('Andromeda_ID')
    #ip = 'http://211.75.14.235:7070/'
    try:
        C4_Def_Gpio.Write_Iris_LED(2)
        
        if pair_id == 0:
            C5_Def_Program.play_music(45,lan,2)
            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'open', 'uri':''}
            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            app = 'LiveTV'
            
        elif pair_id == 1:
            C5_Def_Program.play_music(46,lan,2)
            payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'open', 'uri':''}
            r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            app = 'MediaStore'  
            
        #elif pair_id == 2:
        #    C1_Def_File.ir_file_set('back')
            
        elif app == 'LiveTV':  
            if pair_id == 16:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'close', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                app = '0'
            elif pair_id == 2:
                C1_Def_File.ir_file_set('back')
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'close', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                app = '0'
            elif pair_id == 10:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'change to channel 3', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 11:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'change to channel 49', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 12:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'LiveTV', 'message':'change to channel 50', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)  
                
        elif app == 'MediaStore' :   
            if pair_id == 2:
                C1_Def_File.ir_file_set('back')
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'back', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                app = '0'
            elif pair_id == 3:
                C5_Def_Program.play_music(47,lan,2)
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'video', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 4:
                C5_Def_Program.play_music(48,lan,2)
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'audio', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 5:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'stop', 'uri':''}
                r=r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 6:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'play', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 7:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'pause', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 13:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'play wonderland', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 14:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'play snowboard', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 15:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'play redbull', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
            elif pair_id == 16:
                payload = {'broadcast': 'N', 'username': Andromeda_ID  , 'title':'MediaStore', 'message':'close', 'uri':''}
                r=C3_Def_link.requests_command_payload(ip + "notification.do?action=send",payload,5)
                app = '0'
                    
    except Exception as exc:
        C5_Def_Program.play_music(31,lan,2)
        
    C1_Def_File.clear_cyberon()             