import pymongo

# Configuración de MongoDB
HOST = "localhost"
PUERTO = "27018,27019"  
URL = f"mongodb://{HOST}:{PUERTO}/"
BASEDATOS = "admin"

# Conexión a MongoDB
try:
    cliente = pymongo.MongoClient(URL, serverSelectionTimeoutMS=2000)
    cliente.server_info()  # Verifica conexión
    print("Conexión exitosa a MongoDB")
except pymongo.errors.ServerSelectionTimeoutError as error_tiempo:
    print(f"Error de conexión: Tiempo excedido. Detalles: {error_tiempo}")
    exit()
except pymongo.errors.ConnectionFailure as error_conexion:
    print(f"Error de conexión: Fallo al conectarse. Detalles: {error_conexion}")
    exit()

# Seleccionar la base de datos
db = cliente[BASEDATOS]

# Función para insertar un equipo
def InsertEquipo(db, equipo):
    coleccion = db["nombres_equipos"]
    resultado = coleccion.insert_one(equipo)
    print(f"Equipo insertado con ID: {resultado.inserted_id}")

def ListarEquipos(db):
    coleccion = db["nombres_equipos"]
    print("Empleados en la colección:")
    for equipo in coleccion.find():
        print(equipo)
        
# Programa principal
if __name__ == "__main__":
    #Inserta un equipo como ejemplo
    nuevo_equipo = {"nombre": "Nacional", "Ciudad": "Medellín" }
    InsertEquipo(db, nuevo_equipo)

    #Lista los equipos
    ListarEquipos(db)