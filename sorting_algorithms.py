#Bubble Sort Algorithm
#https://en.wikipedia.org/wiki/Bubble_sort
def bub_sort(a):
	for i in range(0, len(a) - 1):
		for j in range(0, len(a) - 1 - i):
			if a[j + 1] < a[j]:
				tmp = a[j]
				a[j] = a[j+1]
				a[j+1] = tmp
		
	return a

#Selection Sort Algorithm
#https://en.wikipedia.org/wiki/Selection_sort
def sel_sort(a):
	b = [0 for i in range(len(a))]
	
	for i in range(0,len(a)):
		min = a[i]
		for j in range(i,len(a)):
			if (a[j] < min):
				tmp = min
				min = a[j]
				a[j] = tmp
			
			
		b[i] = min
		
	return b

#Insertion  Sort Algorithm
#https://en.wikipedia.org/wiki/Insertion_sort
def insert_sort(a):
	for i in range(1, len(a)):
		temp = a[i]
		j = i - 1
		while j >= 0 and a[j] > temp:
			a[j+1] = a[j]
			j = j - 1
		
		a[j+1] = temp


#Merge Sort Algorithm
#https://en.wikipedia.org/wiki/Merge_sort

#this is the top-down merge fxn within the merge sort algorithm
# see here: https://en.wikipedia.org/wiki/Merge_sort#Bottom-up_implementation_using_lists
def merge(b,c,a):
	i,j,k = 0,0,0
	while i < len(b) and j < len(c):
		if b[i] <= c[j]:
			a[k] = b[i]
			i += 1
		else:
			a[k] = c[j]
			j += 1
		
		k += 1
	
	if i == len(b):
		a[k:] = c[j:]
	else:
		a[k:] = b[i:]

#Merge Sort Algorithm
#https://en.wikipedia.org/wiki/Merge_sort
def merge_sort(a):
	if len(a) > 1:
		b= a[:(len(a)/2)]
		c= a[(len(a)/2):]
		merge_sort(b)
		merge_sort(c)
		merge(b,c,a)

		return a

#Quick Sort Algorithm
#https://en.wikipedia.org/wiki/Quick_sort
def quick_sort(arr):
	less = []
	pivotList = []
	more = []
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		for i in arr:
			if i < pivot:
				less.append(i)
			elif i > pivot:
				more.append(i)
			else:
				pivotList.append(i)
		less = quick_sort(less)
		more = quick_sort(more)
		return less + pivotList + more
		
#because there are only 5 tests this silly function takes the values of a dictionary (in a sorted array) and returns the 
#keys that have those values (note it is extremely unlikely any two will have the same value, which is why this works in this case)
def get_keys_from_vals(dict, search_vals):
	sorted_list = []
	for search_val in search_vals:
		for key, val in dict.items():
		    if val == search_val:
		        sorted_list.append(key)

	return sorted_list

def check_numbers_to_sort():
	n_to_sort = 500
	if len(sys.argv) == 2:
		try:
			n_to_sort = int(sys.argv[1])
			if n_to_sort < 0 or n_to_sort > 99999:
				print 'Usage: $ python sorting_algorithms.py [number of integers to sort]'
				print 'if no number of intgers to sort is supplied, default (500) is used'
				sys.exit(1)
		except:
			print 'Usage: $ python sorting_algorithms.py [number of integers to sort]'
			print 'if no number of intgers to sort is supplied, default (500) is used'
			sys.exit(2)
	elif len(sys.argv) > 2:
		print 'Usage: $ python sorting_algorithms.py [number of integers to sort]'
		print 'if no number of intgers to sort is supplied, default (500) is used'
		sys.exit(1)

	return n_to_sort

import random as rnd
from time import time
import sys

#check for user input, if none use default (500)
n_to_sort = check_numbers_to_sort()

print 'Now sorting ' + str(n_to_sort) + ' randomly selected integers using 5 sorting algorithms\n'

#retrieve a random array of x (default is 500) integers for each algorithm to sort
unsorted_array = [rnd.randint(1,500) for i in range(500)]
unsorted_array_tmp = unsorted_array
times = {}

bs = time()
b = bub_sort(unsorted_array)
bf = time()
times['bubble_time'] = bf - bs
print 'bubble sort took ' + str(times['bubble_time']) + ' seconds'

unsorted_array = unsorted_array_tmp
ss = time()
c = sel_sort(unsorted_array)
sf = time()
times['selection_time'] = sf - ss
print 'selection sort took ' + str(times['selection_time']) + ' seconds'

unsorted_array = unsorted_array_tmp
iis = time()
d = insert_sort(unsorted_array)
iif = time()
times['insert_time'] = iif - iis
print 'insert sort took ' + str(times['insert_time']) + ' seconds'

unsorted_array = unsorted_array_tmp
ms = time()
e = merge_sort(unsorted_array)
mf = time()
times['merge_time'] = mf - ms
print 'merge sort took ' + str(times['merge_time']) + ' seconds'

unsorted_array = unsorted_array_tmp
qs = time()
q = quick_sort(unsorted_array)
qf = time()
times['quick_time'] = qf - qs
print 'quick sort took ' + str(times['quick_time']) + ' seconds'

print '\n********\n[fastest, ... , slowest]'
print get_keys_from_vals(times, sorted(times.values()))