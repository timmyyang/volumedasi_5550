import Library

"""
cspotter = cspotter inital
clisten = clisten inital
stream_check = snapcast inital
master quantenna mac = wifi board mac
search_iris = 192.168.1.246 default search iris ip
search_quantenn = 192.168.1.247 default search quantenn ip
default_quantenna_ip = AP quantenn ip
radio3 = radio default channel
ffserver /etc/ffserver.conf = because it may cost cpu , after python 
"""

def inital_device():
    Library.file_set('/tmp/file/cspotter', '0')
    Library.file_set('/tmp/file/clisten', '0')
    Library.file_set('/tmp/file/stream_check', '0')
    master_quantenna_mac = Library.get_iris_conf('master_quantenna_mac')
    Library.file_set('/tmp/file/master_quantenna_mac', master_quantenna_mac)
    command = "echo '192.168.1.246' > /tmp/file/search_iris"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    command = "echo '192.168.1.247' > /tmp/file/search_quantenna"
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait() 
    default_quantenna_ip = Library.get_iris_conf('default_quantenna_ip')
    Library.file_set('/tmp/file/default_quantenna_ip', default_quantenna_ip)
    Library.set_iris_conf('radio3',1)
    command = ("ffserver /etc/ffserver.conf&")
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
    