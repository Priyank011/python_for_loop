l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
t3=tuple(l1)
t4=tuple(l2)
t5=tuple(zip(l1,l2))
l6=list(zip(l1,l2))
d1=dict(zip(l1,l2))
d11=dict(l6)
t8=tuple(zip(l1,l2))
d2=dict(t8)
d3=dict(zip(t3,t4))
print(l1)
print(l2)
print(t3)
print(t4)
print(t5)
print(l6,"*")
print(d1)
print(d11)
print(d2)
print(d3)
print(t8)
l9=list(d3.keys())
print(l9)
l10=list(d3.items())
print(l10)
l11=list(d3.values())
print(l11)
t9=tuple(d3.keys())
print(t9)
t10=tuple(d3.items())
print(t10)
t11=tuple(d3.values())
print(t11)
t12=tuple(zip(t9,t11))
print(t12)
l13=list(zip(l9,l11))
print(l13)