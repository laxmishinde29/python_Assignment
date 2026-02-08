import hashlib                  #os dependent module
import os
import sys
import time

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

def DeleteDuplicate(DirectoryName):    
    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("It is no such a directory")
        return

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is no such a directory")
        return

    log = open("Log.txt","w")
    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateChecksum(fname)

            if CheckSum in Duplicate:
                os.remove(fname)
                log.write(fname + "\n")
            else:
                Duplicate[CheckSum] = fname

    log.close()
    print("Duplicate file deleted and logged")


def main():
    if(len(sys.argv) != 2):
        print("Invalid arguments")
        return
    start = time.time()
    DeleteDuplicate(sys.argv[1])
    end = time.time()

    print("Execution time is :", end - start, "seconds")

if __name__ == "__main__":
    main()