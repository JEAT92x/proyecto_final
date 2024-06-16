class Pedido:
    """
    Clase para el manejo de pedidos.
    """
    def __init__(self):
        """
        Inicializa la Estructura de Datos para Almacenar los Pedidos.
        """
        self.pedidos = {}
    
    def crear_pedido(self, num_pedido, cliente, producto, precio):
        """Crea un Nuevo Pedido y lo Agrega al Rrgistro de Pedidos.

        Args:
            num_pedido (int): Número Único de Identificación del Pedido.
            cliente (str): Nombre del Cliente que Realizó el Pedido.
            producto (str): Nombre del Producto Solicitado.
            precio (float): Precio del Producto.
            
        Returns:
            None
        """
        self.pedidos[num_pedido] = {
            "Cliente": cliente,
            "Producto": producto,
            "Precio": precio
        }
        
    def cancelar_pedido(self, num_pedido):
        """
        Cancela un Pedido Existente y lo Elimina del Registro de Pedidos.

        Args:
            num_pedido (int): Número Único de Identificación del Pedido a Cancelar.
            
        Returns:
            None
        """
        if num_pedido in self.pedidos:
            del self.pedidos[num_pedido]
            print("Pedido Cancelado Correctamente.")
        else:
            print("El Pedido Especificado No Existe.")