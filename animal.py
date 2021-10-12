import sys
def dog():
    print("Wang")
def default():
    print("Hello")
def main():
    if sys.argv[1]=='dog':
        dog()
    else:
        default()

if __name__=='__main__':
    main()
 