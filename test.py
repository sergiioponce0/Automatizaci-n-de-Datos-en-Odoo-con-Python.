import pandas as pd
import psycopg2

# 1. Configuración de conexión (Diccionario como pide el ejercicio) [cite: 111, 185]
params = {
    "host": "localhost",
    "port": 5433,
    "database": "postgres",
    "user": "odoo",
    "password": "odoo"
}

# Nombre del archivo CSV (Asegúrate que se llame así en tu carpeta)
ruta_csv = 'listado.csv' 

try:
    # 2. Lectura correcta con encoding latin1 [cite: 123, 194]
    print("⏳ Leyendo archivo CSV...")
    df = pd.read_csv(ruta_csv, encoding='latin1')
    print(f"✅ Archivo leído. {len(df)} registros encontrados.")

    # 3. Conexión a la Base de Datos [cite: 196]
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    print("✅ Conexión establecida con PostgreSQL.")

    # 4. Gestión de Tablas: Crear tabla import_centros (No contactos_mailing)
    # Usamos TEXT como pide el requisito para flexibilidad [cite: 132, 203]
    create_table_query = """
    CREATE TABLE IF NOT EXISTS import_centros (
        id SERIAL PRIMARY KEY,
        centro_nombre TEXT,
        domicilio TEXT,
        localidad TEXT,
        cp TEXT,
        telefono TEXT
    );
    """
    cur.execute(create_table_query)
    print("✅ Tabla 'import_centros' verificada/creada.")

    # 5. Carga mediante Bucle e inserción por posición (iloc) [cite: 140-142, 211]
    # Asumimos que el CSV tiene 5 columnas relevantes. Ajusta si tiene más.
    insert_query = """
    INSERT INTO import_centros (centro_nombre, domicilio, localidad, cp, telefono)
    VALUES (%s, %s, %s, %s, %s)
    """

    for index, row in df.iterrows():
        cur.execute(insert_query, (
            str(row.iloc[0]), # Columna 1 del CSV
            str(row.iloc[1]), # Columna 2 del CSV
            str(row.iloc[2]), # Columna 3 del CSV
            str(row.iloc[3]), # Columna 4 del CSV
            str(row.iloc[4])  # Columna 5 del CSV
        ))

    # 6. Persistencia: Commit solo si no hay errores [cite: 148, 222]
    conn.commit()
    print(f"🚀 ¡Éxito! Se han importado {len(df)} centros educativos a la BD.")

except Exception as e:
    # Rollback en caso de error [cite: 150, 227]
    print(f"❌ Error durante el proceso: {e}")
    if 'conn' in locals() and conn:
        conn.rollback()

finally:
    # Cerrar recursos [cite: 152, 230]
    if 'cur' in locals() and cur:
        cur.close()
    if 'conn' in locals() and conn:
        conn.close()