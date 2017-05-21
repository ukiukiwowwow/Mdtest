import copy
import numpy as np
def MSD():
	with open("XDATCAR","r") as f,open("cmMSD","w") as cM:
		L=np.array([[0 for i in range(3)]for j in range(3)])
		for i in range(7):
			line=f.readline()
			if(i==2):
				L[0]=list(map(float,line.split()))
			if(i==3):
				L[1]=list(map(float,line.split()))
			if(i==4):
				L[2]=list(map(float,line.split()))
			if(i==5):
				atoms=line.split()
			if(i==6):
				atomnum=list(map(int,line.split()))
		for i in atoms:
			exec('cm{}=open("cm"+str(i),"w")'.format(i))
		sumatom=sum(atomnum)
		cur=np.array([[0]*3]*sumatom)
		pre=np.array([])
		r=np.array([np.zeros(sumatom)]*3)
		cmMSD=np.zeros(3)
		d=np.zeros(3)
		#Totalstep=int(input())
		time=-0.001
		#Tlines=(sumatom+1)*(Totalstep)
		linecount=0
		#msditerに渡す？
		while True:
			line=f.readline()
			if(line==""):
				print("OK?")
				break
			if(linecount%(sumatom+1)==0):
				#MSD計算
				#msd,cmmsd=calmsd(cur,pre,atom,atomnum)
				if(pre.any()==True):
					for an in range(sumatom):
						for dim in range(3):
							d[dim]=cur[an][dim]-pre[an][dim]
							d[dim]-=round(d[dim])
							r[an][dim]+=d[dim]
					cmMSD=np.sum(r,axis=0)/sumatom
					cM.write(str(time)+" "+str(cmMSD[0])+" "+str(cmMSD[1])+" "+str(cmMSD[2])+"\n")
					#Sir=(Six-cmMSD[0])*L[0]+(Siy-cmMSD[1])*L[1]+(Siz-cmMSD[2])*L[2]
					#Simsd=1/(Sinum)*np.dot(Sir,Sir)
					#ps.write(str(time)+" "+str(Simsd)+"\n")
					atomr=(r-cmMSD)*L[0]+(r-cmMSD)*L[1]+(r-cmMSD)*L[2]#3*N次元の物を3*N次元にする
					temp=0
					for i in range(len(atoms)):
						Latom=atomr[temp:temp+atomnum[i]-1]
						msd=(np.dot(Latom))/atomnum[i]
						exec('cm{}.write(str(time)+" "+str(msd)+"\n")'.format(i))
						temp=atomnum[i]-1
				linecount=1
				time+=0.001
				pre=copy.deepcopy(cur)
				cur=np.array([[0]*3]*sumatom)
				continue
			else:
				print(linecount)
				cur[linecount-1]=list(map(float,line.split()))
				linecount+=1
				continue
			
		for i in atoms:
			exec('cm{}.close()'.format(i))
if __name__ =="__main__":
	MSD()