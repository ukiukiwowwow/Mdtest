import re
def newdiff(flag=0):
	with open("cmSiMSD","r") as f,open("cmOMSD","r") as g,open("subdiff.dat","w") as sd: 
		print("Si-selfdiffusion")
		sd.write("Si-selfdiffusion\n")
		if(flag==1):
			import matplotlib.pyplot as plt
			import numpy as np
			temp=np.empty((0,2), float)
		linecount=0
		for line in f:
			linecount+=1
			if(linecount==1):
				continue
			time,Si=list(map(float,line.split()))
			if(flag==1):
				temp=np.append(temp,np.array([[time,(Si/(6*time)*10)]]),axis=0)
			if(linecount%5000==0):
				print("{0},{1}".format(time,Si/(6*time)*10))
				sd.write(str(time)+" "+str(Si/(6*time)*10)+"\n")
		print(time,Si/(6*time)*10)
		sd.write(str(time)+" "+str(Si/(6*time)*10)+"\n")
		if(flag==1):
			Dsi=temp.T
			temp=np.empty((0,2), float)
		linecount=0
		print("O-selfdiffusion")
		sd.write("O-selfdiffusion\n")
		for line in g:
			linecount+=1
			if(linecount==1):
				continue
			time,O=list(map(float,line.split()))
			if(flag==1):
				temp=np.append(temp,np.array([[time,(O/(6*time)*10)]]),axis=0)
			if(linecount%5000==0):
				print("{0},{1}".format(time,O/(6*time)*10))
				sd.write(str(time)+" "+str(O/(6*time)*10)+"\n")
		print(time,O/(6*time)*10)
		
		sd.write(str(time)+" "+str(O/(6*time)*10)+"\n")
		if(flag==1):
			Do=temp.T
			plt.plot(Dsi[0],Dsi[1],label="Dsi")
			plt.plot(Do[0],Do[1],label="Do")
			plt.legend(loc=1)
			plt.xlabel("Time(fs)", fontsize=16)
			plt.ylabel("$D(10^{-9}m^{2}/s)$", fontsize=16)
			plt.tick_params(labelsize=16)
			plt.savefig('Dliner.eps', dpi=150)
			plt.savefig('Dliner.png', dpi=150)
			plt.tight_layout()
			plt.clf()
			
			plt.plot(Dsi[0],Dsi[1],label="Dsi")
			plt.plot(Do[0],Do[1],label="Do")
			plt.legend(loc=1)
			plt.yscale("log")
			plt.xscale("log")
			plt.grid(which="both")
			plt.xlabel("Time(ps)", fontsize=16)
			plt.ylabel("$D(10^{-9}m^{2}/s)$", fontsize=16)
			plt.tick_params(labelsize=16)
			plt.savefig('Dlog.eps', dpi=150)
			plt.savefig('Dlog.png', dpi=150)
			plt.tight_layout()
			plt.clf()
def cmdiff(flag=0):
	with open("cmMSD","r") as cM,open("cmdiff.dat","w") as cd:
		print("cm-selfdiffusion")
		cd.write("cm-selfdiffusion\n")
		with ("XDATCAR","r") as x:
			L=np.array([[0 for i in range(3)]for j in range(3)])
			for i in range(7):
				line=f.readline()
				if(i==2):
					L[0]=list(map(float,line.split()))
				if(i==3):
					L[1]=list(map(float,line.split()))
				if(i==4):
					L[2]=list(map(float,line.split()))
		if(flag==1):
			import matplotlib.pyplot as plt
			import numpy as np
			temp=np.empty((0,2), float)
		print("Input lattice parameter")
		linecount=0
		for line in cM:
			linecount+=1
			if(linecount==1):
				continue
			time,x,y,z=list(map(float,line.split()))
			r=x*L[0]+y*L[1]+z*L[2]
			r=np.dot(r,r)
			#r=np.dot(x,x)+np.dot(y,y)+np.dot(z,z)
			#r=r*L**2
			if(flag==1):
				temp=np.append(temp,np.array([[time,(r/(6*time)*10)]]),axis=0)
			if(linecount%5000==0):
				print("{0},{1}".format(time,r/(6*time)*10))
				cd.write(str(time)+" "+str(r/(6*time)*10)+"\n")
		print(time,r/(6*time)*10)
		if(flag==1):
			Dc=temp.T
			plt.plot(Dc[0],Dc[1],label="Dcm")
			plt.legend(loc=1)
			plt.xlabel("Time(ps)", fontsize=16)
			plt.ylabel("$D(10^{-9}m^{2}/s)$", fontsize=16)
			plt.tick_params(labelsize=16)
			plt.savefig('Dcmliner.eps', dpi=150)
			plt.savefig('Dcmliner.png', dpi=150)
			plt.tight_layout()
			plt.clf()
			
			plt.plot(Dc[0],Dc[1],label="Dcm")
			plt.legend(loc=1)
			plt.yscale("log")
			plt.xscale("log")
			plt.grid(which="both")
			plt.xlabel("Time(fs)", fontsize=16)
			plt.ylabel("$D(10^{-9}m^{2}/s)$", fontsize=16)
			plt.tick_params(labelsize=16)
			plt.savefig('Dcmlog.eps', dpi=150)
			plt.savefig('Dcmlog.png', dpi=150)
			plt.tight_layout()
			plt.clf()
		
if __name__=="__main__":
	print("Do you want to plot D,type(y)")
	if re.compile("y",re.IGNORECASE).match(input().split()[0]) != None:
		flag=1
	else:
		flag=0
	newdiff(flag)
	#cmdiff(flag)