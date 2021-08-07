# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 09:11:03 2021

@author: hp
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 16:41:11 2021

@author: hp
"""


import matplotlib
matplotlib.use("TkAgg")
from tkinter.messagebox import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter.filedialog as filedialog
#clusters = 0
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import ttk,PhotoImage,Scrollbar,Listbox, Menu, IntVar, StringVar
import numpy as np
from tkhtmlview import HTMLLabel

class EDMapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

#        tk.Tk.iconbitmap(self, default=)
        tk.Tk.wm_title(self, "Science Fair Project")
        def open_callback():
            filename = askopenfilename()
        # add code here to do something with filename
        def saveas_callback():
            filename = asksaveasfilename()
        # add code here to do something with filename
        def destroy():
            tk.Tk.destroy(self)
        menu = Menu()
        tk.Tk.config(self,menu=menu)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label='Open', command=open_callback)
        file_menu.add_command(label='Save as', command=saveas_callback)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=destroy)
        menu.add_cascade(label='File', menu=file_menu)
        menu.add_cascade(label='Options', menu=file_menu)
        menu.add_cascade(label='Help', menu=file_menu)
        menu.add_cascade(label='About', menu=file_menu)
      
        global filename
        global ed
        global ed2
        global plot_vars
        filename = ImageTk.PhotoImage(Image.open('cover3.jpg'))
        container = tk.Canvas(self,background='blue')
        

        style = ttk.Style(self)
        style.configure('TButton',relief='raised')
        container.configure(background='white')
        container.pack(side="top", fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
#        bl = tk.Label(tk.Tk(None),image = filename)
#        bl.place(x=0,y=0,relwidth=1,relheight=1)
##        b1.pack()

        self.frames = {}

        for F in (StartPage, PageOne, PageThree, PageTwo, PageFour, PageFive, PageSix):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
from tkinter.messagebox import *
LARGE_FONT = ('verdana',15)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
#        s = ttk.Style()
#        s.configure(style='Wild.TButton',foreground='black')
        tk.Frame.__init__(self,parent)
        
#        s.configure(style='Wild.TButton',foreground='black')
#        ttk.Style(self).configure("TButton",padding=1,foreground='blue',background='blue')
#        ttk.Style(self).configure("TButton",relief = 'sunken')
        c0 = tk.Canvas(self,bg = 'white',height = 1220,width = 1450)
        global ed
        ed = ImageTk.PhotoImage(Image.open('edumine.png'))
        
        
#        c0.create_image((0,0),image = filename,anchor='nw')
#        c0.grid(row=0,column=0)
#        
        button = tk.Button(self, borderwidth=4,relief = 'ridge',height=1,width = 20,text="Prediction Engine",
                            command=lambda: controller.show_frame(PageFive))
#        button.place(x=20,y=1,width=300,height=35)

        button2 = tk.Button(self,borderwidth=4,relief = 'ridge', height=1,width = 20,text="Analysis Engine",
        
                    command=lambda: controller.show_frame(PageSix))
        def box():
            pass
        button8  = tk.Button(self,borderwidth=4,relief = 'ridge',height=1,width = 20,text="Clustering Engine",command = lambda: controller.show_frame(PageFour))
        label2 = HTMLLabel(self, html="""
        
        <h2>Overview of X High School</h2>
        <ul>
        <li>Pass Percentage for the next year: 89%
            <ul>
            <li>PASSING STUDENTS: 348</li>
            <li>FAILING STUDENTS: 14</li>
            </ul>
        </li>
        <li>Sub-City Aggregate Rank: 9th</li>
        <li>Addis Ababa Aggregate Rank: 56th</li>
    </ul>
    <h3>EduMeter Analysis</h3>
    <ul>
    <li>Computer Science Rookies: 19</li>
    <li>Business Rookies: 10</li>
    <li>Music/Instrumental Rookies: 20</li>
    </ul>
    
    
    """,borderwidth=2, relief = 'ridge')
        
        global filename2
        filename2 = ImageTk.PhotoImage(Image.open('clusters.png'))
        l = tk.Label(self, image=filename2)
#        l2 = ttk.Label(self, text="EduMine")
        l.grid(row=0,column = 0)
#        l2.grid(row=0,column=0)
        button2.grid(row = 2,column = 0)
        button.grid(row=3,column=0)
        button8.grid(row=4,column=0)
        label2.grid(row = 0, column = 1)
        
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
#        c0 = tk.Canvas(self,bg = 'white',height = 1900,width = 2200)
        
        global ed
#        ed = ImageTk.PhotoImage(Image.open('edumine.png'))
#        c0.create_image((0,0),image = ed,anchor='nw')
#        c0.place(x=500,y=0,relwidth=2,relheight=2)
#        
        button1 = tk.Button(self, borderwidth=4,relief = 'ridge',height=1,width = 25,text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button2 = tk.Button(self, borderwidth=4,relief = 'ridge',height=1,width = 25,text="GO", command = lambda: controller.show_frame(StartPage))
        one = ttk.Label(self, text = '1) ') 
        one.grid(row=0,column=0)
        w = ttk.Combobox(self,values =[ "Internet Usage", "two", "three"] )
        w.grid(row=0,column=1)
        to = tk.Label(self, text = 'to',borderwidth=2,relief='ridge',width = 20)
        to.grid(row = 0,column = 2)
        w2 = ttk.Combobox(self,values =[ "Average", "two", "three"] )
        w2.grid(row=0,column=3)
        two = ttk.Label(self,text="2) ")
        two.grid(row=1,column = 0)
        t = tk.Text(self, height=1,width=17, borderwidth=3,relief='ridge')
        t.grid(row=1,column=1)
        cl = tk.Label(self, text = 'Number of Groups/Clusters',borderwidth=2,relief='ridge',width=20)
        cl.grid(row=1,column=2)
        three = ttk.Label(self,text="3) ")
        three.grid(row=2,column = 0)
        CheckVar2 = IntVar()
        cll = tk.Checkbutton(self, text = "Download report as PDF?", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
        cll.grid(row=2,column=1)
        button2.grid(row=3,column=1)
        button1.grid(row=4,column=1)
        
        
        global ed2
        ed2 = ImageTk.PhotoImage(Image.open('cluster6.jpg'))
        l5 = tk.Label(self, image=ed2,borderwidth=5,relief='ridge')
        l5.grid(row=5,column=1)        
        text_box = tk.Text(self, height=23,width=70,wrap='word')
        text_box.grid(row=5,column=2)
    
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global ed3
        ed3 = ImageTk.PhotoImage(Image.open('Abigail.png'))
        ed33 = tk.Label(self,image=ed3)
        t1 = tk.Label(self, text = 'Average Prediction: 98.0%',borderwidth=2,relief='ridge',width = 50,height=5)
        t2 = t1
        global ed4
        ed4 = ed3
        ed44 = tk.Label(self,image=ed4)
        ed33.grid(row =0,column = 0)
        t1.grid(row=1, column = 0)
        label3 = HTMLLabel(self, html="""
        
        <h2>Nathan's Next Year Prediction</h2>
        <ul>
        <li>Math:98.5 (+0.19%)</li>
        <li>Physics:93.53 (+3.19%)</li>
        <li>Chemistry:95.234 (+5.03%)</li>
        <li>Biology:88.965 (+0.1%)</li>
        <li>English:90.154 (+0.9)%</li>
        <liAmharic:100.19 (+0.19%)</li>
        <li>Civic:95.2 (+0.2%)</li>
        <li>TD:90.0 (-2.1%)</li>
    </ul>
    <h3>Nathan Ake's Profile</h3>
    <ul>
    <li> Number of friends: 4</li>
    <li> Internet Usage per day: 2hrs</li>
    <li> Distance from school: 1.45Km</li>
    <li> Business EduMeter:8.45/10</li>
    <li> Instrumental Music Edumeter: 4.5/10</li>
    </ul>
    """,borderwidth=5, relief = 'ridge')
        label3.grid(row=0, column=1)
        button1 = tk.Button(self, borderwidth=2,relief = 'ridge',height=5,width = 50,text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1)
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global ed333
        ed333 = ImageTk.PhotoImage(Image.open('siphon.png'))
        ed33 = tk.Label(self,image=ed333)
        t1 = tk.Label(self, text = 'Average Prediction: 98.0%',borderwidth=2,relief='ridge',width = 50,height=5)
        t2 = t1
        global ed444
        ed444 = ed3
        ed44 = tk.Label(self,image=ed444)
        ed33.grid(row =0,column = 0)
        t1.grid(row=1, column = 0)
        label3 = HTMLLabel(self, html="""
        
        <h2>Siphon's Next Year Prediction</h2>
        <ul>
        <li>Math:48.5 (-0.19%)</li>
        <li>Physics:45.53 (-3.19%)</li>
        <li>Chemistry:43.234 (-5.03%)</li>
        <li>Biology:65.965 (-0.1%)</li>
        <li>English:69.154 (-0.9)%</li>
        <liAmharic:65.19 (-0.19%)</li>
        <li>Civic:60.2 (-0.2%)</li>
        <li>TD:59.0 (-2.1%)</li>
    </ul>
    <h3>Siphon Melese's Profile</h3>
    <ul>
    <li> Number of friends: 1</li>
    <li> Internet Usage per day: 6hrs</li>
    <li> Distance from school: 1.95Km</li>
    <li> Business EduMeter:9.45/10</li>
    
    </ul>
    """,borderwidth=5, relief = 'ridge')
        label3.grid(row=0, column=1)
        button1 = tk.Button(self, borderwidth=2,relief = 'ridge',height=5,width = 50,text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1)
        
import os
import pandas as pd     
from sklearn.cluster import KMeans
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        one = ttk.Label(self, text = '1) ') 
        one.grid(row=0,column=0)
        def getFolderPath():
            folder_selected = filedialog.askdirectory()
            folderPath.set(folder_selected)
        w = ttk.Combobox(self,values =[ "Internet Usage", "Number of friends", "Average","Amh","Eng","Math","Bio","Phy","Chemo","Civic","IT","PE","TD","Parent Status","Older Siblings","Younger Siblings"])
        
        w.grid(row=1,column=1)
        to = tk.Label(self, text = 'to',borderwidth=3,relief='ridge',width = 22, height=2)
        to.grid(row = 1,column = 2)
        w2 = ttk.Combobox(self,values =["Internet Usage", "Number of friends", "Average","Amh","Eng","Math","Bio","Phy","Chemo","Civic","IT","PE","TD","Parent Status","Older Siblings","Younger Siblings"] )
        w2.grid(row=1,column=3)
        keys = {"Internet Usage":18,
                "Average":15,
                "Amh":0,
                "Eng":1,
                "Math":2,
                "Bio":3,
                "Phy":3,
                "Chemo":5,
                "Civic":8,
                "IT":9,
                "PE":10,
                "TD":11,
                "Total":14,
                "Number of friends":17,
                "Parent Status":19,
                "Younger Siblings":20,
                "Older Siblings":21,
                "DS":22
                }
        t = tk.Entry(self, width=23, borderwidth=3,relief='ridge')
        t.grid(row=2,column=1)
        def doStuff():
            yval = w2.get()
            xval = w.get()
            n = int(t.get())
            folder = folderPath.get()
            directory = folder
            files = os.listdir(directory) 
            students = []
            names = []
            for f in files:
                if (directory+f)[-3:] == 'csv' :
                    students.append(pd.read_csv(directory + '/' + f))
                    names.append((f)[:-4])
                    
            for i in range(len(students)):
                for j in range(len(students[i].values.tolist())):        
                    if students[i].loc[j][0] in ['Geo','History','Econ','GB','Conduct']:
                        students[i].drop(j, axis = 0, inplace = True)
            for df in students:
                df2 = df.loc[0:11]
                v = df2['1st ']
                vv = v = df2['2nd']
                v2 = [float(int(i)) for i in v]
                vv2 =[float(int(i)) for i in vv]
                df2['1st '] = v2
                df2['2nd'] = vv2
                df.loc[14][1:] = [df2['1st '].sum(), df2['2nd'].sum()] 
                df.loc[15][1:] = [df2['1st '].mean(), df2['2nd'].mean()]
                    
            l = []
            es = {names[i]: students[i] for i in range(len(names))}
            for i in range(161):
                l.append([students[i].loc[keys[xval]].values[2],students[i].loc[keys[yval]].values[2]])
            
            
            
            l2 = [[] for i in range(len(l))]
            for i in range(len(l2)):
                l2[i].append(float(l[i][0]))
                l2[i].append(float(l[i][1]))
            e2s = {names[i]: l2[i] for i in range(len(names))}
            key_list = list(e2s.keys())
            val_list = list(e2s.values())
            
            l2 = sorted(l2, key = lambda l:l[1])
            val_list = sorted(val_list, key = lambda l:l[1])
            
            def get_key(val):
                for key, value in e2s.items():
                     if val == value:
                         return key
             
                return "key doesn't exist"
             
            # Driver Code
             
            
            
            
            from sklearn.cluster import KMeans
            import numpy as np
            kmeans = KMeans(n_clusters = n)
            l3 = np.array(l2)
            kmeans.fit(l3)
            global plot_vars            
            plot_vars = [l3[:,1],l3[:,0],kmeans.labels_]
            stds = [get_key(l2[i]) for i in range(len(l2))]
            el = [[] for i in range(n)]
            for i in range(len(kmeans.labels_.tolist())):
                el[kmeans.labels_.tolist()[i]].append(stds[i])

            
            y = plot_vars[0]
            x = plot_vars[1]
            labels = plot_vars[2]
            
            

#            f = Figure(dpi=100)
#            f.set_size_inches(3.8,3.9)
#            a = f.add_subplot(111)
##            a.set_xticks(fontsize=12); a.set_yticks(fontsize=12)
##            a.set_xticks([40,50,60,70,80,90,100])
##            a.set_yticks([40,50,60,70,80,90,100])
#            
#
#
##            a.xticks(fontsize=12); a.yticks(fontsize=12)
#            a.set_title("The Effect of Internet on 11th Grade Students", fontsize=11)
##            a.legend(fontsize=12)    
#            axes = f.gca()
#            axes. xaxis. label. set_size(2)
#            axes. yaxis. label. set_size(2)
#            a.scatter(x,y,c = labels,s=19)
##            a.grid(True)
            fig, ax = plt.subplots()
            
            fig, ax = plt.subplots(1, figsize=(8,8))
#            ax.set_xticks([40,50,60,70,80,90,100])
#            plt.xticks([40,50,60,70,80,90,100]); plt.yticks([40,50,60,70,80,90,100])
            plt.title("   11th Grade Students", fontsize=18)
            plt.legend(fontsize=12)  
            plt.scatter(x,y, c = labels, s =40)
            
            plt.grid(True)
            plt.xlabel(xval)
            plt.ylabel(yval)
            fig.set_size_inches(5.8,5.9)

            
            global canvas
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.show()
            canvas.get_tk_widget().grid(row=5,column = 0,columnspan=3)
    
#            toolbar = NavigationToolbar2TkAgg(canvas, self)
#            toolbar.update()
            canvas._tkcanvas.grid(row=5,column = 0,columnspan=3)
#            lambda: controller.show_frame(PageFive)
            string = ''
            for i in range(n):
                string += 'GROUP {}: '.format(str(i))
                string += '\n'
                string += '\n'.join(el[n-1])
                string += '\n'
            text_box.insert(tk.END,string)
        folderPath = StringVar()
#        a = tk.Label(self ,text="Enter name")
#        a.grid(row=0,column = 1)
        E = tk.Entry(self,textvariable=folderPath,width=23,bd=2)
        E.grid(row=0,column=1)
        btnFind = tk.Button(self, text="Browse Folder",command=getFolderPath, borderwidth=1,width=22, height=2)
        btnFind.grid(row=0,column=2)
        
        
        two = ttk.Label(self, text = '2) ') 
        two.grid(row=1,column=0)
        three = ttk.Label(self, text = '3) ') 
        three.grid(row=2,column=0)
        
        cl = tk.Label(self, text = 'Number of Groups/Clusters',borderwidth=3,relief='ridge',width=22,height=2)
        cl.grid(row=2,column=2)
        four = ttk.Label(self, text = '4) ') 
        four.grid(row=3,column=0)
        CheckVar2 = IntVar()
        cll = tk.Checkbutton(self, text = "Download report as PDF?", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
        cll.grid(row=3,column=1)
        c = ttk.Button(self ,text="GO", command=doStuff)
        c.grid(row=4,column=1)
        text_box = tk.Text(self, height=23,width=70,wrap='word')
        text_box.grid(row=5,column=3,columnspan=4)

        

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        directory = '12C'
        files = os.listdir(directory) 
        students = []
        names = []
        for f in files:
            if (directory+f)[-3:] == 'csv' :
                students.append(pd.read_csv(directory + '/' + f))
                names.append((directory+f)[3:-4])
        
        
        
        # Add a Treeview widget
        tree = ttk.Treeview(self, column=("c1", "c2", "c3"), show='headings', height=5)
        
        tree.column("# 1", anchor='center')
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor='center')
        tree.heading("# 2", text="FName")
        tree.column("# 3", anchor='center')
        tree.heading("# 3", text="LName")
        
        # Insert the data in Treeview widget
        for i in range(len(students)):
            tree.insert('','end',text = "1", values = (str(i),names[i].split()[0],names[i].split()[1]))
        def update_item():
            selected = tree.focus()
            temp = tree.item(selected, 'values')
            f = temp[1]+ ' ' + temp[2] + '.csv'
            s1 = pd.read_csv(directory + '/' + f)
            years = []
            for i in range(int((len(s1['1'])/19))):
                years.append([])
            l = s1['2']
            for i in range(5):
                years[i].append(l.values[i*19:i*19 + 19])
            grades = [1,2,3,4,5]
            Amh = []
            for i in range(5):
                Amh.append(int(years[i][0][2]))
            Amh.reverse()
            Eng = []
            for i in range(5):
                Eng.append(int(years[i][0][3]))
            Eng.reverse()
            Math = []
            for i in range(5):
                Math.append(int(years[i][0][4]))
            Math.reverse()
            Bio = []
            for i in range(5):
                Bio.append(int(years[i][0][5]))
            Bio.reverse()
            Phy = []
            for i in range(5):
                Phy.append(int(years[i][0][6]))
            Phy.reverse()
            Chemo = []
            for i in range(5):
                Chemo.append(int(years[i][0][7]))
            Chemo.reverse()
            Civic = []
            for i in range(5):
                Civic.append(int(years[i][0][10]))
            IT = []
            for i in range(5):
                IT.append(int(years[i][0][11]))
            PE = []
            for i in range(5):
                PE.append(int(years[i][0][12]))
            TD = []
            for i in range(5):
                TD.append((years[i][0][13]))
                
            from sklearn.cross_validation import train_test_split
            Amhx_train, Amhx_test, Amhy_train, Amhy_test = train_test_split(grades,Amh,test_size = 0.4, random_state = 101)
            Engx_train, Engx_test, Engy_train, Engy_test = train_test_split(grades,Eng,test_size = 0.4, random_state = 101)
            Mathx_train, Mathx_test, Mathy_train, Mathy_test = train_test_split(grades,Math,test_size = 0.4, random_state = 101)
            Biox_train, Biox_test, Bioy_train, Bioy_test = train_test_split(grades,Bio,test_size = 0.4, random_state = 101)
            Phyx_train, Phyx_test, Phyy_train, Phyy_test = train_test_split(grades,Phy,test_size = 0.4, random_state = 101)
            Chemox_train, Chemox_test, Chemoy_train, Chemoy_test = train_test_split(grades,Chemo,test_size = 0.4, random_state = 101)
            Civicx_train, Civicx_test, Civicy_train, Civicy_test = train_test_split(grades,Civic,test_size = 0.4, random_state = 101)
            ITx_train, ITx_test, ITy_train, ITy_test = train_test_split(grades,IT,test_size = 0.4, random_state = 101)
            PEx_train, PEx_test, PEy_train, PEy_test = train_test_split(grades,PE,test_size = 0.4, random_state = 101)
            TDx_train, TDx_test, TDy_train, TDy_test = train_test_split(grades,TD,test_size = 0.4, random_state = 101)
            
            from sklearn.linear_model import LinearRegression
            AmhRegressor = LinearRegression()
            EngRegressor = LinearRegression()
            MathRegressor = LinearRegression()
            BioRegressor = LinearRegression()
            PhyRegressor = LinearRegression()
            ChemoRegressor = LinearRegression()
            CivicRegressor = LinearRegression()
            ITRegressor = LinearRegression()
            PERegressor = LinearRegression()
            TDRegressor = LinearRegression()
            
            import numpy as np
            
            AmhRegressor.fit(np.array(Amhx_train).reshape(-1,1), Amhy_train)
            EngRegressor.fit(np.array(Engx_train).reshape(-1,1), Engy_train)
            MathRegressor.fit(np.array(Mathx_train).reshape(-1,1), Mathy_train)
            BioRegressor.fit(np.array(Biox_train).reshape(-1,1), Bioy_train)
            PhyRegressor.fit(np.array(Phyx_train).reshape(-1,1), Phyy_train)
            ChemoRegressor.fit(np.array(Chemox_train).reshape(-1,1), Chemoy_train)
            CivicRegressor.fit(np.array(Civicx_train).reshape(-1,1), Civicy_train)
            ITRegressor.fit(np.array(ITx_train).reshape(-1,1), ITy_train)
            PERegressor.fit(np.array(PEx_train).reshape(-1,1), PEy_train)
            TDRegressor.fit(np.array(TDx_train).reshape(-1,1), TDy_train)
            
            Amhprediction = AmhRegressor.predict(np.array(Amhx_test).reshape(-1,1))
            Engprediction = EngRegressor.predict(np.array(Engx_test).reshape(-1,1))
            Mathprediction = MathRegressor.predict(np.array(Mathx_test).reshape(-1,1))
            Bioprediction = BioRegressor.predict(np.array(Biox_test).reshape(-1,1))
            Phyprediction = PhyRegressor.predict(np.array(Phyx_test).reshape(-1,1))
            Chemoprediction = ChemoRegressor.predict(np.array(Chemox_test).reshape(-1,1))
            Civicprediction = CivicRegressor.predict(np.array(Civicx_test).reshape(-1,1))
            ITprediction = ITRegressor.predict(np.array(ITx_test).reshape(-1,1))
            
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots()
            
            fig, ax = plt.subplots(1, figsize=(8,8))
#            ax.set_xticks([40,50,60,70,80,90,100])
#            plt.xticks([40,50,60,70,80,90,100]); plt.yticks([40,50,60,70,80,90,100])
            plt.title("   11th Grade Students", fontsize=18)
            plt.legend(fontsize=12)  
            plt.scatter(Civicx_train, Civicy_train, color = 'blue')
            plt.plot(Civicx_train,CivicRegressor.predict(np.array(Civicx_train).reshape(-1,1)),color = 'cyan')
            
            plt.grid(True)
            
            fig.set_size_inches(7.8,6.9)

            
            
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.show()
            canvas.get_tk_widget().grid(row=0,column = 0)
    
#            toolbar = NavigationToolbar2TkAgg(canvas, self)
#            toolbar.update()
            canvas._tkcanvas.grid(row=0,column = 0)
            label3 = HTMLLabel(self, html="""
        
            <h2>{name}</h2>
            <ul>
            <li>Math:{math} (+0.19%)</li>
            <li>Physics:{phy} (+3.19%)</li>
            <li>Chemistry:{chem} (+5.03%)</li>
            <li>Biology:{bio} (+0.1%)</li>
            <li>English:{eng} (+0.9)%</li>
            <liAmharic:{amh} (+0.19%)</li>
            <li>Civic:{civics} (+0.2%)</li>
            <li>TD:{TD} (-2.1%)</li>
            </ul>
            <h3>Nathan Ake's Profile</h3>
            <ul>
            <li> Number of friends: 4</li>
            <li> Internet Usage per day: 2hrs</li>
            <li> Distance from school: 1.45Km</li>
            <li> Business EduMeter:8.45/10</li>
            <li> Instrumental Music Edumeter: 4.5/10</li>
            </ul>
            """.format(name = temp[1]+ ' ' + temp[2], math = str(45), phy = str(98), chem = str(98), bio = str(78), eng = str(89), amh= str(98), civics=str(98),TD = str(98)),borderwidth=5, relief = 'ridge')
            label3.grid(row=0, column=1)
            CheckVar3 = IntVar()
            cl2 = tk.Checkbutton(self, text = "Download report as PDF?", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
            cl2.grid(row=1,column=1)
            
            
            
        
        b = ttk.Button(self, text='Predict', command=update_item).grid(row=2,column=0)
        tree.grid(row=1,column=0)
        b2 = ttk.Button(self, text='Home', command=lambda: controller.show_frame(StartPage)).grid(row=3,column=0)
        


class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        folderpath = StringVar()
        def getFolderPath():
            folder_selected = filedialog.askdirectory()
            folderpath.set(folder_selected)
        b1 = ttk.Button(self, text = 'Find', command = getFolderPath)
        
        E = tk.Entry(self, textvariable = folderpath)
        E.grid(row=0, column = 2)
        b1.grid(row=0, column = 1)
        def do():
            b1.destroy()
            E.destroy()
            if len(folderpath.get()) > 3:
                index = folderpath.get()[::-1].index('/')
                c = folderpath.get()[-1*index:]
            else:
                c = folderpath.get()
            directory = c
            files = os.listdir(directory) 
            students = []
            names = []
            for f in files:
                if (directory+f)[-3:] == 'csv' :
                    students.append(pd.read_csv(directory + '/' + f))
                    names.append((directory+f)[3:-4])
            
            
            
            # Add a Treeview widget
            tree = ttk.Treeview(self, column=("c1", "c2", "c3"), show='headings', height=5)
            
            tree.column("# 1", anchor='center')
            tree.heading("# 1", text="ID")
            tree.column("# 2", anchor='center')
            tree.heading("# 2", text="FName")
            tree.column("# 3", anchor='center')
            tree.heading("# 3", text="LName")
            
            # Insert the data in Treeview widget
            for i in range(len(students)):
                tree.insert('','end',text = "1", values = (str(i),names[i].split()[0],names[i].split()[1]))
            def update_item():
                selected = tree.focus()
                temp = tree.item(selected, 'values')
                f = temp[1]+ ' ' + temp[2] + '.csv'
                s1 = pd.read_csv(directory + '/' + f)
                years = []
                for i in range(int((len(s1['1'])/19))):
                    years.append([])
                l = s1['2']
                for i in range(5):
                    years[i].append(l.values[i*19:i*19 + 19])
                grades = [1,2,3,4,5]
                Amh = []
                for i in range(5):
                    Amh.append(int(years[i][0][2]))
                Amh.reverse()
                Eng = []
                for i in range(5):
                    Eng.append(int(years[i][0][3]))
                Eng.reverse()
                Math = []
                for i in range(5):
                    Math.append(int(years[i][0][4]))
                Math.reverse()
                Bio = []
                for i in range(5):
                    Bio.append(int(years[i][0][5]))
                Bio.reverse()
                Phy = []
                for i in range(5):
                    Phy.append(int(years[i][0][6]))
                Phy.reverse()
                Chemo = []
                for i in range(5):
                    Chemo.append(int(years[i][0][7]))
                Chemo.reverse()
                Civic = []
                for i in range(5):
                    Civic.append(int(years[i][0][10]))
                IT = []
                for i in range(5):
                    IT.append(int(years[i][0][11]))
                PE = []
                for i in range(5):
                    PE.append(int(years[i][0][12]))
                TD = []
                for i in range(5):
                    TD.append((years[i][0][13]))
                    
                from sklearn.cross_validation import train_test_split
                Amhx_train, Amhx_test, Amhy_train, Amhy_test = train_test_split(grades,Amh,test_size = 0.4, random_state = 101)
                Engx_train, Engx_test, Engy_train, Engy_test = train_test_split(grades,Eng,test_size = 0.4, random_state = 101)
                Mathx_train, Mathx_test, Mathy_train, Mathy_test = train_test_split(grades,Math,test_size = 0.4, random_state = 101)
                Biox_train, Biox_test, Bioy_train, Bioy_test = train_test_split(grades,Bio,test_size = 0.4, random_state = 101)
                Phyx_train, Phyx_test, Phyy_train, Phyy_test = train_test_split(grades,Phy,test_size = 0.4, random_state = 101)
                Chemox_train, Chemox_test, Chemoy_train, Chemoy_test = train_test_split(grades,Chemo,test_size = 0.4, random_state = 101)
                Civicx_train, Civicx_test, Civicy_train, Civicy_test = train_test_split(grades,Civic,test_size = 0.4, random_state = 101)
                ITx_train, ITx_test, ITy_train, ITy_test = train_test_split(grades,IT,test_size = 0.4, random_state = 101)
                PEx_train, PEx_test, PEy_train, PEy_test = train_test_split(grades,PE,test_size = 0.4, random_state = 101)
                TDx_train, TDx_test, TDy_train, TDy_test = train_test_split(grades,TD,test_size = 0.4, random_state = 101)
                
                from sklearn.linear_model import LinearRegression
                AmhRegressor = LinearRegression()
                EngRegressor = LinearRegression()
                MathRegressor = LinearRegression()
                BioRegressor = LinearRegression()
                PhyRegressor = LinearRegression()
                ChemoRegressor = LinearRegression()
                CivicRegressor = LinearRegression()
                ITRegressor = LinearRegression()
                PERegressor = LinearRegression()
                TDRegressor = LinearRegression()
                
                import numpy as np
                
                AmhRegressor.fit(np.array(Amhx_train).reshape(-1,1), Amhy_train)
                EngRegressor.fit(np.array(Engx_train).reshape(-1,1), Engy_train)
                MathRegressor.fit(np.array(Mathx_train).reshape(-1,1), Mathy_train)
                BioRegressor.fit(np.array(Biox_train).reshape(-1,1), Bioy_train)
                PhyRegressor.fit(np.array(Phyx_train).reshape(-1,1), Phyy_train)
                ChemoRegressor.fit(np.array(Chemox_train).reshape(-1,1), Chemoy_train)
                CivicRegressor.fit(np.array(Civicx_train).reshape(-1,1), Civicy_train)
                ITRegressor.fit(np.array(ITx_train).reshape(-1,1), ITy_train)
                PERegressor.fit(np.array(PEx_train).reshape(-1,1), PEy_train)
                TDRegressor.fit(np.array(TDx_train).reshape(-1,1), TDy_train)
                
                Amhprediction = AmhRegressor.predict(np.array(Amhx_test).reshape(-1,1))
                Engprediction = EngRegressor.predict(np.array(Engx_test).reshape(-1,1))
                Mathprediction = MathRegressor.predict(np.array(Mathx_test).reshape(-1,1))
                Bioprediction = BioRegressor.predict(np.array(Biox_test).reshape(-1,1))
                Phyprediction = PhyRegressor.predict(np.array(Phyx_test).reshape(-1,1))
                Chemoprediction = ChemoRegressor.predict(np.array(Chemox_test).reshape(-1,1))
                Civicprediction = CivicRegressor.predict(np.array(Civicx_test).reshape(-1,1))
                ITprediction = ITRegressor.predict(np.array(ITx_test).reshape(-1,1))
                
                import matplotlib.pyplot as plt
                fig, ax = plt.subplots()
                
                fig, ax = plt.subplots(1, figsize=(8,8))
    #            ax.set_xticks([40,50,60,70,80,90,100])
    #            plt.xticks([40,50,60,70,80,90,100]); plt.yticks([40,50,60,70,80,90,100])
                plt.title("   11th Grade Students", fontsize=18)
                plt.legend(fontsize=12)  
                plt.scatter(Civicx_train, Civicy_train, color = 'blue')
                plt.plot(Civicx_train,CivicRegressor.predict(np.array(Civicx_train).reshape(-1,1)),color = 'cyan')
                
                plt.grid(True)
                
                fig.set_size_inches(7.8,6.9)
    
                
                
                canvas = FigureCanvasTkAgg(fig, self)
                canvas.show()
                canvas.get_tk_widget().grid(row=0,column = 0)
        
    #            toolbar = NavigationToolbar2TkAgg(canvas, self)
    #            toolbar.update()
                canvas._tkcanvas.grid(row=0,column = 0)
                label3 = HTMLLabel(self, html="""
            
                <h2>{name}</h2>
                <ul>
                <li>Math:{math} (+0.19%)</li>
                <li>Physics:{phy} (+3.19%)</li>
                <li>Chemistry:{chem} (+5.03%)</li>
                <li>Biology:{bio} (+0.1%)</li>
                <li>English:{eng} (+0.9)%</li>
                <liAmharic:{amh} (+0.19%)</li>
                <li>Civic:{civics} (+0.2%)</li>
                <li>TD:{TD} (-2.1%)</li>
                </ul>
                <h3>Nathan Ake's Profile</h3>
                <ul>
                <li> Number of friends: 4</li>
                <li> Internet Usage per day: 2hrs</li>
                <li> Distance from school: 1.45Km</li>
                <li> Business EduMeter:8.45/10</li>
                <li> Instrumental Music Edumeter: 4.5/10</li>
                </ul>
                """.format(name = temp[1]+ ' ' + temp[2], math = str(45), phy = str(98), chem = str(98), bio = str(78), eng = str(89), amh= str(98), civics=str(98),TD = str(98)),borderwidth=5, relief = 'ridge')
                label3.grid(row=0, column=1)
                CheckVar3 = IntVar()
                cl2 = tk.Checkbutton(self, text = "Download report as PDF?", variable = CheckVar3, \
                     onvalue = 1, offvalue = 0, height=5, \
                     width = 20)
                cl2.grid(row=1,column=1)
                
                
                
            
            b = ttk.Button(self, text='Predict', command=update_item).grid(row=2,column=0)
            tree.grid(row=1,column=0)
            b2 = ttk.Button(self, text='Home', command=lambda: controller.show_frame(StartPage)).grid(row=3,column=0)
            
        b4 = ttk.Button(self, text = 'Show Class', command = do).grid(row=0,column=0)


app = EDMapp()

app.mainloop()



