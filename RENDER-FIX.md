# 🔧 Solución al Error de Deploy en Render

## ❌ Problema

Has intentado desplegar el bot como **Web Service** y te sale un error de puerto (port binding).

## ✅ Solución Rápida

### Paso 1: Eliminar el Servicio Actual
1. Ve a tu Dashboard de Render
2. Busca el servicio que creaste
3. Click en el servicio → Settings (abajo a la izquierda)
4. Scroll hasta el final → Click en **"Delete Web Service"**
5. Confirma la eliminación

### Paso 2: Crear Nuevo Background Worker
1. En el Dashboard, click en **"New +"**
2. **IMPORTANTE**: Selecciona **"Background Worker"** (NO Web Service)
3. Conecta tu repositorio
4. Configura:
   - **Name**: `instagram-quote-bot`
   - **Region**: Frankfurt (o el más cercano)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python telegram_bot.py`
   - **Plan**: Free

### Paso 3: Configurar Variable de Entorno
1. En la página de configuración, busca **"Environment Variables"**
2. Click en **"Add Environment Variable"**
3. Agrega:
   - **Key**: `TELEGRAM_BOT_TOKEN`
   - **Value**: Tu token de @BotFather (ejemplo: `1234567890:ABCdefGHI...`)

### Paso 4: Deploy
1. Click en **"Create Background Worker"**
2. Espera a que termine el build (2-3 minutos)
3. Verifica en los logs que dice: `✅ Bot iniciado correctamente`

---

## 🎯 ¿Por qué Background Worker?

**Web Services** → Para aplicaciones web que reciben peticiones HTTP (necesitan puerto)
- Ejemplos: APIs REST, sitios web, webhooks

**Background Workers** → Para procesos que corren constantemente en segundo plano
- Ejemplos: Bots de Telegram, procesadores de colas, tareas programadas

Los bots de Telegram usan **polling** (preguntan constantemente al servidor de Telegram por nuevos mensajes), NO reciben peticiones HTTP directas, por eso deben ser Background Workers.

---

## 📱 Verificar que Funciona

1. Abre Telegram
2. Busca tu bot
3. Envía: `/start`
4. Escribe una frase
5. Selecciona un estilo
6. ¡Deberías recibir tu imagen!

---

## 🐛 Si Sigue Sin Funcionar

### Ver los Logs
1. En Render, abre tu Background Worker
2. Click en "Logs" (arriba)
3. Busca errores en rojo

### Errores Comunes

**"Token is invalid"**
→ Verifica que copiaste bien el token de @BotFather (sin espacios)

**"ModuleNotFoundError"**
→ Verifica que el Build Command sea: `pip install -r requirements.txt`

**"No module named 'telegram'"**
→ El build no se completó correctamente, intenta hacer un nuevo deploy

---

## 📚 Más Información

- Ver: [DEPLOY_RENDER.md](DEPLOY_RENDER.md) - Guía completa actualizada
- Ver: [QUICK_START_TELEGRAM.md](QUICK_START_TELEGRAM.md) - Para correr local

---

## 💡 Alternativas

Si Render no te funciona, puedes usar:
- **Railway** → Ver [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md)
- **Local** → Ejecuta `start_telegram_bot.bat` en tu computadora
- **VPS** → Cualquier servidor con Python 3.12+
