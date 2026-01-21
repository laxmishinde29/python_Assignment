def ChkVowles(ch):
    if ch in ('a','e','i','o','u'):
        print("Vowel")
    else:
        print("Not Vowel")

def main():
    ch = input("Enter character:")

    ChkVowles(ch)

if __name__ == "__main__":
    main()