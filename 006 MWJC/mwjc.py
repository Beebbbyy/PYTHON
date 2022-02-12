from pathlib import Path
from tkinter import * 
import textwrap
import os


screen=Tk()
screen.geometry("500x400")
screen.title("MWJC Correction Script Generator")
description=Label(screen,text='''These program generates a correction scripts for the following fields 
Recommended Min Sell, Estimated Mfg Cost or Standard Cost\n
Click the button for the appropriate action:
ACITON 1. Load Row As is 
ACTION 2. Change an amount to some other number
ACTION 3. Skip row and never load.
        ''', bg="yellow" , justify= "left")
description.pack(expand=TRUE)
description.place(x=50,y=50)


primaryNumber=IntVar()
primaryNumber1=IntVar()
Action1Folder=StringVar()
def upd_JOB_COST():
    a="{Primary_Number}"
    b="{Primary_Number1}"
    c="MWJC_Correction_"+Action1Folder.get()
    d="MWJC_JOB_COST_KEY_"+str(primaryNumber.get())
    e="T1.1.DWSTG.STG"
    if primaryNumber1.get()== 0:
        save_path=r'C:\Users\Rica Mae\Desktop\MWJC_CHECK_202201' #Path
        path_c=c
        complete_name=os.path.join(save_path,path_c,d,e)
        if not os.path.exists(complete_name):
            os.makedirs(complete_name)
        else:
            print("ERROR!")
        create_log_folder=os.path.join(complete_name,'Logs')
        os.mkdir(create_log_folder)
        logs=Path(create_log_folder,'ExecutionLog_DWSTGP.log.txt')
        logs.write_text('')
        upd_JOB_COST_script=upd_JOB_COST_sc.replace(a,str(primaryNumber.get())).replace(b,'')
        upd_JOB_COST_H_script=upd_JOB_COST_sc_H.replace(a,str(primaryNumber.get())).replace(b,'')
        file=Path(complete_name,'1_UPD_STG_MWJC_JOB_COST.sql')
        file_h=Path(complete_name,'2_UPD_STG_MWJC_JOB_COST_H.sql')
        file.write_text(upd_JOB_COST_script)
        file_h.write_text(upd_JOB_COST_H_script)
    else:
        #for multiple primary key
        save_path=r'C:\Users\Rica Mae\Desktop\MWJC_CHECK_202201'
        path_c=c
        complete_name_m=os.path.join(save_path,path_c,"MWJC_JOB_COST_KEY_T1_AS_IS",e)
        if not os.path.exists(complete_name_m):
            os.makedirs(complete_name_m)
        else:
            print("ERROR!")
        create_log_folder=os.path.join(complete_name_m,'Logs')
        os.mkdir(create_log_folder)
        logs=Path(create_log_folder,'ExecutionLog_DWSTGP.log.txt')
        logs.write_text('')
        upd_JOB_COST_script=upd_JOB_COST_sc.replace(a,str(primaryNumber.get())).replace(b,','+str(primaryNumber1.get()))
        upd_JOB_COST_H_script=upd_JOB_COST_sc_H.replace(a,str(primaryNumber.get())).replace(b,','+str(primaryNumber1.get()))
        file=Path(complete_name_m,'1_UPD_STG_MWJC_JOB_COST.sql')
        file_h=Path(complete_name_m,'2_UPD_STG_MWJC_JOB_COST_H.sql')
        file.write_text(upd_JOB_COST_script)
        file_h.write_text(upd_JOB_COST_H_script)
        
    print("UPDATE SCRIPTS UPLOADED SUCCESFULLY: " + save_path)   


def openNewWindow_Action1():
    newWindow=Toplevel(screen)
    newWindow.title("ACTION 1")
    newWindow.geometry("400x400")
    Label(newWindow, text ="ACTION 1",bg="YELLOW",width=390).pack()

    primary_number= Label(newWindow,text="Primay Number: ")
    primary_number.place(x=130, y=50)

    primaryNumber_entry=Entry(newWindow,textvariable= primaryNumber)   
    primaryNumber_entry.place(x=130, y=75)

    #for Multiple 
    primaryNumber_entry=Entry(newWindow,textvariable= primaryNumber1)   
    primaryNumber_entry.place(x=130, y=100)


    #placeholder for the MWJC Folder
    Action1_Folder=Label(newWindow,text="Date: ")
    Action1_Folder.place(x=130, y=220)

    Action1_Folder_entry=Entry(newWindow, textvariable=Action1Folder)
    Action1_Folder_entry.place(x=130, y=245)

    
    UPD_STG_MWJC_JOB_COST_button = Button(newWindow, text="GENERATE SCRIPT", width="25" , height="2", command= upd_JOB_COST)
    UPD_STG_MWJC_JOB_COST_button.place(x=100, y=300)

upd_JOB_COST_sc= textwrap.dedent('''\
SET TIMING ON
SET ECHO 

--MWJC_JOB_COST_KEY {Primary_Number}{Primary_Number1}--

--BEFORE UPDATES--

SELECT MWJC_JOB_COST_KEY,
       SRC_SYS_NM,
       REC_TYP,
       INVC_NBR,
       TRNS_DT,
       JOB_NBR,
       GROS_SALE,
       XFER_COST ,
       STD_COST_OF_SALE,
       REC_MIN_SELL_AMT,
       LD_STTS_CD,
       LM_LD_STTS_CD
    FROM STG_MWJC_JOB_COST
    WHERE MWJC_JOB_COST_KEY IN ({Primary_Number}{Primary_Number1})
    ;

--EXECUTES UPDATES--
UPDATE STG_MWJC_COST
    SET LD_STTS_CD='N', LM_LD_STTS_CD='N'
 WHERE MWJC_JOB_COST_KEY IN ({Primary_Number}{Primary_Number1})
    AND LD_STTS_CD='H'
;
COMMIT;

--AFTER UPDATES--

SELECT MWJC_JOB_COST_KEY,
       SRC_SYST_NM;
       REC_TYP,
       TRNS_DT,
       JOB_NBR,
       GROS_SALE,
       XFER_COST,
       STD_COST_OF_SALE,
       REC_MIN_SELL_AMT,
       LD_STTS_CD,
       LM_LD_STTS_CD
    FROM STG_MWJC_JOB_COST
    WHERE MWJC_JOB_COST_KEY IN ({Primary_Number}{Primary_Number1})
    ;
''')

upd_JOB_COST_sc_H= textwrap.dedent('''\
SET TIMING ON
SET ECHO 

--EXECUTE MERGE for MWJC_JOB_COST_KEY {Primary_Number}{Primary_Number1} --

MERGE
    INTO STG_MWJC_JOB_COST_H A
USING
(
SELECT MWJC_JOB_COST_KEY,
       INC_NBR,
       LD_STTS_CD,
       LM_LD_STTS_CD
    FROM STG_MWJC_JOB_COST) B
        ON ( A.MWJC_JOB_COST_KEY) = B.MWJC_JOB_COST_KEY
            AND B.MWJC_JOB_COST_KEY IN ({Primary_Number}{Primary_Number1})
    WHEN MATCHED
    THEN
UPDATE
    SET A.LD_STTS_CD=B.LD_STTS_CD,
        A.LM_LD_STTS_CD=B.LM_LD_STTS_CD
    ;
COMMIT;
''')


#ACTION 2
def openNewWindow_Action2():
    newWindow=Toplevel(screen)
    newWindow.title("Action 2")
    newWindow.geometry("500x500")
    Label(newWindow, text ="Action 2").pack()





    

def openNewWindow_Action3():
    newWindow=Toplevel(screen)
    newWindow.title("Action 3")
    newWindow.geometry("500x500")
    Label(newWindow, text ="Action 3").pack()


action_1 = Button(screen, text="Action 1", width="10" , height="2", command= openNewWindow_Action1)
action_2 = Button(screen, text="Action 2", width="10" , height="2", command= openNewWindow_Action2)
action_3 = Button(screen, text="Action 3", width="10" , height="2", command= openNewWindow_Action3)
action_1.place(x=100, y=250)
action_2.place(x=200, y=250)
action_3.place(x=300, y=250)

mainloop()