import time
from decrypt import decrypt
from encrypt import encrypt
from CRT import CRT

def main():
    with open('testcase.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if(lines[i] == '-e\n'):
                print("\n\t\t\t\t\t\tENTERING ENCRYPT PART")
                while lines[i]!='\n':
                    #print(lines[i])
                    if '-msg' in lines[i]:
                        msg = lines[i].split(":")[1].replace(" ","").replace("\n","")
                        print("MSG = " , msg)
                    elif '-N' in lines[i]:
                        N = lines[i].split(":")[1].replace(" ","")
                        print("N = " , N)
                    elif '-ek' in lines[i]:
                        ek = lines[i].split(":")[1].replace(" ","")
                        print("EK = " , ek)
                    i = i+1 
                if msg=='' or N == '' or ek == '':
                    print("MSG / N / EK CANNOT BE NULL, PLZ CHECK UR testcast.txt ")
                    return
                encryptResult = encrypt.main(msg,N,ek)
                print("ENCRYPTRESULT" , encryptResult)
                
            N = ''
            if(lines[i] == '-d\n'):
                print("\n\t\t\t\t\t\tENTERING DECRYPT PART")
                while lines[i]!='\n':
                    #print(lines[i])
                    if '-N' in lines[i]:
                        N = lines[i].split(":")[1].replace(" ","")
                        print("N = " , N)
                    elif '-dk' in lines[i]:
                        dk = lines[i].split(":")[1].replace(" ","")
                        print("DK = " , dk)
                    i = i+1 
                if encryptResult=='' or N == '' or dk == '':
                    print("ENCRYPTRESULT / N / DK CANNOT BE NULL, PLZ CHECK UR testcast.txt ")
                    return
                t1 = time.time()
                decryptResult = decrypt.main(encryptResult,N,dk)
                t2 = time.time()
                print("t1 " ,  t1)
                print("DECRYPTRESULT" , decryptResult)
                print("t2 " ,  t2)
                print("EXEC TIME ",t2-t1)
            dk = ''
            if(lines[i] == '-CRT\n'):
                print("\n\t\t\t\t\t\tENTERING CRT PART")
                while i<len(lines) and lines[i]!='\n':
                    #print(lines[i])
                    if '-p' in lines[i]:
                        p = lines[i].split(":")[1].replace(" ","")
                        print("P = " , p)
                    elif '-q' in lines[i]:
                        q = lines[i].split(":")[1].replace(" ","")
                        print("Q = " , q)
                    elif '-dk' in lines[i]:
                        dk = lines[i].split(":")[1].replace(" ","")
                        print("DK = " , dk)
                    i = i+1 
                if p=='' or q == '' or dk == '':
                    print("P / Q / DK CANNOT BE NULL, PLZ CHECK UR testcast.txt ")
                    return
                t1 = time.time()
                CRTResult = CRT.main(encryptResult,int(p),int(q),int(dk))
                t2 = time.time()
                print("\nt1 " ,  t1)
                print("CRTRESULT" , CRTResult)
                print("t2 " ,  t2)
                print("EXEC TIME ",t2-t1)

if __name__ == '__main__':
    main()