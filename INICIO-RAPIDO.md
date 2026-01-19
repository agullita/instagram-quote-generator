# 🚀 INICIO RÁPIDO - Instagram Quote Generator

## ✅ Estado: **LISTO PARA USAR**

---

## 🎯 Ejecutar en 3 Pasos

### 1️⃣ Abre la Terminal
```bash
cd instagram-quote-generator
```

### 2️⃣ Inicia el Servidor
```bash
start.bat
```

### 3️⃣ Abre el Navegador
```
http://localhost:5000
```

**¡Listo! Ya puedes generar imágenes para Instagram** 🎨

---

## 📱 Funcionalidades Disponibles

### ✨ Aplicación Web (Puerto 5000)
- Genera imágenes de frases (1080x1080px)
- 8 plantillas de diseño profesional
- Carruseles para Instagram
- Descarga directa en PNG
- Palabras destacadas en color

### 🤖 Bot de Telegram (Opcional)
- Genera imágenes desde Telegram
- Interfaz interactiva con botones
- Mismas plantillas que la web
- **Requiere**: Token de @BotFather

---

## 🎨 Plantillas Incluidas

1. 🎯 **Minimalista** - Fondo blanco limpio
2. 🌙 **Oscuro** - Fondo negro elegante
3. 🎨 **Vibrante** - Naranja brillante
4. 🌊 **Océano** - Azul relajante
5. 🌅 **Atardecer** - Tonos cálidos
6. 🌲 **Bosque** - Verde natural
7. 🔶 **Geométrico Naranja** - Diseño moderno
8. 📐 **Geométrico Limpio** - Minimalista con detalle

---

## 📝 Ejemplo de Uso Web

1. Escribe: `"La vida es bella"`
2. Autor (opcional): `Roberto`
3. Selecciona plantilla: `Minimalista`
4. Clic en `Generar Imagen`
5. ¡Descarga y sube a Instagram!

---

## 🤖 Configurar Bot de Telegram (5 minutos)

### Paso 1: Crear Bot
1. Abre Telegram → Busca `@BotFather`
2. Envía `/newbot`
3. Nombre: `Mi Quote Generator`
4. Username: `mi_quote_bot` (debe terminar en _bot)
5. **Copia el token** que te da

### Paso 2: Configurar Token
Edita `.env` en la carpeta del proyecto:
```bash
TELEGRAM_BOT_TOKEN=tu_token_aqui
```

### Paso 3: Iniciar Bot
```bash
start_telegram_bot.bat
```

### Paso 4: Usar Bot
1. Busca tu bot en Telegram
2. `/start` para instrucciones
3. Envía una frase y sigue el asistente

---

## 🌍 Subir a Internet

### Opción Recomendada: Render (Gratis)
1. Sube el proyecto a GitHub
2. Crea cuenta en [Render.com](https://render.com)
3. "New Web Service" → Conecta GitHub
4. Deploy automático ✅

**Guía completa**: Ver `GUIA-DEPLOYMENT.md`

### Otras opciones:
- **Railway** - Rápido y fácil
- **Vercel** - Solo web (no bot)
- **VPS/Docker** - Control total

---

## 📂 Estructura de Archivos

```
instagram-quote-generator/
├── app.py                    # 🌐 Servidor web
├── telegram_bot.py           # 🤖 Bot de Telegram
├── image_generator.py        # 🎨 Generador de imágenes
├── carousel_generator.py     # 📱 Generador de carruseles
├── start.bat                 # 🚀 Iniciar web
├── start_telegram_bot.bat    # 🤖 Iniciar bot
├── requirements.txt          # 📦 Dependencias
├── .env                      # 🔐 Configuración
├── backgrounds/              # 🖼️ Fondos geométricos
├── output/                   # 📁 Imágenes generadas
└── templates/                # 🎭 HTML frontend
```

---

## 🆘 Problemas Comunes

### ❌ "Puerto 5000 ocupado"
**Solución**: Edita `app.py` línea 329 y cambia `port=5000` a `port=5001`

### ❌ "Module not found"
**Solución**: 
```bash
pip install -r requirements.txt
```

### ❌ Bot no responde
**Solución**: Verifica que `TELEGRAM_BOT_TOKEN` en `.env` sea correcto

### ❌ No se generan imágenes
**Solución**: Verifica que la carpeta `output/` existe y tiene permisos

---

## 📚 Documentación Completa

- `INSTRUCCIONES-EJECUCION-LOCAL.md` - Guía detallada local
- `GUIA-DEPLOYMENT.md` - Deployment en servidores
- `README.md` - Documentación técnica completa
- `QUICK_START.md` - Inicio rápido original
- `TELEGRAM_BOT_GUIDE.md` - Guía completa del bot

---

## ✅ Verificación Rápida

### Probar que todo funciona:
```bash
cd instagram-quote-generator
python -c "from image_generator import InstagramQuoteGenerator; g = InstagramQuoteGenerator(); print(g.generate_image('Test OK', 'minimal'))"
```

Deberías ver: `output\quote_minimal_TIMESTAMP.png` ✅

---

## 🎯 Próximos Pasos

1. ✅ **Ejecuta localmente** (ya lo tienes listo)
2. 🎨 **Prueba todas las plantillas**
3. 🤖 **Configura el bot** (opcional)
4. 🌍 **Sube a internet** cuando estés listo
5. 📱 **Comparte con el mundo**

---

## 💡 Tips Profesionales

- **Mejor plantilla**: `geometric1` o `geometric2` para contenido profesional
- **Palabras destacadas**: Usa `#palabra1,palabra2` al final de tu texto
- **Carruseles**: Perfecto para contenido educativo (tips, listas, etc.)
- **Bot vs Web**: Bot para uso personal, Web para clientes

---

## 📞 Comandos Útiles

```bash
# Iniciar web
start.bat

# Iniciar bot
start_telegram_bot.bat

# Ver dependencias
pip list

# Actualizar dependencias
pip install -r requirements.txt --upgrade

# Detener servidor
CTRL + C
```

---

**🎉 ¡Todo listo! Empieza a crear contenido increíble para Instagram.**

¿Preguntas? Consulta la documentación o busca en los archivos DEPLOY_*.md
