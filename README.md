# 🎨 Instagram Quote Generator

Una aplicación web moderna y elegante para generar imágenes de frases optimizadas para Instagram. Crea diseños hermosos con tus frases favoritas en segundos.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🆕 ¡NUEVO! Bot de Telegram 🤖

**Genera quotes directamente desde Telegram** - Sin necesidad de abrir el navegador.

📱 **Quick Start:** Ver [QUICK_START_TELEGRAM.md](QUICK_START_TELEGRAM.md)  
📚 **Guía completa:** Ver [TELEGRAM_BOT_GUIDE.md](TELEGRAM_BOT_GUIDE.md)

```bash
# Ejecutar el bot
start_telegram_bot.bat   # Windows
./start_telegram_bot.sh  # Linux/Mac
```

## ✨ Características

- 🎨 **6 Plantillas Predefinidas**: Minimalista, Oscuro, Vibrante, Océano, Atardecer y Bosque
- 📱 **Optimizado para Instagram**: Imágenes de 1080x1080 px perfectas para posts
- 🎯 **Interfaz Intuitiva**: Diseño limpio y fácil de usar
- ⚡ **Generación Instantánea**: Crea imágenes en menos de un segundo
- 💾 **Descarga Directa**: Descarga tus imágenes en formato PNG de alta calidad
- 📝 **Personalización**: Añade frases, autores y elige entre diferentes estilos

## 🖼️ Plantillas Disponibles

| Plantilla | Descripción | Ideal Para |
|-----------|-------------|------------|
| **Minimalista** | Diseño limpio con fondo blanco | Citas profesionales, frases motivacionales |
| **Oscuro Elegante** | Fondo oscuro con texto blanco | Frases profundas, contenido nocturno |
| **Vibrante** | Colores brillantes y llamativos | Contenido energético, llamadas a la acción |
| **Océano** | Tonos azules relajantes | Meditación, calma, reflexiones |
| **Atardecer** | Colores cálidos de atardecer | Romanticismo, inspiración |
| **Bosque** | Tonos verdes naturales | Ecología, naturaleza, bienestar |

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona o descarga este repositorio**

```bash
cd instagram-quote-generator
```

2. **Crea un entorno virtual (recomendado)**

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

## 🎮 Uso

### Iniciar la Aplicación Web

```bash
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

### Usar como Script de Python

También puedes usar el generador directamente desde Python:

```python
from image_generator import InstagramQuoteGenerator

# Crear instancia del generador
generator = InstagramQuoteGenerator()

# Generar una imagen
output_path = generator.generate_image(
    quote="La vida es lo que pasa mientras estás ocupado haciendo otros planes.",
    template="minimal",
    author="John Lennon"
)

print(f"Imagen generada: {output_path}")
```

### Plantillas Disponibles en Código

```python
# Ver todas las plantillas disponibles
templates = generator.get_available_templates()
for key, info in templates.items():
    print(f"{key}: {info['name']} - {info['description']}")

# Opciones: 'minimal', 'dark', 'vibrant', 'ocean', 'sunset', 'forest'
```

## 📁 Estructura del Proyecto

```
instagram-quote-generator/
├── app.py                  # Servidor Flask principal
├── image_generator.py      # Lógica de generación de imágenes
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
├── .gitignore             # Archivos a ignorar en Git
├── static/                # Archivos estáticos (CSS, JS)
│   ├── css/
│   │   └── style.css      # Estilos de la aplicación
│   └── js/
│       └── app.js         # JavaScript del frontend
├── templates/             # Templates HTML
│   └── index.html         # Página principal
├── output/                # Imágenes generadas (creado automáticamente)
└── fonts/                 # Fuentes personalizadas (opcional)
```

## 🎨 API Endpoints

Si quieres integrar el generador en otra aplicación:

### GET `/api/templates`
Obtiene la lista de plantillas disponibles.

**Respuesta:**
```json
{
  "success": true,
  "templates": {
    "minimal": {
      "name": "Minimalista",
      "description": "Diseño limpio y simple con fondo blanco"
    }
  }
}
```

### POST `/api/generate`
Genera una imagen con una frase.

**Request:**
```json
{
  "quote": "Tu frase aquí",
  "template": "minimal",
  "author": "Autor (opcional)"
}
```

**Respuesta:**
```json
{
  "success": true,
  "message": "Imagen generada exitosamente",
  "filename": "quote_minimal_20240111_123456.png",
  "download_url": "/api/download/quote_minimal_20240111_123456.png"
}
```

### GET `/api/download/<filename>`
Descarga una imagen generada.

### GET `/api/preview/<filename>`
Previsualiza una imagen generada.

## 🛠️ Personalización

### Añadir Nuevas Plantillas

Edita el archivo `image_generator.py` y añade una nueva entrada al diccionario `TEMPLATES`:

```python
'mi_plantilla': {
    'name': 'Mi Plantilla',
    'bg_color': (R, G, B),        # Color de fondo RGB
    'text_color': (R, G, B),      # Color del texto RGB
    'accent_color': (R, G, B),    # Color de acento RGB
    'font_size': 60,               # Tamaño de fuente
    'description': 'Descripción de la plantilla'
}
```

### Usar Fuentes Personalizadas

1. Coloca tus archivos de fuentes `.ttf` en la carpeta `fonts/`
2. Modifica el método `_get_font()` en `image_generator.py` para incluir la ruta a tus fuentes

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para nuevas plantillas, características o mejoras:

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 🐛 Resolución de Problemas

### Error: "No module named 'PIL'"
```bash
pip install Pillow
```

### Error: "Address already in use"
El puerto 5000 está ocupado. Cambia el puerto en `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Usa otro puerto
```

### Las fuentes no se ven bien
El generador usa fuentes del sistema. Asegúrate de tener instaladas fuentes como Arial, Calibri o Segoe UI.

## 📝 Ejemplos de Uso

### Ejemplo 1: Frase Motivacional
```python
generator.generate_image(
    quote="El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.",
    template="vibrant",
    author="Albert Schweitzer"
)
```

### Ejemplo 2: Frase Corta
```python
generator.generate_image(
    quote="Carpe Diem",
    template="dark"
)
```

### Ejemplo 3: Frase Larga
```python
generator.generate_image(
    quote="En medio de la dificultad reside la oportunidad. Cada desafío es una oportunidad disfrazada.",
    template="ocean",
    author="Albert Einstein"
)
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- **Pillow (PIL)**: Por la excelente librería de procesamiento de imágenes
- **Flask**: Por el framework web ligero y potente
- **Instagram**: Por la inspiración en el diseño

## 📧 Contacto

¿Preguntas, sugerencias o feedback? 

- Abre un issue en GitHub
- Contacta al desarrollador

---

**¡Hecho con ❤️ y Python!**

*Crea, comparte e inspira con tus frases.*
