print ("------------ejercicio numero 8:-------------")

precio = input("el precio del producto es: ")
print(precio[:precio.find(".")], "euros y ", precio[precio.find(".")+1:], "centimos")

print ("------------ejercicio numero 10:-------------")

productos = input("sus productos, separados por comas, de la compra son: ")
print(productos.replace(",", "\n"))