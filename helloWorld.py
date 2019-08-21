import sys
import re


#function to read a file go over it 
def Cat(fn):
    f = open(fn, 'rU')

    for line in f:
        print(line,)
    f.close 

def Cat2(fn):
        f1 = open(fn, 'rU')
        lines = f1.readlines()
        print(lines)
#reading whole file into a string
def cat3(fn):
        f2 = open(fn, 'rU')
        text = f2.read()
        print(text)
        f2.close
def searchText(fn):
        f3 = open(fn, 'rU')
        text = f3.read()
        res= re.search('Apache', text)
        print(res)
def main():
#     Cat(sys.argv[1])
#       Cat2(sys.argv[1])
        # cat3(sys.argv[1])
        # Cat(sys.argv[1])
        searchText(sys.argv[1])
if __name__ == "__main__":
    main()
