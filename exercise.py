import sqlite3


def create_or_get_database():
    conn = sqlite3.connect("platillos.db")
    print("Base de datos conectada")
    return conn

def create_tables(conn):
    sql = """
        CREATE TABLE IF NOT EXISTS platillos (
            name VARCHAR NOT NULL,
            description TEXT,
            price DOUBLE NOT NULL,
            ingredients TEXT,
            preparation_time DOUBLE NOT NULL,
            is available VARCHAR NOT NUL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

        )
    """"
conn.execute(sql)
print("La tabla ha sido creada de forma exitosa")

        
    

def validate_user_selection(selection):
    return isinstance(selection, int) and selection > 0 and selection < 3

def get_platillo():
    pass

def ordenar_platillo(conn):
    name = input("Cuál es el nombre de tu platillo?")
    description = input("Escribe la descripción:")
    price = float(input("Cuál es el precio?"))
    ingredients = input("Escribe los ingredientes:")
    preparation_time = float(input("Tiempo de preparación":))


    sql = """
        INSERT INTO
            PLATILLOS (name, description, price, ingredients)
        VALUES (?, ?, ?, ?)


    
    """
    values = (name, description, price, ingredients)

    conn.execute(sql, values)
    conn.commit

    print("Platillos creado")
    



def handle_user_selection(selection):
    if selection == 1:
        get_platillo()
    else:
        ordenar_platillo()
              


def main():
    conn = create_or_get_database()
    create_tables(conn)
    print("Bienvenid@")
    print("Por favor, coloque la siguiente información para iniciar la orden")
    name = input("Nombre:")
    Apellido = input("Apellido:")
    email = input("email:")
    Passport = input("Passport")
    selection = int(input("¿Qué opción eliges?"))

    if validate_user_selection(selection):
        handle_user_selection
    else:
        print("Valor inválido")
        


main()
   



    #print("Su orden ha quedado registrada de manera exitosa")
    #print("Salir de la app (SI/NO)")

# print("Te presentamos nuestro menú de opciones)
    # print("1. Ver los platillos disponibles")
    # print("2. Ordenar platillo")

    