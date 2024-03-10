from tkinter import *
import tkinter
from PIL import Image, ImageTk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import filedialog
import sqlite3
from db import  select, update ,google_list,naver_list
from send import send1 ,send2 
from excelSend import excelplay


root = Tk()
root.title("NADO GUI")
px = "1024" 
py="768"
root.geometry(px+"x"+py)


t_font = ("Helvetica",15)
label_font=("Helvetica",10)
font_3=("Helvetica",15)

def file_open(page):
    global file_path
    file_path = filedialog.askopenfilename(title="파일 선택", filetypes=[("모든 파일", "*.*")])
    path_length = int(len(file_path) /2)

    if file_path:
        if  len(file_path) >= path_length:
            pathname = file_path[:path_length] + "\n" + file_path[path_length:]
            if page == 2:
               path_label2.config(text=f"파일경로:{pathname}")
            elif page == 3:
               path_label3.config(text=f"파일경로:{pathname}")


    else:
        if page == 2:
            path_label2.config(text="파일 선택이 취소되었습니다.")
        if page == 3:
            path_label3.config(text="파일 선택이 취소되었습니다.")






def main_ui_set():


    style = ttk.Style()
    #style.configure("TNotebook", background="red") 
    style.configure("TNotebook.Tab", padding=(20, 5, 20, 5), font=('TkDefaultFont', 14), foreground="black")

    notebook=tkinter.ttk.Notebook(root, width=1024, height=768)
    notebook.pack()

    global f1 ,f2, f3,f4
    bg_f="#D1D1D1"

    f1 = tkinter.Frame(root,bg=bg_f)
    f1.pack(fill="both",expand=True) #익스팬드를 트루로해야지 부모크기에 맞춰짐
    notebook.add(f1,text="기본 전송")

    f2 = tkinter.Frame(root,bg=bg_f)
    f2.pack(fill="both",expand=True) #익스팬드를 트루로해야지 부모크기에 맞춰짐
    notebook.add(f2,text="파일첨부 전송")

    f3 = tkinter.Frame(root,bg=bg_f)
    f3.pack(fill="both",expand=True) #익스팬드를 트루로해야지 부모크기에 맞춰짐
    notebook.add(f3,text="엑셀 자동화 전송")

    f4 = tkinter.Frame(root,bg=bg_f)
    f4.pack(fill="both",expand=True) #익스팬드를 트루로해야지 부모크기에 맞춰짐
    notebook.add(f4,text="설정")



def f1_ui():
    label=tkinter.Label(f1, text="기본 이메일 전송으로 동일한 내용에 이메일을 여러 사람한테 보낼수 있습니다.", width=1024, height=2, fg="black")
    label.pack()

    global title, body
    ####제목 내용 이메일
    lb=Label(f1,text="이메일 제목",width=41,font=label_font)
    lb.place(x=600,y=80)

    title= Text(f1,width=30,height=2,font=t_font)
    title.place(x=600,y=100)

    lb=Label(f1,text="이메일 본문 내용",width=41,font=label_font)
    lb.place(x=600,y=170)
    body= Text(f1,width=30,height=17,font=t_font)
    body.place(x=600,y=190)


    ###전송할 이메일
    lb=Label(f1,text="받는 사람 이메일",width=40,font=label_font)
    lb.place(x=60,y=91)


    all_email_data = []
    datalen = len(all_email_data)
    def inputdata():
        check_email = str(input.get())
        if '@' not in check_email or len(check_email) == 0 or '.' not in check_email:
            commandbox.insert(END,"입력값이 공백 이거나")
            commandbox.insert(END,"@또는.이 안들어 있습니다")
        else:    
            listbox.insert(END,check_email)
            input.delete(0,END)
            all_email_data.append(check_email)
    def minusdata():
        listbox.delete(END)

    input = Entry(f1,width=20,font=font_3)
    input.place(x=60,y=120)
    btn = Button(f1,text="+",width=3,command=inputdata)
    btn.place(x=300,y=121)

    btn_minus= Button(f1,text="-",width=3,command=minusdata)
    btn_minus.place(x=350,y=121)


    listbox = Listbox(f1,width=29,height=10,font=font_3)
    listbox.place(x=60,y=160)


    bar = Scrollbar(f1,command=listbox.yview)
    bar.place(x=366,y=160,height=243)
    listbox.config(yscrollcommand=bar.set)

    ###check 플랫폼
    def check():
        label.config(text=RadioVariety_1.get())

    labelframe=tkinter.LabelFrame(f1, text="이메일 플랫폼 선택",)
    labelframe.place(x=60,y=420)

    RadioVariety_1=tkinter.StringVar()
    RadioVariety_1.set("미선택")

    radio1=tkinter.Radiobutton(labelframe, text="   naver                     ", value="naver", variable=RadioVariety_1, command=check)
    radio1.pack(side="left") 
    radio2=tkinter.Radiobutton(labelframe, text="   google                    ", value="gmail", variable=RadioVariety_1, command=check)
    radio2.pack(side="left")
    label=tkinter.Label(labelframe, text="이메일 선택")
    radio2.pack(side="left")
    print(RadioVariety_1.get())
        

    ###command
    command_title=Label(f1,text="Terminal",width=40,font=label_font)
    command_title.place(x=60,y=500)
    commandbox = Listbox(f1,width=29,height=5,font=font_3)
    commandbox.place(x=60,y=530)

    c_bar = Scrollbar(f1,command=listbox.yview)
    c_bar.place(x=366,y=530,height=125)
    commandbox.config(yscrollcommand=c_bar.set)



    def send_1():
        check = str(RadioVariety_1.get())
        to_email = list(all_email_data)
        title1 = str(title.get("1.0", "end-1c"))
        body1 = str(body.get("1.0", "end-1c"))
        
        
        send1(check,to_email,title1,body1)

    ####
    send_btn = Button(f1,text='이메일 보내기',width=20,font=font_3,command=send_1)
    send_btn.place(x=650,y=600)




def f2_ui():
    label=tkinter.Label(f2, text="파일을 첨부하여 이메일이 전송이 가능합니다", width=1024, height=2, fg="black")
    label.pack()



    ####제목 내용 이메일
    lb=Label(f2,text="이메일 제목",width=41,font=label_font)
    lb.place(x=600,y=80)

    title= Text(f2,width=30,height=2,font=t_font)
    title.place(x=600,y=100)

    lb=Label(f2,text="이메일 본문 내용",width=41,font=label_font)
    lb.place(x=600,y=170)
    body= Text(f2,width=30,height=17,font=t_font)
    body.place(x=600,y=190)


    ###전송할 이메일
    lb=Label(f2,text="받는 사람 이메일",width=40,font=label_font)
    lb.place(x=60,y=91)

    all_email_data = []
    datalen = len(all_email_data)
    def inputdata():
        check_email = str(input.get())
        print(check_email)
        if '@' not in check_email or len(check_email) == 0 or'.' not in check_email:
            commandbox.insert(END,"입력값이 공백 이거나")
            commandbox.insert(END,"@또는.이 안들어 있습니다")
        else:
            listbox.insert(END,check_email)
            input.delete(0,END)
            all_email_data.append(check_email)
            
    def minusdata():
        listbox.delete(END)


    input = Entry(f2,width=20,font=font_3)
    input.place(x=60,y=120)
    btn = Button(f2,text="+",width=3,command=inputdata)
    btn.place(x=300,y=121)
    
    btn_minus= Button(f2,text="-",width=3,command=minusdata)
    btn_minus.place(x=350,y=121)


    listbox = Listbox(f2,width=29,height=10,font=font_3)
    listbox.place(x=60,y=160)


    bar = Scrollbar(f2,command=listbox.yview)
    bar.place(x=366,y=160,height=243)
    listbox.config(yscrollcommand=bar.set)

    ###check 플랫폼
    def check():
        label.config(text=RadioVariety_1.get())
        
    labelframe=tkinter.LabelFrame(f2, text="이메일 플랫폼 선택",)
    labelframe.place(x=60,y=420)

    RadioVariety_1=tkinter.StringVar()
    RadioVariety_1.set("미선택")

    radio1=tkinter.Radiobutton(labelframe, text="   naver                     ", value="naver", variable=RadioVariety_1, command=check)
    radio1.pack(side="left") 
    radio2=tkinter.Radiobutton(labelframe, text="   google                    ", value="google", variable=RadioVariety_1, command=check)
    radio2.pack(side="left")
    label=tkinter.Label(labelframe, text="이메일 선택")
    radio2.pack(side="left")


    ###command
    command_title=Label(f2,text="Terminal",width=40,font=label_font)
    command_title.place(x=60,y=500)
    commandbox = Listbox(f2,width=29,height=5,font=font_3)
    commandbox.place(x=60,y=530)

    c_bar = Scrollbar(f2,command=listbox.yview)
    c_bar.place(x=366,y=530,height=125)
    commandbox.config(yscrollcommand=c_bar.set)




    ## path sys
    global path_label2
    path_label2 = Label(f2, text="")
    path_label2.place(x=670,y=600 )
    
    path_btn = Button(f2,text="파일 첨부",command=lambda: file_open(2))
    path_btn.place(x=600,y=600)



    

    def send_2():
        check = str(RadioVariety_1.get())
        to_email = list(all_email_data)
        title1 = str(title.get("1.0", "end-1c"))
        body1 = str(body.get("1.0", "end-1c"))
        path = file_path
        send2(check,to_email,title1,body1,path)

        ####
    send_btn = Button(f2,text='이메일 보내기',width=20,font=font_3,command=send_2)
    send_btn.place(x=650,y=660)


def f3_ui():
    label=tkinter.Label(f3, text="엑셀을 첨부하여 자동 전송이 가능합니다", width=1024, height=2, fg="black")
    label.pack()


    ###check 플랫폼
    def check():
        label.config(text=RadioVariety_1.get())
     

        
    labelframe=tkinter.LabelFrame(f3, text="이메일 플랫폼 선택",)
    labelframe.place(x=350,y=150)

    RadioVariety_1=tkinter.StringVar()
    RadioVariety_1.set("미선택")

    radio1=tkinter.Radiobutton(labelframe, text="   naver                     ", value="naver", variable=RadioVariety_1, command=check)
    radio1.pack(side="left") 
    radio2=tkinter.Radiobutton(labelframe, text="   google                    ", value="google", variable=RadioVariety_1, command=check)
    radio2.pack(side="left")
    label=tkinter.Label(labelframe, text="이메일 선택")
    radio2.pack(side="left")





    ## path sys
    global path_label3
    path_label3 = Label(f3, text="")
    path_label3.place(x=350,y=220 )

    path_btn = Button(f3,text="엑셀 파일 첨부",command=lambda: file_open(3))
    path_btn.place(x=350,y=270)


    command_title=Label(f3,text="Terminal",width=40,font=label_font)
    command_title.place(x=350,y=330)
    commandbox = Listbox(f3,width=29,height=5,font=font_3)
    commandbox.place(x=350,y=360)

    c_bar = Scrollbar(f3,command=commandbox.yview)
    c_bar.place(x=660,y=360,height=125)
    commandbox.config(yscrollcommand=c_bar.set)


        ####
    def send_excel():
        email_select = RadioVariety_1.get()
        excelplay(email_select,file_path)
        commandbox.insert(END,"이메일이 전송 되었습니다")
    
    

    send_btn = Button(f3,text='이메일 보내기',width=25,font=font_3,command=send_excel)
    send_btn.place(x=375,y=500)

def refresh():
    print("click")


    select()
    print(naver_list,google_list)
    g_data = "아이디:"+ google_list[1] +"\n"+"비밀번호:"+google_list[2]
    n_data="아이디:" + naver_list[1]+"\n"+"비밀번호:"+naver_list[2]
    naver_data.config(text=str(n_data))
    google_data.config(text=str(g_data))
    
def save_db():

    googleID = str(g_id_input.get())
    googlePW = str(g_pw_input.get())
    naverID = str(n_id_input.get())
    naverPW = str(n_pw_input.get())

    update(naverID,naverPW,googleID,googlePW)

    input_reset()

def input_reset():
    g_id_input.delete(0,END)
    g_pw_input.delete(0,END)
    n_id_input.delete(0,END)
    n_pw_input.delete(0,END)


def set_page():
    global g_id_input,g_pw_input,n_id_input,n_pw_input, save_data,naver_data, google_data
    g_id = Label(f4,text="구글 아이디")
    g_pw = Label(f4,text="구글 비밀번호")
    n_id = Label(f4,text="네이버 아이디")
    n_pw = Label(f4,text="네이버 비밀번호")


    g_id_input=Entry(f4,width=30)
    g_pw_input=Entry(f4,width=30)
    n_id_input=Entry(f4,width=30)
    n_pw_input=Entry(f4,width=30)
  
    g_id.place(x=300,y=300)
    g_pw.place(x=300,y=350)
    n_id.place(x=300,y=400)
    n_pw.place(x=300,y=450)
    
    g_id_input.place(x=400,y=300)
    g_pw_input.place(x=400,y=350)
    n_id_input.place(x=400,y=400)
    n_pw_input.place(x=400,y=450)


    save_btn= Button(f4,width=10,height=11,text="저장",command=save_db)
    save_btn.place(x=640,y=300)
    
    
 


    save_data=Label(f4,width=60,height=15,bg="#F0F0F0")
    save_data.place(x=300,y=50)

    save_title=Label(f4,text="저장중인 ID/PW 정보",width=60,height=2,bg="white")
    save_title.place(x=300,y=50)

    refresh_btn = Button(f4,text="새로고침",command=refresh)
    refresh_btn.place(x=650,y=60)

    g_data=Label(f4,text="구글 계정",width=10,height=1,bg="gray")
    g_data.place(x=300,y=100)
    n_data=Label(f4,text="네이버 계정",width=10,height=1,bg="gray")
    n_data.place(x=300,y=200)
    select()

    g_data = "아이디:"+ google_list[1] +"\n"+"비밀번호:"+google_list[2]
    n_data = "아이디:" + naver_list[1]+"\n"+"비밀번호:"+naver_list[2]
    google_data = Label(f4,text=g_data,bg="white")
    naver_data = Label(f4,text=n_data,bg="white")

    google_data.place(x=460,y=100)
    naver_data.place(x=460,y=200)
    



main_ui_set()
f1_ui()
f2_ui()
f3_ui()
set_page()



root.mainloop()
