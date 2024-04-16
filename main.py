def main():
    with open("books/frankenstein.txt") as f:
        # here we are opening and printing to console
        file_contents = f.read()
        words = file_contents.split()
        print(words)

if __name__ == "__main__": 
    main()