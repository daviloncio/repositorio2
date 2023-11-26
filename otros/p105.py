import numpy as np
def root_bracket(f: callable, a: float, b: float, delta=1.)-> tuple:
    '''
    Summary: 
        Mediante un paso delta vamos avanzando en el intervalo desde a hasta b, comprobando en cada iteración que f(a) y f(x) tienen
        el mismo signo. Cuando esta condición no se cumpla, por el teorema de Bolzano, si tenemos un intervalo (a,x) en una función
        continua donde f(a) y f(x) tienen distinto signo, entonces en dicho intervalo tenemos un raíz. Será en este momento cuando 
        devolvamos el intervalo (a,x). En caso de que x se haya salido del intervalo y no se haya dado dicha condición, devolveremos
        (-np.inf,np.inf).
    
    Args: 
        - f (callable):función en la que se define nuestro intervalo
        - a (float): ordenada x donde empieza nuestro intervalo
        - b (float): ordenada x donde finaliza nuestro intervalo, debe ser mayor que a
        - delta (float): paso que definimos para avanzar en la búsqueda de la raíz, debe ser mayor que 0.
    
    Return: 
        - (a,x) (tuple[float, float]):
            -a: ordenada x donde empieza nuestro intervalo
            -x: ordenada x donde acaba nuestro intervalo, será menor o igual que b.
    '''

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
    '''
    Summary:
        Entramos en un bucle donde cogeremos el punto medio (m) del intervalo y calculamos f(m). 
        Si el módulo valor es menor que tol devolvemos m y el nº de interaciones que se han ejecutado. 
        Si aún no se ha dado esta condición debemos quedarnos un nuevo intervalo para la siguiente iteración.
        Por el teorema de Bolzano, si f(a) y f(m) tienen distinto signo, tnedremos dentro una raíz y por tanto
        nos quedamos con el intervalo (a,b=mediatriz). Sino nos quedaremos con (a=mediatriz,b).
    
    Args:
        - f (callable):función en la que se define nuestro intervalo
        - a (float): ordenada x donde empieza nuestro intervalo
        - b (float): ordenada x donde finaliza nuestro intervalo, debe ser mayor que a
        - tol (float): valor cercano a 0 a partir del cual nos saldremos del bucle ya que consideramos que estamos sufientemente próximos a la raíz. 
            El proceso se detendrá cuando el módulo de f(m) sea menor o igual a tol.
        - maxiter (int): número máximo de ejecuciones a hacer en el proceso de búsqueda. Si se supera devolvemos una excepción. 
        
    Returns:
        - (mediatriz,nit) (tuple[float, int]):
            - mediatriz: punto x donde se encuentra la raíz.
            - nit: número de iteraciones realizadas hasta llegar a la raíz.
        
    '''
    nit = 0

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
    
    raise Exception('Se ha superado el número máximo de iteraciones')
    


def regula_falsi(f: callable, a: float, b: float, tol=0.001, maxiter=100)-> tuple[float, int]:
    """
    Summary:
        Regular_falsi es un método para la obtención de una raíz de una función que ya sabemos que tiene en un intervalo dado.
        Primero calculamos el punto x_new que gráficamente sería el punto que genera la recta que une los puntos f(a) y f(b) del 
        bracket al cortar el eje x. A continuación, comprobamos si en este punto hay una raíz. Si es así devolvemos 
        (x_new, nit). Sino, comprobamos si f_a*f_x_new es mayor que cero. Si esto se cumple, entonces el nuevo intervalo
        de busqueda estaría entre x_new y b. En caso de que no se cumpliera el nuevo intervalo estaría formado por a y x_new.
        Repetimos este proceso hasta que se encuentre la raíz o el número máximo de iteraciones se supere.

    Argumentos de entrada:
        - f (callable): funcion de la que queremos encontrar su raíz.
        - a (float): inicio del bracket de f donde buscaremos una raíz.  
        - b (float): final del bracket de f donde buscaremos una raíz. 
        - tol (float): tolerancia
        - maxiter (int): Número máximo de iteraciones que se pueden efectuar para llegar a la raíz de f.

    Returns:
        - (r, nit) (tuple[float, int]): 
            - r: raíz aproximada de la función f. Se tiene que cumplir: f(r)<=tol.
            - nit: número de iteraciones efectuadas para llegar a r.
        
    """
    nit = 0
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

    raise Exception('Se ha superado el número máximo de iteraciones')
            

def secant(f: callable, a: float, b: float, tol=0.001, maxiter=100)-> tuple[float, int]:
    """
    Summary:
        Secant es un método para la obtención de una raíz de una función en un intervalo dado.
        Primero calculamos el punto x_new que gráficamente sería el punto que genera la recta que une los puntos f(a) y f(b) del 
        bracket al cortar el eje x. A continuación, cambiamos el valor de a por el de b y el de b por x_new. 
        Repetimos este proceso hasta que se encuentre la raíz o el número máximo de iteraciones se supere.

    Args:
        - f (callable): funcion de la que queremos encontrar su raíz.
        - a (float): inicio del bracket de f donde buscaremos una raíz.  
        - b (float): final del bracket de f donde buscaremos una raíz. 
        - tol (float): tolerancia
        - maxiter (int): Número máximo de iteraciones que se pueden efectuar para llegar a la raíz de f.

    Returns:
        - (x_new, nit) (tuple[float, int]): 
            - x_new: raíz aproximada de la función f. Se tiene que cumplir: f(x_new)<=tol.
            - nit: número de iteraciones efectuadas para llegar a x_new.
        
    """
    nit = 0
    if b == np.inf:
        return False
    
    f_a=f(a); f_b=f(b)
    pendiente=(f_b-f_a)/(b-a)
    x_new=a-f_a/pendiente
    f_x_new=f(x_new)

    while abs(f_x_new) > tol and nit<= maxiter:
        nit += 1
        if a == b: #Excepción extraña que entramos al hacer algunas pruebas con diversas funciones.
            raise Exception('a y b tiene el mismo valor')
        pendiente=(f_b-f_a)/(b-a)
        x_new=a-f_a/pendiente
        f_x_new=f(x_new)
        a, b=b, x_new
        f_a, f_b = f_b, f_x_new
          
    if abs(f_x_new)<=tol:
        return (x_new,nit)
    
    return
       
def min_bracket(f: callable, x0: float, x2: float, delta=1.)-> tuple[float, float, float, int]:
    """
    Summary: 
        Introducimos una función y un intervalo (x0,x2) en el que buscaremos y devolvermos un mínimo.
        Podemos encontrar dos casos en nuestro algoritmo:
            -Si f(x0)<f(x2) avanzamos desde x0 hacia x2 sumando delta a x1 para encontrar antes el mínimo
            -Si f(x2)<f(x0) retorcedemos desde x2 hacia x1 restando delta a x1 para encontrar antes el mínimo
        En el algoritmo están presentes x1 y next, este último va un paso por delante (o por detrás) de x1.
        Entramos en el while, en el que vamos recorriendo el intervalo, comprobando siempre que x0<=x1<=x2 y 
        que f(next) < f(x1). En caso de que esto último no se cumpla, será porque hemos encontrado un mínimo
        que posteriomente devolveremos. Si en un momento no se cumple que x0<=x1<=x2 significará que x1 se ha
        salido del intervalo y que por tanto no ha encontrado mínimos en este, razón por la que devolverá 
        (-np.inf,np.inf).
    

    Args:
        - f (callable): funcion en la que queremos encontrar uno de sus mínimos.
        - x0 (float): inicio del bracket de f donde buscaremos una raíz.  
        - x2 (float): final del bracket de f donde buscaremos una raíz. 
        - delta(float): paso establecido para recorrer el intervalo en busca de un mínimo.
        

    Returns:
        -(x0, x1, x2, nfev) (tuple[float, float, float, int]):
            -x0: ordenada x donde empieza nuestro intervalo         
            -x1: ordenada x en la que hemos encontrado un mínimo dentro del intervalo (x0,x2)
            -x2: ordenada x donde acaba nuestro intervalo
            -nfev: número de evaluciones de f que efectuamos en el algoritmo
    """
    if x0 > x2:
        raise Exception('a debe de ser menor que b')

    if delta<=0:
        raise Exception('delta debe ser un numero positivo')
    
    def operacion(a, suma:bool):
        if suma:
            return a+delta
        else:
            return a-delta

    if f(x0) < f(x2):
        x1 = x0 ; suma = True  #en este caso avanzamos desde x0 hacia x2 sumando delta
    else:
        x1 = x2 ; suma = False #en este caso retrocedemos desde x2 hacia x1 sumando delta

    next = operacion(x1, suma)
    f_next, f_x1 = f(next), f(x1)

    nfev = 4 # Numero de evaluaciones f efectuada antes de entrar al while.
    while f_next <f_x1 and x0<=x1<=x2: 
        x1, f_x1 = next, f_next 
        next = operacion(next, suma)
        f_next = f(next)
        nfev += 1 # Cada vez que entra en el bucle while hace una evaluación de la funcion f

    if (x0<=x1<=x2)==False:  #se sale del bucle y devuelve (-inf,inf) si no se cumple x0<=x1<=2
        return (-np.inf,np.inf)
    else:
        return (x0, x1, x2, nfev)
    

def trisection(f: callable, bracket: tuple[float, float, float], xtol=0.001, maxiter=100)-> tuple[float, int, int]:
    """
    Summary:
        Trisection es un método para obtener el mínimo de una función en un intervalo dado.
        En este método dividimos el bracket en tres partes iguales. Inicialmente tenemos los puntos x0 y x3, y al 
        hacer la división creamos los puntos x1 y x2. De la forma x0 < x1 < x2 < x3. Se encuentra un mínimo si 
        (x3 - x0) <= xtol, hasta que esto se cumpla o el número máximo de iteraciones se supere, vamos cambiando 
        el intervalo x0 y x3. Si f(x1) < f(x2) entonces x3 = x2, sino xo = x1.
        
    Args:
        - f (callable): Funcion de la que queremos encontrar su mínimo.
        - bracket (tuple[float, float, float]) : Bracket donde sabemos que se encuentra un mínimo de la función. 
        - xtol (float): Tolerancia
        - maxiter (int): Número máximo de iteraciones que se pueden efectuar para llegar a la raíz de f.

    Returns:
        - (x, iter, nfev) (tuple[float, int]): 
            - x: Valor x donde hay un mínimo.
            - iter: Número de iteraciones efectuadas para llegar a x.
            - nfev: Número de evaluaciones de fucunción realizadas. Que es igual a 2*iter.
        
    """
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
        

def golden(f: callable, bracket: tuple[float, float, float], xtol=0.001, maxiter=100)-> tuple[float, int, int]:
    """
    Summary:
        Golden es un método para obtener el mínimo de una función en un intervalo dado usando la razón áurea.
        En este método dividimos el bracket en tres partes iguales con ayuda de la razón áurea. Inicialmente tenemos 
        los puntos x0 y x3, y al hacer la división creamos los puntos x1 y x2. De la forma x0 < x1 < x2 < x3. 
        Se encuentra un mínimo si (x3 - x0) <= xtol, hasta que esto se cumpla o el número máximo de iteraciones 
        se supere, vamos cambiando el intervalo x0 y x3. Si f(x1) < f(x2) entonces x3 = x2, sino xo = x1.
        
    Args:
        - f (callable): Funcion de la que queremos encontrar su mínimo.
        - bracket (tuple[float, float, float]) : Bracket donde sabemos que se encuentra un mínimo de la función. 
        - xtol (float): Tolerancia
        - maxiter (int): Número máximo de iteraciones que se pueden efectuar para llegar a la raíz de f.

    Returns:
        - (x, iter, nfev) (tuple[float, int]): 
            - x: Valor x donde hay un mínimo.
            - iter: Número de iteraciones efectuadas para llegar a x.
            - nfev: Número de evaluaciones de fucunción realizadas. Que es igual a 2*iter.
        
    """
    razon_aurea=1/((1+(5**(1/2)))/2)
    razon_aurea = 1/1.618
    x0,x3=bracket[0],bracket[2]
    
    x2 = x0 + razon_aurea*(x3-x0)
    x1 = x3 - razon_aurea*(x3-x0)
    iter = 0
    while (x3 - x0) > xtol and iter <= maxiter:
        iter += 1

        if f(x1) < f(x2):
            x3 = x2
        else:
            x0 = x1

        x2 = x0 + razon_aurea*(x3-x0)
        x1 = x3 - razon_aurea*(x3-x0)
        

    if (x3 - x0) <= xtol:
        return ((x0+x3)/2, iter, 2*iter)