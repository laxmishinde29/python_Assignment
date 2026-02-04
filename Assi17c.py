def main():
    WordsCount = 0
    fname = input("Enter a file name:")

    fobj = open(fname,"r")

    for line in fobj:             
        words = line.split()
        WordsCount = WordsCount+len(words)

    fobj.close()

    print(f"Numbers of words in {fname} are:",WordsCount)

    
if __name__ == "__main__":
    main()