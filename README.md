# Test
Newbie
d={0:1,1:2,2:3}
a={0:100,1:200,2:300}
c={}
for i in d:
    c[i]=a[i]+d[i]
print(c)
type(c)
def qu():
    a={1:20,3:100,4:5}
    c=sorted(a.items(),key=lambda x: x[1])
    print(c)
    return dict(c)
oi=qu()
print(oi)
for k, v in c.items():
    print(k, v)
