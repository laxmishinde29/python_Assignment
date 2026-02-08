import hashlib                  #os dependent module
import os

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()
    
def DirectoryWatcher(DirectoryName = "rutu"):
    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("There is no such directory")
        
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateChecksum(fname)

            print(f"File name: {fname} CheckSum : {CheckSum}")

def main():
    DirectoryWatcher()

if __name__ == "__main__":
    main()