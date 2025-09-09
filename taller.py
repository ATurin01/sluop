import sqlite3

# 1. Conexión a la base de datos (se crea el archivo si no existe)
conexion = sqlite3.connect("taller_mecanico.db")

# 2. Crear un cursor para ejecutar sentencias SQL
cursor = conexion.cursor()

# 3. Crear tabla Clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT,
    correo TEXT
)
""")
clientes = [
    ("Maria Ruiz", "66655544", "maria@mail.com"),
    ("Carlos Pérez", "78912345", "carlos@mail.com")
]
# 4. Insertar un cliente
cursor.executemany("""
INSERT INTO clientes (nombre, telefono, correo)
VALUES (?, ?, ?)
""", clientes)

# 5. Guardar los cambios
conexion.commit()

# 6. Consultar clientes
cursor.execute("SELECT * FROM clientes")
for fila in cursor.fetchall():
    print(fila)

# 7. Cerrar conexión
conexion.close()
