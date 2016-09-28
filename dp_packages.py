#! /usr/bin/env python
# -*- code: utf-8 -*-

import random
import copy

def max(a,b):
	if a>b:
		return b
	else:
		return a

def get01MaxValues(ws,vs,limits):
	data={}
	strs=""
	choose=""
	for i in range(len(ws)):
		for j in range(1,limits+1):
			count=0
			#if j==0:
			#	data[str(i)+"-"+str(j)]=0
			for x in range(0,max(j/ws[i]+1,2)):
				k=str(i-1)+"-"+str(j-ws[i]*x)
				tmp_count=vs[i]*x+data.get(k,0)
				if tmp_count > count:
					count=tmp_count
			data[str(i)+"-"+str(j)]=count
			strs=strs+"\t"+str(count)
		strs=strs+"\n"
	print strs

def getNoLimitMaxValues(ws,vs,limits):
	detail={}
        data={}
        strs=""
        for i in range(len(ws)):
                for j in range(limits):
                        count=0
                        #if j==0:
                        #       data[str(i)+"-"+str(j)]=0
			sk="0-0"
			m=0
                        for x in range(0,j/ws[i]+1,2):
                                k=str(i-1)+"-"+str(j-ws[i]*x)
                                tmp_count=vs[i]*x+data.get(k,0)
                                if tmp_count > count:
                                        count=tmp_count
					sk=k
					m=x
			#print "----",i,j,m
			tm=[m]
			tm.extend(detail.get(sk,[]))
			detail[str(i)+"-"+str(j)]=tm
                        data[str(i)+"-"+str(j)]=count
                        strs=strs+"\t"+str(count)
                strs=strs+"\n"
        print strs
	print "###########"
	print detail["4-14"]

def main():
	weigths=[5,4,7,2,6]
	values=[12,3,10,3,6]
	store_limit=[]
	total=15
	print "====> 0-1 packages problems" 
	#get01MaxValues(weigths,values,total)
	print "====> no limit packages problems; and print the details"
        getNoLimitMaxValues(weigths,values,total)
	print "====> multi packages problems"
	#max(j/ws[i]+1,2) panduan def
	print "====> three mixture packages problems"
	#max(j/ws[i]+1,2) panduan def
	print "====> one thing two weight and values packages problems"
	#transfer two things
	print "====> groups packages problems"
	#for i in range(len(groups)):
	#	for is in rang(len(groups[i]))
	print "====> rely to other things"
	#c[i]<=c[j]&&w[i]>=w[j]
	#relys transfer to groups
	print "====> interface packages problems"
	#every things is a packages problems
	#v=h(w)
if __name__ == '__main__':
    main()
