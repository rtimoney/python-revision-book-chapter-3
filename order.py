# setting order

# declare and initialize example variables for demonstartion purposes
a = 2
b = 4
c = 8

# addition and multiplication
print ('\nDefault Order:\t', a ,'*' ,c,'+',b,'=',a*c+b)
print ('Forced Order:\t', a ,'* (' ,c,'+',b,') =',a*(c+b))

# subtraction and division
print ('\nDefault Order:\t', c ,'//' ,b,'-',a,'=',c//b-a)
print ('Default Order:\t', c ,'// (' ,b,'-',a,') =',c//(b-a))

# addition and remainder 
print ('\nDefault Order:\t', c ,'%' ,a,'+',b,'=',c%a+b)
print ('Default Order:\t', c ,'%' ,a,'+',b,'=',c%(a+b))


# addition and exponential (**)
print ('\nDefault Order:\t', c ,'**' ,a,'+',b,'=',c**a+b)
print ('Default Order:\t', c ,'**' ,a,'+',b,'=',c**(a+b))
