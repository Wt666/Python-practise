from typing import ContextManager


file = open('my file.txt','r')
Content=file.readlines()



print(Content)