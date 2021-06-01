try:
    file=open('eee','r+')
except Exception as e:
    print('There is no file named as eee')
    response = input('do you want to create a new file')
    if response =='y':
        file = open('eee','w')
    else:
        pass
else:
    file.write('sss')
file.close()