from flask import Flask, render_template, request
from clientes import Cliente
from menu import Menu
from pedidos import Pedido
import sqlite3

# Crear una Instancia de la Clase Cliente
gestor_clientes = Cliente()

# Agregar un Cliente
gestor_clientes.agregar_cliente("001", "Juan González", "Calle 123", "juan@example.com", "1112131415")

# Actualizar un Cliente
gestor_clientes.actualizar_cliente("001", nombre="Juan Gonzálo Pérez García", direccion="Calle 12345", correo="juangzz@sample.com", telefono="12345678910")

# Eliminar un Cliente
gestor_clientes.eliminar_cliente("001")



# Crear una Instancia de la Clase Menu
gestor_menu = Menu()

# Agregar un Producto al Menú
gestor_menu.agregar_producto("001", "Hamburguesa", 5.99)

# Actualizar un Producto en el Menú
gestor_menu.actualizar_producto("001", nombre="Hamburguesa con Queso y Papas", precio=8.66)

# Eliminar un Producto del Menú
gestor_menu.eliminar_producto("001")



# Crear una Instancia de la Clase Pedido
gestor_pedidos = Pedido()

# Crear un Nuevo Pedido
gestor_pedidos.crear_pedido(1, "Miguel Alberto Castanos Alavárez", "Hamburguesa", 5.99)

# Cancelar un Pedido Existente
gestor_pedidos.cancelar_pedido(1)




def calcular_costo_producto():
    nombre_producto = input("Ingresar el Nombre del Producto: ")
    precio_producto = float(input("Ingresar el Precio del Producto: "))
    unidades = int(input("Ingresar la Cantidad de Unidades a Solicitar: "))
    
    costo_total = precio_producto*unidades
    
    print("\nSimulación de Pedido:")
    print(f"Producto: {nombre_producto}")
    print(f"Precio: por Unidad: ${precio_producto}")
    print(f"Unidades: {unidades}")
    print(f"Costo Total: ${costo_total}")
    
def main():
    opcion=""
    
    while opcion !="4":
        imprimir_menu()
        opcion =  input("Escribe Una Opción: ")
        
        if(opcion == 1):
            print("Elegiste la Opción Pedidos")
        elif(opcion == 2):
            print("elegiste la Opción Clientes")
        elif(opcion == 3):
            print("elegiste la Opción Menú")
        elif(opcion == 4):
            print("Elegiste la Opción Salir")
            print("Saliendo del Programa...")
        else:
            print("No Elegiste Una Opcíon Valida")
            
def imprimir_menu():
    print("\nEl Menú: ")
    print("1. Pedidos")
    print("2. Clientes")
    print("3. Menú")
    print("4. Salir")

if __name__ == "__main__":
    main()




class BaseDeDatos:
    def __init__(self, nombre_archivo):
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()
    
    def crear_tablas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                            clave TEXT PRIMARY KEY,
                            nombre TEXT,
                            direccion TEXT,
                            correo TEXT,
                            telefono TEXT) ''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Menu (
                            clave TEXT PRIMARY KEY,
                            nombre TEXT,
                            precio REAL) ''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                            num_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                            cliente TEXT,
                            producto TEXT,
                            precio REAL) ''')
        
    def cerrar_conexion(self):
        self.conexion.commit()
        self.conexion.close()
    

 # Implementando Métodos para Agregar, Actualizar y Eliminar Clientes
class Cliente:
    def __init__(self, db):
        self.db = db
        
    def agregar_cliente(self, clave, nombre, direccion, correo, telefono):
        self.db.cursor.execute("INSERT INTO Clientes VALUES (?,?,?,?,?)", (clave, nombre, direccion, correo, telefono))
        
    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo=None, telefono=None):
        self.db.cursor.execute("UPDATE Clientes SET clave = 005, nombre = 'Juan Gonzálo Pérez Garcia', direcion = 'Calle 12345', correo = 'juan@example.com', telefono = '12345678910'  WHERE clave = 001, nombre = 'Juan González', direccion = 'Calle 123', correo = 'juangzz@sample.com', telefono = '1112131415' "
                               , (clave, nombre, direccion, correo, telefono))
        
    def eliminar_cliente(self, clave):
        self.db.cursor.execute("DELETE FROM Clientes WHERE clave = 001", (clave))

# Implementando Métodos para Agregar, Actualizar y Eliminar Productos
class Menu:
    def __init__(self, db):
        self.db = db
        
    def agregar_producto(self, clave, nombre, precio):
        self.db.cursor.execute("INSERT INTO Menu VALUES (?,?,?,?,?)", (clave, nombre, precio))
    
    def actualizar_producto(self, clave, nombre=None, precio=None):
        self.db.cursor.execute("UPDATE Menu SET clave = 008, nombre= 'Hamburguesa con Queso y Papas', precio = 8.66 WHERE clave = 001, nombre = 'Hamburguesa', precio = 5.99"
                               , (clave, nombre, precio))
        
    def eliminar_producto(self, clave):
        self.db.cursor.execute("DELETE FROM Menu WHERE clave = 001", (clave))
    
class Pedido:
    def __init__(self, db):
        self.db = db
        
    def realizar_pedido(self, cliente_clave, producto_clave):
        # Realizar Consulta para Obtener Nombre del Cliente
        self.db.cursor.execute("SELECT nombre FROM Clientes WHERE clave = ?", (cliente_clave,))
        cliente_nombre = self.db.cursor.fetchone()[0]
        
        # Realizar Consulta para Obtener Nombre y Precio del Producto
        self.db.cursor.execute("SELECT nombre, precio FROM Menu WHERE clave = ?", (producto_clave,))
        producto_nombre, producto_precio =self.db.cursor.fetchone()
        
        # Insertar Pedido en la Tabla Pedido
        self.db.cursor.execute("INSERT INTO Pedidos (cliente, producto, precio) VALUES (?,?,?,?,?)", (cliente_nombre, producto_nombre, producto_precio))
        
        self.db.cursor.execute("UPDATE Pedidos SET cliente = 'Miguel Alberto Castanos Alavárez', producto = 'Hamburguesa con Queso y Papas Crisscut', precio = 11.33 WHERE cliente = 'Juan Gonzálo Pérez García', producto = 'Hamburguesa con Queso y Papas', precio = 8.66 "
                               , (cliente_nombre, producto_nombre, producto_precio))
        
        self.db.cursor.execute("DELETE FROM Pedidos WHERE cliente = 'Miguel Alberto Castanos Alavárez' ", (cliente_nombre))
        
        # Guardar Información en Archivo de Texto (Simulación del Ticket)
        with open("ticket.txt", "a") as file:
            file.write(f"Cliente: {cliente_nombre}\n")
            file.write(f"Producto: {producto_nombre}\n")
            file.write(f"Precio: ${producto_precio}\n\n")
            
            
            
# Uso de las Clases y Métodos
app = Flask(__name__)
db = BaseDeDatos("Mi_Base_De_Datos.db")
db.crear_tablas()

cliente = Cliente(db)
cliente.agregar_cliente("001", "Juan González", "Calle 123", "juan@example.com", "1112131415")

menu = Menu(db)
menu.agregar_producto("001", "Hamburguesa", 5.99)

pedido = Pedido(db)
pedido.realizar_pedido("001", "001")

@app.route('/')
def index():
    return render_template('pedido.html')
    return render_template("consulta_pedido.html")

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    if request.method == 'POST':
        clave = request.form['clave']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        correo = request.form['correo']
        telefono = request.form['telefono']
        cliente.agregar_cliente(clave, nombre, direccion, correo, telefono)
        return "Cliente Agregado Correctamente."
    
@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    if request.method == 'POST':
        clave = request.form['clave']
        nombre = request.form['nombre']
        precio = request.form['precio']
        menu.agregar_producto(clave, nombre, precio)
        return "Producto Agregado Correctamente."
    
@app.route('/realizar_pedido', methods=['GET', 'POST'])
def realizar_pedido():
    if request.method == 'POST':
        clave = request.form['clave']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        correo = request.form['correo']
        telefono = request.form['telefono']
        cliente_clave = request.form['cliente_clave']
        producto_clave = request.form['producto_clave']
        producto_nombre = request.form['producto_nombre']
        producto_precio = request.form['producto_precio']
        pedido.realizar_pedido(cliente_clave, producto_clave)
        return render_template('pedido.html', detalles_pedido = detalle_pedido) # type:ignore
    
    else:
        return render_template('consulta_pedido.html')

@app.route('/consultar_pedido', methods=['GET', 'POST'])
def consultar_pedido():
    if request.method == 'POST':
        num_pedido = request.form['num_pedido']
        pedido.realizar_pedido(num_pedido)
        # Realizar Consulta en la Base de Datos para Obtener Detalles del Pedido
        # Luego, Renderizar la Plantilla HTML con los Detalles del Pedido
        return render_template('pedido.html', detalles_pedido = detalles_pedido) # type: ignore
    
    else:
        return render_template('consulta_pedido.html')
    
if __name__ == '__main__':
    app.run(debug=True)
        

db.cerrar_conexion()