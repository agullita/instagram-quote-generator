# 🎯 Deploy en Render SIN Conectar GitHub

## ✨ Solución Rápida: Usar Repositorio Público

Ya tienes tu código en: `https://github.com/agullita/instagram-quote-generator.git`

Este es un repositorio **público**, así que puedes usarlo en Render SIN conectar tu cuenta de GitHub.

---

## 🚀 Pasos (5 minutos)

### Paso 1: Ir a Render

1. Abre https://render.com/dashboard con tu nueva cuenta
2. Click en **"New +"** (arriba derecha)
3. Selecciona **"Background Worker"**

---

### Paso 2: Conectar Repositorio Público

En la pantalla de "Create a new Background Worker":

1. Busca la opción **"Public Git repository"** o un campo para pegar URL
2. Pega esta URL:
   ```
   https://github.com/agullita/instagram-quote-generator.git
   ```

Si no ves opción para repositorio público:
- Click en **"Connect to GitHub"** (es solo para este proyecto)
- O busca opción "Deploy from Git URL"

---

### Paso 3: Configurar el Worker

**Name:** `instagram-quote-bot`

**Region:** Frankfurt (o el más cercano a España)

**Branch:** `main`

**Root Directory:** *(dejar vacío)*

**Runtime:** Python 3

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
python telegram_bot.py
```

**Instance Type:** Free

---

### Paso 4: Agregar Token del Bot

⚠️ **IMPORTANTE**: Antes de crear, agrega la variable de entorno:

1. Busca sección **"Environment Variables"** o **"Advanced"**
2. Click **"Add Environment Variable"**
3. Configura:
   - **Key:** `TELEGRAM_BOT_TOKEN`
   - **Value:** `8573033645:AAG7CC8OB7KgymvZDjaTDS-yJKS0M60Wrg8`

---

### Paso 5: Crear y Esperar

1. Click en **"Create Background Worker"**
2. Render descargará el código del repositorio
3. Instalará las dependencias (2-3 minutos)
4. Iniciará el bot

---

## ✅ Verificar que Funciona

### En Render - Ver Logs:

1. Una vez creado, click en tu worker
2. Ve a la pestaña **"Logs"**
3. Deberías ver:
```
Iniciando bot...
✅ Bot iniciado correctamente
Presiona Ctrl+C para detener
Application started
```

### En Telegram:

1. Abre Telegram en tu móvil
2. Busca tu bot (el que creaste con @BotFather)
3. Envía: `/start`
4. Escribe: `Hola mundo | Autor`
5. Selecciona un estilo (ej: 🌈 Gradient)
6. **¡Deberías recibir tu imagen!** 🎉

---

## 🔄 Si Render Pide Conectar GitHub

Render tiene dos formas de trabajar:

### Opción A: Solo Para Este Proyecto
- Click en "Connect to GitHub"
- Autoriza SOLO para este proyecto
- No te preocupes, no afecta tus slots del plan gratuito

### Opción B: Railway (Más Fácil)
Si Render insiste en conectar GitHub y no quieres:

1. Ve a https://railway.app
2. Sign up con email (sin GitHub)
3. Sigue estas instrucciones más simples: [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md)

---

## 🐛 Problemas Comunes

### "Cannot access private repository"
→ Verifica que uses la URL correcta:
`https://github.com/agullita/instagram-quote-generator.git`

El repositorio es público, así que no debería pedir autenticación.

### "Build failed"
→ Ve a los logs y busca el error específico
→ Normalmente es porque falta el token en las variables de entorno

### "Bot no responde en Telegram"
→ Verifica en los logs que diga "✅ Bot iniciado correctamente"
→ Verifica que el token esté bien copiado (sin espacios)

### "Port binding error"
→ Creaste un **Web Service** en lugar de **Background Worker**
→ Elimínalo y crea uno nuevo como Background Worker

---

## 💡 Ventajas de Esta Solución

✅ **No necesitas conectar tu cuenta de GitHub a Render**  
✅ **El repositorio ya está actualizado con la configuración correcta**  
✅ **El `render.yaml` ya está configurado como Background Worker**  
✅ **Solo necesitas agregar el token y listo**

---

## 📱 Después del Deploy

Una vez funcionando, el bot estará:
- ✅ Corriendo 24/7 en la nube
- ✅ Respondiendo automáticamente en Telegram
- ✅ Generando imágenes para Instagram

⚠️ **Nota sobre el plan Free de Render:**
El servicio puede "dormirse" después de 15 minutos de inactividad, pero se despierta automáticamente cuando llega un mensaje (puede tardar 30-60 segundos la primera vez).

---

## 🎯 Resumen - 3 Pasos Esenciales

1. **New + → Background Worker**
2. **URL:** `https://github.com/agullita/instagram-quote-generator.git`
3. **Variable:** `TELEGRAM_BOT_TOKEN` = tu token

¡Y listo! 🚀
