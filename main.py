import time

# Check out README first as you may not understand why we are skipping over some cases and doing matrix multiplication on steroids.

n = 5 # For nxn matrix
try:
	f = open("data.txt",'x+')
except FileExistsError:
	f = open("data.txt","w")

def matmul(m1,m2):
	res = [[]]*n

	for k in range(n):
		res[k] = [False]*n
		
		# Checks if the row is empty
		if True not in m1[k]:
			continue

		# Boolean matrix multiplicaton.
		# Here, we have replaced Arithmetic operations into Logic operators
		# This gives us values in True or False which saves a lot of unnecessary calculations
		for i in range(n):
			for j in range(n):
				if m1[k][j] and m2[j][i]:
					res[k][i] = True

	return res

def calculate(s):
	for g in range(s):
		a = bin(g)[2:][::-1] # This turns a number into binary form and reverses it.
		b = a[::n+1] # This gives us a string with only diagonal values since it's reversed.
		itr = 1

		# Checks if there are multiple '1's in diagonal
		if b.count('1')>1:
			continue

		# Checks if given matrix have any empty columns
		found = False
		a = a[::-1]
		for i in range(n):
			if '1' not in a[i::n]:
				found = True
				break
		if found:
			continue

		# Converting Binary representation into a matrix
		a = a.zfill(n*n) # This adds zero at the beggining to make it n*n digit long.
		num = [c=='1' for c in a]
		base = [[]]*n
		for i in range(n):
			base[i] = num[:n]
			num = num[n:]
		mat = base.copy()

		# Checks if True values are symmetric
		for i in range(n):
			for j in range(i+1,n):
				if base[i][j] and base[j][i]:
					found = True
					break
			if found:
				break
		if found:
			continue


		while itr < 7 and not found:  # If we look at any more powers, it'll take up too much time
			mat = matmul(mat,base)
			itr+=1
			fil = 0
			t=0

			# Checks if diagonal have more than 1 True value
			for i in range(n):
				if mat[i][i]:
					t += 1
			if t>1:
				itr = 10
				continue


			# Checks if given matrix have any symmetric True values
			for i in range(n):
				for j in range(i+1,n):
					if mat[i][j] and mat[j][i]:
						itr = 10
						break
				if itr==10:
					break
			if itr==10:
				continue
			
			# Checks for the number of empty rows.
			for i in range(n):
				if True in mat[i]:
					fil += 1
					if fil>1:
						break

			# If there is only one row which has True in it, then we have got our desired result.
			if fil==1:
				found = True

				# We dont need to reach our destination in just 1 or 2 steps. That's boring. 
				if itr > 3:
					f.write(str([itr]+[g]) + "\n")

if __name__ == '__main__':

	start = time.perf_counter()

	calculate(5000000)

	end = time.perf_counter()
	print(f"{end-start}")
