#! /usr/bin/env python
# -*- code: utf-8 -*-

import random
import copy
 
def dp_LIS(arr):
	length=1
	arrl=len(arr)
	d=[1]*arrl
	for i in range(arrl):
		d[i]=1
		for j in range(i):
			if arr[j]<=arr[i] and d[j]+1>d[i]:
				d[i]=d[j]+1
		if d[i]>length:length=d[i]
	return length

def insert(l,n):
	start=0
	end=len(l)-1
	while(start<end):
		mid=(start+end)/2
		if l[mid]>n:
			end=mid
		else:
			start=mid+1
	return start

def dp_LIS_adjust(arr):
	b=[]
	b.append(arr[0])
	for i in range(1,len(arr)):
		number=arr[i]
		if number < b[-1]:
			pos=insert(b,number)
			b[pos]=number
		else:
			b.append(number)
	return len(b)

def main():
	a = [2,1,5,3,6,4,8,9,7]
	print "====>LIS DP BY O(N^2)"
	print dp_LIS(a)
	print "====>LIS DP BY O(Nlg(N^2))"
	print dp_LIS_adjust(a)
if __name__ == '__main__':
    main()
