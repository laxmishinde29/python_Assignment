import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

log_file_path = None
last_zip_file = None


# ---------------- CREATE LOG ----------------

def CreateLog(Source):

    global log_file_path
    Border = "-"*50

    if not os.path.exists("Logs"):
        os.mkdir("Logs")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join("Logs","DataShield_%s.log" % timestamp)

    log_file_path = FileName

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("------ Marvellous Data Shield System ------\n")
    fobj.write("Backup Started at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    fobj.close()

    DataShieldStart(Source)



# ---------------- HASH FUNCTION ----------------

def CalculateHash(path):

    hobj = hashlib.md5()

    try:
        fobj = open(path,"rb")
        while True:
            data = fobj.read(1024)
            if not data:
                break
            hobj.update(data)
        fobj.close()
    except:
        return None

    return hobj.hexdigest()



# ---------------- BACKUP FUNCTION ----------------

def BackupFiles(Source, Destination):

    copied_files = []

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):

        for file in files:

            # ---- EXCLUDE FILES ----
            if file.endswith((".tmp",".log",".exe")):
                continue

            src_path = os.path.join(root,file)
            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            if (not os.path.exists(dest_path)) or \
               (CalculateHash(src_path) != CalculateHash(dest_path)):

                shutil.copy2(src_path,dest_path)
                copied_files.append(relative)

    return copied_files



# ---------------- ZIP CREATION ----------------

def MakeZip(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    zobj = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)
            zobj.write(full_path,relative)

    zobj.close()

    return zip_name



# ---------------- MAIN BACKUP PROCESS ----------------

def DataShieldStart(Source):

    global log_file_path
    global last_zip_file

    Border = "-"*50
    BackupFolder = "BackupFiles"

    try:
        if not os.path.exists(Source):
            return

        files = BackupFiles(Source, BackupFolder)
        zip_file = MakeZip(BackupFolder)
        last_zip_file = zip_file

        fobj = open(log_file_path,"a")

        fobj.write("Files Copied : %d\n" % len(files))
        fobj.write("Zip File Created : %s\n" % zip_file)

        # Backup history
        history = open("BackupHistory.txt","a")
        history.write("Date : %s | Files : %d | Zip : %s\n" %
                      (time.ctime(), len(files), zip_file))
        history.close()

        fobj.write(Border+"\n")
        fobj.write("Backup Completed Successfully\n")
        fobj.write(Border+"\n")

        fobj.close()

    except Exception as e:

        fobj = open(log_file_path,"a")
        fobj.write("Error Occurred : %s\n" % str(e))
        fobj.write(Border+"\n")
        fobj.close()



# ---------------- RESTORE FEATURE ----------------

def RestoreBackup(zipname, destination):

    if not os.path.exists(destination):
        os.makedirs(destination)

    zobj = zipfile.ZipFile(zipname,'r')
    zobj.extractall(destination)
    zobj.close()

    print("Backup Restored Successfully")



# ---------------- EMAIL FUNCTION ----------------

def SendMail(sender, app_password,receiver):

    global log_file_path
    global last_zip_file

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Backup Completed Successfully"

    msg.set_content("Backup completed. Log and Zip attached.")

    # Attach log
    with open(log_file_path,"rb") as f:
        msg.add_attachment(f.read(),
                           maintype="application",
                           subtype="octet-stream",
                           filename=os.path.basename(log_file_path))

    # Attach zip
    with open(last_zip_file,"rb") as f:
        msg.add_attachment(f.read(),
                           maintype="application",
                           subtype="octet-stream",
                           filename=os.path.basename(last_zip_file))

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    smtp.login(sender,app_password)
    smtp.send_message(msg)
    smtp.quit()



# ---------------- MAIN FUNCTION ----------------

def main():

    Border = "-"*50

    print(Border)
    print("------ Marvellous Data Shield System ------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scipt is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        sender_email = "rutus1329@gmail.com"

        app_password = "qhsz oebk lcfc tpgc"

        receiver_email = "nirajnale333@gmail.com"

        schedule.every(int(sys.argv[1])).minutes.do(SendMail,sender_email, app_password,receiver_email)

        print(Border)
        print("Data Sheild System started succesfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv) == 4 and sys.argv[1] == "--restore"):

        RestoreBackup(sys.argv[2],sys.argv[3])

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank You ---------")
    print(Border)



if __name__ == "__main__":
    main()
