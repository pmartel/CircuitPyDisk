import time

def fact(n):
    prod = 1
    for i in range(1, n+1) :
        prod *= i
        #print(prod)
    return prod

while True :
	s = input('enter a number ')
	n = int(s)
	t0 = time.monotonic()
	f = fact(n)
	t1 = time.monotonic()
	print(f)
	t2 = time.monotonic()
	print('Calculating {0} factorial took {1} seconds'.format( n, t1 - t0) )
	print('Printing {0} factorial took {1} seconds'.format( n, t2 - t1) )
        print('test')

