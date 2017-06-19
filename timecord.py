import re
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
def cord_time_change(sisi,sio):
	"""sisiはSi-Siの結合距離 sioはSi-Oの結合距離
	方針として各Si[i]ごとに結合パターンSi:O=[x,y]を求める
	それを時間との表にして順次出力する。(原子ごとに異なるファイルにする？)
	プロットは別にやる(理由空間計算量大)
	入れ替わったかどうかを判断するのは難しく入れ替わりだけを対象としているのでそれ以外は捕らえられない
	
	
	Si原子ごとに周囲のOの数とSiの数を記録する
	
	"""
	print(os.getcwd())
	shutil.copyfile("../XDATCAR","./XDATCAR")
	print("copy")
	with open("XDATCAR","r") as f,open("Sitimecord.dat","w") as Sc:
		L=np.array([np.zeros(3)]*3)
		for i in range(5):
			line=f.readline()
			if(i==2):
				L[0]=list(map(float,line.split()))
				continue
			if(i==3):
				L[1]=list(map(float,line.split()))
				continue
			if(i==4):
				L[2]=list(map(float,line.split()))
				continue
		print(L)
		atomname=np.array(f.readline().split())
		atomnum=np.array(list(map(int,f.readline().split())))
		sumatom=np.sum(atomnum)
		#cur=np.array([np.zeros(3)]*sumatom)
		#pre=np.array([np.zeros(3)]*sumatom)
		atom=np.array([np.zeros(3)]*sumatom)
		linecount=0
		for index in range(atomnum[0]):
			Sc.write("Si"+str(index+1)+" ")
		Sc.write("\n")
		while True:
			line=f.readline()
			if(line==""):
				print("OK?")
				break
			if(linecount%(sumatom+1)==0):
				#Siの各結合数を数える
				#Si-O
				SiOnum=np.zeros(atomnum[0])
				SiSinum=np.zeros(atomnum[0])
				for Siindex,Si in enumerate(atom[:atomnum[0]]):
					Ocount=0
					for O in atom[atomnum[0]:]:
						fracdis=Si-O
						#0.5以上の距離を持つ場合周期的境界条件の補正を加える
						for dim in range(3):
							fracdis[dim]-=round(fracdis[dim])
						realdis=L[0]*fracdis[0]+L[1]*fracdis[1]+L[2]*fracdis[2]
						#Lをかけよう
						if(np.linalg.norm(realdis)<=sio):
							Ocount+=1
					SiOnum[Siindex]=Ocount
				for Siindex,Si1 in enumerate(atom[:atomnum[0]]):
					Sicount=0
					for Si2 in atom[:atomnum[0]]:
						fracdis=Si1-Si2
						#0.5以上の距離を持つばあい周期的境界条件の補正を加える
						for dim in range(3):
							fracdis[dim]-=round(fracdis[dim])
						realdis=L[0]*fracdis[0]+L[1]*fracdis[1]+L[2]*fracdis[2]
						#Lをかけよう
						if(np.linalg.norm(realdis)<=sisi):
							Sicount+=1
					SiSinum[Siindex]=Sicount-1
				linecount=1
				for index in range(atomnum[0]):
					Sc.write(str(SiOnum[index])+","+str(SiSinum[index])+" ")
				Sc.write("\n")
			else:
				atom[linecount-1]=list(map(float,line.split()))
				linecount+=1
				continue
	return atomnum[0]
def plot(Sinum):
	with open("Sitimecord.dat","r") as Sc:
		print(Sc.readline())
		print(Sc.readline())
		time=0.001#ps
		count=0
		SiSi=np.array([])
		SiO=np.array([])
		while True:
			line=Sc.readline()
			if(line==""):
				print("OK")
				break
			temp=line.split()
			for i in temp:
				t1,t2=i.split(",");t2=float(t2);t1=float(t1)
				SiSi=np.append(SiSi,int(t1))
				SiO=np.append(SiO,int(t2))
			count+=1
			time+=0.001
		SiSi=SiSi.reshape(int(len(SiSi)/Sinum),Sinum).T
		SiO=SiO.reshape(int(len(SiO)/Sinum),Sinum).T
		time=np.linspace(0.001,time,num=len(SiSi[0]))
		plt.plot(time,SiSi[0])
		plt.savefig("test.png",dpi=150)
				
if __name__ =="__main__":
	#if not os.path.exists("./change_cord"):
	#	#os.mkdir("./change_cord")
	#os.chdir("./change_cord")
	#cord_time_change(3.5,2.0)
	plot(24)
