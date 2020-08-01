def filename():
        ch = 'y'
        while ch == 'y' or ch == 'Y':
                filename=input('Enter a filename: ')
                index=0
                for i in range(len(filename)):
                        if filename[i]=='.':
                                index=i
                print("Extention of file",filename,"is",filename[index+1: ])
                ch = input("Do you wish to continue??(y/n):")
filename()
