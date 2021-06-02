from itertools import permutations, product
#from itertools import product
#for i in permutations('ABCD'):
   #print(i)
#for s in product('+-*/', '+-*/', '+-*/'):
   #print(s)

def game24(n1,n2,n3,n4):
		for a,b,c,d in permutations((n1,n2,n3,n4),4):
			for o1,o2,o3 in product(['+','-','*','/'], repeat=3): 
				cases = list()
				cases.append('%d%s%d%s%d%s%d'%(a,o1,b,o2,c,o3,d))
				cases.append('(%d%s%d)%s%d%s%d'%(a,o1,b,o2,c,o3,d))
				cases.append('%d%s%d%s(%d%s%d)'%(a,o1,b,o2,c,o3,d))
				cases.append('%d%s(%d%s%d)%s%d'%(a,o1,b,o2,c,o3,d))
				cases.append('(%d%s%d)%s(%d%s%d)'%(a,o1,b,o2,c,o3,d))
				cases.append('(%d%s%d%s%d)%s%d'%(a,o1,b,o2,c,o3,d))
				cases.append('((%d%s%d)%s%d)%s%d'%(a,o1,b,o2,c,o3,d))
				cases.append('(%d%s(%d%s%d))%s%d'%(a,o1,b,o2,c,o3,d))
				cases.append('%d%s(%d%s%d%s%d)'%(a,o1,b,o2,c,o3,d))
				cases.append('%d%s((%d%s%d)%s%d)'%(a,o1,b,o2,c,o3,d))
				cases.append('%d%s(%d%s(%d%s%d))'%(a,o1,b,o2,c,o3,d))
				for answer in cases:
					try: 
						if eval(answer) == 24:
							print('Result：%s = 24'%answer)
							return
					except:
						pass
		print('No Result')
game24(7,9,8,10)	                
                
