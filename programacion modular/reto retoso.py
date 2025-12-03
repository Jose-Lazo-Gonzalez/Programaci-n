ventas = [
    ["Portátil", 150, 799.99, 4.5],
    ["Smartphone", 250, 599.99, 4.3],
    ["Auriculares", 400, 49.99, 4.0],
    ["Tablet", 120, 299.99, 3.9],
    ["Monitor", 180, 199.99, 4.2],
    ["Smartwatch", 220, 149.99, 4.1],
    ["Teclado mecánico", 300, 89.99, 4.4],
    ["Ratón gaming", 350, 59.99, 4.0],
    ["Cámara digital", 90, 999.99, 4.6],
    ["Consola", 200, 399.99, 4.7]
]
lista=[]
def getProducto (a,ventas):
    i=0
    producto =[]
    
    encontrado = False
    while i< len(ventas) and not encontrado:
        if ventas[i][0]==a:
            encontrado= True
            producto = ventas[i]
        
        else:
            i+=1
    return producto


a=input("dime el producto que quieres buscar:")
print (getProducto(a,ventas))

def calcularingreso (ventas):
    resultado=(getProducto(a,ventas)[1])*(getProducto(a,ventas)[2])
    return resultado

print (calcularingreso (ventas))

def producto_destacado(ventas,getProducto):
    if getProducto(a, ventas)[3]>=4.2:
        destacado=True
    else:
        destacado=False
    return destacado
print (producto_destacado(ventas,getProducto))

def getProductosDestacados(ventas):
    listadestacada=[]
    for i in ventas:
        if producto_destacado(ventas,ventas[i])==True:
            listadestacada.append(getProducto)
    return listadestacada
print (getProductosDestacados(ventas))
