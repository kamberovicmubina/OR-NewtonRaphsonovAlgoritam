from sympy import Symbol, lambdify
import numpy as np
x = Symbol('x')


def NR (f, df, ddf, x0, N, eps):  
    if NR.n < N:
        NR.n += 1
        if np.abs(ddf(x0)) < eps:
            x0 = x0 + 0.5
        xn = x0 - (df(x0) / ddf(x0))        
        if np.abs(f(xn) - f(x0)) < eps:
            return xn       
        return NR(f, df, ddf, xn, N, eps)     
    return x0       

NR.n = 0
f1 = 3*x*x - 1
df1 = f1.diff(x)
ddf1 = df1.diff(x)
f1 = lambdify(x, f1)
df1 = lambdify(x, df1)
ddf1 = lambdify(x, ddf1)
prvaKoordinata1 = NR(f1, df1, ddf1, 1, 100, 0.00001)
print('(x, y) = (',  prvaKoordinata1, ',', f1(prvaKoordinata1), ')')
prvaKoordinata1 = NR(f1, df1, ddf1, 10, 100, 0.00001)
print('(x, y) = (',  prvaKoordinata1, ',', f1(prvaKoordinata1), ')')

NR.n = 0
f2 = -(16*x*x -24*x + 5) * np.e**(-x)
df2 = f2.diff(x)
ddf2 = df2.diff(x)
f2 = lambdify(x, f2)
df2 = lambdify(x, df2)
ddf2 = lambdify(x, ddf2)
prvaKoordinata2  = NR(f2, df2, ddf2, 0.5, 100, 0.00001)
print('(x,y) = (', prvaKoordinata2, ',', f2(prvaKoordinata2), ')')
prvaKoordinata2 = NR(f2, df2, ddf2, 2, 100, 0.00001)
print('(x,y) = (', prvaKoordinata2, ',', f2(prvaKoordinata2), ')')



NR.n = 0
f3 = lambda a: np.sin(a) + np.sin((10/3) * a)
df3 = lambda a: 10*np.cos((10/3)*a)/3 + np.cos(a)
ddf3 = lambda a: -((100/9)*np.sin((10/3)*a)) - np.sin(a)
prvaKoordinata3  = NR(f3, df3, ddf3, 3, 100, 0.00001)
print('(x,y) = (', prvaKoordinata3, ',', f3(prvaKoordinata3), ')')
prvaKoordinata3  = NR(f3, df3, ddf3, 6, 100, 0.00001)
print('(x,y) = (', prvaKoordinata3, ',', f3(prvaKoordinata3), ')')
prvaKoordinata3  = NR(f3, df3, ddf3, 7, 100, 0.00001)
print('(x,y) = (', prvaKoordinata3, ',', f3(prvaKoordinata3), ')')


NR.n = 0
f4 = np.e**(-x)
df4 = f4.diff(x)
ddf4 = df4.diff(x)
f4 = lambdify(x, f4)
df4 = lambdify(x, df4)
ddf4 = lambdify(x, ddf4)
prvaKoordinata4  = NR(f4, df4, ddf4, 1, 100, 0.00001)
print('(x,y) = (', prvaKoordinata4, ',', f4(prvaKoordinata4), ')')
prvaKoordinata4  = NR(f4, df4, ddf4, 10, 100, 0.00001)
print('(x,y) = (', prvaKoordinata4, ',', f4(prvaKoordinata4), ')')
































