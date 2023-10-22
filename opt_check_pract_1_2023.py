#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
import textwrap

import numpy as np

#import autograd.numpy as anp  
#from autograd import grad

import p105 as p1

####################################### main
def f(x):
    return -x * np.sin(x) + 1.

def df(x):
    return -x * np.cos(x) - np.sin(x)

def main(tol: float):
    """Comprobador de practica 1.
    
    Comprueba: 
    * bracketing de ceros
    * ceros mediante bisect, regula falsi, secante
    * bracketing de mínimos
    * mínimos medainte trisección y golden
    
    Args: 
        tol: tolerancia para ceros
        
    Returns:
        None
    """
    
    ##### check roots
    a, b = -3., 0.
    
    print(30*'_' + "Checking bracketing de ceros")
    
    print('\t sobre una función dada, se genera un bracket sobre un intervalo inicial' +
          '\n\t y se comprueba que en efecto lo es')
    
    x0, x1 = p1.root_bracket(f, a=a, b=b, delta=.1)
    if f(x0) * f(x1) >= 0.:
        print("not a bracket")
    else: 
        print("bracket ok")
    
    print(x0, x1)
    
    _ = input("\npulsar Intro para continuar " + 20*'.' + "\n")
    
    print(30*'_' + "Checking búsqueda de ceros con bisect, regula falsi y secante")
    
    print('\t sobre la función y bracket anteriores, se aplican estos métodos' +
          '\n\t y se comprueba que devuelven ceros con la tolerancia fijada')
          
    r, nit = p1.bisection(f, x0, x1, tol=tol, maxiter=1000)
    if np.abs(f(r)) > tol:
        print("bisect: not a root")
        print(np.abs(f(r)), nit)
    else: 
        print("bisect ok")
        print('\tf at root', f(r))
    
    r, nit = p1.regula_falsi(f, x0, x1, tol=tol, maxiter=1000)
    if np.abs(f(r)) > tol:
        print("regula: not a root")
        print(np.abs(f(r)), nit)
    else: 
        print("regula ok")
        print('\tf at root', f(r))
    
    r, nit = p1.secant(f, x0, x1, tol=tol, maxiter=1000)
    if np.abs(f(r)) > tol:
        print("secant: not a root")
        print(np.abs(f(r)), nit)
    else: 
        print("secant ok")
        print('\tf at root', f(r))
    
    _ = input("\npulsar Intro para continuar " + 20*'.' + "\n")
    
    ##### check minima
    a, b = -3., 0.
    
    print(30*'_' + "Checking bracketing de mínimos")
    
    print('\t sobre la función se genera un bracket de mínimos sobre un intervalo inicial' +
          '\n\t y se comprueba que en efecto es un tal bracket')
          
    x0, x1, x2, _ = p1.min_bracket(f, a, b, delta=0.1)
    if f(x0) > f(x1) and f(x2) > f(x1):
        print("min bracket ok")
    else: 
        print("not a min bracket")
    
    _ = input("\npulsar Intro para continuar " + 20*'.' + "\n")
    
    print(30*'_' + "Checking búsqueda de mínimos con trisección y golden search")
    
    print('\t sobre la función y bracket anteriores, se aplican estos métodos' +
          '\n\t y se comprueba que devuelven mínimos adecuados')
    #check this con autograd para la derivada 
    x, _, _ = p1.trisection(f, (x0, x1, x2), xtol=tol, maxiter=100)
    
    if np.abs(df(x)) > 10. * tol:
        print("trisection: not a min")
        print(np.abs(df(x)))
    else: 
        print("trisection ok")
        print('\tder at min', df(x))
        
    x, _, _ = p1.golden(f, (x0, x1, x2), xtol=tol, maxiter=100)
    
    if np.abs(df(x)) > 10. * tol:
        print("golden: not a min")
        print(np.abs(df(x)))
    else: 
        print("golden ok")
        print('\tder at min', df(x))
        
        
###############################################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
        """
        Comprobador de la práctica 1. 
        
        Comprueba: 
            * bracketing de ceros
            * ceros mediante bisect, regula falsi, secante
            * bracketing de mínimos
            * mínimos medainte trisección y golden
    
        Args: 
            tol: tolerancia para ceros
    
        Ejecutar por ejemplo en Linux como 
        
            ./opt_check_pract_1_2023.py -t 1.e-3 
            
        y en Windows como 
        
            python opt_check_pract_1_2023.py -t 1.e-3
        """))
    
    #parser.add_argument("-p", "--pareja", type=str, default=None)
    parser.add_argument("-t", "--tol", help="tolerancia para búsqueda de ceros; default=1.e-3", type=float, default=1.e-3)
    
    args = parser.parse_args()
    
    if len(sys.argv) > 1:
        import p105 as p1 
            
        main(args.tol)
    
    else:
        parser.print_help()
            
        