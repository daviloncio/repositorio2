import numpy as np

def funcion(x):
    return x**2-3*x-1
def funcion2(x):
    return x**2+4*x-6
def funcion3(x):
    return x**3+ 2*x**2 +10*x -20
def funcion4(x):
    return 0.5 + -(x + np.sin(x)) * np.exp(-x**2.0)
def x_sin_exp(x):
    return 0.5 -(x + np.sin(x)) * np.exp(-x**2.0) 
    
    

def root_bracket(f: callable, a: float, b: float, delta=1.)-> tuple:
    '''
    Summary: 
    Mediante un paso delta vamos avanzando en el intervalo desde a hasta b, comprobando en cada iteración que f(a) y f(x) tienen
    el mismo signo. Cuando esta condición no se cumpla, por el teorema de Bolzano, si tenemos un intervalo (a,x) en una función
    continua donde f(a) y f(x) tienen distinto signo, entonces en dicho intervalo tenemos un raíz. Será en este momento cuando 
    devolvamos el intervalo (a,x). En caso de que x se haya salido del intervalo y no se haya dado dicha condición, devolveremos
    (-np.inf,np.inf).
    
    Args: 
    f:función en la que se define nuestro intervalo
    a: ordenada x donde empieza nuestro intervalo
    b: ordenada x donde finaliza nuestro intervalo, debe ser mayor que a
    delta: paso que definimos para avanzar en la búsqueda de la raíz, debe ser mayor que 0
    f debe ser de tipo callable y el resto int o float'''
    if a > b:
        raise Exception('a debe de ser menor que b')
    if delta<=0:
        raise Exception('delta debe ser un numero positivo')
    x = a + delta
    f_a = f(a)

    while f_a*f(x)>0:
        
        if x > b:
            return (-np.inf,np.inf)
        x += delta
    return (a,x)



def bisection(f: callable, a: float, b: float, tol=0.001, maxiter=100)-> tuple[float, int]:
    '''Args: En primer lugar comprobamos con root_bracket que nuestro intervalo tiene al menos una raíz.
    Si es así entraremos en un bucle donde cogeremos el punto medio (m) del intervalo y calculamos f(m). 
    Si el módulo valor es menor que tol devolvemos m y el nº de interaciones que se han ejecutado. 
    Si aún no se ha dado esta condición debemos quedarnos un nuevo intervalo para la siguiente iteración.
    Por el teorema de Bolzano, si f(a) y f(m) tienen distinto signo, tnedremos dentro una raíz y por tanto
    nos quedamos con el intervalo (a,b=mediatriz). Sino nos quedaremos con (a=mediatriz,b).
    
    f:función en la que se define nuestro intervalo
    a: ordenada x donde empieza nuestro intervalo
    b: ordenada x donde finaliza nuestro intervalo, debe ser mayor que a
    tol: valor cercano a 0 a partir del cual nos saldremos del bucle ya que consideramos que estamos
    sufientemente próximos a la raíz. El proceso se detendrá cuando el módulo de f(m) sea menor o igual a tol.
    maxiter: número máximo de ejecuciones a hacer en el proceso de búsqueda. Si se supera devolvemos una excepción.
    f debe ser de tipo callable, a y b pueden ser tanto int como float, tol debería ser float y maxiter un entero '''
    nit = 0
    a,b = root_bracket(f,a,b)
    if b == np.inf:
        return False
    f_a=f(a)
    while nit<= maxiter :
        mediatriz=(a+b)/2
        f_m=f(mediatriz)
        nit += 1
        if abs(f_m )<=tol:
            return (mediatriz,nit)
        if f_a*f_m<0:
            b=mediatriz

        else:
            a=mediatriz
            f_a=f_m
        
    raise Exception('se ha superado el número máximo de iteraciones')
    


def regula_falsi(f: callable, a: float, b: float, tol=0.001, maxiter=100)-> tuple[float, int]:
    nit = 0
    a,b = root_bracket(f,a,b)
    if b == np.inf:
        return False
    f_a=f(a); f_b=f(b)

    while nit<= maxiter:
        nit +=1
        pendiente=(f_b-f_a)/(b-a)
        x_new=a-f_a/pendiente
        f_x_new=f(x_new)
        if abs(f_x_new)<=tol:
            return (x_new,nit)
        if f_a*f_x_new>0:
            a,f_a=x_new,f_x_new
        else:
            b,f_b=x_new,f_x_new
            

def secant(f: callable, a: float, b: float, tol=0.001, maxiter=100)-> tuple[float, int]:
    nit = 0
    a,b = root_bracket(f,a,b)
    if b == np.inf:
        return False
    f_a=f(a); f_b=f(b)
    pendiente=(f_b-f_a)/(b-a)
    x_new=a-f_a/pendiente
    f_x_new=f(x_new)
    while abs(f_x_new) > tol and nit<= maxiter:
        nit += 1
        if a == b:
            print(nit)
            raise Exception('a y b tiene el mismo valor')
        pendiente=(f_b-f_a)/(b-a)
        x_new=a-f_a/pendiente
        f_x_new=f(x_new)
        a, b=b, x_new
        f_a, f_b = f_b, f_x_new
        
        
    if abs(f_x_new)<=tol:
        return (x_new,nit)
    
    if nit>maxiter:
        return a,b
       
def min_bracket(f: callable, x0: float, x2: float, delta=1.)-> tuple[float, float, float, int]:
    if x0 > x2:
        raise Exception('a debe de ser menor que b')

    if delta<=0:
        raise Exception('delta debe ser un numero positivo')
    
    def operacion(a, suma:bool):
        if suma:
            return a+delta
        else:
            return a-delta
    def comprobacion_fuera_del_intervalo(x1,suma):  
        if suma==True:#devuelve false si nos hemos salido del intervalo y se acaba el while
            return x1<x2
        else:
            return x0<x1
    if f(x0) < f(x2):
        x1 = x0 ; suma = True
    else:
        x1 = x2 ; suma = False

    next = operacion(x1, suma)
    f_next, f_x1 = f(next), f(x1)

    nfev = 4 # Numero de evaluaciones f efectuadas. Antes de entrar al while ya hemos hecho 4.
    while f_next <f_x1 and comprobacion_fuera_del_intervalo(x1,suma): #or --> solo es False si los dos son False.
        x1, f_x1 = next, f_next 
        next = operacion(next, suma)
        f_next = f(next)
        nfev += 1 # Cada vez que entra en el bucle while hace una evaluación de la funcion f

    if f(next)<f(x1): #si esto es True lo que no se está cumpliendo es (x1<x2 or x1>x0), por lo que no hay mínimo.
        return (-np.inf,np.inf)  #david:este if lo quitaría, sale ínf,inf sin pasar por aquí.
    else:
        return (x0, x1, x2, nfev)
    

def trisection(f: callable, bracket: tuple[float, float, float], xtol=0.001, maxiter=100)-> tuple[float, int, int]:
    x0, x3 = bracket[0], bracket[2]
    x1 = x0 + 1/3*(x3-x0)
    x2 = x3 - 1/3*(x3-x0)
    iter = 0
    while (x3 - x0) > xtol and iter <= maxiter:
        iter += 1

        if f(x1) < f(x2):
            x3 = x2
        else:
            x0 = x1

        x1 = x0 + 1/3*(x3-x0)
        x2 = x3 - 1/3*(x3-x0)
        

    if (x3 - x0) <= xtol:
        return ((x0+x3)/2, iter, 2*iter)
    
    else:
        return 
        

def golden(f: callable, bracket: tuple[float, float, float], xtol=0.001, maxiter=100)-> tuple[float, int, int]:
    razon=1/(1+np.roots(5)/2)
    x0,x2=bracket[0],bracket[2]
    
    x1 = x0 + razon*(x3-x0)
    x2 = x3 - razon*(x3-x0)
    iter = 0
    while (x3 - x0) > xtol and iter <= maxiter:
        iter += 1

        if f(x1) < f(x2):
            x3 = x2
        else:
            x0 = x1

        x1 = x0 + razon*(x3-x0)
        x2 = x3 - razon*(x3-x0)
        

    if (x3 - x0) <= xtol:
        return ((x0+x3)/2, iter, 2*iter)
    
    else:
        return 