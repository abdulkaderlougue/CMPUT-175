def open_safe(fileName):
    try:
        file = open(fileName, 'r')
    except Exception:
        print("f = safe_open('" + str(fileName) +"','r')")
        print('I/O error: No such file or dirctory\nf == None: True\n')
        
    else:
        print("f = safe_open('" + str(fileName) +"','r')")
        print('f==None:False')
        return file
def main():
    fileName = input('input the name of file you want to open: ')
    f = open_safe(fileName)

main()