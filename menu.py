class Menu:
    """
    Clase para el Manejo del Menú
    """
    def __init__(self):
        """
        Inicializa la Estructura de Datos del Menú.
        """
        self.menu = {}
        
    def agregar_producto(self, clave, nombre, precio):
        """
        Agrega un Nuevo Producto con Toda La Nueva Información.

        Args:
            clave (int): La Clave del Producto.
            nombre (str): El Nombre del Producto.
            precio (float): El Precio del Producto.
            
        Returns:
            None
        """
        self.menu[clave] = {
            "Nombre": nombre,
            "Precio": precio
        }
        
    def eliminar_producto(self, clave):
        """
        Elimina un Producto Existente.

        Args:
            clave (int): La Clave Existente del Prodcuto.
            
        Returns:
            None
        """
        if clave in self.menu:
            del self.menu[clave]
            print("Producto Eliminado Correctamente.")
        else:
            print("La Clave del Producto No Existe.")
            
    def actualizar_producto(self, clave, nombre=None, precio=None):
        """
        Actualiza un Producto y su Infomración Existente.

        Args:
            clave (int): La Clave Existente del Producto que se Actualizará.
            nombre (str, optional): El Nombre Existente del Producto que se Actualizará. Defaults to None.
            precio (float, optional): El Precio Existente del Producto que se Actualizará. Defaults to None.
        """
        if clave in self.menu:
            if nombre:
                self.menu[clave]["Nombre"] = nombre
            if precio:
                self.menu[clave]["Precio"] = precio
            print("Producto Actualizado Correctamente.")
        else:
            print("La Clave del Producto No Existe.")