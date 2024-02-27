# Step 1. Process input
eq=input('Enter the quadratic equation: ') # user have to input quadratic equation: ax^2+bx+c 

eq ='4x^2 +4x +    (-8) =  0'
eq = eq.replace(" ", "").split('+') 

a = int(eq[0].rstrip('x^2')) 
b = int(eq[1].rstrip('x')) 
c = eq[2].lstrip('(').rstrip(')=0') 

print('a =',a,'b =',b,'c =',c) # 4 4 -8

#Step 2. Calculate answer
a=int(a) 
b=int(b)
c=int(c)

x1=int((-b-(b**2-4*a*c)**0.5)/(2*a)) 
x2=int((-b+(b**2-4*a*c)**0.5)/(2*a))

print('x1 =',x1,'x2 =',x2) # -2 1