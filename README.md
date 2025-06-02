# Workflow de ETL para Datos del Oro con GitHub Actions
Este proyecto implementa un flujo completo de ETL (Extracción, Transformación y Carga) para datos del Oro usando GitHub Actions como orquestador de CI/CD.

## Estructura del Flujo de Trabajo
El proceso está dividido en cuatro workflows de GitHub Actions:

1. Setup Environment (0-Setup-Environment.yml)

Prepara el entorno y la estructura del proyecto
Instala dependencias usando setup.py
Se ejecuta al hacer push al branch principal o manualmente
Data Extraction (1-Data-Extraction.yml)

2. Extrae datos del oro desde Yahoo Finance
Guarda los datos en un archivo CSV
Se ejecuta cada 12 horas o manualmente
Si la extracción falla, detiene el pipeline
Data Ingestion (2-Data-Ingestion.yml)

3. Carga los datos del CSV en una base de datos SQLite
Elimina el CSV temporal después de la ingesta
Se ejecuta automáticamente después de una extracción exitosa
Data Monitoring (3-Data-Monitoring.yml)

4. Monitorea la base de datos SQLite verificando integridad y tendencias
Genera logs y envía alertas si es necesario
Se ejecuta después de una ingesta exitosa, cada 6 horas o manualmente

# Requisitos para la Configuración
Para que este workflow funcione correctamente, necesitas configurar los siguientes secretos en GitHub:

1. Para el envío de alertas por correo electrónico:
   
EMAIL_SENDER: Dirección de correo del remitente

EMAIL_RECEIVER: Dirección de correo del destinatario

EMAIL_PASSWORD: Contraseña o token de la cuenta del remitente

SMTP_SERVER: Servidor SMTP (valor predeterminado: smtp.gmail.com)

SMTP_PORT: Puerto SMTP (valor predeterminado: 587)
