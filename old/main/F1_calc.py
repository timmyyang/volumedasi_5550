import time

f_calc = open('/tmp/file/calc_count.txt', 'w')
f_calc.write('0'+'\n') 
f_calc.close()
f_calc = open('/tmp/file/calc_word.txt', 'w')
f_calc.write('PartyModeOn\n') 
f_calc.close()

#####start calc############
while True:
    detect = open('/tmp/file/clisten_check.txt', 'r').read().strip()
    if detect == '1':
    
        default = open('/tmp/file/clisten.txt', 'r').read().strip()
        filename = "/tmp/file/calc_word.txt" 
        myfile = open(filename) 
        lines = len(myfile.readlines()) 
        lengh = 0;find_check=0
        while lengh < lines :
            f = open('/tmp/file/calc_word.txt')
            f = f.readlines()[lengh].strip()
            info = f.find(default)
            if info >= 0 :
                f_calc = open('/tmp/file/calc_count.txt', 'r+')
                f_tmp = f_calc.readlines()[lengh].strip()
                f_tmp = int(f_tmp) + 1
                f_calc = open('/tmp/file/calc_count.txt', 'r+')
                f_calc= f_calc.readlines()
                f_calc[lengh]=str(f_tmp)+'\n'
                f=open('/tmp/file/calc_count.txt','w+')
                f.writelines(f_calc)
                f.close()
                find_check=1
                break
            lengh = lengh + 1

            if find_check==0 :
                f_calc = open('/tmp/file/calc_count.txt', 'a')    
                f_calc.write('1'+'\n') 
                f_calc.close()
                f_calc = open('/tmp/file/calc_word.txt', 'a')
                f_calc.write(default+'\n') 
                f_calc.close()
                

    time.sleep(1)
            
            
            
