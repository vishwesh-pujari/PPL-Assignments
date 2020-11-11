/**/

student(s1, comp).
student(s1, math).
student(s2, comp).
student(s2, math).
student(s3, comp).
student(s3, math).
student(s4, entc).
student(s4, math).
student(s5, entc).
student(s5, math).
student(s6, elec).
student(s6, math).
student(s7, elec).
student(s7, math).
student(s8, instru).
student(s8, math).

teacher(t1, math).
teacher(t2, math).
teacher(t3, ppl).
teacher(t4, dsgt).
teacher(t5, dld).
teacher(t6, dld).

dept(math, math).
dept(ppl, comp).
dept(dsgt, comp).
dept(dld, comp).

has_subject(X, Y):- student(X,S), dept(Y, S).
has_teacher(X, Y):- student(X, S), dept(P, S), teacher(Y,P).
