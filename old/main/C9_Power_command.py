import requests

power_on_link = {
    0 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=0&power_3=0&power_4=0",
    1 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=0&power_2=1&power_3=0&power_4=0",
    2 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=0&power_2=0&power_3=1&power_4=0",
    3 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=0&power_2=0&power_3=0&power_4=1",
    4 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=1&power_3=0&power_4=0",
    5 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=0&power_3=1&power_4=0",
    6 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=0&power_3=0&power_4=1",
    7 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=0&power_2=1&power_3=1&power_4=0",
    8 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=0&power_2=1&power_3=0&power_4=1",
    9 :  "http://wilsonliu.me/upload.php?power_on_off=on&power_1=0&power_2=0&power_3=1&power_4=1",
    10 : "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=1&power_3=1&power_4=0",
    11 : "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=1&power_3=0&power_4=1",
    12 : "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=0&power_3=0&power_4=1",
    13 : "http://wilsonliu.me/upload.php?power_on_off=on&power_1=0&power_2=1&power_3=1&power_4=1",
    14 : "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=1&power_3=1&power_4=1",
    15 : "http://wilsonliu.me/upload.php?power_on_off=on&power_1=1&power_2=1&power_3=1&power_4=1"
}

power_off_link = {
    0 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=1&power_3=1&power_4=1",
    1 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=1&power_2=0&power_3=1&power_4=1",
    2 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=1&power_2=1&power_3=0&power_4=1",
    3 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=1&power_2=1&power_3=1&power_4=0",
    4 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=0&power_3=1&power_4=1",
    5 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=1&power_3=0&power_4=1",
    6 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=1&power_3=1&power_4=0",
    7 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=1&power_2=0&power_3=0&power_4=1",
    8 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=1&power_2=0&power_3=1&power_4=0",
    9 :  "http://wilsonliu.me/upload.php?power_on_off=off&power_1=1&power_2=1&power_3=0&power_4=0",
    10 : "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=0&power_3=0&power_4=1",
    11 : "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=0&power_3=1&power_4=0",
    12 : "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=1&power_3=1&power_4=0",
    13 : "http://wilsonliu.me/upload.php?power_on_off=off&power_1=1&power_2=0&power_3=0&power_4=0",
    14 : "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=0&power_3=0&power_4=0",
    15 : "http://wilsonliu.me/upload.php?power_on_off=off&power_1=0&power_2=0&power_3=0&power_4=0"
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

power_show_link = {
    0 :  "http://192.168.1.150/volume/user_file/1600.txt",
    1 :  "http://192.168.1.150/volume/user_file/1600.txt",
    2 :  "http://192.168.1.150/volume/user_file/1600.txt",
    3 :  "http://192.168.1.150/volume/user_file/1600.txt",
    4 :  "http://192.168.1.150/volume/user_file/1600.txt",
    5 :  "http://192.168.1.150/volume/user_file/1600.txt",
    6 :  "http://192.168.1.150/volume/user_file/1600.txt",
    7 :  "http://192.168.1.150/volume/user_file/1600.txt",
    8 :  "http://192.168.1.150/volume/user_file/1600.txt",
    9 :  "http://192.168.1.150/volume/user_file/1600.txt",
    10:  "http://192.168.1.150/volume/user_file/1600.txt",
    11:  "http://192.168.1.150/volume/user_file/1600.txt",
    12:  "http://192.168.1.150/volume/user_file/1600.txt",
    13:  "http://192.168.1.150/volume/user_file/1600.txt",
    14:  "http://192.168.1.150/volume/user_file/1600.txt",
    15:  "http://192.168.1.150/volume/user_file/1600.txt"
}

def power_command(need_command , command_number):
    if need_command == 1:
        try :
            #print(power_control_link[command_number])
            a = power_control_link[command_number]
        except Exception as exc:
            a = 99
        return a
            
           