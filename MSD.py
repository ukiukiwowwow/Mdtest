import numpy as np
from copy import deepcopy
def subMSD():
	with open("XDATCAR","r") as f,open("cmSiMSD","w") as ps,open("cmOMSD","w") as po,open("cmMSD","w") as cM:
		L=np.array([[0 for i in range(3)]for j in range(3)])
		for i in range(7):
			line=f.readline()
			if(i==2):
				L[0]=list(map(float,line.split()))
			if(i==3):
				L[1]=list(map(float,line.split()))
			if(i==4):
				L[2]=list(map(float,line.split()))
			if(i==6):
				Sinum,Onum=list(map(int,line.split()))
		print(L)
		l=[]
		l.append(np.sqrt(np.dot(L[0],L[0])))
		l.append(np.sqrt(np.dot(L[1],L[1])))
		l.append(np.sqrt(np.dot(L[2],L[2])))
		linecount=0
		"""
		print("input lattice parameter")
		L=float(input())
		print("input number of species")
		SN=int(input())
		el=np.array([])
		for i in range(SN):
			print("{0} atom")
			el=np.append(el,input())
		"""
		
		
		#L=10.23
		#Sinum=24
		#Onum=48
		Sicur=np.empty((0,3), float)
		Ocur=np.empty((0,3), float)
		Sipre,Opre=[np.array([])for i in range(2)]
		Six,Siy,Siz=[np.zeros(Sinum)for i in range(3)]
		Ox,Oy,Oz=[np.zeros(Onum)for i in range(3)]
		cmMSD=np.zeros(3)
		d=np.zeros(3)
		print("Input Total timestep")
		Totalstep=int(input())
		time=-0.001
		Tlines=(Sinum+Onum+1)*(Totalstep)
		for line in range(Tlines):
			if(linecount%(Sinum+Onum+1)==0):
				f.readline()
				if Sipre.any()==True:
					for N in range(Sinum):
						for dim in range(3):
							d[dim]=Sicur[N][dim]-Sipre[N][dim]
							d[dim]-=round(d[dim])
						Six[N]+=d[0]
						Siy[N]+=d[1]
						Siz[N]+=d[2]


				if Opre.any()==True:
					for N in range(Onum):
						for dim in range(3):
							d[dim]=Ocur[N][dim]-Opre[N][dim]
							d[dim]-=round(d[dim])
						Ox[N]+=d[0]
						Oy[N]+=d[1]
						Oz[N]+=d[2]
					cmMSD[0]=(np.sum(Ox,axis=0)+np.sum(Six,axis=0))/(Sinum+Onum)
					cmMSD[1]=(np.sum(Oy,axis=0)+np.sum(Siy,axis=0))/(Sinum+Onum)
					cmMSD[2]=(np.sum(Oz,axis=0)+np.sum(Siz,axis=0))/(Sinum+Onum)
					cM.write(str(time)+" "+str(cmMSD[0])+" "+str(cmMSD[1])+" "+str(cmMSD[2])+"\n")
				if Sipre.any()==True:
					Sir=(Six-cmMSD[0])*L[0]+(Siy-cmMSD[1])*L[1]+(Siz-cmMSD[2])*L[2]
					Simsd=1/(Sinum)*np.dot(Sir,Sir)
					ps.write(str(time)+" "+str(Simsd)+"\n")
				if Opre.any()==True:
					Or=(Ox-cmMSD[0])*L[0]+(Oy-cmMSD[1])*L[1]+(Oz-cmMSD[2])*L[2]
					Omsd=1/(Onum)*np.dot(Or,Or)
					po.write(str(time)+" "+str(Omsd)+"\n")
				time+=0.001
				linecount+=1
				Sipre=deepcopy(Sicur)
				Opre=deepcopy(Ocur)
				Sicur=np.empty((0,3),float)
				Ocur=np.empty((0,3),float)
				continue
				
				
				
			if(linecount%(Sinum+Onum+1)<(Sinum+1)):
				#Si=np.concatenate(Si,np.arrylist(map(float,f.readline().split())))
				#Si=np.vstack(Si,list(map(float,f.readline().split())))
				Sicur=np.append(Sicur,np.array([list(map(float,f.readline().split()))]),axis=0)
				linecount+=1
				continue
			else:
				#O=np.vstack(O,list(map(float,f.readline().split())))
				#O=np.append(O,list(map(float,f.readline().split())),axis=0)
				Ocur=np.append(Ocur,np.array([list(map(float,f.readline().split()))]),axis=0)
				linecount+=1
				continue
if __name__ =="__main__":
	subMSD()