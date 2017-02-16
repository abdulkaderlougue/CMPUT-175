import sys
import os

dic={}
file_name='accounts.txt'
if os.path.exists(file_name):
    accounts_file=open('accounts.txt','r')
else:
    print('Input file not found, program will exit')
    sys.exit()
    
for aline in accounts_file.readlines():
    values=aline.split(':')
    try:
        balance=float(values[1])
        dic[values[0]]=balance
    except ValueError:
        pass
    
#print(dic)

while True:
    account=input("Enter account name, or 'Stop' to exit: ")
    if account in dic.keys():
        try:
            dic[account]+=float(input('Enter transaction amount: '))
            print('New balance for account '+ str(account)+':'+str(dic[account]))
        except ValueError:
            print('Illegal value for transaction, transaction canceled')
    elif account=='Stop':
        sys.exit()
    else:
        print('Account does not exist, transaction canceled')
        