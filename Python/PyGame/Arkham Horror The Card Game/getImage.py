import os

def changeName():
    s = input('Input:')
    s = s.replace('.', '')
    s = s.replace('/', '')
    s = s.replace(':', '')
    s = s.replace('-', '')
    print(s)

def main():
    while True:
        changeName()

if __name__ == "__main__":
    main()
