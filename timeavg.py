import math
import sys
import collections
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
def osioang(si,o):
	count=0
	sumav=0
	countang=[]
	for i in range(len(si)):
		t=[]
		ang=0
		o1=[]
		o2=[]
		#print("si,",si[i])
		for j in range(len(o)):
			d=0
			temp=0
			for k in range(3):
				temp+=(o[j][k]-si[i][k])**2
			d+=math.sqrt(temp)
			if(d<2.0):
				#t0x,t0y,t0z=o[for i in range(3)][j]
				t.append(o[j][:3])
				l=len(t)*(len(t)-1)	
		for o1 in t:
			for o2 in t:
				t1=[0]*3
				t2=[0]*3
				#print(o2,"o2b")
				#print(si[i],"si")
				if(o1==o2):
					continue
				for k in range(3):
					t1[k]=o1[k]-si[i][k]
					t2[k]=o2[k]-si[i][k]
				p=[x*y for (x,y) in zip(t1,t2)]
				n=sum(p)
				rad=math.acos(n/(math.sqrt(t1[0]**2+t1[1]**2+t1[2]**2)*math.sqrt(t2[0]**2+t2[1]**2+t2[2]**2)))
				#print(math.degrees(rad))
				countang.append(int(math.degrees(rad)))
				ang+=math.degrees(rad)
				#print(o2,"o2a")
		if(ang!=0):
			count+=1
		sumav+=ang/(l)
	avang=sumav/count
	print(avang)
	#print(sorted(countang))
	return sorted(countang)
	
def siosiang(si,o):
	count=0
	countang=[]
	
	for i in range(len(o)):
		t=[]
		si1=[]
		si2=[]
		for j in range(len(si)):
			d=0
			temp=0
			for k in range(3):
				temp+=(o[i][k]-si[j][k])**2
			d+=math.sqrt(temp)
			if(d<2.5):
				t.append(si[j][:3])
				
				#print(t)
		
		for si1 in t:
			for si2 in t:
				t1=[0]*3
				t2=[0]*3
				#print(o2,"o2b")
				#print(si[i],"si")
				if(si1[0]==si2[0]):
					continue
				for k in range(3):
					t1[k]=si1[k]-o[i][k]
					t2[k]=si2[k]-o[i][k]
				p=[x*y for (x,y) in zip(t1,t2)]
				n=sum(p)
				rad=math.acos(n/(math.sqrt(t1[0]**2+t1[1]**2+t1[2]**2)*math.sqrt(t2[0]**2+t2[1]**2+t2[2]**2)))
				#print(math.degrees(rad))
				countang.append(int(math.degrees(rad)))
				
				#print(o2,"o2a")
		
		
	#avang=sumav/count
	#print(avang)
	#print(sorted(countang))
	d=defaultdict(int)
	for i in sorted(countang):
		d[i]+=1
	
	return sorted(d)
	
"""	
def angdis(a):

	d=defaultdict(int)
	print("Input to write file name")
	n=input()
	f=open(n,"w")
	for i in a:
		d[i]+=1
	sd=sorted(d)
	for i in sd:
		print(i,d[i])
		f.write(str(i)+" "+str(d[i])+"\n")
"""		
#XDATCAR One iter->[Si,O]->Fang(List)->Add angdis->Next iter
#Iter end -> angdis/totalTimeStep

def ReadXDATCAR():
	print("This program calculates  only SiO2 properties")
	print("Input lattice constant")
	L=float(input())
	print("Input total time step ")
	T=int(input())
	
	with open("testXDATCAR","r") as xdat:
		for i in range(6):
			print(xdat.readline())
		Sinum,Onum=list(map(int,xdat.readline().split()))
		Si=np.empty((0,3),float)
		O=np.empty((0,3),float)
		N=Sinum+Onum+1
		linecount=0
		for i in xdat:
			linecount+=1
			if(linecount%N==1):
				if Si.any()==True:
					SiOSi=siosiang(Si,O)
					print(type(SiOSi))
				#ここでF(list)にする
				
				Si=np.empty((0,3),float)
				O=np.empty((0,3),float)
				continue
			elif(linecount%N<1+Sinum):
				Si=np.append(Si,L*np.array([list(map(float,i.split()))]),axis=0)
				continue
			elif(linecount%N<1+Sinum+Onum):
				O=np.append(O,L*np.array([list(map(float,i.split()))]),axis=0)
				continue
		#if Si.any()==True:
		#ここでF(list)にする
		
		Si=np.empty((0,3),float)
		O=np.empty((0,3),float)
ReadXDATCAR()