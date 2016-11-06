import math
def isprime(startnumber):
    startnumber2=1.0 * startnumber
    prime = True
    for divisor in range(2, startnumber):
        if startnumber2/divisor==int(startnumber2/divisor):
            prime=False
    return prime
if __name__ == "__main__":
	pstr = input("p:")
	qstr = input("q:")
	dstr = input("d:")
	p = int(pstr)
	q = int(qstr)
	d = int(dstr)
	n = p * q
	z = (p-1) * (q-1)
	e = 1
	for i in range(2, 1000):
		if isprime(i):
			if ((d * i) % z) == 1:
				e = i
				break
	print(e)
	#print((d*e) % z)



