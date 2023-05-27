def fib_num(n): 
 	 a, b = 0, 1 
 	 counter = 0 
 	 while counter < n: 
 	 	 print(a) 
 	 	 a, b = b, a+b 
 	 	 counter += 1
 
def fib_list(n): 
 	 series = [] 
 	 a, b = 0, 1 
 	 counter = 0 
 	 while counter < n: 
 	 	 series.append(a) 
 	 	 a, b = b, a+b 
 	 	 counter += 1 
 	 return series