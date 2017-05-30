import copy
import numpy as np
def MSD():
	with open("XDATCAR","r") as f,open("cmMSD","w") as cM,open("MSD","w") as M:
		L=np.array([[0]*3]*3)
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
		#方針を変えて一つのMSDファイルにまとめる Si O/time SiMSD OMSDのようにする？ 
		
		for i in atoms:
			M.write(str(i)+" ")
		#exec('cm{}MSD=open("cm"+str(i),"w")'.format(i))#cmSiMSDの後cmOMSDを作ると前のcmSiMSDのような変数が破棄される？
		M.write("\n")
		sumatom=sum(atomnum)
		cur=np.array([np.zeros(3)]*sumatom)
		pre=np.array([np.zeros(3)]*sumatom)
		r=np.array([np.zeros(3)]*sumatom)
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
					atomr=(r-cmMSD)[:,0].reshape(1,len(r)).T*L[0]+(r-cmMSD)[:,1].reshape(1,len(r)).T*L[1]+(r-cmMSD)[:,2].reshape(1,len(r)).T*L[2]#3*N次元の物を3*N次元にする
					#atomrがおかしい r,cmMSDは間違いなく同一である。
					temp=0;M.write(str(time)+" ")
					for i in range(len(atoms)):
						Latom=atomr[temp:temp+atomnum[i]]#-1?
						msd=(np.linalg.norm(Latom)**2)/atomnum[i]
						M.write(str(msd)+" ")#exec('cm{}MSD.write(str(time)+" "+str(msd)+"\n")'.format(i))
						temp=atomnum[i]#-1?
					M.write("\n")
				linecount=1
				time+=0.001
				pre=copy.deepcopy(cur)
				cur=np.array([np.zeros(3)]*sumatom)
				continue
			else:
				
				cur[linecount-1]=list(map(float,line.split()))
				linecount+=1
				continue
		"""	
		for i in atoms:
			exec('cm{}.close()'.format(i))
		"""
if __name__ =="__main__":
	MSD()
[-0.00781719  0.02319196 -0.00135567]
[-0.0153165   0.04721292 -0.00460734]
[-0.0225384   0.07191144 -0.00988226]
[-0.02952098  0.09711545 -0.01728913]
[-0.03629731  0.12261765 -0.02690245]
[-0.04289241  0.14815643 -0.0387283 ]
[-0.04931879  0.17339352 -0.05267043]
[-0.05556582  0.19788396 -0.06848482]
[-0.06159236  0.22105757 -0.08574845]
[-0.06731357  0.24222204 -0.10384898]
[-0.072596    0.26055114 -0.12197026]
[-0.07724481  0.27506108 -0.13907365]