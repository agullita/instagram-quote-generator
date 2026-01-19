# 🎨 Instagram Quote Generator

> Genera imágenes profesionales de frases para Instagram con plantillas personalizables. Incluye aplicación web y bot de Telegram.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Características

- 🎨 **8 Plantillas Profesionales** - Diseños modernos y elegantes
- 📱 **Formato Instagram** - Imágenes de 1080x1080px perfectas
- 🤖 **Bot de Telegram** - Genera desde el chat
- 🌐 **Aplicación Web** - Interfaz visual intuitiva
- 📊 **Carruseles** - Crea múltiples slides
- ✨ **Palabras Destacadas** - Resalta términos clave
- 🎯 **Tipografía Adaptativa** - Se ajusta al contenido

---

## 🚀 Inicio Rápido

### Instalación Local

```bash
# Clonar el repositorio
git clone https://github.com/agullita/instagram-quote-generator.git
cd instagram-quote-generator

# Instalar dependencias
pip install -r requirements.txt

# Iniciar aplicación web
python app.py
# O usar: start.bat (Windows) / ./start.sh (Linux/Mac)
```

**Abre tu navegador en:** `http://localhost:5000`

---

## 📖 Documentación

- 📘 **[INICIO-RAPIDO.md](INICIO-RAPIDO.md)** - Empieza en 3 minutos
- 📗 **[INSTRUCCIONES-EJECUCION-LOCAL.md](INSTRUCCIONES-EJECUCION-LOCAL.md)** - Guía detallada local
- 📕 **[GUIA-DEPLOYMENT.md](GUIA-DEPLOYMENT.md)** - Sube a internet (Render, Railway, Vercel)
- 📙 **[TELEGRAM_BOT_GUIDE.md](TELEGRAM_BOT_GUIDE.md)** - Configura el bot de Telegram
- 📔 **[TEMPLATES_GUIDE.md](TEMPLATES_GUIDE.md)** - Guía de plantillas

---

## 🎨 Plantillas Incluidas

| Plantilla | Descripción | Uso Recomendado |
|-----------|-------------|-----------------|
| 🎯 **Minimalista** | Fondo blanco limpio | Profesional, corporativo |
| 🌙 **Oscuro** | Fondo negro elegante | Sofisticado, nocturno |
| 🎨 **Vibrante** | Naranja brillante | Energético, motivacional |
| 🌊 **Océano** | Azul relajante | Tranquilo, wellness |
| 🌅 **Atardecer** | Tonos cálidos | Romántico, inspirador |
| 🌲 **Bosque** | Verde natural | Ecológico, natural |
| 🔶 **Geométrico Naranja** | Formas modernas | Creativo, moderno |
| 📐 **Geométrico Limpio** | Minimalista con detalle | Tech, startup |

---

## 🤖 Bot de Telegram

### Configuración (5 minutos)

1. **Crear bot con @BotFather:**
   ```
   /newbot
   Mi Quote Generator
   mi_quote_bot
   ```

2. **Configurar token:**
   ```bash
   # Crear archivo .env
   TELEGRAM_BOT_TOKEN=tu_token_aqui
   ```

3. **Iniciar bot:**
   ```bash
   python telegram_bot.py
   # O usar: start_telegram_bot.bat
   ```

### Uso del Bot

```
# Imagen simple
"La vida es bella"

# Con autor
"La vida es bella | Roberto"

# Con palabras destacadas
"La vida es bella | Roberto #vida,bella"

# Carrusel
CAROUSEL: Consejo 1. Consejo 2. Consejo 3.
TITLE: 3 Consejos de Vida
#palabras,clave
```

---

## 🌐 API Endpoints

### GET `/api/templates`
Obtiene plantillas disponibles

### POST `/api/generate`
Genera imagen única
```json
{
  "quote": "Tu frase aquí",
  "template": "minimal",
  "author": "Nombre del autor",
  "highlight_words": ["palabra1", "palabra2"]
}
```

### POST `/api/generate-carousel`
Genera carrusel de imágenes
```json
{
  "content": "Slide 1. Slide 2. Slide 3.",
  "template": "vibrant",
  "title": "Mi Carrusel",
  "cta_text": "Sígueme para más"
}
```

---

## 🌍 Deployment

### Render (Recomendado - Gratis)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

1. Fork este repositorio
2. Crea cuenta en Render.com
3. "New Web Service" → Conecta GitHub
4. Deploy automático ✅

**Guía completa:** [DEPLOY-WEB-RENDER.md](DEPLOY-WEB-RENDER.md)

### Otras Opciones
- **Railway** - Rápido y fácil ([Guía](DEPLOY_RAILWAY.md))
- **Vercel** - Solo web ([Guía](VERCEL-INFO.md))
- **Docker** - Control total

---

## 📂 Estructura del Proyecto

```
instagram-quote-generator/
├── app.py                    # Servidor Flask
├── telegram_bot.py           # Bot de Telegram
├── image_generator.py        # Generador de imágenes
├── carousel_generator.py     # Generador de carruseles
├── requirements.txt          # Dependencias
├── .env                      # Variables de entorno
├── Procfile                  # Para Heroku/Render
├── runtime.txt               # Versión de Python
├── backgrounds/              # Fondos geométricos
├── output/                   # Imágenes generadas
├── static/                   # CSS/JS frontend
└── templates/                # HTML frontend
```

---

## 🛠️ Tecnologías

- **Backend:** Python 3.8+, Flask 3.0
- **Procesamiento de Imágenes:** Pillow 10.1
- **Bot:** python-telegram-bot 20.7
- **Frontend:** HTML5, CSS3, JavaScript vanilla
- **Deployment:** Gunicorn, Docker

---

## 💡 Ejemplos de Uso

### Python API
```python
from image_generator import InstagramQuoteGenerator

generator = InstagramQuoteGenerator()

# Generar imagen
output_path = generator.generate_image(
    quote="La vida es bella",
    template="minimal",
    author="Roberto",
    highlight_words=["vida", "bella"]
)

print(f"Imagen generada: {output_path}")
```

### cURL
```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "quote": "La vida es bella",
    "template": "minimal",
    "author": "Roberto"
  }'
```

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/NuevaPlantilla`)
3. Commit cambios (`git commit -m 'Añadir nueva plantilla'`)
4. Push a la rama (`git push origin feature/NuevaPlantilla`)
5. Abre un Pull Request

---

## 📝 Roadmap

- [ ] Más plantillas de diseño
- [ ] Soporte para Stories (1080x1920)
- [ ] Editor visual de plantillas
- [ ] Integración con Canva API
- [ ] Publicación automática en Instagram
- [ ] Analytics de imágenes generadas

---

## 🐛 Reporte de Bugs

¿Encontraste un bug? [Abre un issue](https://github.com/agullita/instagram-quote-generator/issues)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**Eduardo Agulla**
- GitHub: [@agullita](https://github.com/agullita)

---

## ⭐ Dale una Estrella

Si este proyecto te ayudó, ¡dale una estrella! ⭐

---

## 📞 Soporte

- 📖 [Documentación completa](README.md)
- 💬 [Discussions](https://github.com/agullita/instagram-quote-generator/discussions)
- 🐛 [Issues](https://github.com/agullita/instagram-quote-generator/issues)

---

**¡Empieza a crear contenido increíble para Instagram! 🎨✨**
