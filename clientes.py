class Cliente:
    """
    Clase para el Manejo de los Clientes
    """
    def __init__(self):
        """
        Inicializa la Estructura de Datos del Cliente.
        """
        self.clientes = {}
    
    def agregar_cliente(self, clave, nombre, direccion, correo, telefono):
        """
        Agrega un Nuevo Cliente con Toda La Nueva Información

        Args:
            clave (int): La Clave del Cliente.
            nombre (str): El Nombre del Cliente.
            direccion (str): La Dirección del Cliente.
            correo (str): El Correo del Cliente.
            telefono (str): El Tel{efono} del Cliente.
            
        Returns:
            None
        """
        self.clientes[clave] = {
            "Nombre": nombre,
            "Dirección": direccion,
            "Correo": correo,
            "Teléfono": telefono
        }
        
    def eliminar_cliente(self, clave):
        """
        Elimina un Cliente Existente.

        Args:
            clave (int): La Clave Existente del Cliente.
        """
        if clave in self.clientes:
            del self.clientes[clave]
            print("Cliente Eliminado Correctamente.")
        else:
            print("La Clave del Cliente No Existe.")
            
    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo=None, telefono=None):
        """
        Actualiza un Cliente y su Infomración Existente.

        Args:
            clave (int): La Clave Existente del Cliente que se Actualizará.
            nombre (str, optional): El Nombre Existente del Cliente que se Actualizará. Defaults to None.
            direccion (str, optional): La Dirección Existente del Cliente que se Actualizará. Defaults to None.
            correo (str, optional): El Correo Existente del Cliente que se Actualizará. Defaults to None.
            telefono (str, optional): El Teléfono Existente del Cliente que se Actualizará. Defaults to None.
        """
        if clave in self.clientes:
            if nombre:
                self.clientes[clave]["Nombre"] = nombre
            if direccion:
                self.clientes[clave]["Dirección"] = direccion
            if correo:
                self.clientes[clave]["Correo"] = correo
            if telefono:
                self.clientes[clave]["Teléfono"] = telefono
            print("Cliente Actualizado Correctamente.")
        else:
            print("La Clave del Cliente No Existe.")