def sinf(a):
	g=open(a,"r")
	linecount=0
	s=[]
	sn=[]
	si=[]
	o=[]
	print("Input Lattice constant")
	L=float(input())
	for line in g:
		linecount+=1
		if linecount <=5:
			continue
		elif linecount == 6:
			s.extend(line.split())
			continue
		elif linecount == 7:
			sn.extend(line.split())
			#si=[[0 for i in range(3)] for j in range(int(sn[0]))]
			#o=[[0 for i in range(3)] for j in range(int(sn[1]))]
			continue
		elif linecount == 8 or linecount ==9:
			continue
		elif linecount <(10+int(sn[0])):
			t=line.split()
			temp=[float(i)*L for i in t[:3]]
			si.append(temp)
			continue
		elif linecount<(34+int(sn[1])):
			t=line.split()
			temp=[float(i)*L for i in t[:3]]
			o.append(temp)
			continue
	g.close()
	return(si,o)