()
T=(0,)
print("T:",T)

T1=(0,'Ni',1.2, 4)
print("T1:",{T1})

T2=0, 'Ni', 2.5,6
print("T2:",T2)

T3=('abc',('def',('sri','ja'),'uvw'))
print("T3:",T3[0],T3[1][0])
print("T3:",T3[1][1][0],T3[1][1][1])

T4= tuple('spam')
print("T4:",T4)

T5=T1[2]
print(T5)

T6=T3[1]
print(T6)

T7=T4[2:4]
print(T7)

T8=len(T2)
print(T8)
