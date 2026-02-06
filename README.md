# Proceso ETL: Extracción de Centros Educativos a PostgreSQL con Python y Docker

Este repositorio contiene la resolución de la tarea de administración de sistemas ERP. El objetivo es desarrollar un proceso ETL (Extracción, Transformación y Carga) para volcar un listado externo de colegios (`listado.csv`) en un servidor PostgreSQL corriendo en un entorno Dockerizado.

## 🛠️ Requisitos Técnicos
- **Lenguaje**: Python 3.10+
- **Librerías**: `pandas`, `psycopg2-binary`
- **Infraestructura**: Docker Desktop (Contenedores de Odoo y DB activos)
- **Base de Datos**: PostgreSQL (Puerto 5433 externo)

## 📋 Procedimiento Realizado

1. **Configuración del Entorno**: 
   Se ha utilizado un archivo `docker-compose.yml` para levantar los servicios de Odoo, PostgreSQL y pgAdmin. El puerto de la base de datos se mapeó como `5433:5432` para evitar conflictos locales.

2. **Desarrollo del Script (`importar.py`)**:
   - **Conexión**: Se implementó una conexión robusta mediante un diccionario de credenciales.
   - **Lectura**: Se utilizó Pandas con codificación `latin1` para procesar correctamente caracteres especiales y tildes del archivo CSV.
   - **Gestión de Tablas**: El script crea automáticamente la tabla `import_centros` si no existe, definiendo las columnas como tipo `TEXT`.
   - **Carga de Datos**: Se realizó un bucle mediante `iloc` para recorrer el DataFrame e insertar los registros de forma segura.
   - **Persistencia**: Se incluyó un bloque `try-except-finally` con `commit()` y `rollback()` para asegurar la integridad de la base de datos.

3. **Verificación**: 
   Se comprobó la carga mediante consultas SQL en pgAdmin y la terminal de VS Code.

## 📸 Evidencias de Funcionamiento

### 1. Conexión Exitosa (test.py)
Esta captura demuestra que la conexión entre Python y el contenedor de Docker es correcta antes de la carga.
![Conexión Exitosa](<img width="889" height="227" alt="Captura de pantalla 2026-02-06 123346" src="https://github.com/user-attachments/assets/30d810a6-661d-4c81-8487-168dcc92632b" />)

### 2. Ejecución del Script de Importación
[cite_start]Terminal de VS Code mostrando el mensaje de éxito tras procesar el archivo CSV.
![Éxito Importación](<img width="1323" height="729" alt="Captura de pantalla 2026-02-06 123555" src="https://github.com/user-attachments/assets/9456a37e-f6bd-47f1-a501-67c64ffeb1ed" />)

### 3. Verificación en pgAdmin con Reloj del Sistema
[cite_start]Vista de la tabla `import_centros` con los datos cargados mediante la consulta `SELECT` y el reloj del sistema visible, cumpliendo con el requisito de verificación de la tarea
![Verificación pgAdmin](<img width="1365" height="560" alt="Captura de pantalla 2026-02-06 122606" src="https://github.com/user-attachments/assets/1d052f3f-68c5-4908-b94d-d848c9375f98" />
)
