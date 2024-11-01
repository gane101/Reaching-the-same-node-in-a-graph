import time
import multiprocessing as mp

# I will recommend you to go through the main file as I haven't explaned anything here.
# If you know any way to optimize ths code further, I would appreciate it.

# For nxn Matrix
n = 5 # make sure to change it at line 40
try:
	f = open("data.txt",'x+')
except FileExistsError:
	f = open("data.txt","w")

def matmul(m1,cl):
	res = [[]]*n

	# Going through rows of first matrix
	for k in range(n):
		res[k] = [False]*n
		
		# Checks if the row is empty
		if True not in m1[k]:
			continue

		# Makes a set of number of columns which have True in k'th row 
		ls = set()
		for i in range(n):
			if m1[k][i]:
				ls.add(i)
		
		# We are checking if there is intersecton between current row set and each column set we made at 75 to 81
		# If there is any intersection, we'll know that atleast two number can be multiplied, which gives us True value
		for i in range(n):
			if cl[i] & ls:
				res[k][i] = True

	return res

def start_from(s):
	n = 5
	for g in range(s,s+frac):
		a = bin(g)[2:]

		# Checks Diagonals
		if a[::-n-1].count('1')>1:
			continue

		# Checks Columns
		found = False
		for i in range(n):
			if '1' not in a[i::n]:
				found = True
				break
		if found:
			continue

		# Convert Binary representation to matrix
		num = [False]*(n*n-len(a)) + [c=='1' for c in a]
		base = [[]]*n
		for i in range(n):
			base[i] = num[:n]
			num = num[n:]
		mat = base.copy()

		# Checks for symmetric True values
		for i in range(n):
			for j in range(i+1,n):
				if base[i][j] and base[j][i]:
					found = True
					break
			if found:
				break
		if found:
			continue

		# Set version of Columns of base matrix for faster matrix multiplication
		cl = [{}]*n
		for i in range(n):
			temp = set()
			for j in range(n):
				if base[j][i]:
					temp.add(j)
			cl[i] = temp

		itr = 1

		while itr < 7 and not found: # If we look at more powers, it'll take way too much time.
			itr+=1
			mat = matmul(mat,cl)
			fil = 0
			t=0

			# Checks Diagonals
			for i in range(n):
				if mat[i][i]:
					t += 1
			if t>1:
				itr = 10
				continue


			# Checks if there are any aymmetric True values
			for i in range(n):
				for j in range(i+1,n):
					if mat[i][j] and mat[j][i]:
						itr = 10
						break
				if itr==10:
					break
			if itr==10:
				continue
			
			# Gives us number of rows with atleast one True value
			for i in range(n):
				if True in mat[i]:
					fil += 1
					if fil>1:
						break

			# We check if there is only one row filled
			if fil==1:
				found = True
				# We dont have to look at boring 1 and 2 powers
				if itr > 3:
					f.write(str([itr]+[g]) + "\n")


frac = 2**23

if __name__ == '__main__':

	# I am using all the CPU cores I have. If you have more, you can add more lines here.
	p1 = mp.Process(target = start_from,args=(0,))
	p2 = mp.Process(target = start_from,args=(frac,))
	p3 = mp.Process(target = start_from,args=(frac*2,))
	p4 = mp.Process(target = start_from,args=(frac*3,))

	start = time.perf_counter()

	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p1.join()
	p2.join()
	p3.join()
	p4.join()

	end = time.perf_counter()
	
	print(f"{end-start}")

