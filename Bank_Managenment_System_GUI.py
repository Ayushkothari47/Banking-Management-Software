import customtkinter as ctk
from PIL import Image, ImageTk
import csv
import os
import random
import webbrowser

url = 'https://www.instagram.com/aayush_kotharii/'


def screenAdjuster():
    #Getting Screen Width
    screenWidth= app.winfo_screenwidth()
    screenHeight= app.winfo_screenheight()
    mainScreenWidth= (screenWidth*75)//100
    mainScreenHeight= (screenHeight*75)//100
    return mainScreenWidth,mainScreenHeight

def success(caller,id):
        clearScreen()
        Width= app.winfo_screenwidth()
        Height= app.winfo_screenheight()
        Width= app.winfo_screenwidth()
        Height= app.winfo_screenheight()

        frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
        frame.pack(expand=True, fill="both")

        container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
        container.place(x=((Width*15)//100),y=((Height*10)//100))


        text= ctk.CTkLabel(container,text="Success !",text_color="#4CBB17",font=("default",40,"bold"))
        text.place(x=(Width*28)//100, y=(Height*10)//100)


        decoder= caller[:7]
        print("called: ",caller)
        print("Decoder: ",decoder)

        if caller=="deposite" or caller=="withdraw" or caller=="accountDeleted":
            text_wait= ctk.CTkLabel(container,text="Please wait, you will be redirected to dashboard",text_color="black",font=("default",30,))
            text_wait.place(x=(Width*10)//100, y=(Height*25)//100)
            app.after(5000,lambda: dashboard(id))
        
        elif decoder=="newUser":
            accountNumber=str(caller[7:])
            print("Account number: ",accountNumber)
            text_wait= ctk.CTkLabel(container,text="New Account Number: "+accountNumber,text_color="black",font=("default",25,))
            text_wait.place(x=(Width*18)//100, y=(Height*25)//100)

            buttonDone= ctk.CTkButton(container, text="DONE",fg_color="#5D3FD3",font=("default",18,"bold"), height=40, width=140, command=lambda: app.after(5000,lambda: dashboard(id)),hover_color="#8a2be2")
            buttonDone.place(x=(Width*30)//100, y=(Height*40)//100)
            
def fail(caller,id):
    clearScreen()
    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()
    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
    container.place(x=((Width*15)//100),y=((Height*10)//100))


    text= ctk.CTkLabel(container,text="failed !",text_color="red",font=("default",40,"bold"))
    text.place(x=(Width*30)//100, y=(Height*10)//100)


    if caller=="emptyDatabase":
        text_wait= ctk.CTkLabel(container,text="Database not exists!, If this is first time please open account first!",text_color="black",font=("default",20))
        text_wait.place(x=(Width*10)//100, y=(Height*20)//100)

        text_wait= ctk.CTkLabel(container,text="If you already opened account, it means file is either deleted or moved",text_color="black",font=("default",20))
        text_wait.place(x=(Width*10)//100, y=(Height*25)//100)

        okBtn= ctk.CTkButton(container,text="OKAY",font=("default",20,"bold"), text_color="white",fg_color="#5D3FD3", hover_color="green", height=40, width=140, command= lambda: dashboard(id))
        okBtn.place(x=(Width*28)//100, y=(Height*35)//100)


    elif caller=="insuffcientBal":
        text_wait= ctk.CTkLabel(container,text="Not enough Balance",text_color="red",font=("default",24))
        text_wait.place(x=(Width*28)//100, y=(Height*20)//100)

        text_wait= ctk.CTkLabel(container,text="Kindly check account balance first, before withdrawing.",text_color="black",font=("default",24))
        text_wait.place(x=(Width*15)//100, y=(Height*30)//100)

        okBtn= ctk.CTkButton(container,text="OKAY",font=("default",20,"bold"), text_color="white",fg_color="#5D3FD3", hover_color="green", height=40, width=140, command= lambda: withdraw(id))
        okBtn.place(x=(Width*29)//100, y=(Height*40)//100)

    
    elif caller=="userNotFound":
        text_wait= ctk.CTkLabel(container,text="User Not Found !",text_color="red",font=("default",24))
        text_wait.place(x=(Width*28)//100, y=(Height*20)//100)

        text_wait= ctk.CTkLabel(container,text="Either invalid account number or account does not exists",text_color="black",font=("default",24))
        text_wait.place(x=(Width*15)//100, y=(Height*30)//100)

        okBtn= ctk.CTkButton(container,text="OKAY",font=("default",20,"bold"), text_color="white",fg_color="#5D3FD3", hover_color="green", height=40, width=140, command= lambda: fetchDetail(id))
        okBtn.place(x=(Width*29)//100, y=(Height*40)//100)

    elif caller=="userNotFoundD":
        text_wait= ctk.CTkLabel(container,text="User Not Found !",text_color="red",font=("default",24))
        text_wait.place(x=(Width*28)//100, y=(Height*20)//100)

        text_wait= ctk.CTkLabel(container,text="Either invalid account number or account does not exists",text_color="black",font=("default",24))
        text_wait.place(x=(Width*15)//100, y=(Height*30)//100)

        okBtn= ctk.CTkButton(container,text="OKAY",font=("default",20,"bold"), text_color="white",fg_color="#5D3FD3", hover_color="green", height=40, width=140, command= lambda: delectAccount(id))
        okBtn.place(x=(Width*29)//100, y=(Height*40)//100)

def saveData(userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,id):
    filepath= os.path.dirname(os.path.abspath(__file__))
    print("File path: ",filepath)
    
    newAccountNumber= random.randint(10**11,10**13)
    newBal=0
    file_exists= os.path.exists(filepath+"\\data\\database\\accounts.csv")
    if file_exists:
        with open(filepath+"\\data\\database\\accounts.csv","a+",newline='') as accountFile:
                writer= csv.writer(accountFile)
                record=[newAccountNumber,userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,newBal]
                writer.writerow(record)
        
    else:
        print("File not exists!, new file created")
        with open(filepath+"\\data\\database\\accounts.csv","w",newline='') as accountFile:
            writer= csv.writer(accountFile)
            record=[newAccountNumber,userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,newBal]
            writer.writerow(record)
    
    success("newUser"+str(newAccountNumber),id)

def wrongUserDetail(userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,redFlagFName,redFlagLName,redFlagDOB,redFlagPan,redFlagAadhaar,redFlagPhone,redFlagGender,redFlagAddress,id):
    clearScreen()

    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
    container.place(x=((Width*15)//100),y=((Height*10)//100))

    imgContainer= ctk.CTkFrame(container, fg_color="grey", height=200, width=200)
    imgContainer.place(x=(Width*5)//100, y=(Height*5)//100)

    imgUploadBtn= ctk.CTkButton(container, text="UPLOAD IMAGE", fg_color="orange", text_color="white", height=40, width=160, font=("default",18,"bold"))
    imgUploadBtn.place(x=(Width*7)//100, y=(Height*36)//100) 

    if(redFlagFName==1):
        userFNameBox= ctk.CTkEntry(container, placeholder_text="First Name", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userFNameBox.place(x=(Width*25)//100, y=(Height*10)//100)
    else:
        userFNameBox= ctk.CTkEntry(container, placeholder_text=userFName, font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=0)
        userFNameBox.place(x=(Width*25)//100, y=(Height*10)//100)
        userFNameBox.delete(0, ctk.END)
        userFNameBox.insert(0, userFName)

    if(redFlagLName==1):
        userLNameBox= ctk.CTkEntry(container, placeholder_text="Last Name", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userLNameBox.place(x=(Width*45)//100, y=(Height*10)//100)
    else:
        userLNameBox= ctk.CTkEntry(container, placeholder_text=userLName, font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=0)
        userLNameBox.place(x=(Width*45)//100, y=(Height*10)//100)
        userLNameBox.delete(0, ctk.END)
        userLNameBox.insert(0, userLName)

    if(redFlagDOB==1):
        userDOBBox= ctk.CTkEntry(container, placeholder_text="DOB: DD-MM-YYYY", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color="red", border_width=1) 
        userDOBBox.place(x=(Width*25)//100, y=(Height*20)//100)
    else:
        userDOBBox= ctk.CTkEntry(container, placeholder_text=userDOB, font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=0)
        userDOBBox.place(x=(Width*25)//100, y=(Height*20)//100)
        userDOBBox.delete(0, ctk.END)
        userDOBBox.insert(0, userDOB)

    if(redFlagPan==1):
        userPanBox= ctk.CTkEntry(container, placeholder_text="PAN card number", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userPanBox.place(x=(Width*25)//100, y=(Height*30)//100)
    else:
        userPanBox= ctk.CTkEntry(container, placeholder_text=userPan, font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=0)
        userPanBox.place(x=(Width*25)//100, y=(Height*30)//100)
        userPanBox.delete(0, ctk.END)
        userPanBox.insert(0, userPan)
        
    if(redFlagAadhaar==1):
        userAadhaarBox= ctk.CTkEntry(container, placeholder_text="Aadhaar card number", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userAadhaarBox.place(x=(Width*25)//100, y=(Height*40)//100)
    else:
        userAadhaarBox= ctk.CTkEntry(container, placeholder_text=userAadhaar, font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=0)
        userAadhaarBox.place(x=(Width*25)//100, y=(Height*40)//100)
        userAadhaarBox.delete(0, ctk.END)
        userAadhaarBox.insert(0, userAadhaar)

    if(redFlagPhone==1):
        userPhoneBox= ctk.CTkEntry(container, placeholder_text="Phone number", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userPhoneBox.place(x=(Width*45)//100, y=(Height*20)//100)
    else:
        userPhoneBox= ctk.CTkEntry(container, placeholder_text=userPhone, font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=0)
        userPhoneBox.place(x=(Width*45)//100, y=(Height*20)//100)
        userPhoneBox.delete(0, ctk.END)
        userPhoneBox.insert(0, userPhone)
    
    if(redFlagGender==1):
        userGenderBox= ctk.CTkEntry(container, placeholder_text="Gender", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userGenderBox.place(x=(Width*45)//100, y=(Height*30)//100)
    else:
        userGenderBox= ctk.CTkEntry(container, placeholder_text=userGender, font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=0)
        userGenderBox.place(x=(Width*45)//100, y=(Height*30)//100)
        userGenderBox.delete(0, ctk.END)
        userGenderBox.insert(0, userGender)
        
    if(redFlagAddress==1):
        userAddressBox= ctk.CTkEntry(container, placeholder_text="Address", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userAddressBox.place(x=(Width*45)//100, y=(Height*40)//100)
    else:
        userAddressBox= ctk.CTkEntry(container, placeholder_text=userAddress, font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=0)
        userAddressBox.place(x=(Width*45)//100, y=(Height*40)//100)
        userAddressBox.delete(0, ctk.END)
        userAddressBox.insert(0, userAddress)

    submitBtn= ctk.CTkButton(container,text="SUBMIT",fg_color="green", text_color="white", height=40, width=160, font=("default",18,"bold"), hover_color="lime",command=lambda: checkDetails(userFNameBox.get(),userLNameBox.get(), userDOBBox.get(),userPanBox.get(),userAadhaarBox.get(),userPhoneBox.get(),userGenderBox.get(),userAddressBox.get(),id))
    submitBtn.place(x=(Width*35)//100, y=(Height*50)//100)

def checkDetails(userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,id):

    redFlagFName,redFlagLName,redFlagDOB,redFlagPan,redFlagAadhaar,redFlagPhone,redFlagGender,redFlagAddress=1,1,1,1,1,1,1,1


    if(len(userFName)>0 and userFName.isalpha()):
        redFlagFName=0
        
    if(len(userLName)>0 and userLName.isalpha()):
        redFlagLName=0

    try:
        if(userDOB[2]=='-' and userDOB[5]=='-' and 0<int(userDOB[0:2])<=31 and 0<int(userDOB[3:5])<=12):
            redFlagDOB=0
    except Exception:
        pass
    
    if(len(userPan)==10):
        redFlagPan=0

    if(len(userAadhaar)==12):
        redFlagAadhaar=0
    
    if(len(userPhone)==10):
        redFlagPhone=0
    
    if(userGender!=''):
        redFlagGender=0
    
    if(userAddress!=''):
        redFlagAddress=0
    
    if(redFlagFName==0 and redFlagLName==0 and redFlagDOB==0 and redFlagPan==0 and redFlagAadhaar==0 and redFlagPhone==0 and redFlagGender==0 and redFlagAddress==0):
        print("\nNew User Details are all set")
        saveData(userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,id)
    else:
        wrongUserDetail(userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,redFlagFName,redFlagLName,redFlagDOB,redFlagPan,redFlagAadhaar,redFlagPhone,redFlagGender,redFlagAddress,id) 

def wrongDepositeDetails(userFName,userAccountNumber,userPan,amount,nameFlag,accountFlag,panFlag,amountFlag,id):
    clearScreen()
    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()
    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")
    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*65)//100, width=(Width*25)//100)
    container.place(x=((Width*40)//100),y=((Height*15)//100))
    textDepo= ctk.CTkLabel(container,text="MONEY DEPOSITE WINDOW",font=("default",20,"bold"),text_color="black")
    textDepo.place(x=(Width*2)//100, y=(Height*5)//100)

    if nameFlag==1:
        userFNameBox= ctk.CTkEntry(container, placeholder_text="First Name", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userFNameBox.place(x=(Width*2)//100, y=(Height*15)//100)
    else:
        userFNameBox= ctk.CTkEntry(container, placeholder_text=userFName, font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
        userFNameBox.place(x=(Width*2)//100, y=(Height*15)//100)
        userFNameBox.delete(0, ctk.END)
        userFNameBox.insert(0, userFName)
    
    if accountFlag==1:
        userAccountNumberBox= ctk.CTkEntry(container, placeholder_text="Account Number", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userAccountNumberBox.place(x=(Width*2)//100, y=(Height*25)//100)
    else:
        userAccountNumberBox= ctk.CTkEntry(container, placeholder_text=userAccountNumber, font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
        userAccountNumberBox.place(x=(Width*2)//100, y=(Height*25)//100)
        userAccountNumberBox.delete(0, ctk.END)
        userAccountNumberBox.insert(0, userAccountNumber)

    if panFlag==1:
        userPanBox= ctk.CTkEntry(container, placeholder_text="PAN Card Number", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userPanBox.place(x=(Width*2)//100, y=(Height*35)//100)
    else:
        userPanBox= ctk.CTkEntry(container, placeholder_text=userPan, font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
        userPanBox.place(x=(Width*2)//100, y=(Height*35)//100)
        userPanBox.delete(0, ctk.END)
        userPanBox.insert(0, userPan)

    if amountFlag==1:
        amountBox= ctk.CTkEntry(container, placeholder_text="Amount", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        amountBox.place(x=(Width*2)//100, y=(Height*45)//100)
    else:
        amountBox= ctk.CTkEntry(container, placeholder_text=amount, font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
        amountBox.place(x=(Width*2)//100, y=(Height*45)//100)
        amountBox.delete(0, ctk.END)
        amountBox.insert(0, amount)

    submitBtn= ctk.CTkButton(container, text="DEPOSITE",font=("default",20,"bold"),height=40,width=140,text_color="white", fg_color="orange", command=lambda: checkDepoDetails(userFNameBox.get(),userAccountNumberBox.get(),userPanBox.get(),amountBox.get(),id))
    submitBtn.place(x=(Width*7)//100, y=(Height*55)//100)

def depoAmount(userAccountNumber, amount, id):
    filepath = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(filepath, "data", "database", "accounts.csv")
    file_exists = os.path.exists(file_path)

    tranFilePath= os.path.dirname(os.path.abspath(__file__))
    TF_exists= os.path.exists(tranFilePath+"\\data\\database\\transactionRecorder.csv")

    transactionID= random.randint(10**11, 12**13)

    if file_exists:
        updated_records = []
        with open(file_path, "r", newline='') as account_file:
            reader = csv.reader(account_file)
            for row in reader:
                if userAccountNumber == row[0]:
                    user_bal = int(row[9])
                    new_bal = str(user_bal + int(amount))
                    row[9] = new_bal 
                updated_records.append(row)
        
        if TF_exists:
            with open(tranFilePath+"\\data\\database\\transactionRecorder.csv","a+",newline='') as TF_File:
                TFwriter= csv.writer(TF_File)
                amount= int(amount)
                rec=[str(userAccountNumber),str((amount)),str(transactionID)]
                TFwriter.writerow(rec)
        else:
            print("Transaction file not exists so new file auto created !")
            with open(tranFilePath+"\\data\\database\\transactionRecorder.csv","w",newline='') as TF_File:
                TFwriter= csv.writer(TF_File)
                amount= int(amount)
                rec=[str(userAccountNumber),str((amount)),str(transactionID)]
                TFwriter.writerow(rec)
        
        vaultFilePath= os.path.dirname(os.path.abspath(__file__))
        with open(vaultFilePath+"\\data\\database\\bankVault.csv","r",newline='') as vault_file:
            rec=[]
            vaultFileReader = csv.reader(vault_file)
            for row in vaultFileReader:
                vaultMoney= row[0]
            newVaultValue=str(int(vaultMoney)+int(amount))
            rec.append(newVaultValue)
            print("\n\nold vault Money: ",vaultMoney)
            print("\nWithdrawl amount: ",amount)
            print("\nNew Vault Value: ",newVaultValue)
           

        with open(vaultFilePath+"\\data\\database\\bankVault.csv","w",newline='') as vault_file:
            writer = csv.writer(vault_file)
            writer.writerow(rec)



        with open(file_path, "w", newline='') as account_file:
            writer = csv.writer(account_file)
            writer.writerows(updated_records)

        print("user balance updated successfully!")
        success("deposite",id)
    else:
        print("File not found or accounts.csv does not exist.")

def checkDepoDetails(userFName,userAccountNumber,userPan,amount,id):
    nameFlag=1
    accountFlag=1
    panFlag=1
    amountFlag=1

    filepath= os.path.dirname(os.path.abspath(__file__))
    file_exists= os.path.exists(filepath+"\\data\\database\\accounts.csv")

    if(file_exists):
        with open(filepath+"\\data\\database\\accounts.csv","r",newline='') as accountFile:
            reader= csv.reader(accountFile)

            for row in reader:
                if userAccountNumber==row[0]:
                    accountFlag=0

                if userFName.lower()==row[1].lower():
                    nameFlag=0

                if userPan==row[4]:
                    panFlag=0
        
        
        with open(filepath+"\\data\\database\\bankVault.csv","r",newline='') as vaultFile:
            reader2= csv.reader(vaultFile)
            for row in reader2:
                vaultAmount= row[0]
        
        print("Bank Vault: ",vaultAmount)

        if int(amount)<int(vaultAmount):
            amountFlag=0

        if(nameFlag==0 and accountFlag==0 and panFlag==0 and amountFlag==0):
            print("\nAll details are ok, going for deposite")
            depoAmount(userAccountNumber,amount,id)
            
        else:
            wrongDepositeDetails(userFName,userAccountNumber,userPan,amount,nameFlag,accountFlag,panFlag,amountFlag,id)
        

    
    else:
        fail("emptyDatabase",id)

def deposit(id):
    clearScreen()
    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*65)//100, width=(Width*25)//100)
    container.place(x=((Width*40)//100),y=((Height*15)//100))

    textDepo= ctk.CTkLabel(container,text="MONEY DEPOSITE WINDOW",font=("default",20,"bold"),text_color="black")
    textDepo.place(x=(Width*2)//100, y=(Height*5)//100)


    userFName= ctk.CTkEntry(container, placeholder_text="First Name", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userFName.place(x=(Width*2)//100, y=(Height*15)//100)

    userAccountNumber= ctk.CTkEntry(container, placeholder_text="Account Number", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userAccountNumber.place(x=(Width*2)//100, y=(Height*25)//100)

    userPan= ctk.CTkEntry(container, placeholder_text="PAN Card Number", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userPan.place(x=(Width*2)//100, y=(Height*35)//100)

    amount= ctk.CTkEntry(container, placeholder_text="Amount", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    amount.place(x=(Width*2)//100, y=(Height*45)//100)

    submitBtn= ctk.CTkButton(container, text="DEPOSITE",font=("default",20,"bold"),height=40,width=140,text_color="white", fg_color="orange", command=lambda: checkDepoDetails(userFName.get(),userAccountNumber.get(),userPan.get(),amount.get(),id))
    submitBtn.place(x=(Width*7)//100, y=(Height*55)//100)

def wrongWithdrawDetails(userFName,userAccountNumber,userPan,amount,nameFlag,accountFlag,panFlag,amountFlag,id):
    clearScreen()
    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()
    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")
    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*65)//100, width=(Width*25)//100)
    container.place(x=((Width*40)//100),y=((Height*15)//100))
    textDepo= ctk.CTkLabel(container,text="MONEY WITHDRAW WINDOW",font=("default",20,"bold"),text_color="black")
    textDepo.place(x=(Width*2)//100, y=(Height*5)//100)

    if nameFlag==1:
        userFNameBox= ctk.CTkEntry(container, placeholder_text="First Name", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userFNameBox.place(x=(Width*2)//100, y=(Height*15)//100)
    else:
        userFNameBox= ctk.CTkEntry(container, placeholder_text=userFName, font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
        userFNameBox.place(x=(Width*2)//100, y=(Height*15)//100)
        userFNameBox.delete(0, ctk.END)
        userFNameBox.insert(0, userFName)
    
    if accountFlag==1:
        userAccountNumberBox= ctk.CTkEntry(container, placeholder_text="Account Number", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userAccountNumberBox.place(x=(Width*2)//100, y=(Height*25)//100)
    else:
        userAccountNumberBox= ctk.CTkEntry(container, placeholder_text=userAccountNumber, font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
        userAccountNumberBox.place(x=(Width*2)//100, y=(Height*25)//100)
        userAccountNumberBox.delete(0, ctk.END)
        userAccountNumberBox.insert(0, userAccountNumber)

    if panFlag==1:
        userPanBox= ctk.CTkEntry(container, placeholder_text="PAN Card Number", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        userPanBox.place(x=(Width*2)//100, y=(Height*35)//100)
    else:
        userPanBox= ctk.CTkEntry(container, placeholder_text=userPan, font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
        userPanBox.place(x=(Width*2)//100, y=(Height*35)//100)
        userPanBox.delete(0, ctk.END)
        userPanBox.insert(0, userPan)

    if amountFlag==1:
        amountBox= ctk.CTkEntry(container, placeholder_text="Amount", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color="red", border_width=1)
        amountBox.place(x=(Width*2)//100, y=(Height*45)//100)
    else:
        amountBox= ctk.CTkEntry(container, placeholder_text=amount, font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
        amountBox.place(x=(Width*2)//100, y=(Height*45)//100)
        amountBox.delete(0, ctk.END)
        amountBox.insert(0, amount)

    submitBtn= ctk.CTkButton(container, text="WITHDRAW",font=("default",20,"bold"),height=40,width=140,text_color="white", fg_color="orange", command=lambda: checkWithdrawDetails(userFNameBox.get(),userAccountNumberBox.get(),userPanBox.get(),amountBox.get(),id))
    submitBtn.place(x=(Width*7)//100, y=(Height*55)//100)

def withdrawAmount(userAccountNumber, amount, id):
    filepath = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(filepath, "data", "database", "accounts.csv")
    file_exists = os.path.exists(file_path)

    tranFilePath= os.path.dirname(os.path.abspath(__file__))
    TF_exists= os.path.exists(tranFilePath+"\\data\\database\\transactionRecorder.csv")

    transactionID= random.randint(10**11, 12**13)

    if file_exists:
        updated_records = []
        with open(file_path, "r", newline='') as account_file:
            reader = csv.reader(account_file)
            for row in reader:
                if userAccountNumber == row[0]:
                    user_bal = int(row[9])  
                    amount= int(amount)

                    if(user_bal<amount):
                        fail("insuffcientBal",id)
                    

                    new_bal = str(int(user_bal) -   int(amount))
                    row[9] = new_bal 
                updated_records.append(row)

        if TF_exists:
            with open(tranFilePath+"\\data\\database\\transactionRecorder.csv","a+",newline='') as TF_File:
                TFwriter= csv.writer(TF_File)
                amount= int(-amount)
                rec=[str(userAccountNumber),str((amount)),str(transactionID)]
                TFwriter.writerow(rec)
        
        else:
            print("Transaction file not exists so new file auto created !")
            with open(tranFilePath+"\\data\\database\\transactionRecorder.csv","w",newline='') as TF_File:
                TFwriter= csv.writer(TF_File)
                amount= int(-amount)
                rec=[str(userAccountNumber),str((amount)),str(transactionID)]
                TFwriter.writerow(rec)
                
        vaultFilePath= os.path.dirname(os.path.abspath(__file__))
        with open(vaultFilePath+"\\data\\database\\bankVault.csv","r",newline='') as vault_file:
            rec=[]
            vaultFileReader = csv.reader(vault_file)
            for row in vaultFileReader:
                vaultMoney= row[0]
                #DECDUCTION OF MONEY, AS AMOUNT IS IN NEGATIVE FORM SO (+) + (-) = -
            newVaultValue=str(int(vaultMoney)-int(amount))
            rec.append(newVaultValue)
            print("\n\nold vault Money: ",vaultMoney)
            print("\nWithdrawl amount: ",amount)
            print("\nNew Vault Value: ",newVaultValue)
           

        with open(vaultFilePath+"\\data\\database\\bankVault.csv","w",newline='') as vault_file:
            writer = csv.writer(vault_file)
            writer.writerow(rec)

        with open(file_path, "w", newline='') as account_file:
            writer = csv.writer(account_file)
            writer.writerows(updated_records)

        print("user balance updated successfully!")
        success("withdraw",id)
    else:
        print("File not found or accounts.csv does not exist.")
        fail("emptyDatabase",id)

def checkWithdrawDetails(userFName,userAccountNumber,userPan,amount,id):
    nameFlag=1
    accountFlag=1
    panFlag=1
    amountFlag=1

    filepath= os.path.dirname(os.path.abspath(__file__))
    file_exists= os.path.exists(filepath+"\\data\\database\\accounts.csv")

    

    if(file_exists):
        with open(filepath+"\\data\\database\\accounts.csv","r",newline='') as accountFile:
            reader= csv.reader(accountFile)

            for row in reader:
                if userAccountNumber==row[0]:
                    accountFlag=0

                if userFName.lower()==row[1].lower():
                    nameFlag=0

                if userPan==row[4]:
                    panFlag=0
        
        
        with open(filepath+"\\data\\database\\bankVault.csv","r",newline='') as vaultFile:
            reader2= csv.reader(vaultFile)
            for row in reader2:
                vaultAmount= row[0]
        
        print("Bank Vault: ",vaultAmount)

        if int(amount)<int(vaultAmount):
            amountFlag=0
        
        print("Amount Flag: ",amountFlag,"As Withdrawl amout: ",amount,"and vault amount:",vaultAmount)

        if(nameFlag==0 and accountFlag==0 and panFlag==0 and amountFlag==0):
            print("\nAll details are ok, going for withdraw")
            withdrawAmount(userAccountNumber,amount,id)
            
        else:
            wrongWithdrawDetails(userFName,userAccountNumber,userPan,amount,nameFlag,accountFlag,panFlag,amountFlag,id)
        

    else:
        fail("emptyDatabase",id)

def withdraw(id):
    clearScreen()
    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")
    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*65)//100, width=(Width*25)//100)
    container.place(x=((Width*40)//100),y=((Height*15)//100))
    textDepo= ctk.CTkLabel(container,text="MONEY WITHDRAW WINDOW",font=("default",20,"bold"),text_color="black")
    textDepo.place(x=(Width*2)//100, y=(Height*5)//100)

    userFName= ctk.CTkEntry(container, placeholder_text="First Name", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userFName.place(x=(Width*2)//100, y=(Height*15)//100)

    userAccountNumber= ctk.CTkEntry(container, placeholder_text="Account Number", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userAccountNumber.place(x=(Width*2)//100, y=(Height*25)//100)

    userPan= ctk.CTkEntry(container, placeholder_text="PAN Card Number", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userPan.place(x=(Width*2)//100, y=(Height*35)//100)

    amount= ctk.CTkEntry(container, placeholder_text="Amount", font=("default",18), fg_color="#D1D1D1", height=40, width=260,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    amount.place(x=(Width*2)//100, y=(Height*45)//100)

    submitBtn= ctk.CTkButton(container, text="WITHDRAW",font=("default",20,"bold"),height=40,width=140,text_color="white", fg_color="orange", command=lambda: checkWithdrawDetails(userFName.get(),userAccountNumber.get(),userPan.get(),amount.get(),id))
    submitBtn.place(x=(Width*7)//100, y=(Height*55)//100)

def detailFetcher(userAccountNumber,id):
    if(userAccountNumber==''):
        fail("userNotFound",id)
        
    filepath= os.path.dirname(os.path.abspath(__file__))
    file_exists= os.path.exists(filepath+"\\data\\database\\accounts.csv")

    if(file_exists):
        with open(filepath+"\\data\\database\\accounts.csv","r",newline='') as accountFile:
            reader= csv.reader(accountFile)
            found=0
            for row in reader:
                try:
                    if userAccountNumber==row[0]:
                        found=1
                        userFName= row[1]
                        userLName= row[2]
                        userDOB= row[3]
                        userPan= row[4]
                        userAadhaar= row[5]
                        userPhone= row[6]
                        userGender= row[7]
                        userAddress= row[8]
                        userBal= row[9]
                except UnboundLocalError:
                    print("Local Error Handled !")
        
        if(found==1):
            fetch(userAccountNumber,userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,userBal,id)
        else:
            fail("userNotFound",id)
        
def fetch(userAccountNumber,userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,userBal,id):
    clearScreen()
    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()


    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
    container.place(x=((Width*15)//100),y=((Height*10)//100))

    text= ctk.CTkLabel(container,text="Fetch account information",font=("default",30,"bold"),text_color="black")
    text.place(x=((Width*20)//100),y=((Height*5)//100))

    userDetailContainer= ctk.CTkFrame(container, fg_color="#E3E3E3", height=400, width=500)
    userDetailContainer.place(x=((Width*30)//100),y=((Height*12)//100))


    userAccountNumberBox= ctk.CTkEntry(container, placeholder_text="Account number", fg_color="#E3E3E3", height=40, width=200, placeholder_text_color="black",text_color="black")
    userAccountNumberBox.place(x=((Width*5)//100),y=((Height*15)//100))
    userAccountNumberBox.delete(0, ctk.END)
    userAccountNumberBox.insert(0, userAccountNumber)

    
    userNameText= ctk.CTkLabel(userDetailContainer, text="Name: "+userFName+" "+userLName, font=("default",20), text_color="black")
    userNameText.place(x=((Width*3)//100),y=((Height*5)//100))

    userDOBText= ctk.CTkLabel(userDetailContainer, text="Date Of Birth: "+userDOB, font=("default",20), text_color="black")
    userDOBText.place(x=((Width*3)//100),y=((Height*10)//100))

    userPanText= ctk.CTkLabel(userDetailContainer, text="Pan number: "+userPan, font=("default",20), text_color="black")
    userPanText.place(x=((Width*3)//100),y=((Height*15)//100))

    useraadhaarText= ctk.CTkLabel(userDetailContainer, text="Aadhaar number: "+userAadhaar, font=("default",20), text_color="black")
    useraadhaarText.place(x=((Width*3)//100),y=((Height*20)//100))

    userPhoneText= ctk.CTkLabel(userDetailContainer, text="Mobile number: "+userPhone, font=("default",20), text_color="black")
    userPhoneText.place(x=((Width*3)//100),y=((Height*25)//100))

    userGenderText= ctk.CTkLabel(userDetailContainer, text="Gender: "+userGender, font=("default",20), text_color="black")
    userGenderText.place(x=((Width*3)//100),y=((Height*30)//100))

    userAddressText= ctk.CTkLabel(userDetailContainer, text="Address: "+userAddress, font=("default",20), text_color="black")
    userAddressText.place(x=((Width*3)//100),y=((Height*35)//100))

    userBalText= ctk.CTkLabel(userDetailContainer, text="Balance: "+userBal, font=("default",20), text_color="black")
    userBalText.place(x=((Width*3)//100),y=((Height*40)//100))

    
    checkBtn= ctk.CTkButton(container, text="CHECK", font=("default",20,"bold"), height=40, width=150, command=lambda: fetch(userAccountNumberBox.get(),id), state=ctk.DISABLED)
    checkBtn.place(x=((Width*7)//100),y=((Height*30)//100))

    okBtn= ctk.CTkButton(container,text="OKAY",font=("default",20,"bold"), text_color="white",fg_color="#5D3FD3", hover_color="green", height=40, width=140, command= lambda: dashboard(id))
    okBtn.place(x=(Width*7)//100, y=(Height*40)//100)

def fetchDetail(id):
    clearScreen()

    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
    container.place(x=((Width*15)//100),y=((Height*10)//100))

    text= ctk.CTkLabel(container,text="Fetch account information",font=("default",30,"bold"),text_color="black")
    text.place(x=((Width*20)//100),y=((Height*5)//100))

    userDetailContainer= ctk.CTkFrame(container, fg_color="#E3E3E3", height=400, width=500)
    userDetailContainer.place(x=((Width*30)//100),y=((Height*12)//100))

    dataLabel= ctk.CTkLabel(userDetailContainer, text="NO DATA", font=("default",30,"bold"), text_color="#969696")
    dataLabel.place(x=((Width*15)//100),y=((Height*10)//100))

    userAccountNumber= ctk.CTkEntry(container, placeholder_text="Account number", fg_color="#E3E3E3", height=40, width=200, placeholder_text_color="black",text_color="black")
    userAccountNumber.place(x=((Width*5)//100),y=((Height*15)//100))

    checkBtn= ctk.CTkButton(container, text="CHECK", font=("default",20,"bold"), height=40, width=150, command=lambda: detailFetcher(userAccountNumber.get(),id))
    checkBtn.place(x=((Width*7)//100),y=((Height*30)//100))

    okBtn= ctk.CTkButton(container,text="BACK",font=("default",20,"bold"), text_color="white",fg_color=None, height=40, width=140, command= lambda: dashboard(id))
    okBtn.place(x=(Width*7)//100, y=(Height*40)//100)

def delAcc(accountNumber,id):
    filepath = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(filepath, "data", "database", "accounts.csv")
    
    if os.path.exists(file_path):
        with open(file_path, "r", newline='') as account_file:
            reader = csv.reader(account_file)
            rows = list(reader)

        updated_records = [row for row in rows if row[0] != accountNumber]

        with open(file_path, "w", newline='') as account_file:
            writer = csv.writer(account_file)
            writer.writerows(updated_records)

        print("User removed successfully!")
        success("accountDeleted", id)
    else:
        print("File not found or accounts.csv does not exist.")
        fail("emptyDatabase", id)
    
def readyForDelete(accountNumber,userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,userBal,id):
    clearScreen()
    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
    container.place(x=((Width*15)//100),y=((Height*10)//100))

    text= ctk.CTkLabel(container,text="Fetch account information",font=("default",30,"bold"),text_color="black")
    text.place(x=((Width*20)//100),y=((Height*5)//100))

    userDetailContainer= ctk.CTkFrame(container, fg_color="#E3E3E3", height=400, width=500)
    userDetailContainer.place(x=((Width*30)//100),y=((Height*12)//100))


    userAccountNumberBox= ctk.CTkEntry(container, placeholder_text="Account number", fg_color="#E3E3E3", height=40, width=200, placeholder_text_color="black",text_color="black")
    userAccountNumberBox.place(x=((Width*5)//100),y=((Height*15)//100))
    userAccountNumberBox.delete(0, ctk.END)
    userAccountNumberBox.insert(0, accountNumber)

    
    userNameText= ctk.CTkLabel(userDetailContainer, text="Name: "+userFName+" "+userLName, font=("default",20), text_color="black")
    userNameText.place(x=((Width*3)//100),y=((Height*5)//100))

    userDOBText= ctk.CTkLabel(userDetailContainer, text="Date Of Birth: "+userDOB, font=("default",20), text_color="black")
    userDOBText.place(x=((Width*3)//100),y=((Height*10)//100))

    userPanText= ctk.CTkLabel(userDetailContainer, text="Pan number: "+userPan, font=("default",20), text_color="black")
    userPanText.place(x=((Width*3)//100),y=((Height*15)//100))

    useraadhaarText= ctk.CTkLabel(userDetailContainer, text="Aadhaar number: "+userAadhaar, font=("default",20), text_color="black")
    useraadhaarText.place(x=((Width*3)//100),y=((Height*20)//100))

    userPhoneText= ctk.CTkLabel(userDetailContainer, text="Mobile number: "+userPhone, font=("default",20), text_color="black")
    userPhoneText.place(x=((Width*3)//100),y=((Height*25)//100))

    userGenderText= ctk.CTkLabel(userDetailContainer, text="Gender: "+userGender, font=("default",20), text_color="black")
    userGenderText.place(x=((Width*3)//100),y=((Height*30)//100))

    userAddressText= ctk.CTkLabel(userDetailContainer, text="Address: "+userAddress, font=("default",20), text_color="black")
    userAddressText.place(x=((Width*3)//100),y=((Height*35)//100))

    userBalText= ctk.CTkLabel(userDetailContainer, text="Balance: "+userBal, font=("default",20), text_color="black")
    userBalText.place(x=((Width*3)//100),y=((Height*40)//100))

    
    checkBtn= ctk.CTkButton(container, text="CHECK", font=("default",20,"bold"), height=40, width=150, command=lambda: fetch(userAccountNumberBox.get(),id), state=ctk.DISABLED)
    checkBtn.place(x=((Width*7)//100),y=((Height*30)//100))

    okBtn= ctk.CTkButton(container,text="DELETE",font=("default",20,"bold"), text_color="white",fg_color="#5D3FD3", hover_color="green", height=40, width=140,command= lambda: delAcc(accountNumber,id))
    okBtn.place(x=(Width*7)//100, y=(Height*40)//100)

def checkAccountForDeletion(accountNumber,id):
    filepath= os.path.dirname(os.path.abspath(__file__))
    file_exists= os.path.exists(filepath+"\\data\\database\\accounts.csv")

    if(file_exists):
        with open(filepath+"\\data\\database\\accounts.csv","r",newline='') as accountFile:
            reader= csv.reader(accountFile)
            found=0
            for row in reader:
                if(accountNumber==row[0]):
                    found=1
                    userFName= row[1]
                    userLName= row[2]
                    userDOB= row[3]
                    userPan= row[4]
                    userAadhaar= row[5]
                    userPhone= row[6]
                    userGender= row[7]
                    userAddress= row[8]
                    userBal= row[9]
                    readyForDelete(accountNumber,userFName,userLName,userDOB,userPan,userAadhaar,userPhone,userGender,userAddress,userBal,id)
            
        if(found==0):
            fail("userNotFoundD",id)
    
    else:
        fail("emptyDatabase",id)

def delectAccount(id):
    clearScreen()

    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
    container.place(x=((Width*15)//100),y=((Height*10)//100))

    heading= ctk.CTkLabel(container, text="DELETE ACCOUNT", font=("default",25,"bold"),text_color="black")
    heading.place(x=((Width*5)//100),y=((Height*5)//100))

    accountNumberBox= ctk.CTkEntry(container, placeholder_text="Account number", font=("default",20),fg_color="#c5c6d0", height=40, width=200, placeholder_text_color="black", text_color="black")
    accountNumberBox.place(x=((Width*5)//100),y=((Height*20)//100))

    checkbtn= ctk.CTkButton(container, text="CHECK", height=40, width=140, fg_color="#5D3FD3",hover_color="#9400D3", font=("default",18,"bold"),command=lambda: checkAccountForDeletion(accountNumberBox.get(),id))
    checkbtn.place(x=((Width*8)//100),y=((Height*30)//100))

def new_account(id):
    clearScreen()

    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
    container.place(x=((Width*15)//100),y=((Height*10)//100))

    imgContainer= ctk.CTkFrame(container, fg_color="grey", height=200, width=200)
    imgContainer.place(x=(Width*5)//100, y=(Height*5)//100)

    imgUploadBtn= ctk.CTkButton(container, text="UPLOAD IMAGE", fg_color="orange", text_color="white", height=40, width=160, font=("default",18,"bold"))
    imgUploadBtn.place(x=(Width*7)//100, y=(Height*36)//100) 

    userFName= ctk.CTkEntry(container, placeholder_text="First Name", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userFName.place(x=(Width*25)//100, y=(Height*10)//100)
    

    userLName= ctk.CTkEntry(container, placeholder_text="Last Name", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userLName.place(x=(Width*45)//100, y=(Height*10)//100)
    

    userDOB= ctk.CTkEntry(container, placeholder_text="DOB: DD-MM-YYYY", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userDOB.place(x=(Width*25)//100, y=(Height*20)//100)
    

    userPan= ctk.CTkEntry(container, placeholder_text="PAN Card Number", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userPan.place(x=(Width*25)//100, y=(Height*30)//100)
    

    userAadhaar= ctk.CTkEntry(container, placeholder_text="Aadhaar Card Number", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userAadhaar.place(x=(Width*25)//100, y=(Height*40)//100)
    

    userPhone= ctk.CTkEntry(container, placeholder_text="Phone Number", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userPhone.place(x=(Width*45)//100, y=(Height*20)//100)
    

    userGender= ctk.CTkEntry(container, placeholder_text="Gender: M / F / other", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userGender.place(x=(Width*45)//100, y=(Height*30)//100)
    

    userAddress= ctk.CTkEntry(container, placeholder_text="Residental Address", font=("default",18), fg_color="#D1D1D1", height=40, width=200,text_color="black",placeholder_text_color="black", border_color=None, border_width=None)
    userAddress.place(x=(Width*45)//100, y=(Height*40)//100)


    submitBtn= ctk.CTkButton(container,text="SUBMIT",fg_color="green", text_color="white", height=40, width=160, font=("default",18,"bold"), hover_color="lime",command=lambda: checkDetails(userFName.get(),userLName.get(), userDOB.get(),userPan.get(),userAadhaar.get(),userPhone.get(),userGender.get(),userAddress.get(),id))
    submitBtn.place(x=(Width*35)//100, y=(Height*50)//100)

def seeVault(id):
    clearScreen()

    Width= app.winfo_screenwidth()
    Height= app.winfo_screenheight()

    frame= ctk.CTkFrame(app, fg_color="#5D3FD3")
    frame.pack(expand=True, fill="both")

    container= ctk.CTkFrame(frame, fg_color="white", height=(Height*70)//100, width=(Width*70)//100)
    container.place(x=((Width*15)//100),y=((Height*10)//100))

    filepath= os.path.dirname(os.path.abspath(__file__))
    file_exists= os.path.exists(filepath+"\\data\\database\\bankVault.csv")

    if(file_exists):
        with open(filepath+"\\data\\database\\bankVault.csv","r",newline='') as accountFile:
            reader= csv.reader(accountFile)
            for row in reader:
                vaultMoney= row[0]
                break
    

    textVault= ctk.CTkLabel(container, text="BANK VAULT", text_color="black", font=("default",30,"bold"))
    textVault.place(x=((Width*30)//100),y=((Height*5)//100))

    textVault2=ctk.CTkLabel(container, text="VALUE: ",text_color="black", font=("default",30,"bold"))
    textVault2.place(x=((Width*5)//100),y=((Height*25)//100))

    textVault3=ctk.CTkLabel(container, text=vaultMoney,text_color="#5D3FD3", font=("default",30,"bold"))
    textVault3.place(x=((Width*15)//100),y=((Height*25)//100))

    goBack= ctk.CTkButton(container, text="BACK", height=40, width=140, fg_color="#5D3FD3", hover_color="purple",text_color="white", font=("default",18,"bold"), command= lambda: dashboard(id))
    goBack.place(x=((Width*10)//100),y=((Height*38)//100))

    prevTransaction= ctk.CTkLabel(container, text="LAST 5 TRANSACTION HISTORY", text_color="black", font=("default",18,"bold"))
    prevTransaction.place(x=(Width*37)//100,y=((Height*16)//100))

    transactionFrame= ctk.CTkFrame(container, height=((Height*42)//100), width=(Width*38)//100, border_color="black", border_width=2, fg_color="white")
    transactionFrame.place(x=(Width*30)//100,y=((Height*20)//100))


    allTransaction=[]
    allTransactionID=[]
    allAccountId=[]

    filepath= os.path.dirname(os.path.abspath(__file__))
    file_exists= os.path.exists(filepath+"\\data\\database\\transactionRecorder.csv")

    if(file_exists):
        with open(filepath+"\\data\\database\\transactionRecorder.csv","r",newline='') as recordFile:
            reader= csv.reader(recordFile)
            for row in reader:
                allAccountId.append(float(row[0]))
                allTransaction.append(float(row[1]))
                allTransactionID.append(float(row[2]))
    
                
    
    else:
        fail("emptyDatabase",id)

    
    lastFive= []
    lastFiveAcc=[]
    lastFiveID=[]

    try:
        for i in range(len(lastFive)-1, len(lastFive)-6,-1):
            lastFive.append(allTransaction[i])
            lastFiveAcc.append(allAccountId[i])
            lastFiveID.append(allTransactionID[i])
    
    
        
    
        print("last 5 amount: ",lastFive)
        print("last 5 account",lastFiveAcc)
        print("last 5 transid",lastFiveID)

        TID_transaction1= str(lastFiveID[0]).replace('.0','')
        TID_transaction1= TID_transaction1.replace(TID_transaction1[5:],'XXXXX')
        amountOfTransaction1= str(lastFive[0])
        accountOfTranstion1= str(lastFiveAcc[0]).replace('.0','')
        accountOfTranstion1= accountOfTranstion1.replace(accountOfTranstion1[5:],'XXXXX')


        TID_transaction2= str(lastFiveID[1]).replace('.0','')
        TID_transaction2= TID_transaction2.replace(TID_transaction2[5:],'XXXXX')
        amountOfTransaction2= str(lastFive[1])
        accountOfTranstion2= str(lastFiveAcc[1]).replace('.0','')
        accountOfTranstion2= accountOfTranstion2.replace(accountOfTranstion2[5:],'XXXXX')


        TID_transaction3= str(lastFiveID[2]).replace('.0','')
        TID_transaction3= TID_transaction3.replace(TID_transaction3[5:],'XXXXX')
        amountOfTransaction3= str(lastFive[2])
        accountOfTranstion3= str(lastFiveAcc[2]).replace('.0','')
        accountOfTranstion3= accountOfTranstion3.replace(accountOfTranstion3[5:],'XXXXX')


        TID_transaction4= str(lastFiveID[3]).replace('.0','')
        TID_transaction4= TID_transaction4.replace(TID_transaction4[5:],'XXXXX')
        amountOfTransaction4= str(lastFive[3])
        accountOfTranstion4= str(lastFiveAcc[3]).replace('.0','')
        accountOfTranstion4= accountOfTranstion4.replace(accountOfTranstion4[5:],'XXXXX')

        TID_transaction5= str(lastFiveID[4]).replace('.0','')
        TID_transaction5= TID_transaction5.replace(TID_transaction5[5:],'XXXXX')
        amountOfTransaction5= str(lastFive[4])
        accountOfTranstion5= str(lastFiveAcc[4]).replace('.0','')
        accountOfTranstion5= accountOfTranstion5.replace(accountOfTranstion5[5:],'XXXXX')




        t1Label= ctk.CTkLabel(transactionFrame, text="1. "+TID_transaction1+"     "+amountOfTransaction1+"     "+accountOfTranstion1, font=("default",18), text_color="black")
        t1Label.place(x=(Width*3)//100,y=((Height*3)//100))

        t2Label= ctk.CTkLabel(transactionFrame, text="2. "+TID_transaction2+"     "+amountOfTransaction2+"     "+accountOfTranstion2, font=("default",18), text_color="black")
        t2Label.place(x=(Width*3)//100,y=((Height*10)//100))

        t3Label= ctk.CTkLabel(transactionFrame, text="3. "+TID_transaction3+"     "+amountOfTransaction3+"     "+accountOfTranstion3, font=("default",18), text_color="black")
        t3Label.place(x=(Width*3)//100,y=((Height*17)//100))

        t4Label= ctk.CTkLabel(transactionFrame, text="4. "+TID_transaction4+"     "+amountOfTransaction4+"     "+accountOfTranstion4, font=("default",18), text_color="black")
        t4Label.place(x=(Width*3)//100,y=((Height*24)//100))

        t5Label= ctk.CTkLabel(transactionFrame, text="5. "+TID_transaction5+"     "+amountOfTransaction5+"     "+accountOfTranstion5, font=("default",18), text_color="black")
        t5Label.place(x=(Width*3)//100,y=((Height*31)//100))
    
    except NameError:
        t1Label= ctk.CTkLabel(transactionFrame, text="MIN 5 TRANSACTION REQUIRED", font=("default",20,"bold"), text_color="red")
        t1Label.place(x=(Width*8)//100,y=((Height*10)//100))
        print("Transaction is lesser than five")

def dashboard(id):
    clearScreen()

    mainContainer= ctk.CTkFrame(master=app, fg_color="#5D3FD3")
    mainContainer.pack(expand=True, fill="both")

    Height= app.winfo_screenheight()
    Width= app.winfo_screenwidth()

    displayContainer= ctk.CTkFrame(master=mainContainer, fg_color="white", height=Height, width=Width)
    displayContainer.place(x=((windowWidth*34)//100),y=0)

    imgContainerFrame= ctk.CTkFrame(master= mainContainer, height=150, width=170, border_width=4, border_color='white')
    imgContainerFrame.place(x=(Width*6)//100,y=(Height*5)//100)

    adminInfoContainer= ctk.CTkFrame(master=mainContainer, height=(Height*50)//100, width= (Width*23)//100, fg_color="#5D3FD3")
    adminInfoContainer.place(x=(Width*1.2)//100,y=(Height*30)//100)

    currentPath= os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))



    with open(currentPath+'\\data\\database\\admin.csv',"r",newline='') as accountFile:
        reader= csv.reader(accountFile)
        found=0

        for row in reader:
            if(id in row[0]):
                found=1
                userID=row[0]
                userName= row[2]
                userEmail= row[3]
                userPhone= row[4]
                userPost= row[5]
                break
        
        imagePath= "data\\adminProfiles\\"+userID+".png"
        image = Image.open(imagePath)
        photo = ImageTk.PhotoImage(image)
        label= ctk.CTkLabel(imgContainerFrame, text=None, image=photo)
        label.place(x=(Width*1)//100,y=(Height*1.5)//100)

        
        UserID_label= ctk.CTkLabel(master=adminInfoContainer, text="ID: "+userID, text_color="white", font=("default",16,"bold"))
        UserID_label.place(x=(Width*1)//100,y=(Height*1)//100)
        UserID_label= ctk.CTkLabel(master=adminInfoContainer, text="Name: "+userName, text_color="white", font=("default",16,"bold"))
        UserID_label.place(x=(Width*1)//100,y=(Height*6)//100)
        UserID_label= ctk.CTkLabel(master=adminInfoContainer, text="Email: "+userEmail, text_color="white", font=("default",16,"bold"))
        UserID_label.place(x=(Width*1)//100,y=(Height*12)//100)
        UserID_label= ctk.CTkLabel(master=adminInfoContainer, text="Phone: "+userPhone, text_color="white", font=("default",16,"bold"))
        UserID_label.place(x=(Width*1)//100,y=(Height*18)//100)
        UserID_label= ctk.CTkLabel(master=adminInfoContainer, text="Post: "+userPost, text_color="white", font=("default",16,"bold"))
        UserID_label.place(x=(Width*1)//100,y=(Height*24)//100)
        signOutButton= ctk.CTkButton(adminInfoContainer,text="SIGN OUT", height=40, width=140, text_color="white", fg_color="#FFAC1C", font=("default",18,"bold"),command=login)
        signOutButton.place(x=(Width*5)//100,y=(Height*40)//100)

        
        image = Image.open("data\\images\\newuser.jpg")
        photo = ImageTk.PhotoImage(image)
        openAccountBtn= ctk.CTkButton(master=displayContainer, image=photo, text=None, fg_color="white", border_color="#C0C0C0",hover_color="white",border_width=2,command= lambda: new_account(id))
        openAccountBtn.place(x=(Width*5)//100, y=(Height*5)//100)
        

        image = Image.open("data\\images\\withdraw.png")
        photo = ImageTk.PhotoImage(image)
        depositeBtn= ctk.CTkButton(master=displayContainer,image=photo, text=None, fg_color="white", border_color="#C0C0C0",hover_color="white",border_width=2,command= lambda: withdraw(id))
        depositeBtn.place(x=(Width*25)//100, y=(Height*5)//100)
        
        image = Image.open("data\\images\\deposite.png")
        photo = ImageTk.PhotoImage(image)
        withdrawBtn= ctk.CTkButton(master=displayContainer,image=photo, text=None, fg_color="white", border_color="#C0C0C0",hover_color="white",border_width=2,command= lambda: deposit(id))
        withdrawBtn.place(x=(Width*45)//100, y=(Height*5)//100)

        image = Image.open("data\\images\\fetch.png")
        photo = ImageTk.PhotoImage(image)
        infoBtn= ctk.CTkButton(master=displayContainer,image=photo, text=None, fg_color="white", border_color="#C0C0C0",hover_color="white",border_width=2, command= lambda: fetchDetail(id))
        infoBtn.place(x=(Width*5)//100, y=(Height*40)//100)


        image = Image.open("data\\images\\delete.png")
        photo = ImageTk.PhotoImage(image)
        deleteBtn= ctk.CTkButton(master=displayContainer,image=photo, text=None, fg_color="white", border_color="#C0C0C0",hover_color="white",border_width=2,command=lambda: delectAccount(id))
        deleteBtn.place(x=(Width*25)//100, y=(Height*40)//100)

        
        image = Image.open("data\\images\\vault.jpg")
        photo = ImageTk.PhotoImage(image)
        bankTotalBtn= ctk.CTkButton(master=displayContainer, image=photo, text=None, fg_color="white", border_color="#C0C0C0",hover_color="white",border_width=2, command=lambda: seeVault(id))
        bankTotalBtn.place(x=(Width*45)//100, y=(Height*40)//100)

        textAK= ctk.CTkLabel(displayContainer, text="CREATE BY AYUSH KOTHARI",font=("default",20,"bold"), text_color="grey")
        textAK.place(x=(Width*25)//100, y=(Height*75)//100)

        contactBtn= ctk.CTkButton(displayContainer, text="CONTACT", height=40, width=140, fg_color="orange", text_color="white",font=("default",18,"bold"),command= lambda: webbrowser.open(url))
        contactBtn.place(x=(Width*30)//100, y=(Height*80)//100)

def checkLogin(id,pswd):
    currentPath= os.path.dirname(os.path.abspath(__file__))
    with open(currentPath+'\\data\\database\\admin.csv',"r",newline='') as accountFile:
        reader= csv.reader(accountFile)
        found=0

        #Matching the id wiht row[0] and password with row[1]...
        for row in reader:
            if(id in row[0] and pswd in row[1]):
                found=1
                break
        
        if found:
            #Successfully login...
            dashboard(id)
        else:
            #Failed to login...
            login()
                
def clearScreen():
    for widget in app.winfo_children():
        widget.destroy()

def login():
    clearScreen()
    mainContainer= ctk.CTkFrame(master=app, fg_color="#262626", border_color="white", border_width=2, width=((windowWidth)*95)//100, height=((windowHeight)*95)//100)
    mainContainer.pack(pady=(50,0))

    ImageContainer= ctk.CTkFrame(master=mainContainer, width=((windowWidth)*40)//100, height=((windowHeight)*95)//100)
    ImageContainer.place(x=0,y=0)

    
    folderPath= os.path.dirname(os.path.abspath(__file__))
    image = Image.open(folderPath+"\\data\\images\\bg2.png")
    tk_image = ImageTk.PhotoImage(image)
    imageLabel= ctk.CTkLabel(master=ImageContainer, image=tk_image, text=None)
    imageLabel.place(x=0,y=0)

    inputContainer= ctk.CTkFrame(master=mainContainer, width=((windowWidth)*60)//100, height=((windowHeight)*95)//100)
    inputContainer.place(x=(((windowWidth)*40)//100)-10,y=0)

    textLabel= ctk.CTkLabel(master= inputContainer, text="LOGIN", font=("default",30,"bold"), text_color="white")
    textLabel.place(x=((((windowWidth*60)//100)//2.5)),y=10)


    nameBox= ctk.CTkEntry(master=inputContainer, placeholder_text="Admin ID", height=40, width=300, font=('default',18,"bold"))
    nameBox.place(x=((((windowWidth*60)//100)//4)),y=100)

    passBox= ctk.CTkEntry(master=inputContainer, placeholder_text="Password", height=40, width=300,font=('default',18,"bold"), show='*')
    passBox.place(x=((((windowWidth*60)//100)//4)),y=180)

    subButton= ctk.CTkButton(master=inputContainer, text="SUBMIT", font=("default",20,"bold"), height=40, width=150, text_color="white", fg_color="#339900", hover_color="#33CC00",  command=lambda:checkLogin(nameBox.get(),passBox.get()))
    subButton.place(x=((((windowWidth*60)//100)//2.5)),y=(((windowHeight)*95)//100)//1.8)


app= ctk.CTk()
app.title("Bank Managenment System with GUI")

global windowHeight
global windowWidth

windowWidth,windowHeight= screenAdjuster()
print("Window Height: ",windowHeight)
print("Window Width: ",windowWidth)
app.geometry(f'{windowWidth}x{windowHeight}')

screenAdjuster()

login()

app.mainloop()