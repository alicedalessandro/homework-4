
from itertools import tee,islice
s = "nucleotidesequence"
n=""
d=""
o=[ ]
o1=[ ]
for j in s:
	if j=="A":
		n+="T" 
	if j=="C":
		n+="G"
	if j=="T":
		n+="A"
	if j=="G":
		n+="C"
for i in range(1, len(n)+1):
	d+=n[-i]
for p in range(4, 13):
	v=tee(s, p)
	for i, j in enumerate (v):
		next(islice(j, i, i), None)
	q=["".join(k) for k in zip(*v)]
	d1={ }
	c1=0
	for t in q:
		d1[c1]=t
		c1+=1
	v=tee(n, p)
	for i, j in enumerate (v):
		next(islice(j, i, i), None)
	y=["".join(k) for k in zip(*v)]
	d2={ }
	c2=0
	for t1 in y:
		d2[c2]=t1
		c2+=1
	for u in range(len(d1)):
		m=0
		for g in range(len(d1[u])):
			if d1[u][g-1]!=d2[u][-g]:
				m=1
		if m==0:
			o.append(str(u+1) + " " + str(len(d1[u])))
for j in o:
	print(j)
