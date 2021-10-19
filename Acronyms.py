a=input('Enter a phrase: ').split(' ')
acr=''
for i in a:
    acr+=str(i[0]).upper()
print(acr)