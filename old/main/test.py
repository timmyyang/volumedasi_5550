f = open('/home/volume/trunk/iris/main/iris.conf', 'r')
f = f.read().strip().split('\n')
f[0]='language=DE'
f_1 = open('/home/volume/trunk/iris/main/iris.txt','w')
for i in range(0,len(f)):
    f_1.write(str(f[i])+'\n')

