import os
import random
from sqlite3.dbapi2 import Row
import tempfile
from datetime import *
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector as connector
from tkcalendar import *
from PIL import ImageTk,Image 
import sqlite3




    
#------------------homepage----------------
class granthmedical:
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1530x800+0+0")

        #-----------------My menu--------------                                                                            
        my_menu = Menu(self.root,font=("arial",20))
        self.root.config(menu=my_menu)

        #------------------menu item-----------
        Home_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Home",command=self.root)
        

        add_menu=Menu(my_menu,tearoff=0,bg="white")
        my_menu.add_cascade(label="Add",menu=add_menu)
        add_menu.add_command(label="Add New Stock",command=self.additem)
        add_menu.add_separator()
        add_menu.add_command(label="Add New Dictionary",command=self.addnew)
        add_menu.add_separator()
        add_menu.add_command(label="Add Doctor",command=self.adddoctor)
        add_menu.add_separator()
        add_menu.add_command(label="Add Company",command=self.addcompany)


        open_menu=Menu(my_menu,tearoff=0,bg="white")
        my_menu.add_cascade(label="Open",menu=open_menu)
        open_menu.add_command(label="Bill Area",command=self.bill)
        open_menu.add_separator()
        open_menu.add_command(label="Inventory",command=self.inventbutton)
        open_menu.add_separator()
        open_menu.add_command(label="Search Stock",command=self.searchwindow)
      

        info_menu=Menu(my_menu,tearoff=0)
        my_menu.add_command(label="Add Info",command=self.info)

        exit_menu=Menu(my_menu,tearoff=0)
        my_menu.add_command(label="Exit",command=self.exitwindow)


        self.bg=ImageTk.PhotoImage(file="images/CyNYPO.png")
        bg=Label(self.root,image=self.bg,).pack(fill=BOTH,side=TOP)

        


        lbtitle=Label(self.root,text="GRANTH MEDICAL store4",bg="#33DFFF",
                        fg="white",font=("times new roman",50,"bold"),padx=2,pady=4)

        lbtitle.place(x=0,y=0,width=1530,height=100)
        self.image9=PhotoImage(file='images/exit.png')
        self.image9= self.image9.subsample(4,4)
        btn=Button(lbtitle,image=self.image9,bd=0,bg="#33DFFF",activebackground="#33DFFF",command=self.exitwindow)
        btn.place(x=1410,y=10)

        #-------------------frames-------------

        self.image1=PhotoImage(file='images/unnamed.png')
        self.image1= self.image1.subsample(3,3)
        btn=Button(self.root,text='Manage Stock',image=self.image1,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF",pady=25,activebackground="white",command=self.additem)
        btn.place(x=350,y=130,width=190,height=250)
        

        self.image2=PhotoImage(file='images/dic.png')
        self.image2= self.image2.subsample(3,3)
        btn=Button(self.root,text='Dictionary',image=self.image2,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF",pady=0,activebackground="white",command=self.addnew)
        btn.place(x=570,y=130,width=190,height=250)
        
        self.image3=PhotoImage(file='images/bill-clipart-hospital-bill-5.png')
        self.image3= self.image3.subsample(2,2)
        btn=Button(self.root,text='Bill Area',image=self.image3,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF",pady=50,activebackground="white",command=self.bill)
        btn.place(x=790,y=130,width=190,height=250)
        

        self.image4=PhotoImage(file='images/drug_medicine_list_recipe_capsule_paper-512.png')
        self.image4= self.image4.subsample(3,3)
        btn=Button(self.root,text='Inventory',image=self.image4,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF",pady=25,activebackground="white",command=self.inventbutton)
        btn.place(x=1010,y=130,width=190,height=250)
        

        self.image5=PhotoImage(file='images/doctor 1.png')
        self.image5= self.image5.subsample(3,3)
        btn=Button(self.root,text='Doctor',image=self.image5,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF",pady=30,activebackground="white",command=self.adddoctor)
        btn.place(x=350,y=400,width=190,height=250)
    

        self.image6=PhotoImage(file='images/company.png')
        self.image6= self.image6.subsample(1,1)
        btn=Button(self.root,text='Company',image=self.image6,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF",activebackground="white",command=self.addcompany)
        btn.place(x=570,y=400,width=190,height=250)
        

        self.image7=PhotoImage(file='images/search.png')
        self.image7= self.image7.subsample(3,3)
        btn=Button(self.root,text='Search Box',image=self.image7,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF",pady=25,activebackground="white",command=self.searchwindow)
        btn.place(x=790,y=400,width=190,height=250)
        

        self.image8=PhotoImage(file='images/wholesale.png')
        self.image8= self.image8.subsample(3,3)
        btn=Button(self.root,text='Holesaler',image=self.image8,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF",pady=25,activebackground="white",command=self.addwhole)
        btn.place(x=1010,y=400,width=190,height=250)




        

        
        # self.image8=PhotoImage(file='images/back2.jpg')
        # self.image8= self.image8.subsample(3,3)
        # btn=Button(self.root,text='click',image=self.image8,compound=TOP,fg="white",bd=2,relief=RIDGE,font=("times new roman",18,"bold"),bg="#33DFFF")
        # btn.place(x=1010,y=400,width=190,height=250)
        # framemain=Frame(self.root,bd=1,relief=FLAT,bg="white",image=bg)
        # framemain.place(x=200,y=170,width=1100,height=550)


        # framecenter=Frame(framemain,bd=4,relief=GROOVE,bg="white")
        # framecenter.place(x=200,y=0,width=700,height=550)

        # scroll_x=ttk.Scrollbar(framecenter,orient=HORIZONTAL)
        # scroll_x.pack(side=BOTTOM,fil=X)

        # scroll_y=ttk.Scrollbar(framecenter,orient=VERTICAL)
        # scroll_y.pack(side=RIGHT,fil=Y)

        # self.pharmacy_table=ttk.Treeview(framecenter,column=('id','name','type','paking','batchno','expiry','quantity','company','pharma','mrp','rate','gst','totalamount','grandtotal'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        # scroll_x.config(command=self.pharmacy_table.xview)
        # scroll_y.config(command=self.pharmacy_table.yview)


        # self.pharmacy_table['show']='headings'


        # self.pharmacy_table.heading('id',text='ID')
        # self.pharmacy_table.heading('name',text=' Name')
        # self.pharmacy_table.heading('type',text='Type')
        # self.pharmacy_table.heading('paking',text='Paking')
        # self.pharmacy_table.heading('batchno',text='Batch No')
        # self.pharmacy_table.heading('expiry',text='Expiry')
        # self.pharmacy_table.heading('quantity',text='Quantity')
        # self.pharmacy_table.heading('company',text='Company')
        # self.pharmacy_table.heading('pharma',text='Pharma')
        # self.pharmacy_table.heading('mrp',text='MRP')
        # self.pharmacy_table.heading('rate',text='Rate')
        # self.pharmacy_table.heading('gst',text='GST')
        # self.pharmacy_table.heading('totalamount',text='TotalAmount')
        # self.pharmacy_table.heading('grandtotal',text='GrandTotal')
        

        
        # self.pharmacy_table.pack(fill=BOTH,expand=1)

        # self.pharmacy_table.column('id',width=30)
        # self.pharmacy_table.column('name',width=130)
        # self.pharmacy_table.column('type',width=60)
        # self.pharmacy_table.column('paking',width=100)
        # self.pharmacy_table.column('batchno',width=100)
        # self.pharmacy_table.column('expiry',width=60)
        # self.pharmacy_table.column('quantity',width=30)
        # self.pharmacy_table.column('company',width=100)
        # self.pharmacy_table.column('pharma',width=100)
        # self.pharmacy_table.column('mrp',width=100)
        # self.pharmacy_table.column('rate',width=100)
        # self.pharmacy_table.column('gst',width=50)
        # self.pharmacy_table.column('totalamount',width=50)  
        # self.pharmacy_table.column('grandtotal',width=50) 
        # self.fetch_data()

        # frame1=Frame(framemain,bd=4,relief=GROOVE,bg="white")
        # frame1.place(x=0,y=0,width=200,height=550)

        # btninventory=Button(frame1,text="INVENTORY",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.inventbutton)
        # btninventory.place(x=3,y=70,width=180,height=30)

        # btnbill=Button(frame1,text="BILL",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.bill)
        # btnbill.place(x=3,y=150,width=180,height=30)

        # btncheckstock=Button(frame1,text="CHECK STOCK",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.searchwindow)
        # btncheckstock.place(x=3,y=230,width=180,height=30)

        # btnexitmain=Button(frame1,text="EXIT",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.exitwindow)
        # btnexitmain.place(x=3,y=310,width=180,height=30)
        

        


        # frame2=Frame(framemain,bd=4,relief=GROOVE,bg="white")
        # frame2.place(x=900,y=0,width=200,height=550)

        # btnaddstock=Button(frame2,text="ADD STOCK",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.additem)
        # btnaddstock.place(x=3,y=70,width=180,height=30)

        # btnadddoctor=Button(frame2,text="ADD DOCTOR",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.adddoctor)
        # btnadddoctor.place(x=3,y=150,width=180,height=30)

        # btnaddcompany=Button(frame2,text="ADD NEW COMPANY",bd=0,bg="#16A085",fg="white",font=("times new roman",12,"bold"),command=self.addcompany)
        # btnaddcompany.place(x=3,y=230,width=180,height=30)

        # btnaddpharma=Button(frame2,text="ADD HOLESALE",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"))
        # btnaddpharma.place(x=3,y=310,width=180,height=30)

        # btnaddnew=Button(frame2,text="ADD NEW ITEM",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.addnew)
        # btnaddnew.place(x=3,y=310,width=180,height=30)
        
        


    def exitwindow(self):
        self.exitwnidow= messagebox.askyesno("Exit","Do You Want To Exit ?")
        if self.exitwnidow > 0:
            self.root.destroy()
        
        else:
            command = self.root
            return

    def fetch_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select quantity from addstock")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
               
                
                self.pharmacy_table.insert("",END,value=i)

            conn.commit()
        conn.close()


    

    def inventbutton(self):
        self.newWindow=Toplevel(self.root)
        self.app=INVENTORY(self.newWindow)

    def additem(self):
        self.newWindow=Toplevel(self.root)
        self.app=addstock(self.newWindow)

    def addnew(self):
        self.newWindow=Toplevel(self.root)
        self.app=additem(self.newWindow)

    def adddoctor(self):
        self.newWindow=Toplevel(self.root)
        self.app=adddoctor(self.newWindow)

    def addwhole(self):
        self.newWindow=Toplevel(self.root)
        self.app=addwholesale(self.newWindow)

    def addcompany(self):
        self.newWindow=Toplevel(self.root)
        self.app=addcompany(self.newWindow)

    def info(self):
        self.newWindow=Toplevel(self.root)
        self.app=addinfo(self.newWindow)

    def searchwindow(self):
        self.newWindow=Toplevel(self.root)
        self.app=searchstock(self.newWindow)

    def bill(self):
        self.newWindow=Toplevel(self.root)
        self.app=billsystem(self.newWindow)
#-----------------------inventory page---------------------------

class INVENTORY:
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1550x800+0+0")

        self.id=IntVar()

        lbtitle2=Label(self.root,text="GRANTH MEDICAL INVENTORY",bd=15,relief=RIDGE,
                        bg="#16A085",fg="white",font=("times new roman",40,"bold"),padx=2,pady=4)

        lbtitle2.pack(side=TOP,fill=X)


        nb = ttk.Notebook(self.root)
        nb.place(x=20,y=110,width=1200,height=600)

        stockinv=Entry(self.root,text="id",bd=0,bg="#16A085",fg="white",textvariable=self.id,font=("times new roman",15,"bold"))
        stockinv.place(x=1280,y=130,width=180,height=30)

        frameinv1=ttk.Frame(nb) 
        nb.add(frameinv1, text='SEE ALL ADDED STOCK')

        scroll_x=ttk.Scrollbar(frameinv1,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fil=X)

        scroll_y=ttk.Scrollbar(frameinv1,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)

        

        self.pharmacy_table=ttk.Treeview(frameinv1,column=('id','name','type','paking','batchno','expiry','quantity','company','pharma','mrp','rate','gst','totalamount','grandtotal'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)


        self.pharmacy_table['show']='headings'


        self.pharmacy_table.heading('id',text='ID')
        self.pharmacy_table.heading('name',text=' Name')
        self.pharmacy_table.heading('type',text='Type')
        self.pharmacy_table.heading('paking',text='Paking')
        self.pharmacy_table.heading('batchno',text='Batch No')
        self.pharmacy_table.heading('expiry',text='Expiry')
        self.pharmacy_table.heading('quantity',text='Quantity')
        self.pharmacy_table.heading('company',text='Company')
        self.pharmacy_table.heading('pharma',text='Pharma')
        self.pharmacy_table.heading('mrp',text='MRP')
        self.pharmacy_table.heading('rate',text='Rate')
        self.pharmacy_table.heading('gst',text='GST')
        self.pharmacy_table.heading('totalamount',text='TotalAmount')
        self.pharmacy_table.heading('grandtotal',text='GrandTotal')
        

        
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column('id',width=30)
        self.pharmacy_table.column('name',width=130)
        self.pharmacy_table.column('type',width=60)
        self.pharmacy_table.column('paking',width=100)
        self.pharmacy_table.column('batchno',width=100)
        self.pharmacy_table.column('expiry',width=60)
        self.pharmacy_table.column('quantity',width=30)
        self.pharmacy_table.column('company',width=100)
        self.pharmacy_table.column('pharma',width=100)
        self.pharmacy_table.column('mrp',width=100)
        self.pharmacy_table.column('rate',width=100)
        self.pharmacy_table.column('gst',width=50)
        self.pharmacy_table.column('totalamount',width=50)  
        self.pharmacy_table.column('grandtotal',width=50) 
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease>",self.get_cursor)
       
                          
        frameinv3=ttk.Frame(nb) 
        nb.add(frameinv3, text='SEE DICTIONARY')
        
        scroll_x=ttk.Scrollbar(frameinv3,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fil=X)

        scroll_y=ttk.Scrollbar(frameinv3,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)

        

        self.pharmacy_table1=ttk.Treeview(frameinv3,column=('ref','name','medtype','paking','company','pharma','mrp','rate'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.pharmacy_table1.xview)
        scroll_y.config(command=self.pharmacy_table1.yview)


        self.pharmacy_table1['show']='headings'


        self.pharmacy_table1.heading('ref',text='ID')
        self.pharmacy_table1.heading('name',text=' Name')
        self.pharmacy_table1.heading('medtype',text='Type')
        self.pharmacy_table1.heading('paking',text='Paking')
        self.pharmacy_table1.heading('company',text='Company')
        self.pharmacy_table1.heading('pharma',text='Pharma')
        self.pharmacy_table1.heading('mrp',text='MRP')
        self.pharmacy_table1.heading('rate',text='Rate')

        
        self.pharmacy_table1.pack(fill=BOTH,expand=1)

        self.pharmacy_table1.column('ref',width=100)
        self.pharmacy_table1.column('name',width=130)
        self.pharmacy_table1.column('medtype',width=100)
        self.pharmacy_table1.column('paking',width=100)
        self.pharmacy_table1.column('company',width=100)
        self.pharmacy_table1.column('pharma',width=100)
        self.pharmacy_table1.column('mrp',width=100)
        self.pharmacy_table1.column('rate',width=100)
        self.data_fetch()


        #----------------------frame2-----------------
        frameinv2=Frame(self.root,bg="white")
        frameinv2.place(x=1280,y=190,width=200,height=500)

        btnaddstockinv=Button(frameinv2,text="ADD STOCK",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.additem)
        btnaddstockinv.place(x=10,y=50,width=180,height=30)


        btnaddnewinv=Button(frameinv2,text="ADD NEW ITEM",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.addnew)
        btnaddnewinv.place(x=10,y=130,width=180,height=30)

        btnupdate=Button(frameinv2,text="UPDATE",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"))
        btnupdate.place(x=10,y=210,width=180,height=30)

        btndeleteinv=Button(frameinv2,text="DELETE",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.delete_data)
        btndeleteinv.place(x=10,y=290,width=180,height=30)

        btnexit=Button(frameinv2,text="EXIT",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.exitwindow)
        btnexit.place(x=10,y=370,width=180,height=30)

        #----------------frame3-----------------------
        frameinv3=Frame(self.root,bg="white")
        frameinv3.place(x=20,y=720,width=1200,height=50)

        btnadddoctorinv=Button(frameinv3,text="ADD DOCTOR",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.adddoctor)
        btnadddoctorinv.place(x=30,y=10,width=180,height=30)

        btnaddcompanyinv=Button(frameinv3,text="ADD NEW COMPANY",bd=0,bg="#16A085",fg="white",font=("times new roman",12,"bold"),command=self.addcompany)
        btnaddcompanyinv.place(x=250,y=10,width=180,height=30)

        btnaddpharmainv=Button(frameinv3,text="ADD HOLESALE",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"))
        btnaddpharmainv.place(x=460,y=10,width=180,height=30)

        btnaddnewinv=Button(frameinv3,text="ADD NEW ITEM",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.addnew)
        btnaddnewinv.place(x=690,y=10,width=180,height=30)
        
       

    def exitwindow(self):
        self.root.destroy()

    def data_fetch(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from items ")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table1.delete(*self.pharmacy_table1.get_children())
            for i in row:
                self.pharmacy_table1.insert("",0,value=i)
            conn.commit()
        conn.close()


    
        

    def get_cursor(self,event):
        cursor_row=self.pharmacy_table.focus()
        contents=self.pharmacy_table.item(cursor_row)
        row= contents['values']

        self.id.set(row[0])
        

    def delete_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        if self.id.get()=="" :
            self.delete=messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            self.delete=messagebox.askyesno("Ask Something","You Delete The Data !  Are You Sure",parent=self.root)
            if self.delete>0:
                sql="delete from addstock where id=?"
                val=(self.id.get(),)
                my_cursor.execute(sql,val)
                conn.commit()
                conn.close()
                self.fetch_data()
            
            else:
                command=self.root
                return


    def fetch_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from addstock where quantity=0")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,value=i)
            conn.commit()
        conn.close()



    def additem(self):
        self.newWindow=Toplevel(self.root)
        self.app=addstock(self.newWindow)

    def addnew(self):
        self.newWindow=Toplevel(self.root)
        self.app=additem(self.newWindow)

    def adddoctor(self):
        self.newWindow=Toplevel(self.root)
        self.app=adddoctor(self.newWindow)

    def addcompany(self):
        self.newWindow=Toplevel(self.root)
        self.app=addcompany(self.newWindow)

    
        
#-----------------------------addstock page------------------------
class addstock:
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1000x600+270+120")
        self.root.configure(bg="blue",bd="8",relief=RIDGE)

        #------------------variable for add stock-----------
        self.id=IntVar()
        x=random.randint(1,50000)
        self.id.set(str(x))
        self.name=StringVar()
        self.type=StringVar()
        self.paking=StringVar()
        self.batch=StringVar()
        self.exp=StringVar()
        self.quantity=StringVar()
        self.company=StringVar()
        self.pharma=StringVar()
        self.mrp=DoubleVar()
        self.rate=DoubleVar()
        self.gst=IntVar()
        self.totalamount=DoubleVar()
        self.grandtotal=DoubleVar()

       
        #-------------addstock frames-----------------
        frame1=Frame(self.root,bd=0,bg="lightblue")
        frame1.place(x=0,y=0,width=980,height=445)

        

        #------------frame 1 blocks-----------------
        #------------------id---------------
        lblrefnoaddstock=Label(frame1,text="Id",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        lblrefnoaddstock.grid(row=1,column=0,sticky=W)
        
        # conn=connector.connect(host="localhost",port="3306",user="root",password="NO",database="pharmacy")
        # my_cursor=conn.cursor()
        # my_cursor.execute("select ref from items")
        # row1=my_cursor.fetchall()

        ref_comboaddstock = Entry(frame1,width=23,font=("arial",11,"bold" ),textvariable=self.id)
        ref_comboaddstock.grid(row=1,column=1)
        
        # ref_comboaddstock=ttk.Combobox(frame1,width=23,font=("arial",10),textvariable=self.id)
        # ref_comboaddstock['values']=row1
        # ref_comboaddstock.grid(row=1,column=1)
       

        #-----------------------medicine name-------------
        lblcompn=Label(frame1,text="Product Name",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        lblcompn.grid(row=2,column=0,sticky=W)

        
        options=[]
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        sql="select name,medtype,ref from items"
        my_cursor.execute(sql)
        ids=my_cursor.fetchall()
        for ans in ids:
            options.append(str(ans[0])+" "+ans[1])
        
     
        # medcombo=ttk.Combobox(frame1,width=23,font=("arial",10),textvariable=self.name)
        # medcombo['values']=options
        # medcombo.grid(row=2,column=1)
        # medcombo.bind('<Tab>',self.search) 
        # medcombo.bind('<KeyRelease>',self.search_data)

        # ref_combo = Entry(frame1,width=23,font=("arial",11,"bold" ),textvariable=self.name)
        # ref_combo.grid(row=2,column=1)


        # self.searchtxt_var=StringVar()
        # txtsearch=Entry(frame1,bd=0,width=20,textvariable=self.searchtxt_var,font=("arial",14,"bold"))
        # txtsearch.grid(row=2,column=1)
        # txtsearch.bind('<KeyRelease>',self.search_data)
        # txtsearch.bind("<Tab>",self.search)

        

        #-------------search frame----------
        framesearch=Frame(frame1,bd=5,relief=RIDGE,bg="white")
        framesearch.place(x=350,y=50,width=200,height=100)

        scroll_y=ttk.Scrollbar(framesearch,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)       

        self.pharmacy_table1=ttk.Treeview(framesearch,column=('name','medtype'),yscrollcommand=scroll_y.set)
        
        scroll_y.config(command=self.pharmacy_table1.yview)


       

        self.pharmacy_table1['show']='headings' 
        self.pharmacy_table1.heading('name',text=' Name')
        self.pharmacy_table1.heading('medtype',text=' Type')
     
        self.pharmacy_table1.pack(fill=BOTH,expand=1)


        medcombo=Entry(self.pharmacy_table1,width=23,font=("arial",10),textvariable=self.name)
        # medcombo['values']=options
        medcombo.grid(row=0,column=1)
        medcombo.bind('<Key>',self.search) 
        medcombo.bind('<KeyRelease>',self.search_data)

        self.pharmacy_table1.column('name',width=80) 
        self.pharmacy_table1.column('medtype',width=80) 

        self.fetch_data_search() 

        # self.pharmacy_table1.bind("<Button-1>",self.get_cursor)
        self.pharmacy_table1.bind("<ButtonRelease>",self.get_cursor_search)
        
   
        
        

        
        #-------------------itemtype----------
        itemtype=Label(frame1,text="Item Type",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        itemtype.grid(row=3,column=0,sticky=W)

        # my_cursor.execute("select medtype from items")
        # row=my_cursor.fetchall()

        # ref_comboitemtype=ttk.Combobox(frame1,width=23,font=("arial",10),textvariable=self.type)
        # ref_comboitemtype['values']=row
        # ref_comboitemtype.grid(row=3,column=1)
        ref_comboitemtype = Entry(frame1,width=23,font=("arial",11,"bold" ),textvariable=self.type)
        ref_comboitemtype.grid(row=3,column=1)
        ref_comboitemtype.bind("<Tab>",self.search) 
        


        #-------------------paking----------
        paking=Label(frame1,text="Paking",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        paking.grid(row=4,column=0,sticky=W)

        # ref_combopaking=ttk.Combobox(frame1,width=23,font=("arial",10),textvariable=self.paking)
        # ref_combopaking['values']=('Ref','Medicine','Lot')
        # ref_combopaking.grid(row=4,column=1)
        ref_combopaking = Entry(frame1,width=23,font=("arial",11,"bold" ),textvariable=self.paking)
        ref_combopaking.grid(row=4,column=1)

        #----------------batch number------------
        lblcompnbatch=Label(frame1,text="Batch No",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        lblcompnbatch.grid(row=5,column=0,sticky=W)
        txtcompnbatch=Entry(frame1,width=23,font=("arial",11,"bold"),textvariable=self.batch)
        txtcompnbatch.grid(row=5,column=1)

        #--------------expiry------------
        lblcompnexpiry=Label(frame1,text="Expiry",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        lblcompnexpiry.grid(row=6,column=0,sticky=W)
        # txtcompnexpiry=Entry(frame1,bd=2,width=23,relief=RIDGE,font=("arial",11,"bold"),textvariable=self.exp)
        # txtcompnexpiry.grid(row=6,column=1)
        txtcompnexpiry = DateEntry(frame1,width=20,font=("arial",11,"bold"),textvariable=self.exp)
        txtcompnexpiry.grid(row=6,column=1)

        #--------------qty------------
        lblcompnqty=Label(frame1,text="Quantity",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        lblcompnqty.grid(row=7,column=0,sticky=W)
        txtcompnqty=Entry(frame1,width=23,font=("arial",11,"bold"),textvariable=self.quantity)
        txtcompnqty.grid(row=7,column=1)
     
        txtcompnqty.bind("<Tab>",self.total)
        

        #-------------------comapny----------
        company=Label(frame1,text="Company",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        company.grid(row=8,column=0,sticky=W)

        # conn=connector.connect(host="localhost",port="3306",user="root",password="NO",database="pharmacy")
        # my_cursor=conn.cursor()
        # my_cursor.execute("select companyname from company")
        # row=my_cursor.fetchall()

        # ref_combocompany=ttk.Combobox(frame1,width=23,font=("arial",10),textvariable=self.company)
        # ref_combocompany['values']=row
        # ref_combocompany.grid(row=8,column=1)
        # ref_combocompany.current(0)
        ref_combocompany =Entry(frame1,width=23,font=("arial",11,"bold"),textvariable=self.company)
        ref_combocompany.grid(row=8,column=1)

        


        #------------------mrpframe--------------------------
        halfframe=Frame(frame1,bd=0,bg="lightblue")
        halfframe.place(x=600,y=0,width=400,height=450)
        #----------------pharma----------
        pharma=Label(halfframe,text="Pharma",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        pharma.grid(row=1,column=4,sticky=W)

        

        # ref_combopharma=ttk.Combobox(frame1,width=23,font=("arial",10),textvariable=self.pharma)
        # ref_combopharma['values']=row
        # ref_combopharma.grid(row=9,column=1)
        # ref_combopharma.current(0)

        txtpharma=Entry(halfframe,width=23,font=("arial",11,"bold"),textvariable=self.pharma)
        txtpharma.grid(row=1,column=5)


        #-------------------mrp----------
        mrp=Label(halfframe,text="MRP",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        mrp.grid(row=2,column=4,sticky=W)

        txtcompnmrp=Entry(halfframe,width=23,font=("arial",11,"bold"),textvariable=self.mrp)
        txtcompnmrp.grid(row=2,column=5)

        #-------------------rate----------
        rate=Label(halfframe,text="Rate",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        rate.grid(row=3,column=4,sticky=W)

        txtcompnrate=Entry(halfframe,width=23,font=("arial",11,"bold"),textvariable=self.rate)
        txtcompnrate.grid(row=3,column=5)

        #-----------------totalamount-------------
        total=Label(halfframe,text="Total Amount",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        total.grid(row=4,column=4,sticky=W)

        txtcompntotal=Entry(halfframe,textvariable=self.totalamount,width=23,font=("arial",11,"bold"))
        txtcompntotal.grid(row=4,column=5)
        txtcompntotal.bind("<Tab>",self.addstockitem)

        #-------------------gst----------
        

        # #-----------------totalamount-------------
        # totalgrandtotal=Label(halfframe,text="Grand Total",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        # totalgrandtotal.grid(row=6,column=4,sticky=W)

        # txtgrandtotal=Entry(halfframe,width=23,font=("arial",11,"bold"),textvariable=self.grandtotal)
        # txtgrandtotal.grid(row=6,column=5)
        # txtgrandtotal.bind("<Return>",self.addstockitem)
        

        #--------------save--------------
        btnaddstock=Button(halfframe,text="Update Stock",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.addstockitem)
        btnaddstock.grid(row=7,column=5)
        btnaddstock.bind("<Return>",self.addstockitem)

        btndelete=Button(halfframe,text="EXIT",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.root.destroy)
        btndelete.place(x=20,y=340)

        btnupdate=Button(halfframe,text="UPDATE",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.update_data)
        btnupdate.place(x=100,y=340)

        btndelete=Button(halfframe,text="DELETE",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.delete_data)
        btndelete.place(x=210,y=340)

        

        #--------------frame 2------------------
        frame2=Frame(self.root,bd=5,relief=RIDGE,bg="darkblue",width=980)
        frame2.place(x=0,y=380,width=980,height=200)

        scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fil=X)

        scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)

        

        self.pharmacy_table=ttk.Treeview(frame2,column=('id','name','type','paking','batchno','expiry','quantity','company','pharma','mrp','rate','gst','totalamount','grandtotal'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)


        self.pharmacy_table['show']='headings'


        self.pharmacy_table.heading('id',text='ID')
        self.pharmacy_table.heading('name',text=' Name')
        self.pharmacy_table.heading('type',text='Type')
        self.pharmacy_table.heading('paking',text='Paking')
        self.pharmacy_table.heading('batchno',text='Batch No')
        self.pharmacy_table.heading('expiry',text='Expiry')
        self.pharmacy_table.heading('quantity',text='Quantity')
        self.pharmacy_table.heading('company',text='Company')
        self.pharmacy_table.heading('pharma',text='Pharma')
        self.pharmacy_table.heading('mrp',text='MRP')
        self.pharmacy_table.heading('rate',text='Rate')
        self.pharmacy_table.heading('totalamount',text='TotalAmount')
        self.pharmacy_table.heading('grandtotal',text='GrandTotal')
        

        
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column('id',width=30)
        self.pharmacy_table.column('name',width=130)
        self.pharmacy_table.column('type',width=60)
        self.pharmacy_table.column('paking',width=100)
        self.pharmacy_table.column('batchno',width=100)
        self.pharmacy_table.column('expiry',width=60)
        self.pharmacy_table.column('quantity',width=60)
        self.pharmacy_table.column('company',width=100)
        self.pharmacy_table.column('pharma',width=100)
        self.pharmacy_table.column('mrp',width=100)
        self.pharmacy_table.column('rate',width=100)
        self.pharmacy_table.column('totalamount',width=50)  
        self.pharmacy_table.column('grandtotal',width=50) 
        self.fetch_data()
        
        
        
        self.pharmacy_table.bind("<Double-Button-1>",self.get_cursor)
     
    def search_data(self,event):
        conn=sqlite3.connect("database/store3.db")
        cur=conn.cursor()
        cur.execute("select name,medtype from items where name Like '%"+str(self.name.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            self.pharmacy_table1.delete(*self.pharmacy_table1.get_children())
            for i in rows:
                self.pharmacy_table1.insert("",END,values=i)
            conn.commit()
        conn.close()

    def fetch_data_search(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select name medtype from items")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table1.delete(*self.pharmacy_table1.get_children())
            for i in row:
                self.pharmacy_table1.insert("",END,value=i)
            conn.commit()
        conn.close() 

    
    def check(self):
        if self.quantity.get().isnumeric():
                return True
        else:
            messagebox.showinfo("sorry")
    def exitwindow(self,event):
        self.root.destroy()

    def fetch_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from addstock")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",0,value=i)
            conn.commit()
        conn.close()
        


    def total(self,event):
      
        self.totalprice=(
                        float(self.rate.get()) * float(self.quantity.get())
        )   
        self.totalamount.set(str(self.totalprice))


    def search(self,event):
        
        try:

            conn=sqlite3.connect("database/store3.db")
            my_cursor=conn.cursor()
            option=self.name.get()
        
            cid=option.split(" ")[0]
            query="select * from items where name=?"
            my_cursor.execute(query,(cid,))
            rows=my_cursor.fetchall()
            
            
            
            for i in rows:
                
                self.type.set(i[2])
                self.paking.set(i[3])
                self.company.set(i[4])
                self.pharma.set(i[5])
                self.mrp.set(i[6])
                self.rate.set(i[7])
            
            conn.close()

        except:
            print("eror")


    def update_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE addstock set id=?,name=?,type=?,paking=?,expiry=?,quantity=?,company=?,pharma=?,mrp=?,rate=?,totalamount=?,grandtotal=? where id=?",(
                                                                           
                                                                                                     self.id.get(),   
                                                                                                     self.name.get(),
                                                                                                     self.type.get(),
                                                                                                     self.paking.get(),
                                                                                                     self.batch.get(),
                                                                                                     self.exp.get(),
                                                                                                     self.quantity.get(),
                                                                                                     self.company.get(),
                                                                                                     self.pharma.get(),
                                                                                                     self.mrp.get(),
                                                                                                     self.rate.get(),
                                                                                                     
                                                                                                     self.totalamount.get(),
                                                                                                     self.grandtotal.get()
                                                                                                                                       

        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success","Medicine Update Succesfully",parent=self.root)
        self.fetch_data()
        self.clear()
    
    def delete_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        if self.name.get()=="" or self.mrp.get()=="":
            self.delete=messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            self.delete=messagebox.askyesno("Ask Something","You Delete The Data !  Are You Sure",parent=self.root)
            if self.delete>0:
                sql="delete from addstock where id=?"
                val=(self.id.get(),)
                my_cursor.execute(sql,val)
                conn.commit()
                conn.close()
                self.fetch_data()
                self.clear()
            else:
                command=self.root
                return

        
    def clear(self):
        self.id.set("")
        x=random.randint(1,50000)
        self.id.set(str(x))
        self.name.set("")
        self.type.set("")
        self.paking.set("")
        self.batch.set("")
        self.exp.set("")
        self.quantity.set("")
        self.company.set("")
        self.pharma.set("")
        self.mrp.set("0.0")
        self.rate.set("0.0")
        self.totalamount.set("0.0")
        self.grandtotal.set("0.0")

    def get_cursor_search(self,event):
        cursor_row=self.pharmacy_table1.focus()
        contents=self.pharmacy_table1.item(cursor_row)
        row= contents['values']

        self.name.set(row[0]+" "+row[1])
        

        

    def get_cursor(self,event):
        cursor_row=self.pharmacy_table.focus()
        contents=self.pharmacy_table.item(cursor_row)
        row= contents['values']

        self.id.set(row[0])
        self.name.set(row[1])
        self.type.set(row[2])
        self.paking.set(row[3])
        self.batch.set(row[4])
        self.exp.set(row[5])
        self.quantity.set(row[6])
        self.company.set(row[7])
        self.pharma.set(row[8])
        self.mrp.set(row[9])
        self.rate.set(row[10])
        self.totalamount.set(row[12])
        self.grandtotal.set(row[13])

    def addstockitem(self,event=""):
        if self.id.get()=="" or self.name.get()=="" or self.batch.get()=="" or self.exp.get()=="" or self.quantity.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            
        else:

            conn=sqlite3.connect("database/store3.db")
            my_cursor=conn.cursor()
            my_cursor.execute("create table if not exists addstock(id INTEGER,name TEXT,type INTEGER,paking INTEGER,batchno TEXT,expiry TEXT,quantity INTEGER,company TEXT,pharma TEXT,mrp INTEGER,rate INTEGER,gst INTEGER,totalamount INTEGER,grandtotal INTEGER)")
            my_cursor.execute("insert into addstock(id,name,type,paking,batchno,expiry,quantity,company,pharma,mrp,rate,gst,totalamount,grandtotal) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                                                                                                     self.id.get(),
                                                                                                     self.name.get()+"  	       "+self.batch.get(),
                                                                                                     self.type.get(),
                                                                                                     self.paking.get(),
                                                                                                     self.batch.get(),
                                                                                                     self.exp.get(),
                                                                                                     self.quantity.get(),
                                                                                                     self.company.get(),
                                                                                                     self.pharma.get(),
                                                                                                     self.mrp.get(),
                                                                                                     self.rate.get(),
                                                                                                     self.gst.get(),
                                                                                                     self.totalamount.get(),
                                                                                                     self.grandtotal.get()
                                                                                                                                       

            ))

            conn.commit()
        
            conn.close()

            messagebox.showinfo("success","stock Updated",parent=self.root)
            self.fetch_data()
            self.clear()

        
   

        


class additem():
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1000x600+270+120")
        self.root.configure(bg="blue",bd="8",relief=RIDGE)


        #--------------------variable for add stock-----------------
        self.id=IntVar()
        x=random.randint(1,50000)
        self.id.set(str(x))
        self.name=StringVar()
        self.type=StringVar()
        self.paking=StringVar()
        self.company=StringVar()
        self.pharma=StringVar()
        self.mrp=StringVar()
        self.rate=StringVar()
        
        

    

        frame1=Frame(self.root,bd=0,bg="lightblue")
        frame1.place(x=0,y=0,width=980,height=445)

        


        #-------------------addnew frame1-------------
        #------------------id---------------
        lblrefnoaddstock=Label(frame1,text="Id",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        lblrefnoaddstock.grid(row=1,column=0,sticky=W)
        txtcompnbatch=Entry(frame1,bd=2,textvariable=self.id,width=23,relief=RIDGE,font=("arial",11,"bold"))
        txtcompnbatch.grid(row=1,column=1)



        #-----------------------compname-------------
        lblcompn=Label(frame1,text="Product Name",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        lblcompn.grid(row=2,column=0,sticky=W)

        txtcompnbatch=Entry(frame1,bd=2,textvariable=self.name,width=23,relief=RIDGE,font=("arial",11,"bold"))
        txtcompnbatch.grid(row=2,column=1)
        txtcompnbatch.bind("<Return>",self.check)

        #-------------------itemtype----------
        itemtype=Label(frame1,text="Item Type",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        itemtype.grid(row=3,column=0,sticky=W)
        ref_comb=ttk.Combobox(frame1,width=23,textvariable=self.type,font=("arial",10))
        ref_comb['values']=('tab','syp','lotion','cream','oinment','powder','ing','iv','surgical','other')
        ref_comb.grid(row=3,column=1)
        ref_comb.current(1)
    

        #-------------------paking----------
        paking=Label(frame1,text="Paking",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        paking.grid(row=4,column=0,sticky=W)

    
        ref_combopaking=ttk.Combobox(frame1,width=23,textvariable=self.paking,font=("arial",10))
        ref_combopaking.grid(row=4,column=1)

        

        if self.type.get():         
            ref_combopaking['values']=(10,40,100)

        else:
            ref_combopaking['values']=(300,40,100)




        #-------------------comapny----------
        company=Label(frame1,text="Company",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        company.grid(row=8,column=0,sticky=W)

        ref_combocompany=ttk.Combobox(frame1,width=23,textvariable=self.company,font=("arial",10))
        ref_combocompany['values']=('corona','skylife','Lot')
        ref_combocompany.grid(row=8,column=1)
        ref_combocompany.current(0)

        #----------------pharma----------
        pharma=Label(frame1,text="Pharma",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        pharma.grid(row=9,column=0,sticky=W)

        ref_combopharma=ttk.Combobox(frame1,width=23,textvariable=self.pharma,font=("arial",10))
        ref_combopharma['values']=('mahaveer','Medicine','Lot')
        ref_combopharma.grid(row=9,column=1)
        ref_combopharma.current(0)

        #------------------mrpframe--------------------------
        halfframe=Frame(frame1,bd=0,bg="lightblue")
        halfframe.place(x=600,y=0,width=400,height=450)
        #-------------------mrp----------
        mrp=Label(halfframe,text="MRP",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        mrp.grid(row=1,column=4,sticky=W)

        txtcompnmrp=Entry(halfframe,bd=2,width=23,textvariable=self.mrp,relief=RIDGE,font=("arial",11,"bold"))
        txtcompnmrp.grid(row=1,column=5)

        #-------------------rate----------
        rate=Label(halfframe,text="Rate",font=("arial",10,"bold"),bd=0,fg="black",bg="lightblue",padx=10,pady=15)
        rate.grid(row=2,column=4,sticky=W)

        txtcompnrate=Entry(halfframe,bd=2,width=23,textvariable=self.rate,relief=RIDGE,font=("arial",11,"bold"))
        txtcompnrate.grid(row=2,column=5)
        txtcompnrate.bind("<Return>",self.addstock)


        #--------------save--------------
        btnaddstock=Button(halfframe,text="ADD STOCK",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.addstock)
        btnaddstock.grid(row=5,column=5)
        btnaddstock.bind("<Return>",self.addstock)
        
        btnupdate=Button(halfframe,text="UPDATE",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.update_data)
        btnupdate.place(x=10,y=150)

        btndelete=Button(halfframe,text="DELETE",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.delete_data)
        btndelete.place(x=110,y=150)

        btnexit=Button(halfframe,text="EXIT",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.exitwindow)
        btnexit.place(x=210,y=150)

        
        

        #------------bottom frame-----------
        frame2=Frame(self.root,bd=5,relief=RIDGE,bg="darkblue",width=980,height=150)
        frame2.pack(fill=X,side=BOTTOM)

        scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fil=X)

        scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)

        

        self.pharmacy_table=ttk.Treeview(frame2,column=('ref','name','medtype','paking','company','pharma','mrp','rate'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)


        self.pharmacy_table['show']='headings'


        self.pharmacy_table.heading('ref',text='ID')
        self.pharmacy_table.heading('name',text=' Name')
        self.pharmacy_table.heading('medtype',text='Type')
        self.pharmacy_table.heading('paking',text='Paking')
        self.pharmacy_table.heading('company',text='Company')
        self.pharmacy_table.heading('pharma',text='Pharma')
        self.pharmacy_table.heading('mrp',text='MRP')
        self.pharmacy_table.heading('rate',text='Rate')

        
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column('ref',width=100)
        self.pharmacy_table.column('name',width=130)
        self.pharmacy_table.column('medtype',width=100)
        self.pharmacy_table.column('paking',width=100)
        self.pharmacy_table.column('company',width=100)
        self.pharmacy_table.column('pharma',width=100)
        self.pharmacy_table.column('mrp',width=100)
        self.pharmacy_table.column('rate',width=100)
        self.fetch_data()

        self.pharmacy_table.bind("<Double-Button-1>",self.get_cursor)

    def check(self,event):
        if self.name.get().isdigit():
            print('yes')
        else:
            messagebox.showerror("error","Enter Valid name")
        
        
    def exitwindow(self):
        self.root.destroy()

    def fetch_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from items")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",0,value=i)
            conn.commit()
        conn.close()

    def update_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("UPDATE items set name=?,medtype=?,paking=?,company=?,pharma=?,mrp=?,rate=? where ref=?",(
                                                                           
                                                                           self.name.get(),
                                                                           self.type.get(),
                                                                           self.paking.get(),    
                                                                           self.company.get(),
                                                                           self.pharma.get(),
                                                                           self.mrp.get(),                                                            
                                                                           self.rate.get(),
                                                                           self.id.get()                                                            

        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success","Medicine Update Succesfully",parent=self.root)
    
    def delete_data(self):
       
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        if self.name.get()=="" or self.mrp.get()=="":
            self.delete=messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            self.delete=messagebox.askyesno("Ask Something","You Delete The Data !  Are You Sure",parent=self.root)
            if self.delete>0:
                sql="delete from items where ref=?"
                val=(self.id.get(),)
                my_cursor.execute(sql,val)
                conn.commit()
                conn.close()
                self.fetch_data()
                self.clear()
            else:
                command=self.root
                return
        
    def clear(self):
        self.id.set("")
        x=random.randint(1,50000)
        self.id.set(str(x))
        self.name.set("")
        self.type.set("")
        self.paking.set("")
        self.company.set("")
        self.pharma.set("")
        self.mrp.set("")
        self.rate.set("")


    def get_cursor(self,event):
        cursor_row=self.pharmacy_table.focus()
        contents=self.pharmacy_table.item(cursor_row)
        row= contents['values']

        self.id.set(row[0])
        self.name.set(row[1])
        self.type.set(row[2])
        self.paking.set(row[3])
        self.company.set(row[4])
        self.pharma.set(row[5])
        self.mrp.set(row[6])
        self.rate.set(row[7])

    


    def addstock(self,event=""):
        if self.id.get()=="" or self.name.get()=="" or self.mrp.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            
        else:
            conn=sqlite3.connect("database/store3.db")
            my_cursor=conn.cursor()
            my_cursor.execute("create table if not exists items(ref INTEGER,name TEXT,medtype INTEGER,paking TEXT,company TEXT,pharma TEXT,mrp INTEGER,rate INTEGER)")
            my_cursor.execute("insert into items(ref,name,medtype,paking,company,pharma,mrp,rate) values(?,?,?,?,?,?,?,?)",(
                                                                           self.id.get(),
                                                                           self.name.get(),
                                                                           self.type.get(),
                                                                           self.paking.get(),    
                                                                           self.company.get(),
                                                                           self.pharma.get(),
                                                                           self.mrp.get(),                                                            
                                                                           self.rate.get()
                                                                                                                                       

            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("success","Medicine Added",parent=self.root)
            self.fetch_data()
            self.clear()





class adddoctor():
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1000x600+270+120")
        self.root.configure(bg="blue",bd="8",relief=RIDGE)

        #------------variable for doctor-------------
        self.doctorname=StringVar()
        self.doctoradd=StringVar()


        frame1=Frame(self.root,bd=10,relief=RIDGE,bg="lightblue")
        frame1.place(x=0,y=0,width=985,height=585)

        lable1=Label(frame1,text="Doctorname",bg="lightblue",fg="black",font=("arial",10,"bold"))
        lable1.place(x=300,y=100)

        lable1entry=Entry(frame1,width=30,bd=3,textvariable=self.doctorname)
        lable1entry.place(x=400,y=100)

        lable2=Label(frame1,text="Doctoraddress",bg="lightblue",fg="black",font=("arial",10,"bold"))
        lable2.place(x=300,y=150)

        lable1add=Entry(frame1,width=30,bd=3,textvariable=self.doctoradd)
        lable1add.place(x=400,y=150)

        btnadddoctor=Button(frame1,text="ADD doctor",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.adddoctor)
        btnadddoctor.place(x=400,y=200)

        btnexit=Button(frame1,text="EXIT",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.exitwindow)
        btnexit.place(x=420,y=250)




    def exitwindow(self):
        self.root.destroy()

    def adddoctor(self):
        if self.doctorname.get()=="" or self.doctoradd.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
            
        else:
            conn=sqlite3.connect("database/store3.db")
            my_cursor=conn.cursor()
            my_cursor.execute("create table if not exists doctor(doctorname TEXT,doctoradd TEXT)")
            my_cursor.execute("insert into doctor(doctorname,doctoradd) values(?, ?)",(
                                                                           self.doctorname.get(),
                                                                           self.doctoradd.get()
                                                                                                                                       

            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("success","Doctor Added",parent=self.root)


class addwholesale():
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1000x600+270+120")
        self.root.configure(bg="blue",bd="8",relief=RIDGE)

        #------------variable for doctor-------------
        self.wholename=StringVar()
        self.wholeadd=StringVar()


        frame1=Frame(self.root,bd=10,relief=RIDGE,bg="lightblue")
        frame1.place(x=0,y=0,width=985,height=585)

        lable1=Label(frame1,text="Wholesaler name",bg="lightblue",fg="black",font=("arial",10,"bold"))
        lable1.place(x=300,y=100)

        lable1entry=Entry(frame1,width=30,bd=3,textvariable=self.wholename)
        lable1entry.place(x=450,y=100)

        lable2=Label(frame1,text="Wholesaler address",bg="lightblue",fg="black",font=("arial",10,"bold"))
        lable2.place(x=300,y=150)

        lable1add=Entry(frame1,width=30,bd=3,textvariable=self.wholeadd)
        lable1add.place(x=450,y=150)

        btnaddwhole=Button(frame1,text="ADD",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.addwhole)
        btnaddwhole.place(x=420,y=200)

        btnexit=Button(frame1,text="EXIT",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.exitwindow)
        btnexit.place(x=420,y=250)




    def exitwindow(self):
        self.root.destroy()

    def addwhole(self):
        if self.wholename.get()=="" or self.wholeadd.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
            
        else:
            conn=sqlite3.connect("database/store3.db")
            my_cursor=conn.cursor()
            my_cursor.execute("create table if not exists wholesaler(wholename TEXT,wholeadd TEXT)")
            my_cursor.execute("insert into wholesaler(wholename,wholeadd) values(?,?)",(
                                                                           self.wholename.get(),
                                                                           self.wholeadd.get()
                                                                                                                                       

            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("success","Doctor Added",parent=self.root)

class addcompany():
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1000x600+270+120")
        self.root.configure(bg="blue",bd="8",relief=RIDGE)

        #--------------variable for company----------------
        self.comname=StringVar()
        self.comid=StringVar()


        frame1=Frame(self.root,bd=10,relief=RIDGE,bg="lightblue",height=500)
        frame1.place(x=0,y=0,width=985,height=585)

        lable1=Label(frame1,text="Company Name",bg="lightblue",fg="black",font=("arial",10,"bold"))
        lable1.place(x=300,y=100)

        lable1entry=Entry(frame1,width=30,bd=3,textvariable=self.comname)
        lable1entry.place(x=440,y=100)

        lable2=Label(frame1,text="Company id",bg="lightblue",fg="black",font=("arial",10,"bold"))
        lable2.place(x=300,y=150)

        lable1add=Entry(frame1,width=30,bd=3,textvariable=self.comid)
        lable1add.place(x=440,y=150)

        btnaddcompany=Button(frame1,text="ADD Company",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.addcompany)
        btnaddcompany.place(x=400,y=200)

        btnexit=Button(frame1,text="EXIT",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.exitwindow)
        btnexit.place(x=430,y=250)




    def exitwindow(self):
        self.root.destroy()

    def addcompany(self):
        if self.comname.get()=="" or self.comid.get()=="" :
            messagebox.showerror("Error","All fields are required",parent=self.root)
            
        else:
            conn=sqlite3.connect("database/store3.db")
            my_cursor=conn.cursor()
            my_cursor.execute("create table if not exists compnay(companyname TEXT,companyid TEXT)")
            my_cursor.execute("insert into compnay(companyname,companyid) values(?,?)",(
                                                                           self.comname.get(),
                                                                           self.comid.get()
                                                                                                                                       

            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("success","Company Added",parent=self.root)

    

class addinfo():
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1000x600+270+120")
        self.root.configure(bg="lightblue")

        #------------------variables-------------
        self.medname=StringVar()
        self.medadd=StringVar()
        self.medphone=StringVar()
        self.medgstno=StringVar()
        self.meddlno=StringVar()


        #-------------frames------------------
        medical_name=Label(self.root,text="Medical Name",bg="lightblue",fg="black",font=("arial",10))
        medical_name.place(x=30,y=30)
        medical_name_entry=Entry(self.root,bd=0,width=30,textvariable=self.medname,font=("arial",13,"bold"))
        medical_name_entry.place(x=210,y=28)
        
        
        

        medical_add=Label(self.root,text="Medical Address",bg="lightblue",fg="black",font=("arial",10))
        medical_add.place(x=30,y=75)
        medical_add_entry=Entry(self.root,bd=0,width=30,textvariable=self.medadd,font=("arial",13,"bold"))
        medical_add_entry.place(x=210,y=73)

        medical_phoneno=Label(self.root,text="Owner Mobile Number",bg="lightblue",fg="black",font=("arial",10))
        medical_phoneno.place(x=30,y=120)
        medical_phoneno_entry=Entry(self.root,bd=0,textvariable=self.medphone,width=30,font=("arial",13,"bold"))
        medical_phoneno_entry.place(x=210,y=118)

        medical_gstno=Label(self.root,text="Medical GST number",bg="lightblue",fg="black",font=("arial",10))
        medical_gstno.place(x=30,y=170)
        medical_gstno_entry=Entry(self.root,bd=0,textvariable=self.medgstno,width=30,font=("arial",13,"bold"))
        medical_gstno_entry.place(x=210,y=168)

        medical_dlno=Label(self.root,text="Medical DL Number",bg="lightblue",fg="black",font=("arial",10))
        medical_dlno.place(x=30,y=220)
        medical_dlno_entry=Entry(self.root,bd=0,textvariable=self.meddlno,width=30,font=("arial",13,"bold"))
        medical_dlno_entry.place(x=210,y=218)

        btnaddinfo=Button(self.root,text="Submit Information",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.addinformation)
        btnaddinfo.place(x=160,y=260)
        btnaddinfo=Button(self.root,text="Delete Record",bd=0,bg="#16A085",fg="white",font=("times new roman",15,"bold"),command=self.delete_data)
        btnaddinfo.place(x=160,y=300)

       
        #---------------show frame------------------
        frame_show_info=Frame(self.root,bd=0,bg="white")
        frame_show_info.place(x=540,y=15,width=450,height=570)

        

        scroll_x=ttk.Scrollbar(frame_show_info,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fil=X)

        scroll_y=ttk.Scrollbar(frame_show_info,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)

        

        self.pharmacy_table=ttk.Treeview(frame_show_info,column=('medname','medadd','medpho','medgst','meddlno'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)


        self.pharmacy_table['show']='headings'


        self.pharmacy_table.heading('medname',text='Medical Name')
        self.pharmacy_table.heading('medadd',text=' Medical Address')
        self.pharmacy_table.heading('medpho',text='Phone Number')
        self.pharmacy_table.heading('medgst',text='Gst Number')
        self.pharmacy_table.heading('meddlno',text='DL Number')
        

        
        self.pharmacy_table.pack(fill=BOTH,expand=1)
         
        self.pharmacy_table.column('medname',width=100)
        self.pharmacy_table.column('medadd',width=130)
        self.pharmacy_table.column('medpho',width=100)
        self.pharmacy_table.column('medgst',width=100)
        self.pharmacy_table.column('meddlno',width=100)


        
        self.fetch_data()
        self.pharmacy_table.bind("<Double-Button-1>",self.get_cursor)


    
        


    def addinformation(self):
        if self.medname.get()=='' or self.medadd.get()=='' or self.medphone.get()=='' or self.medgstno.get()=='' or self.meddlno.get()=='':
            messagebox.showerror("Error","All Fields Are Reqired!",parent=self.root)

        else:
            conn=sqlite3.connect("database/store3.db")
            my_cursor=conn.cursor()
            my_cursor.execute("create table if not exists add_info(medname TEXT,medadd TEXT,medpho INTEGER,medgst TEXT,meddlno TEXT)")
            my_cursor.execute("insert into add_info(medname,medadd,medpho,medgst,meddlno) values(?,?,?,?,?)",(
                                                                           self.medname.get(),
                                                                           self.medadd.get(),
                                                                           self.medphone.get(),
                                                                           self.medgstno.get(),
                                                                           self.meddlno.get()
                                                                                                                                       

            ))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success","Your Inforfmation are Succesfully Added",parent=self.root)
            self.fetch_data()
            self.clear()



    def fetch_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select medname,medadd,medpho,medgst,meddlno from add_info")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",0,value=i)
            conn.commit()
        conn.close()

    def delete_data(self):
           
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        if self.medname.get()=="" or self.medgstno.get()=="":
            self.delete=messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            self.delete=messagebox.askyesno("Ask Something","You Delete The Data !  Are You Sure",parent=self.root)
            if self.delete>0:
                sql="delete from add_info where medname=?"
                val=(self.medname.get(),)
                my_cursor.execute(sql,val)
                conn.commit()
                conn.close()
                self.fetch_data()
                self.clear()
            else:
                command=self.root
                return
        
    def clear(self):
        self.medname.set("")
        self.medadd.set("")
        self.medphone.set("")
        self.medgstno.set("")
        self.meddlno.set("")
        

    def get_cursor(self,event):
        cursor_row=self.pharmacy_table.focus()
        contents=self.pharmacy_table.item(cursor_row)
        row= contents['values']

        self.medname.set(row[0])
        self.medadd.set(row[1])
        self.medphone.set(row[2])
        self.medgstno.set(row[3])
        self.meddlno.set(row[4])


    







class searchstock():

    def fetch_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from addstock")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,value=i)
            conn.commit()
        conn.close()

    


    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1000x600+270+120")
        self.root.configure(bg="blue",bd="8",relief=RIDGE)

         #--------------------serch box-----------
        lblsearchby=Label(self.root,text="STOCK CHECK BY",font=("arial",15,"bold"),bd=0,fg="white",bg="blue",padx=10,pady=5)
        #btnadd.grid(row=0,column=0)
        lblsearchby.place(x=70,y=18)

        #----------variable---------
        self.search_var=StringVar()
        

        search_combo=ttk.Combobox(self.root,width=18,textvariable=self.search_var,font=("arial",15),state='readonly')
        search_combo['values']=('id','name','batchno','quantity','mrp')
        search_combo.place(x=280,y=20)
        search_combo.current(1)

        self.searchtxt_var=StringVar()
        txtsearch=Entry(self.root,bd=3,relief=RIDGE,textvariable=self.searchtxt_var,font=("arial",15,"bold"))
        txtsearch.place(x=520,y=18)
        txtsearch.bind('<KeyRelease>',self.search)

        btnsearch=Button(self.root,text="SEARCH",font=("arial",12,"bold"),bd=0,fg="white",bg="#16A085",padx=10,command=self.search)
        #btnadd.grid(row=0,column=0)
        btnsearch.place(x=770,y=20)

        btnshow=Button(self.root,text="SHOW ALL",font=("arial",12,"bold"),bd=0,fg="white",bg="#16A085",padx=10,command=self.fetch_data)
        #btnadd.grid(row=0,column=0)
        btnshow.place(x=450,y=60)


        frameinv1=Frame(self.root,bg="white")
        frameinv1.place(x=0,y=113,width=985,height=470)

        scroll_x=ttk.Scrollbar(frameinv1,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fil=X)

        scroll_y=ttk.Scrollbar(frameinv1,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)

        

        self.pharmacy_table=ttk.Treeview(frameinv1,column=('id','name','type','paking','batchno','expiry','quantity','company','pharma','mrp','gst','rate','totalamount'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)


        self.pharmacy_table['show']='headings'


        self.pharmacy_table.heading('id',text='ID')
        self.pharmacy_table.heading('name',text=' Name')
        self.pharmacy_table.heading('type',text='Type')
        self.pharmacy_table.heading('paking',text='Paking')
        self.pharmacy_table.heading('batchno',text='Batch No')
        self.pharmacy_table.heading('expiry',text='Expiry')
        self.pharmacy_table.heading('quantity',text='Quantity')
        self.pharmacy_table.heading('company',text='Company')
        self.pharmacy_table.heading('pharma',text='Pharma')
        self.pharmacy_table.heading('mrp',text='MRP')
        self.pharmacy_table.heading('gst',text='GST')
        self.pharmacy_table.heading('rate',text='Rate')
        self.pharmacy_table.heading('totalamount',text='TotalAmount')

        
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column('id',width=100)
        self.pharmacy_table.column('name',width=100)
        self.pharmacy_table.column('type',width=100)
        self.pharmacy_table.column('paking',width=100)
        self.pharmacy_table.column('batchno',width=100)
        self.pharmacy_table.column('expiry',width=100)
        self.pharmacy_table.column('quantity',width=100)
        self.pharmacy_table.column('company',width=100)
        self.pharmacy_table.column('pharma',width=100)
        self.pharmacy_table.column('mrp',width=100)
        self.pharmacy_table.column('gst',width=100)
        self.pharmacy_table.column('rate',width=100)
        self.pharmacy_table.column('totalamount',width=100)   
        self.fetch_data()

        self.root.bind("<Escape>",self.exitwindow)

    def exitwindow(self,event):
        self.root.destroy()
    
    def search(self,event):
        conn=sqlite3.connect("database/store3.db")
        cur=conn.cursor()
        cur.execute("select * from addstock where " + str(self.search_var.get()) +" Like '%"+str(self.searchtxt_var.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        
        conn.close()

    

class billsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Granth Medical")
        self.root.geometry("1530x800+0+0")


        #-----------------My menu--------------                                                                            
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)

        #------------------menu item-----------
        Home_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Home",command=self.root)
        

        add_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Add",menu=add_menu)
        add_menu.add_command(label="Add New Stock",command=self.additem)
        add_menu.add_command(label="Add New Dictionary",command=self.addnew)
        add_menu.add_command(label="Add Doctor",command=self.adddoctor)
        add_menu.add_command(label="Add Company",command=self.addcompany)


        open_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Open",menu=open_menu)
        open_menu.add_command(label="Bill Area",command=self.root)
        open_menu.add_command(label="Inventory",command=self.inventbutton)
        open_menu.add_command(label="Search Stock",command=self.searchwindow)
      

        info_menu=Menu(my_menu,tearoff=0)
        my_menu.add_command(label="Add Info")

        exit_menu=Menu(my_menu,tearoff=0)
        my_menu.add_command(label="Exit",command=self.exitwindow)

        #-------------variables-----------
        self.customes_name=StringVar()
        self.date=StringVar()
        self.doctor_name=StringVar()
        self.gst_number=StringVar()
        self.address=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1,50000)
        self.bill_no.set(str(x))
        self.payment_type=StringVar()
        self.dl_no=StringVar()
        self.phone_no=StringVar()

        self.id=StringVar()
        self.name=StringVar()
        self.batchno1=StringVar()
        self.quantity=IntVar()
        self.Expiry=StringVar()
        self.mrp=IntVar()
        self.totalamount=DoubleVar()
        self.discount=DoubleVar()
        self.gst_amount=DoubleVar()
        self.cgst_number=DoubleVar()
        self.grandamount=DoubleVar()
        self.old_stock=IntVar()

        self.medicalname=StringVar()
        self.medicaladd=StringVar()
        self.medicalphone=StringVar()
        self.medicalgst=StringVar()
        self.medicaldlno=StringVar()

        
        frame1=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        frame1.place(x=280,y=0,width=1000,height=800)

        

        framebill1=Frame(frame1,bd=0,bg="lightgreen")
        framebill1.place(x=0,y=0,width=990,height=150)

        framebill2=Frame(frame1,bd=0,bg="white")
        framebill2.place(x=0,y=150,width=990,height=450)

        framebill3=Frame(frame1,bd=0,bg="lightgreen")
        framebill3.place(x=0,y=600,width=990,height=200)

        #----------------lable 1 ---------------
        #------------customer name-----------


        # txtmedicalname=Entry(framebill1,bd=0,textvariable=self.medicalname,width=50,bg="lightgreen",font=("arial",13,"bold"))
        # txtmedicalname.place(x=50,y=10)


        # txtmedicaladdress=Entry(framebill1,bd=0,textvariable=self.medicaladd,width=60,bg="lightgreen",font=("arial",13,"bold"))
        # txtmedicaladdress.place(x=300,y=10)

        #------------date-----------
        labledate=Label(framebill1,text="Date  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        labledate.place(x=700,y=3)
        
        txtdate=DateEntry(framebill1,bd=1,relief=RIDGE,bg="lightgreen",textvariable=self.date,font=("arial",13,"bold"))
        txtdate.place(x=800,y=3)
        


        lablename=Label(framebill1,text="Customer Name  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lablename.place(x=25,y=50)

        txtname=Entry(framebill1,bd=1,relief=RIDGE,textvariable=self.customes_name,bg="lightgreen",font=("arial",13,"bold"))
        txtname.place(x=180,y=50)
        self.root.bind(txtname.focus())


        #------------address-------------
        lableaddress=Label(framebill1,text="Address  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lableaddress.place(x=380,y=50)
     
        txtaddress=Entry(framebill1,bd=1,relief=RIDGE,bg="lightgreen",textvariable=self.address,font=("arial",13,"bold"))
        txtaddress.place(x=470,y=53)

         #-----------bill no-----------
        lablephoneno=Label(framebill1,text="Phone NO : ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lablephoneno.place(x=700,y=50)
     
        txtphoneno=Entry(framebill1,bd=1,relief=RIDGE,textvariable=self.phone_no,bg="lightgreen",font=("arial",13,"bold"))
        txtphoneno.place(x=800,y=53)

        
       
        #------------med name-------------
        # lablegstnumber=Label(framebill1,text="GST Number  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        # lablegstnumber.place(x=25,y=100)
     
        # # txtmedname=Entry(framebill1,bd=1,relief=RIDGE,bg="lightgreen",textvariable=self.gst_number,font=("arial",13,"bold"))
        # # txtmedname.place(x=180,y=123)

        # txtgstnumber=Entry(framebill1,textvariable=self.gst_number,font=("arial",13,"bold"))
        # txtgstnumber.place(x=180,y=103)

        
    
        #-----------bill no-----------
        # lablebillno=Label(framebill1,text="Bill NO  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        # lablebillno.place(x=700,y=100)

     
        # txtbillno=Entry(framebill1,bd=1,relief=RIDGE,bg="lightgreen",font=("arial",13,"bold"))
        # txtbillno.place(x=800,y=103)

        #-----------billtype-------------
        lablebilltype=Label(framebill1,text="Bill Type  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lablebilltype.place(x=140,y=100)
     
        # txtmedname=Entry(framebill1,bd=1,relief=RIDGE,bg="lightgreen",textvariable=self.medical_name,font=("arial",13,"bold"))
        # txtmedname.place(x=180,y=123)

        txtbilltype=ttk.Combobox(framebill1,textvariable=self.payment_type,width=15,font=("arial",13,"bold"),state='readonly')
        txtbilltype['values']=('Cash','UPI')
        txtbilltype.place(x=250,y=103)
        txtbilltype.current(0)


         #------------doctor-------------
        labledoctor=Label(framebill1,text="Doctor Name   :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        labledoctor.place(x=520,y=100)
     
        # txtdoctor=Entry(framebill1,bd=1,relief=RIDGE,bg="lightgreen",textvariable=self.doctor_name,font=("arial",13,"bold"))
        # txtdoctor.place(x=660,y=100)

        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select doctorname from doctor")
        row=my_cursor.fetchall()

        txtdoctor=ttk.Combobox(framebill1,textvariable=self.doctor_name,font=("arial",13,"bold"))
        txtdoctor['values']=row
        txtdoctor.place(x=660,y=100)
        txtdoctor.current(0)


        
        #------------address-------------
        # labledl_no=Label(framebill1,text="D.L.No  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        # labledl_no.place(x=400,y=150)
     
        # # txtdl_no=Entry(framebill1,bd=1,relief=RIDGE,textvariable=self.dl_no,bg="lightgreen",font=("arial",13,"bold"))
        # # txtdl_no.place(x=500,y=153)

        # txtdl_no=Entry(framebill1,textvariable=self.medicaldlno,width=17,font=("arial",13,"bold"))     
        # txtdl_no.place(x=500,y=153)
    
       

  
        
        # #------------lable 2-------------
        # #-----------Entry box---------

        # Heading0=Label(framebill2,text="id",font=("arial",13),bd=0,fg="black",bg="white",padx=10,pady=4)
        # Heading0.grid(row=0,column=0)

        # Heading1=Label(framebill2,text="Name",font=("arial",13),bd=0,fg="black",bg="white",padx=10,pady=4)
        # Heading1.grid(row=0,column=1)

        # Heading2=Label(framebill2,text="Batch No",font=("arial",13),bd=0,fg="black",bg="white",padx=10,pady=4)
        # Heading2.grid(row=0,column=2)

        # Heading3=Label(framebill2,text="Quantity",font=("arial",13),bd=0,fg="black",bg="white",padx=10,pady=4)
        # Heading3.grid(row=0,column=3)

        

        # Heading4=Label(framebill2,text="Expiry",font=("arial",13),bd=0,fg="black",bg="white",padx=10,pady=4)
        # Heading4.grid(row=0,column=4)

        # Heading5=Label(framebill2,text="MRP",font=("arial",13),bd=0,fg="black",bg="white",padx=10,pady=4)
        # Heading5.grid(row=0,column=5)

        # Heading6=Label(framebill2,text="Total",font=("arial",13),bd=0,fg="black",bg="white",padx=10,pady=4)
        # Heading6.grid(row=0,column=6)
        
        # end_bill=self.root.bind("<End>" , self.endbill)

        

        # for i in range(1,100):

        #     txtidbox=Entry(framebill2,bd=1,width=5,relief=RIDGE,bg="white",font=("arial",13,"bold"),textvariable=self.id)
        #     txtidbox.grid(row=i,column=0)

        #     options=[]
        #     conn=connector.connect(host="localhost",port="3306",user="root",password="NO",database="pharmacy")
        #     my_cursor=conn.cursor()
        #     sql="select name,type from addstock"
        #     my_cursor.execute(sql)
        #     ids=my_cursor.fetchall()
        #     for ans in ids:
        #         options.append(str(ans[0])+"-"+ans[1])

        #     txtfirstbox=Entry(framebill2,bd=1,width=30,relief=RIDGE,bg="white",font=("arial",13,"bold"),textvariable=self.name)
        #     txtfirstbox.grid(row=i,column=1)
        #     txtfirstbox.bind("<Return>",self.search)

        #     txtsecondbox=Entry(framebill2,bd=1,relief=RIDGE,bg="white",font=("arial",13,"bold"))
        #     txtsecondbox.grid(row=i,column=2)

        #     txttypebox=Entry(framebill2,bd=1,relief=RIDGE,width=10,bg="white",font=("arial",13,"bold"))
        #     txttypebox.grid(row=i,column=3)

        #     txtfourthbox=Entry(framebill2,bd=1,relief=RIDGE,width=13,bg="white",font=("arial",13,"bold"))
        #     txtfourthbox.grid(row=i,column=4)

        #     txtfifthbox=Entry(framebill2,bd=1,relief=RIDGE,width=13,bg="white",font=("arial",13,"bold"))
        #     txtfifthbox.grid(row=i,column=5)

        #     txtlastbox=Entry(framebill2,bd=1,relief=RIDGE,width=15,bg="white",font=("arial",13,"bold"))
        #     txtlastbox.grid(row=i,column=6)

        #----------------bill frame-----------------

        Heading1=Label(framebill2,text="Name",font=("arial",13),bd=0,fg="black",bg="white",padx=15,pady=24)
        Heading1.grid(row=1,column=0)
        
        global options
        options=[]
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        sql="select name from addstock"
        my_cursor.execute(sql)
        ids=my_cursor.fetchall()
        for ans in ids:
            options.append(str(ans[0]))
            
            
            
      
        # medcombo=ttk.Combobox(framebill2,width=23,font=("arial",10,"bold"),textvariable=self.name)
        # medcombo['values']=options
        # medcombo.grid(row=1,column=1)
        # # medcombo.bind("<KeyRelease>",self.check)
        # medcombo.bind("<<ComboboxSelected>>",self.fetch_all)

        framesearch=Frame(framebill2,bd=0,relief=RIDGE,bg="white")
        framesearch.place(x=100,y=0,width=200,height=140)


        scroll_y=ttk.Scrollbar(framesearch,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)       

        self.pharmacy_table1=ttk.Treeview(framesearch,column=('name'),yscrollcommand=scroll_y.set)
        
        scroll_y.config(command=self.pharmacy_table1.yview)


       

        self.pharmacy_table1['show']='headings' 
        self.pharmacy_table1.heading('name',text=' Name')
     
        self.pharmacy_table1.pack(fill=BOTH,expand=1)


        medcombo=Entry(self.pharmacy_table1,width=23,font=("arial",10),textvariable=self.name)
        # medcombo['values']=options
        medcombo.place(x=0,y=0)
        medcombo.bind('<Key>',self.fetch_all) 
        medcombo.bind('<KeyRelease>',self.search_data)

        self.pharmacy_table1.column('name')  

        self.fetch_data_search() 

        # self.pharmacy_table1.bind("<Button-1>",self.get_cursor)
        self.pharmacy_table1.bind("<ButtonRelease>",self.get_cursor_search)


        Heading2=Label(framebill2,text="",font=("arial",13),bd=0,fg="black",bg="white",padx=15,pady=24)
        Heading2.grid(row=2,column=0)
        
        
        txtid1=Entry(framebill2,bd=1,relief=RIDGE,bg="white",textvariable=self.id,font=("arial",13,"bold"))
        txtid1.place(x=500,y=0)


        Heading2=Label(framebill2,text="Batch No",font=("arial",13),bd=0,fg="black",bg="white",padx=15,pady=24)
        Heading2.grid(row=3,column=0)
        txtsecondbox=Entry(framebill2,bd=1,relief=RIDGE,bg="white",textvariable=self.batchno1,font=("arial",13,"bold"))
        txtsecondbox.grid(row=3,column=1)
       
        
        Heading3=Label(framebill2,text="Quantity",font=("arial",13),bd=0,fg="black",bg="white",padx=15,pady=24)
        Heading3.grid(row=4,column=0)
        txttypebox=Entry(framebill2,bd=1,relief=RIDGE,bg="white",textvariable=self.quantity,font=("arial",13,"bold"))
        txttypebox.grid(row=4,column=1)
        txttypebox.bind("<Tab>",self.itemlist)
        



         
        
        

        Heading4=Label(framebill2,text="Expiry",font=("arial",13),bd=0,fg="black",bg="white",padx=15,pady=24)
        Heading4.grid(row=5,column=0)
        txtfourthbox=Entry(framebill2,bd=1,relief=RIDGE,bg="white",textvariable=self.Expiry,font=("arial",13,"bold"))
        txtfourthbox.grid(row=5,column=1)

        Heading5=Label(framebill2,text="MRP",font=("arial",13),bd=0,fg="black",bg="white",padx=15,pady=24)
        Heading5.grid(row=6,column=0)
        txtfifthbox=Entry(framebill2,bd=1,relief=RIDGE,bg="white",textvariable=self.mrp,font=("arial",13,"bold"))
        txtfifthbox.grid(row=6,column=1)

        Heading6=Label(framebill2,text="Discount",font=("arial",13),bd=0,fg="black",bg="white",padx=15,pady=24)
        Heading6.grid(row=7,column=0)
        txtsixthbox=Entry(framebill2,bd=1,relief=RIDGE,bg="white",textvariable=self.discount,font=("arial",13,"bold"))
        txtsixthbox.grid(row=7,column=1)
        txtsixthbox.bind("<Return>",self.gbill)

        #----------------bill generate----------
        framegeneratebill2=Frame(framebill2,bd=3,relief=RIDGE,bg="white")
        framegeneratebill2.place(x=300,y=0,width=690,height=450)

        scroll_y=Scrollbar(framegeneratebill2,orient=VERTICAL)
        self.textarea=Text(framegeneratebill2,bd=0,yscrollcommand=scroll_y,undo=True)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack()
        self.billarea()
        

        #----------------bill generate----------
        self.root.bind("<Control-n>",self.clear)
        self.root.bind("<End>",self.gbill)
        self.root.bind("<Control-p>",self.print_bill)
        self.root.bind("<Control-s>",self.savebill)
        self.root.bind("<Escape>",self.exitwindow)
        
        
        #-----------------frame 3 parts-------------
        frame31=Frame(framebill3,bd=1,relief=SOLID,bg="lightgreen")
        frame31.place(x=-5,y=0,width=500,height=200)

        frame32=Frame(framebill3,bd=1,relief=SOLID,bg="lightgreen")
        frame32.place(x=495,y=0,width=505,height=200)

        #------------mrp total -----------
        lableamount=Label(frame31,text="Total Amount  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lableamount.place(x=10,y=10)
     
        txtamount=Entry(frame31,bd=1,relief=RIDGE,bg="lightgreen",textvariable=self.totalamount,font=("arial",13,"bold"))
        txtamount.place(x=180,y=10)

        lableDiscount=Label(frame31,text="Discount  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lableDiscount.place(x=10,y=50)
     
        txtDiscount=Entry(frame31,bd=1,relief=RIDGE,textvariable=self.discount,bg="lightgreen",font=("arial",13,"bold"))
        txtDiscount.place(x=180,y=50)
        txtDiscount.bind("<Return>",self.gbill)

        lablegst=Label(frame31,text="GST  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lablegst.place(x=10,y=90)
     
        txtgst=Entry(frame31,bd=1,relief=RIDGE,bg="lightgreen",textvariable=self.gst_amount,font=("arial",13,"bold"))
        txtgst.place(x=180,y=90)

        lablecgst=Label(frame31,text="CGST  :  ",font=("arial",13),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lablecgst.place(x=10,y=130)
     
        txtcgst=Entry(frame31,bd=1,relief=RIDGE,bg="lightgreen",textvariable=self.cgst_number,font=("arial",13,"bold"))
        txtcgst.place(x=180,y=130)

        lablegrandtotal=Label(frame32,text="Grand Total  :  ",font=("arial",15),bd=0,fg="black",bg="lightgreen",padx=10,pady=5)
        lablegrandtotal.place(x=40,y=30)

        txtgrandtotal=Entry(frame32,bd=0,relief=RIDGE,width=13,textvariable=self.grandamount,bg="lightgreen",font=("arial",35,"bold"))
        txtgrandtotal.place(x=60,y=90,height=90)

        #---------------list frame---------------

        frame_list=Frame(self.root,bd=10,relief=RIDGE,bg="white")
        frame_list.place(x=1280,y=0,width=240,height=800)

        show_list_lable=Label(frame_list,text="Search Bill Area",font=("arial",10,"bold"))
        show_list_lable.pack(fill=X,side=TOP)


        self.searchtxt=StringVar()
        txtsearch=Entry(frame_list,bd=2,relief=RIDGE,width=10,textvariable=self.searchtxt,font=("arial",14,"bold"))
        txtsearch.place(x=5,y=35)
        txtsearch.bind('<Return>',self.find_bill)

        btnsearch=Button(frame_list,text="SEARCH",font=("arial",11,"bold"),bd=0,fg="white",bg="#16A085",padx=10,command=self.find_bill)
        #btnadd.grid(row=0,column=0)
        btnsearch.place(x=125,y=35)

        list_frame=Frame(frame_list,bd=0,bg="white")
        list_frame.place(x=0,y=80,width=220,height=670)

        scroll_y=Scrollbar(list_frame,orient=VERTICAL)
        self.file_list=Listbox(list_frame,font=("arial",10,"bold"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        
         #--------------------serch box-----------
        lblsearchby=Label(self.root,text="Search",font=("arial",15,"bold"),bd=0,fg="black",padx=0,pady=5)
        #btnadd.grid(row=0,column=0)
        lblsearchby.place(x=80,y=5)

        self.search_var=StringVar()
        search_combo=ttk.Combobox(self.root,width=9,textvariable=self.search_var,font=("arial",11),state='readonly')
        search_combo['values']=('name','quantity','mrp')
        search_combo.place(x=25,y=35)
        search_combo.current(0)


        self.searchtxt_var=StringVar()
        txtsearch=Entry(self.root,bd=0,width=10,textvariable=self.searchtxt_var,font=("arial",14,"bold"))
        txtsearch.place(x=125,y=35)
        txtsearch.bind('<KeyRelease>',self.search)

        btnsearch=Button(self.root,text="SEARCH",font=("arial",10,"bold"),bd=0,fg="white",bg="#16A085",padx=10,command=self.search)
        #btnadd.grid(row=0,column=0)
        btnsearch.place(x=80,y=70)

        #-------------search frame----------
        framesearch=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        framesearch.place(x=10,y=100,width=265,height=400)

        scroll_x=ttk.Scrollbar(framesearch,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fil=X)

        scroll_y=ttk.Scrollbar(framesearch,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fil=Y)       

        self.pharmacy_table=ttk.Treeview(framesearch,column=('name','quantity','mrp'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)


        self.pharmacy_table['show']='headings' 
        self.pharmacy_table.heading('name',text=' Name')
        self.pharmacy_table.heading('quantity',text='Quantity')
        self.pharmacy_table.heading('mrp',text='MRP')

        
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        
        self.pharmacy_table.column('name',width=80)
        self.pharmacy_table.column('quantity',width=40)
        self.pharmacy_table.column('mrp',width=40) 
        self.fetch_data() 

        #-----------frame keys----------------
        framekeys=LabelFrame(self.root,text='ShortCut Keys',bd=5,relief=RIDGE,bg="white",font=("arial",10,"bold"))
        framekeys.place(x=10,y=500,width=265,height=270)


        first=Label(framekeys,text="END \t\t End the bill",bg="white",fg="black",bd=0,font=("arial",12),pady=10)
        first.place(x=10,y=0)

        second=Label(framekeys,text="CTRL+S \t\t Save the bill",bg="white",fg="black",bd=0,font=("arial",12),pady=10)
        second.place(x=10,y=30)

        third=Label(framekeys,text="CTRL+N \t\t For new bill",bg="white",fg="black",bd=0,font=("arial",12),pady=10)
        third.place(x=10,y=60)

        print_bill=Label(framekeys,text="CTRL+P \t\t For Print bill",bg="white",fg="black",bd=0,font=("arial",12),pady=10)
        print_bill.place(x=10,y=90)

        fourth=Label(framekeys,text="ESC \t\t For exit ",bg="white",fg="black",bd=0,font=("arial",12),pady=10)
        fourth.place(x=10,y=120)

        self.root.bind("<Control-z>",self.textarea.edit_undo)

         #--------------------connection---------------------
        
        conn=sqlite3.connect("database/store3.db")
        cur=conn.cursor()
        cur.execute("select * from add_info")
        row=cur.fetchall()
        for i in row:
            self.medicalname.set(i[0])
            self.medicaladd.set(i[1])
            self.medicalphone.set(i[2])
            self.medicalgst.set(i[3])
            self.medicaldlno.set(i[4])


        #--------------------connection---------------------
       

    # def delete(self):
    #     conn=sqlite3.connect("database/store3.db")
    #     my_cursor=conn.cursor()

    #     sql="SELECT id FROM addstock WHERE quantity=0"
           
    #     my_cursor.execute(sql)
                  
    #     row=my_cursor.fetchone()

    #     sqli="DELETE FROM addstock WHERE id"
        
           
    #     my_cursor.execute(sqli)
                  
    #     row=my_cursor.fetchall()
        
            

    #     messagebox.showinfo("Success","item deleted",parent=self.root)
    def fetch_data_search(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select name from addstock")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table1.delete(*self.pharmacy_table1.get_children())
            for i in row:
                self.pharmacy_table1.insert("",END,value=i)
            conn.commit()
        conn.close() 


    def search_data(self,event):
        conn=sqlite3.connect("database/store3.db")
        cur=conn.cursor()
        cur.execute("select name from addstock where name Like '%"+str(self.name.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            self.pharmacy_table1.delete(*self.pharmacy_table1.get_children())
            for i in rows:
                self.pharmacy_table1.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    def get_cursor_search(self,event):
        cursor_row=self.pharmacy_table1.focus()
        contents=self.pharmacy_table1.item(cursor_row)
        row= contents['values']

        self.name.set(row[0])
    

    def check(self,event):
        conn=sqlite3.connect("database/store3.db")
        cur=conn.cursor()
        cur.execute("select * from addstock where " + str(self.search_var.get()) +" Like '%"+str(self.searchtxt_var.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            for i in rows:
                options.insert("",END,values=i)
            conn.commit()
        
        conn.close()

                  
        


    def search(self,event):
        conn=sqlite3.connect("database/store3.db")
        cur=conn.cursor()
        cur.execute("select name,quantity,mrp from addstock where " + str(self.search_var.get()) +" Like '%"+str(self.searchtxt_var.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def fetch_data(self):
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        my_cursor.execute("select name type,quantity,mrp from addstock")
        row=my_cursor.fetchall()

        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,value=i)
            conn.commit()
        conn.close() 
    

    def fetch_all(self,event):
        
        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()
        option=self.name.get()
        
        
        cid=option
            
        query="select * from addstock where name=?"
        my_cursor.execute(query,(cid,))
        rows=my_cursor.fetchall()
       
             
        for i in rows:
            self.id.set(i[0])
            self.batchno1.set(i[4])
            self.Expiry.set(i[5])
            self.mrp.set(i[9])
            self.old_stock.set(i[6])


        # sql="select name from addstock"
        # my_cursor.execute(sql)
        # ids=my_cursor.fetchall()
        # for i in ids:
        #     if i==self.name.get():
        #         return True
        #     else:
        #         messagebox.showerror("error","opps this is not in stock")

            
           
        conn.close()
    
    global l
    l=[] 
    
         
        
    def billarea(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,f" {self.medicalname.get()} ")
        self.textarea.insert(END,f"\t\t\t\t\t{self.customes_name.get()}")
        self.textarea.insert(END,f"\t\t\tDate : {self.date.get()}\n")

        self.textarea.insert(END,f" {self.medicaladd.get()} ")   
        self.textarea.insert(END,f"\t\t\t\t\t{self.address.get()}\n")
         
        self.textarea.insert(END,f" Phone No : {self.medicalphone.get()}")   
        self.textarea.insert(END,f"\t\t\t\t\t{self.phone_no.get()}\n")

        self.textarea.insert(END,"--------------------------------------------------------------------------------\n")
        self.textarea.insert(END,f" GSTIN : {self.medicalgst.get()}")
        self.textarea.insert(END,f"\t\t\t\t\t\t\tBill No : {self.bill_no.get()}\n")
        self.textarea.insert(END,f" D.L.No : {self.medicaldlno.get()}")
        self.textarea.insert(END,f"\t\t\t\t\t\t\tDue Date : {self.date.get()}\n")
        self.textarea.insert(END,f"\t\t\t\t\t\t\tBill Type : {self.payment_type.get()}\n")
        self.textarea.insert(END,"--------------------------------------------------------------------------------\n")
        self.textarea.insert(END,"Product Name \t\t   Batch No   \t\t     Quantity  \t\t Expiry \t\t Mrp  \t Total\n")
        self.textarea.insert(END,"--------------------------------------------------------------------------------\n")
     
    def itemlist(self,event):


        n=self.mrp.get()
        m=self.quantity.get()*n
        l.append(m)
        
        self.decrease()
        if self.mainqty>=0:  
            self.textarea.insert((11.0+float(len(l)-1)),f"{self.name.get()} \t\t\t\t {self.quantity.get()} \t  {self.Expiry.get()} \t\t {self.mrp.get()} \t {m}\n")
            
                         
        self.entryclear()

        


    def gbill(self,event):
        tex=self.textarea.get(11.0,(11.0+float(len(l))))
        sumall=sum(l)
        dis=sumall*self.discount.get()//100
        total=sumall-dis
        
        self.totalamount.set(sum(l))
        self.grandamount.set(total)
        

        self.billarea()
        self.textarea.insert(11.0+float(len(l)),tex)
        self.textarea.insert(END,"--------------------------------------------------------------------------------\n")
        self.textarea.insert(END,f"\t\t\t\t\t\tSub Total Amount : {self.totalamount.get()}\n")
        self.textarea.insert(END,f"\t\t\t\t\t\t\tDiscount : {self.discount.get()}\n")
        self.textarea.insert(END,f"\t\t\t\t\t\tAll Total Amount : {self.grandamount.get()}\n")
        
        self.textarea.insert(END,"--------------------------------------------------------------------------------\n")
        # self.savebill()
        
        
        

      

    def savebill(self,event):
        if self.customes_name.get()=="":
            messagebox.showerror("Error","Customer Name Are Required!",parent=self.root)
        
        else:
            op=messagebox.askyesno("Save Bill","Do You Want To Save Bill?",parent=self.root)
            if op>0:
                self.bill_details=self.textarea.get(1.0,END)
                f1=open("bill/"+str(self.bill_no.get())+" "+str(self.customes_name.get())+".txt",'w')
                f1.write(self.bill_details)
                f1.close()
                messagebox.showinfo("Success",f"Bill no :{self.bill_no.get()} {self.customes_name.get()} Saved Successfully",parent=self.root)
                
            else:
                return
        self.show_files()

    def entryclear(self):
        self.id.set("")
        self.name.set("")
        self.batchno1.set("")
        self.quantity.set(0)
        self.Expiry.set("")
        self.mrp.set(0)
        self.discount.set(0)
        
        
        
    def clear(self,event):
        self.customes_name.set("")
        self.address.set("Hoshangabad") 
        self.phone_no.set("")

        self.id.set("")
        self.name.set("")
        self.batchno1.set("")
        self.quantity.set(0)
        self.Expiry.set("")
        self.mrp.set(0)
        self.totalamount.set(0)
        self.discount.set(0)
        self.grandamount.set(0)
        self.textarea.delete(1.0,END)
        self.bill_no.set("")
        x=random.randint(1,50000)
        self.bill_no.set(str(x))
        l.clear()
        self.billarea()

    
    def decrease(self):
        


        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()


        # query='select name from addstock'
        # my_cursor.execute(query)
        # product=my_cursor.fetchall()
        

        sql='select quantity from addstock where id='+self.id.get()+''
        my_cursor.execute(sql)
        row=my_cursor.fetchone()
        global mainqty

        for i in row:

            
            
            self.mainqty= i - self.quantity.get()    

            if self.mainqty>=0:
                my_cursor.execute('update addstock set quantity =? where id=? ',(
                                                            self.mainqty,
                                                            self.id.get()
                ))
            
                # messagebox.showinfo("Success","Medicine Update Succesfully",parent=self.root)
                
               
            else:
                
                messagebox.showinfo("Stock Error","Opps This is "+str(i)+" in Stock",parent=self.root)
                
       
        
            
                
                
        conn.commit()
        conn.close()
        



        # self.qty=self.quantity.get()
 

        # self.mainqty = row - self.qty

        # sql='update addstock set quantity ='+ self.qty +' where name="'+ row+ '";'
        # my_cursor.execute(sql) 
        

        # today = date.today()
        # item_no = self.name.get()
        # qty = self.quantity.get()

        # sql = 'update addstock set quantity = quantity-'+ qty +' where name='+item_no+';'
        
        # my_cursor.execute(sql)
        # print('\n\nItem upated successfully')
       

        # conn.close()

        # conn=sqlite3.connect("database/store3.db")
        # my_cursor=conn.cursor()
        
        # self.qty=self.quantity.get()
        # self.get_name=self.name.get()

        # query='select * from addstock where name="%s"'
        # my_cursor.execute(query)
        # self.pc=my_cursor.fetchall()
        # if self.pc:
        #     for self.r in self.pc:
        #         self.get_id=self.r
        #         self.get_name=self.r
        #         print(self.id)
            
        # product_list.append(self.get_name)
        
        # que='select quantity from addstock where name="%s"'
        # self.dc=my_cursor.execute(que)
        # for j in self.pc:
        #     self.old_stock=j

        # for i in product_list:
        #     for j in self.pc:
        #         self.old_stock=j
        #     self.new_stock=int(self.old_stock) - int(self.qty)
        #     my_cursor.execute("update addstock set quantity=%s where name=%s")
        #     conn.commit()

            




    def Expiry(self):

        conn=sqlite3.connect("database/store3.db")
        my_cursor=conn.cursor()

        exp=self.Expiry.get()
        today=date.today()
        d1=today.strftime("%m/%d/%y")
        sql='select expiry from addstock where expiry="'+ d1 +'"'
        my_cursor.execute(sql)
        row=my_cursor.fetchall()



    def show_files(self):
        files=os.listdir("bill/")
        if len(files)>0:
            self.file_list.delete(0,END)
            for i in files:
                self.file_list.insert(END,i)


    def find_bill(self,event):
        present="no"
        for i in os.listdir("bill/"):
            if i.split('.')[0]==self.searchtxt.get():
                f1=open(f"bill/{i}","r")
                self.textarea.delete("1.0",END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No",parent=self.root)

    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        #print(get_cursor)
        f1=open("bill/"+self.file_list.get(get_cursor))
        self.textarea.delete("1.0",END)
        for f in f1:
            self.textarea.insert(END,f)

    def print_bill(self,ev):
        q=self.textarea.get('1.0',END)
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'Print')


    def inventbutton(self):
        self.newWindow=Toplevel(self.root)
        self.app=INVENTORY(self.newWindow)

    def additem(self):
        self.newWindow=Toplevel(self.root)
        self.app=addstock(self.newWindow)

    def addnew(self):
        self.newWindow=Toplevel(self.root)
        self.app=additem(self.newWindow)

    def adddoctor(self):
        self.newWindow=Toplevel(self.root)
        self.app=adddoctor(self.newWindow)

    def addcompany(self):
        self.newWindow=Toplevel(self.root)
        self.app=addcompany(self.newWindow)

    def searchwindow(self):
        self.newWindow=Toplevel(self.root)
        self.app=searchstock(self.newWindow)

    def exitwindow(self,event):
        self.root.destroy()
        
    

if __name__ == "__main__":
    root = Tk()
    obj=granthmedical(root)
    root.mainloop()
