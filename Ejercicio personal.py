#Vamos a buscar patrones en el 7

def buscar_patrones_en_el_7():
    for i in range(1, 200):
        if i % 7 == 0:
            totalNumero = 0
            for numero in str(i):
                totalNumero += int(numero)
            print(f"El numero es: {i} y la suma de sus digitos es: {totalNumero}")
            
buscar_patrones_en_el_7()