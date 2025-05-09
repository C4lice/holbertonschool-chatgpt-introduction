#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Il manquait cette ligne
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <nombre_entier_positif>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError("Le nombre doit être positif.")
    except ValueError as e:
        print("Erreur :", e)
        sys.exit(1)

    f = factorial(num)
    print(f)
