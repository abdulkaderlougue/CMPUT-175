import sys
file = open('accounts.txt','r')
accounts = {}
for line in file:
    el = line.split(':')
    accounts[el[0]] = el[1]        


while True:
    userName = input('Enter account name, or "Stop" to exit:')
    if userName =='Stop':
        sys.exit()
    else:
        balance = accounts[str(userName)]
    if str(balance) != 'Not_A_Float!\n':
        cb = input('Enter transaction amount:')    
        try:
            nBalance = float(balance) + float(cb)
            accounts[str(userName)] = nBalance
            print(nBalance)
        except ValueError:
            print('Illegal value for transaction, transaction canceled')
            cb = input('Enter transaction amount:')
            
    else:
        print('Account does not exist, transaction canceled')
        break
  