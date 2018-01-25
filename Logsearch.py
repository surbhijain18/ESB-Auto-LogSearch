import Tkinter as tk
import tkMessageBox
from Tkinter import *
import socket,os,sys,pickle, datetime, threading,gzip
import ConfigParser
from functools import partial
from itertools import chain


class Helper:
    def __init__(self, section, file):
        self.readline = partial(next, chain(("[{0}]\n".format(section),), file, ("",)))

config = ConfigParser.RawConfigParser(allow_no_value=True)
with open("config_file.cfg") as ifh:
    config.readfp(Helper("Data", ifh))

global st_delimiter
global end_delimiter
global path    
global host
global port

st_delimiter=str((config.get("Data", "st_delimiter")))
end_delimiter=str((config.get("Data", "end_delimiter")))
host=str((config.get("Data", "host")))
port = (config.get("Data", "port"))
path = (config.get("Data", "path"))






def connect():
        global HOST
        global PORT
        global sock
        HOST = '172.18.104.42'    #server name goes in here
        PORT = 50068
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((HOST,PORT))
        return





class windowclass():

        def __init__(self,master):
            self.master = master
            self.frame = tk.Frame(master)
            master.title("LOGIN")
             #self.lbl = Label(master , text = "Label")

            self.lb = tk.Label( master, text="").pack()
            self.lb = tk.Label( master, text="").pack()
            self.lbl = tk.Label( master, text="USERNAME")
            self.E1 = tk.Entry(master, bd =15)
            self.lbl.pack()
            self.E1.pack()
            self.lbl2 = tk.Label( master, text="PASSWORD")
            self.E12 = tk.Entry(master, bd =15, show="*")
            self.lbl2.pack()
            self.E12.pack()
            self.lb = tk.Label( master, text="").pack()
            
            self.btn = tk.Button(master , text = "LOGIN" , width=15,command = self.command)
            self.btn.pack()
            self.frame.pack()  

        def command(self):
            if self.E1.get()=="" and self.E12.get()=="":
                self.master.withdraw()
                self.newWindow = tk.Toplevel(self.master)
                self.newWindow.geometry("350x350")
                self.app = windowclass2(self.newWindow)
                  
            else:
                tkMessageBox.showinfo("Sorry!", "Incorrect Username or Password")
                self.master.destroy()
                sys.exit()


class windowclass2():

        def __init__(self , master):
                self.master = master
                self.frame = tk.Frame(master)
                master.title("Select...")
                for i in range(3):
                        self.lb = tk.Label( master, text="").pack()
                
                self.btn=tk.Button(master, text ="UDT", width=30,command = self.func1).pack()
                for i in range(3):
                        self.lb = tk.Label( master, text="").pack()
                self.btn=tk.Button(master, text ="ESB", width=30, command = self.func2).pack()
                self.frame.pack()


        def func2(self):
                self.master.withdraw()
                self.newWindow = tk.Toplevel(self.master)
                self.newWindow.geometry("450x670")
                self.app = windowclass1(self.newWindow)

        def func1(self):
                tkMessageBox.showinfo("Sorry!", "Currently unavailable")
                #self.master.destroy()

class windowclass1():

        def __init__(self , master):
                now=datetime.datetime.now()
                self.master = master
                self.frame = tk.Frame(master)
                master.title("Details")
                self.lb=tk.Label(master, text ="DETAILS", font=('Times', 20)).pack()
                self.lb = tk.Label( master, text="").pack()
                self.lb=tk.Label(master, text ="MSISDN", font=('Times', 14)).pack()
                self.msdn = tk.StringVar()
                self.msdn = tk.Entry(master, bd=15)
                self.msdn.pack()
                self.service = tk.StringVar()
                self.service.set("")
                self.lb = tk.Label( master, text="").pack()
                self.lb = tk.Label( master, text="").pack()
                self.lb1=tk.Label(master, text ="Select Type", font=('Times', 14)).pack()
                self.rb1=tk.Radiobutton(master, text="BackLog", width=15,variable=self.service, indicatoron=0, font=('Times', 12),value="BackLog").pack()
                self.lb = tk.Label( master, text="").pack()
                self.rb2=tk.Radiobutton(master, text="Rotation", width=15,variable=self.service,indicatoron=0,font=('Times', 12), value="Rotation").pack()
                self.lb = tk.Label( master, text="").pack()
                self.rb3=tk.Radiobutton(master, text="Current",width=15, variable=self.service,indicatoron=0,font=('Times', 12), value="Current").pack()

                self.lb = tk.Label( master, text="").pack()
                self.lb3=tk.Label(master, text ="Select Date", font=('Times', 14)).pack()
                self.date_var = tk.StringVar()
                if now.day < 10:
                        day="0"+str(now.day)
                else:
                        day=str(now.day)
                self.date_var.set(day)
                self.option = OptionMenu(master, self.date_var,"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31",).pack()

                self.month_var = tk.StringVar()
                if now.month < 10:
                        month="0"+str(now.month)
                else:
                        month=(now.month)
                self.month_var.set(month)
                self.option = OptionMenu(master, self.month_var,"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12").pack()

                self.year_var = tk.StringVar()
                self.year_var.set(now.year)
                self.option = OptionMenu(master, self.year_var,"2035","2034","2033","2032","2031","2030","2029","2028","2027","2026","2025","2024","2023","2022","2021","2020","2019","2018","2017","2016", "2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005").pack()
                
                self.cls = tk.StringVar()
                self.lb = tk.Label( master, text="").pack()
                self.lb = tk.Label( master, text="").pack()
                self.lb3=tk.Label(master, text ="Select Cluster Number", font=('Times', 14)).pack()
                self.cls.set("")
                self.option = OptionMenu(master, self.cls, "1", "2", "3", "4", "5", "6").pack()

                self.lb = tk.Label( master, text="").pack()
               
                self.B1 = tk.Button(master, text ="Submit", width=20,command = self.func).pack(side=LEFT)
                self.B2 = tk.Button(master, text ="Quit",width=20, command = self.func3).pack(side=RIGHT)
                
                master.wait_window()               

        def func(self):
                connect()
                msisdn=self.msdn.get()
                
                serv= self.service.get()
                cluster= self.cls.get()
                dd=self.date_var.get()
                mm=self.month_var.get()
                yy=self.year_var.get()
                working(msisdn,serv,cluster,dd,mm,yy)
                self.frame.pack()
                self.master.withdraw()
                sock.close()
                os.system("cls")
                self.newWindow = tk.Toplevel(self.master)
                self.newWindow.geometry("350x350")
                self.app = windowclass2(self.newWindow)
                

        def func3(self):
                result = tkMessageBox.askquestion("Quit", "Are You Sure?", icon='warning')
                if result == 'yes':
                        self.master.destroy()
                        



def working(msisdn,serv,cluster,dd,mm,yy):

        dd1 = int(dd)
        mm1 = int(mm)
        yy1 = int(yy)
        x=validate(dd1,mm1,yy1)
        check=True
        
        if len(msisdn)==10 or len(msisdn)==12:
                
                check=True
        else:
                tkMessageBox.showinfo("SORRY!", "Invalid Number Entered")
                check=False

        if len(cluster)==0:
                tkMessageBox.showinfo("SORRY!", "Invalid Cluster selected")
                check=False
                
        if len(serv)==0:
                tkMessageBox.showinfo("SORRY!", "Invalid type selected")
                check=False

        if x==0:
                tkMessageBox.showinfo("SORRY!", "Invalid date")
                check=False

        if not ((x==1 and  serv=="BackLog") or (x==2 and serv=="Rotation")):
                tkMessageBox.showinfo("SORRY!", "Date doesn't match log type")
                check=False

        
        if check== True:        
                
                sock.send("YES")
                print msisdn
                if len(msisdn) ==12:
                        sock.send(msisdn[2:12])
                else:
                        sock.send(msisdn)
                print serv
                print cluster
                sock.send(cluster)
                print dd
                print mm
                print yy
                now=datetime.datetime.now()
                
                if x==1:
                        flag="o"
                elif x==2:
                        flag="r"
                
                sock.send(flag)
                sock.send(serv)
                sock.send(dd)
                sock.send(mm)
                sock.send(yy)
                print "waiting for the files to download at server..."
                fname=sock.recv(1024)
                name=""
                name = fname[:10]
                if flag=="r":
                        name=path+name+".txt"
                else:
                        name=path+name+".gz"
                
                fl=open(name,"wb")
                print('receiving data...')
                while True:
                        #print('receiving data...')
                        data = sock.recv(1024)
                        if not data :
                            break
                        fl.write(data)
        
                fl.close()    
                print ('file recieved')
     
                search= ">"+msisdn+"</"
                search2=">91"+msisdn+"<"
                
                d=open(path+"data.txt","w")
                
                if flag=="r":
                        with open(name,'r') as f:
                                line = f.readlines()
                elif flag=="o":
                        with gzip.open(name,'r') as f:
                                line = f.readlines() 
                count=0    
                for linenum , lines in enumerate(line):
                        
                        #while linenum!=count:
                                #linenum=linenum+1
                                
                        if ((search in lines) or (search2 in lines)) and linenum > count:
                                
                                line_up=linenum
                                while (line_up>0):
                                        if line[line_up].find(st_delimiter)>-1:
                                                break
                                        else:
                                                line_up=line_up-1
                                pos=line_up
                                line_down=linenum
                                while(True):
                                        if line[line_down].find(end_delimiter)>-1:
                                                line_down=line_down-1
                                                break
                                        else:
                                                line_down=line_down+1
                                    
                                pos2=line_down
                                count=pos2
                           
                                for data_line in line[pos:pos2+1]:
                                        d.write(data_line)
                                        
                                
                   
                print "ending "
                f.close()
                d.close()
                statinfo = os.path.getsize(path+"data.txt")
                if statinfo >0:
                        #raw_input("Press enter to continue...")
                        print "File has been downloaded at C:\Python27\\data.txt"
                        os.startfile(path+"data.txt")
                else:
                        tkMessageBox.showinfo("SORRY!", "File download failed. Please retry or contact admin")
                
                    
                sock.close()
                
            
        else:
               sock.send("ERR")
            
        return       

                
def validate( dd,mm,yy):
    if dd in range (1,31):
        if mm in range (1,12):
            if (now.year>=yy):
                if (now.year>yy):
                    return 1
                elif(now.year==yy):
                    if(now.month>mm):
                        return 1
                    elif(now.month==mm and now.day>dd):
                        return 1
                    elif(now.month==mm and now.day==dd):
                        return 2
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0



root = Tk()
root.title("window")
root.geometry("350x350")
cls = windowclass(root)
now=datetime.datetime.now()
root.mainloop()


