class Carro:
    def __init__(self,request):
        self.request = request  # Almacena el objeto request que contiene la petición HTTP.
        self.session = request.session  # Accede a la sesión del usuario a través del request.
        carro = self.session.get("carro") # Intenta obtener el carrito de la sesión
        if not carro:
            carro = self.session["carro"]={} # Si no existe el carrito en la sesión, lo crea como un diccionario vacío
        # else: 
        self.carro = carro  # Si ya existe el carrito, lo asigna a la variable de instancia self.carro
    
    def agregar (self, producto):   
        if (str(producto.id) not in self.carro.keys()):  #Convierte el id del producto en una cadena y verifica si esa clave ya existe en el carrito (self.carro), que es un diccionario
            self.carro[producto.id]={
                "producto_id" : producto.id,
                "nombre" : producto.nombre,
                "contenido" : producto.contenido,
                "precio" : str(producto.precio),
                "imagen" : producto.imagen.url,
                "cantidad" : 1,
                
                #imagen" : producto.imagen.url,
                }
        else:
            for key, value in self.carro.items(): #Se recorre el diccionario self.carro para buscar el producto cuyo ID coincide
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+float(producto.precio)
                    break
        self.guardar_carro()

    def guardar_carro(self):    #Después de agregar o actualizar el producto, llama a la función guardar_carro para guardar el carrito en la sesión.
        self.session["carro"]=self.carro    #Almacena el diccionario self.carro en la sesión del usuario bajo la clave "carro". Esto permite que el carrito persista entre solicitudes HTTP.
        self.session.modified=True  #Al marcar la sesión como modificada, se asegura que Django guarde los cambios en la sesión. Esto es necesario porque las sesiones no se guardan automáticamente a menos que se detecten cambios.

    def eliminar(self, producto):
        producto.id=str(producto.id)    #Convertir el ID del producto a cadena
        if producto.id in self.carro:   #Verificar si el producto está en el carrit
            del self.carro[producto.id] #Eliminar el producto del carrito
            self.guardar_carro()        #Guardar el carrito actualizado

    def restar_producto(self, producto):    
        for key, value in self.carro.items():   #Recorrer el carrito de compras
                if key==str(producto.id):   #Buscar el producto en el carrito
                    value["precio"]=float(value["precio"])-float(producto.precio)  #Reducir el precio del producto en el carrito
                    value["cantidad"]=value["cantidad"]-1   #Reducir la cantidad del producto en el carrito
                    if value["cantidad"]<1:     #Eliminar el producto si su cantidad es menor que 1
                        self.eliminar(producto)
                    break
        self.guardar_carro()    #Guardar el carrito actualizado

    def limpiar_carro(self):
        self.session["carro"]={}    #Vaciar el carrito
        self.session.modified=True  #Al marcar la sesión como modificada


    