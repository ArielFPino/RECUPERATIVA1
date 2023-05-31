vEntnino=5500
vEntjov=7000
vEntadult=9000
vTotalnino=0
vTotaljov=0
vTotaladult=0
sw=1
total1=0
total2=0
total3=0
decision=0
while sw==1:
    try:
        VOp=int(input("Ingrese tipo de entrada: \n1.- Niño (1 a 13 años)\n2.- Jóven (14 a 21 años)\n3.- Adulto (Mayor a 22)\n4.- Salir\nDigite: "))
        if VOp==1:
            total=vEntnino
            cantent=int(input(f"El precio de su entrada es de ${vEntnino} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total*=cantent
            vTotalnino+=cantent
            print(f"======BOLETA======\nCategoría: Niño\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total1=total
            print("Gracias por su compra, disfrute la función.")
        if VOp==2:
            total=vEntjov
            cantent=int(input(f"El precio de su entrada es de ${vEntjov} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total*=cantent
            vTotaljov+=cantent
            print(f"======BOLETA======\nCategoría: Jóven\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total2=total
            print("Gracias por su compra, disfrute la función.")
        if VOp==3:
            total=vEntadult
            cantent=int(input(f"El precio de su entrada es de ${vEntadult} pesos, ¿Cuántas entradas desea comprar?\nDigite: "))
            total*=cantent
            vTotaladult+=cantent
            print(f"======BOLETA======\nCategoría: Adulto\nCantidad de entradas: {cantent}\nTotal a pagar: ${total} pesos")
            total3=total
            print("Gracias por su compra, disfrute la función.")
        if VOp==4:
            sw=0
        totalent=(vTotalnino+vTotaljov+vTotaladult)
        vtotaltodo= total1+total2+total3
        print(f"La cantidad de entradas de categoría \"Niño\" vendidas es: {vTotalnino} ({((vTotalnino*1.00)//totalent)}% de las entradas totales.)")
        print(f"La cantidad de entradas de categoría \"Jóven\" vendidas es: {vTotaljov} ({((vTotaljov*100)//totalent)}% de las entradas totales.)")
        print(f"La cantidad de entradas de categoría \"Adulto\" vendidas es: {vTotaladult} ({((vTotaladult*100)//totalent)}% de las entradas totales.)")
        print(f"Total de ganancias del día: ${vtotaltodo} pesos")
    except ValueError:
        print("Incorrecto")