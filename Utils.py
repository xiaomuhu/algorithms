#! /usr/bin/env python
# -*- code: utf-8 -*-

import random
import copy

def HANOI_move(f,tmp,t,k):
	if k==2:
		#print a,b,c
		print "number %s from %s to %s" % (1,f,tmp)
		print "number %s from %s to %s" % (2,f,t)
		print "number %s from %s to %s" % (1,tmp,t)
	elif k==1:
		print "number %s from %s to %s" % (1,f,t)
	else:
		HANOI_move(f,t,tmp,k-1)
                print "number %s from %s to %s" % (k,f,t)
		HANOI_move(tmp,f,t,k-1)

def HANOI(n):
	arr1="a"
	arr2="b"
	arr3="c"
	HANOI_move(arr1,arr2,arr3,n)


def DC_MaxMin_get(s,e,arr):
	
	if(e-s<=1):
		max=0
		min=0
		if arr[e]>arr[s]:
			max=arr[e]
			min=arr[s]
		else:
			min=arr[e]
			max=arr[s]
		return max,min
	else:
		max=0
		min=0
		mid=(s+e)/2
		max1,min1=DC_MaxMin_get(s,mid,arr)
		max2,min2=DC_MaxMin_get(mid,e,arr)
		if max1>max2:
			max=max1
		else:
			max=max2
		if min1<min2:
			min=min1
		else:
			min=min2
		return max,min
		
	
def DC_MaxMin():
	a = [4,5,6,3,4,7,7,4,3,3,2,4,5,5,6,9,5,4,3,45,3,23,44,55,33,5,8]
	print DC_MaxMin_get(0,len(a)-1,a)
def main():
	#HANOI(4)
	DC_MaxMin()
if __name__ == '__main__':
    main()
