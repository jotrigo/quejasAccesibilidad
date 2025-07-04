# Analizador de Quejas sobre Dispositivos

Este proyecto analiza archivos Excel que contienen conversaciones para identificar quejas relacionadas con dispositivos tecnológicos utilizando la API de OpenAI.

## Características

- ✅ Análisis automático de conversaciones en archivos Excel
- ✅ Identificación de quejas sobre dispositivos usando IA
- ✅ Clasificación por tipo de dispositivo y gravedad
- ✅ Generación de reportes detallados
- ✅ Soporte para múltiples archivos

## Instalación

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Configurar API Key de OpenAI:**
```bash
export OPENAI_API_KEY='tu-api-key-aqui'
```

## Uso

### 1. Explorar la estructura de los archivos (opcional)

Antes de ejecutar el análisis completo, puedes explorar la estructura de tus archivos Excel:

```bash
python explore_files.py
```

Esto te mostrará:
- Número de filas y columnas
- Nombres de las columnas
- Muestras de datos
- Columnas con texto largo (posibles conversaciones)

### 2. Ejecutar el análisis completo

```bash
python analyze_complaints.py
```

El script:
- Procesa los archivos `Casos 2022.xlsx` y `Casos 2023.xlsx`
- Analiza cada conversación usando OpenAI GPT-3.5-turbo
- Identifica quejas sobre dispositivos
- Genera un reporte en `reporte_quejas_dispositivos.json`

### 3. Personalizar el análisis

Puedes modificar el script `analyze_complaints.py` para:

- Cambiar el número máximo de conversaciones por archivo (línea 150)
- Ajustar el prompt de análisis (línea 25-40)
- Modificar los criterios de clasificación
- Cambiar el formato del reporte

## Estructura del Reporte

El reporte generado incluye:

```json
{
  "fecha_analisis": "2024-01-01T12:00:00",
  "resumen": {
    "total_conversaciones": 100,
    "quejas_dispositivos": 15,
    "porcentaje_quejas": 15.0
  },
  "tipos_dispositivos": {
    "computadora": 8,
    "teléfono": 4,
    "impresora": 3
  },
  "gravedad_quejas": {
    "baja": 5,
    "media": 7,
    "alta": 3
  },
  "quejas_detalladas": [...]
}
```

## Tipos de Dispositivos Detectados

El sistema puede identificar quejas sobre:
- Computadoras y laptops
- Teléfonos móviles
- Tablets
- Impresoras
- Monitores
- Teclados y mouse
- Dispositivos de red
- Y otros dispositivos tecnológicos

## Consideraciones

- **Costo**: Cada análisis de conversación consume tokens de OpenAI
- **Rate Limiting**: El script incluye pausas para evitar límites de API
- **Límite de texto**: Las conversaciones se limitan a 2000 caracteres para optimizar costos
- **Archivos grandes**: Por defecto se procesan máximo 50 conversaciones por archivo

## Solución de Problemas

### Error: "No module named 'pandas'"
```bash
pip install pandas openpyxl
```

### Error: "OPENAI_API_KEY not set"
```bash
export OPENAI_API_KEY='tu-api-key-aqui'
```

### Error al leer archivo Excel
- Verifica que el archivo existe en el directorio
- Asegúrate de tener instalado `openpyxl` para archivos .xlsx

## Personalización Avanzada

### Modificar el prompt de análisis

Edita la función `analyze_conversation` en `analyze_complaints.py` para ajustar los criterios de clasificación.

### Agregar nuevos tipos de dispositivos

Modifica el prompt para incluir categorías específicas de dispositivos que necesites detectar.

### Cambiar el modelo de OpenAI

Cambia `gpt-3.5-turbo` por otro modelo disponible en tu cuenta de OpenAI. 