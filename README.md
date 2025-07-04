# Analizador de Quejas de Accesibilidad

Este proyecto analiza archivos Excel que contienen conversaciones para identificar quejas relacionadas con dispositivos y servicios de accesibilidad utilizando la API de OpenAI.

## 🎯 Propósito

El proyecto está diseñado específicamente para analizar quejas sobre dispositivos de accesibilidad como:
- Teclados ampliados y adaptados
- Mouse tipo trackball y joystick
- Seguidores oculares (Tobii, PCEye)
- Pulsadores y botones de acceso
- Auriculares y micrófonos
- Soportes y atriles
- Software de accesibilidad (NVDA, lectores de pantalla)
- Rampas digitales y valijas de evaluación

## 📊 Datos Actuales

El proyecto incluye análisis de:
- **Casos 2022.xlsx**: 966 casos analizados
- **Casos 2023.xlsx**: 1129 casos analizados
- **Total de quejas de accesibilidad identificadas**: 1946 casos

## 🚀 Características

- ✅ Análisis automático de conversaciones en archivos Excel
- ✅ Identificación específica de quejas sobre dispositivos de accesibilidad
- ✅ Clasificación por tipo de dispositivo y gravedad
- ✅ Generación de reportes detallados en JSON
- ✅ Soporte para múltiples archivos
- ✅ Filtrado inteligente usando IA de OpenAI

## 📦 Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/jotrigo/quejasAccesibilidad.git
cd quejasAccesibilidad
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configurar API Key de OpenAI:**
```bash
export OPENAI_API_KEY='tu-api-key-aqui'
```

## 🔧 Uso

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
- Analiza cada conversación usando OpenAI GPT-4o-mini
- Identifica quejas específicas sobre dispositivos de accesibilidad
- Genera un reporte en `quejas_accesibilidad.json`

## 📈 Estructura de Datos

### Archivo de resultados: `quejas_accesibilidad.json`

Cada queja identificada incluye:

```json
{
  "archivo": "Casos 2023.xlsx",
  "fila": 17,
  "caso_numero": 14409006,
  "texto": "Aclaro: lo que se le rompió al usuario es el teclado ampliado accesible...",
  "es_queja": true,
  "es_accesibilidad": true,
  "motivo": "El usuario reporta la rotura de un teclado ampliado accesible",
  "palabras_clave": ["teclado ampliado", "accesible", "reparar"],
  "resumen": "El usuario tiene un teclado ampliado accesible roto y pregunta por el procedimiento de reparación."
}
```

## 🎯 Tipos de Dispositivos de Accesibilidad Detectados

El sistema identifica quejas sobre:

### Hardware de Accesibilidad
- **Teclados**: Ampliados, de alto contraste, adaptados
- **Mouse**: Trackball, joystick, por botones
- **Pulsadores**: Botones de acceso, switches
- **Audio**: Auriculares, micrófonos, vinchas
- **Soportes**: Brazos articulados, flexibles, atriles

### Seguidores Oculares
- **Tobii**: Eye Tracker, PCEye
- **Dispositivos de rastreo ocular**

### Software de Accesibilidad
- **NVDA**: Lector de pantalla
- **CBoard**: Comunicación aumentativa
- **Centro de Accesibilidad**: Configuraciones

### Infraestructura
- **Valijas**: Equipos de evaluación
- **Rampas digitales**: Dispositivos de apoyo
- **Señalización**: Braille, pictogramas

## 💡 Consideraciones Importantes

- **Costo**: Cada análisis consume tokens de OpenAI (aproximadamente $0.001 por análisis)
- **Rate Limiting**: El script incluye pausas para evitar límites de API
- **Límite de texto**: Las conversaciones se limitan a 2000 caracteres para optimizar costos
- **Precisión**: El modelo está entrenado específicamente para detectar dispositivos de accesibilidad

## 🔧 Solución de Problemas

### Error: "No module named 'pandas'"
```bash
pip install pandas openpyxl openai
```

### Error: "OPENAI_API_KEY not set"
```bash
export OPENAI_API_KEY='tu-api-key-aqui'
```

### Error al leer archivo Excel
- Verifica que los archivos `Casos 2022.xlsx` y `Casos 2023.xlsx` existen
- Asegúrate de tener instalado `openpyxl` para archivos .xlsx

## 🛠️ Personalización Avanzada

### Modificar el prompt de análisis

Edita la función `analyze_conversation` en `analyze_complaints.py` para ajustar los criterios de clasificación.

### Agregar nuevos tipos de dispositivos

Modifica la lista `ITEMS_BUSQUEDA` en el script para incluir nuevos dispositivos de accesibilidad.

### Cambiar el modelo de OpenAI

Cambia `gpt-4o-mini` por otro modelo disponible en tu cuenta de OpenAI.

## 📊 Estadísticas del Proyecto

- **Total de casos analizados**: 2095
- **Quejas de accesibilidad identificadas**: 1946
- **Tasa de detección**: 92.9%
- **Archivos procesados**: 2 (2022 y 2023)

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autor

- **Joaquín Trigo** - [GitHub](https://github.com/jotrigo)

## 📞 Contacto

Para preguntas o sugerencias sobre el proyecto, puedes:
- Abrir un issue en GitHub
- Contactar directamente al autor

---

**Nota**: Este proyecto está diseñado específicamente para el análisis de quejas relacionadas con dispositivos y servicios de accesibilidad en el contexto educativo uruguayo. 