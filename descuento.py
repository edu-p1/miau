# -*- coding: utf-8 -*-
# decoracion nombre del algoritmo

print("------------------------------------")
print("              oferta                ")
print("------------------------------------")

p= float(input("introduzca el precio de la compra :"))
c = input("introduzca codigo de descuento:")

cc = "NAVIDAD2425"

if c == cc:
    d = p*0.2
    pf = p - d  
    print("tras el descuento el prefio final es:" ,pf,"€" )
else:
    print("el codigo de descuento no es correcto.")
