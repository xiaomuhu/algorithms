#! /usr/bin/env python
# -*- code: utf-8 -*-

import random
import copy

 
def BT_packages_iterable(ws, max):
	print "null"	

s=[0]*5
def BT_packages_recursion(w,t,n,cw):
	if n >= len(w):
		if (cw<=t):
			print s,cw
	else:
		for i in range(2):
			tcm=cw
			if i==1:
				s[n]=1
				tcm=cw+w[n]
			else:
				s[n]=0
			if tcm<=t:
				BT_packages_recursion(w,t,n+1,tcm)

def isOK(tx,tnum,ti):
	#print x
	for row in tx:
		if row < tnum:
			if ti==tx[row] or tnum-row == ti-tx[row] or tnum-row == tx[row]-ti:
				return False
	return True
			
x={}
def Queens(t,num):
	if t>=num:
		s=""
		for m in range(num):
			for n in range(num):
				if n==x[m]:
					s=s+"O"
				else:
					s=s+"*"
			s=s+"\n"
		print s
		print "==============\n"
		
	else:
		for i in range(num):
			#print x
			if isOK(x,t,i):
				x[t]=i
				Queens(t+1,num)
	
def main():
	#weigths=[5,4,7,2,6]
	#total=15
	#BT_packages_recursion(weigths,total,0,0)
	#print BT_packages(weigths,total)
	Queens(0,8)
#print x
if __name__ == '__main__':
    main()
