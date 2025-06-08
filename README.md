# Workflow de ETL para Datos del Oro con GitHub Actions
## Aplicación para de Datos de pagina Web con GitHub Actions
Un pipeline de datos automatizado que extrae, transforma y carga datos históricos del oro, utilizando GitHub Actions para orquestar todo el proceso.
Este proyecto implementa un flujo de trabajo ETL (Extracción, Transformación y Carga) completamente automatizado para obtener datos del oro desde fuentes públicas. El pipeline está diseñado para ser modular, robusto y fácil de monitorear, utilizando GitHub Actions como el orquestador principal.

## ¿Cómo Funciona el Pipeline ETL?
El proceso está dividido en cuatro flujos de trabajo secuenciales y condicionales que garantizan la integridad del dato en cada etapa.
## 1.	Preparación del Entorno (0-Setup-Environment.yml)
•	Acción: Prepara el entorno, crea la estructura de directorios necesaria e instala todas las dependencias del proyecto definidas en setup.py.
•	Disparador: Se ejecuta automáticamente con cada push a la rama main o puede ser iniciado manualmente.
## 2.	Extracción de Datos (1-Data-Extraction.yml)
•	Acción: Extrae los datos históricos del oro desde Yahoo Finance y los guarda temporalmente como un artefacto (gold_data.csv).
•	Disparador: Programado para ejecutarse cada 12 horas o manualmente. Si este paso falla, todo el pipeline se detiene para prevenir datos corruptos.
## 3.	Ingesta de Datos (2-Data-Ingestion.yml)
•	Acción: Carga los datos desde el archivo .csv a una base de datos SQLite. Una vez completada la carga, el archivo temporal es eliminado.
•	Disparador: Se ejecuta automáticamente solo si el workflow de extracción fue exitoso.
## 4.	Monitoreo de Datos (3-Data-Monitoring.yml)
•	Acción: Realiza verificaciones de integridad, analiza tendencias y busca anomalías en los datos cargados en la base de datos. Genera logs y envía alertas por correo electrónico si detecta problemas.
•	Disparador: Se ejecuta después de una ingesta exitosa, de forma programada cada 6 horas o manualmente.

# Configuración de Secretos
Para que el pipeline funcione correctamente, especialmente el sistema de alertas, se  debe configurar los siguientes secretos en tu repositorio de GitHub (Settings > Secrets and variables > Actions).
Secreto	                    Descripción
EMAIL_SENDER	            Dirección de correo que enviará la alerta.
EMAIL_RECEIVER	            Dirección de correo que recibirá la alerta.
EMAIL_PASSWORD	            Contraseña o token de aplicación del remitente.
SMTP_SERVER	            Servidor SMTP del proveedor de correo.
SMTP_PORT	            Puerto del servidor SMTP.

# Instalación y Uso
## 1.	Clona el repositorio: 
Bash
https://github.com/carlosisaza/pad_2025_1_2
## 2.	Configura los secretos: 
Sigue las instrucciones de la sección anterior para añadir los secretos en la configuración de tu repositorio en GitHub.
## 3.	Activa los Workflows: 
Los flujos de trabajo se activarán automáticamente según su programación (cron) o en cada push a main. También puedes ejecutarlos manualmente desde la pestaña Actions de tu repositorio.

# Características Principales
•	Modularidad: Cada fase del ETL está encapsulada en su propio archivo YAML, facilitando el mantenimiento y la depuración.
•	Ejecución Condicional: Los trabajos dependen del éxito de los anteriores, asegurando que los datos solo avancen en el pipeline si son correctos.
•	Monitoreo Automatizado: Incorpora análisis de tendencias y detección de anomalías para garantizar la calidad de los datos a lo largo del tiempo.
•	Sistema de Alertas: Notifica por correo electrónico sobre problemas o cambios importantes, permitiendo una respuesta rápida.
•	Persistencia de Artefactos: Los datos y logs se conservan de forma segura entre ejecuciones de workflows, permitiendo la trazabilidad.
•	Gestión de Dependencias: Utiliza un archivo setup.py para una instalación de paquetes limpia y reproducible.

# Estructura del Proyecto
.github/
└── workflows/
    ├── 0-Setup-Environment.yml
    ├── 1-Data-Extraction.yml
    ├── 2-Data-Ingestion.yml
    └── 3-Data-Monitoring.yml
src/
└── etl/
    ├── __init__.py
    ├── dataweb.py          # Lógica de extracción
    ├── database.py         # Lógica de carga y monitoreo
    └── mail.py             # Lógica de envío de correos
data/
    └── .gitkeep
logs/
    └── .gitkeep
setup.py
requirements.txt
README.md

# Personalización
Puedes adaptar fácilmente este proyecto a tus necesidades:
•	Cambiar la fuente de datos: Modifica la lógica en src/etl/dataweb.py para extraer datos de otras APIs o sitios web.
•	Ajustar la frecuencia: Cambia las expresiones cron en los archivos .yml para modificar la frecuencia de ejecución de los workflows.
•	Mejorar el monitoreo: Añade nuevas funciones de análisis o transformación de datos en la clase DatabaseMonitor dentro de src/etl/database.py.
•	Añadir dependencias: Si necesitas nuevos paquetes de Python, agrégalos al archivo setup.py y a requirements.txt.
