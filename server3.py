import socket,os,sys
HOST = ''
PORT =  50086
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
socket.bind((HOST,PORT))
socket.listen(10)
conn, addr = socket.accept()
msisdn = conn.recv(1024)
print msisdn
cluster = conn.recv(1024)
print "cluster %s" %cluster
serv = conn.recv(1024)
print serv
dd = conn.recv(2)
print dd
mm = conn.recv(2)
print mm
yy = conn.recv(4)
print yy
path = '/eaiapp1/esb_scripts/log_search'
x = os.getcwd()
os.chdir(path)
command = "./Cluster%s%s.sh %s" % (cluster, serv, msisdn)
#os.system(command)
cluster=int(cluster)
if cluster == 1:
        cmd="ls Aircel_MS?_%s_%s_%s_* > /eaiapp1_logs/Test_scrpits/names.txt" % (yy , mm , dd)
        os.system(cmd)
        f =  open("/eaiapp1_logs/Test_scrpits/clu1log.txt",'rb')
        l = f.read(1024)
        st=l.split("\n")
        del st[-1]
        a1 = [ s.replace('\n','') for s in st]
        print a1
        test = raw_input("these are the files downloaded")
        var = ',  '.join(map(str,a1))
        conn.send(var)
        f.close()
        k = 0
        for var in a1:
                f2 = open(var,'r')
                m = f2.readline(1024)
                while (m) :
                        conn.send(m)
                        m = f2.readline(1024)
                f2.close()
                k = k + 1
                print "done sending file %d" %k
        print "goodbye"
elif cluster == 2:
        cmd="ls AircelESB_MS?_%s_%s_%s_* > /eaiapp1_logs/Test_scrpits/names.txt" % (yy , mm , dd)
        os.system(cmd)
        f =  open("/eaiapp1_logs/Test_scrpits/names.txt",'rb')
        l = f.read(1024)
        st=l.split("\n")
        del st[-1]
        a1 = [ s.replace('\n','') for s in st]
        print a1
        test = raw_input("these are the files downloaded")
        var = ',  '.join(map(str,a1))
        conn.send(var)
        f.close()
        k = 0
        for var in a1:
                f2 = open(var,'r')
                m = f2.readline(1024)
                while (m) :
                        conn.send(m)
                        m = f2.readline(1024)
                f2.close()
                k = k + 1
                print "done sending file %d" %k
        print "goodbye"

elif cluster == 3:
        cmd="ls ESB_MS?_%s_%s_%s_* > /eaiapp1_logs/Test_scrpits/names.txt" % (yy , mm , dd)
        os.system(cmd)
        f =  open("/eaiapp1_logs/Test_scrpits/clu3logs.txt",'rb')
        l = f.read(1024)
        st=l.split("\n")
        del st[-1]
        a1 = [ s.replace('\n','') for s in st]
        print a1
        test = raw_input("these are the files downloaded")
        var = ',  '.join(map(str,a1))
       
 conn.send(var)
        f.close()
        k = 0
        for var in a1:
                f2 = open(var,'r')
                m = f2.readline(1024)
                while (m) :
                        conn.send(m)
                        m = f2.readline(1024)
                f2.close()
                k = k + 1
                print "done sending file %d" %k
        print "goodbye"
elif cluster == 4:
        cmd="ls AIRCEL_ESB_MS_?_%s_%s_%s_* > /eaiapp1_logs/Test_scrpits/names.txt" % (yy , mm , dd)
        os.system(cmd)
        f =  open("/eaiapp1_logs/Test_scrpits/clu4log.txt",'rb')
        l = f.read(1024)
        st=l.split("\n")
        del st[-1]
        a1 = [ s.replace('\n','') for s in st]
        print a1
        test = raw_input("these are the files downloaded")
        var = ',  '.join(map(str,a1))
        conn.send(var)
        f.close()
        k = 0
        for var in a1:
                f2 = open(var,'r')
                m = f2.readline(1024)
                while (m) :
                        conn.send(m)
                        m = f2.readline(1024)
                f2.close()
                k = k + 1
                print "done sending file %d" %k
        print "goodbye"
elif cluster == 5:
        cmd="ls ALSB_MS?_%s_%s_%s_* > /eaiapp1_logs/Test_scrpits/names.txt" % (yy , mm , dd)
        os.system(cmd)
        f =  open("/eaiapp1_logs/Test_scrpits/clu5logs.txt",'rb')
        l = f.read(1024)
        st=l.split("\n")
        del st[-1]
        a1 = [ s.replace('\n','') for s in st]
        print a1
        test = raw_input("these are the files downloaded")
        var = ',  '.join(map(str,a1))
        conn.send(var)
        f.close()
        k = 0
        for var in a1:
                f2 = open(var,'r')
                m = f2.readline(1024)
                while (m) :
                        conn.send(m)
                        m = f2.readline(1024)
                f2.close()
                k = k + 1
                print "done sending file %d" %k
        print "goodbye"
elif cluster == 6:
        cmd="ls OSB_MS?_%s_%s_%s_* > /eaiapp1_logs/Test_scrpits/names.txt" % (yy , mm , dd)
        os.system(cmd)
        f =  open("/eaiapp1_logs/Test_scrpits/clu6logs.txt",'rb')
        l = f.read(1024)
        st=l.split("\n")
        del st[-1]
        a1 = [ s.replace('\n','') for s in st]
        print a1
        test = raw_input("these are the files downloaded")
        var = ',  '.join(map(str,a1))
        conn.send(var)
        f.close()
        k = 0
        for var in a1:
                f2 = open(var,'r')
                m = f2.readline(1024)
                while (m) :
                        conn.send(m)
                        m = f2.readline(1024)
                f2.close()
                k = k + 1
                print "done sending file %d" %k
        print "goodbye"
