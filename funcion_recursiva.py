def contarDigitos(cad):
    print(cad)
    if len(cad) == 0:
        return 0
    else:
        c= cad[0]
        if c.isdigit():
            return 1 + contarDigitos(cad[1:])
        else:
            return 0 + contarDigitos(cad[1:])
        
print("c:", contarDigitos("hola175"))