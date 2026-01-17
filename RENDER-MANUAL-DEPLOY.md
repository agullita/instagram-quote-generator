# 🚀 Deploy Manual en Render (Sin GitHub)

## 📋 Requisitos
- Cuenta en Render (nueva sin GitHub conectado)
- Token de Bot de Telegram
- Acceso a esta carpeta del proyecto

---

## 🎯 Pasos para Deploy Manual

### Paso 1: Preparar los Archivos

En esta carpeta (`instagram-quote-generator`) ya tienes todo listo:
- ✅ `telegram_bot.py` - El bot
- ✅ `image_generator.py` - Generador de imágenes
- ✅ `carousel_generator.py` - Generador de carruseles
- ✅ `requirements.txt` - Dependencias
- ✅ `backgrounds/` - Fondos para las imágenes

---

### Paso 2: Comprimir el Proyecto

**Windows PowerShell:**
```powershell
# Desde la carpeta instagram-quote-generator
Compress-Archive -Path * -DestinationPath ../instagram-bot-deploy.zip -Force
```

**O manualmente:**
1. Selecciona todos los archivos de la carpeta `instagram-quote-generator`
2. Click derecho → "Enviar a" → "Carpeta comprimida"
3. Nombra el archivo: `instagram-bot-deploy.zip`

⚠️ **IMPORTANTE**: Comprime el CONTENIDO de la carpeta, no la carpeta misma.

---

### Paso 3: Crear Background Worker en Render

1. Ve a https://render.com/dashboard
2. Click en **"New +"** (arriba derecha)
3. Selecciona **"Background Worker"** (NO Web Service)

---

### Paso 4: Configurar el Worker

En la pantalla de configuración:

#### **Deployment Method:**
- Selecciona: **"Deploy from Git repository"** 
- Pero como NO tienes GitHub conectado, busca la opción **"Public Git repository"** o **"Private repository"**

**Alternativa si no puedes conectar repositorio:**
Render requiere un repositorio Git. Tienes 3 opciones:

1. **Conectar GitHub a esta nueva cuenta** (recomendado)
2. **Usar GitLab o Bitbucket** y subir el código ahí
3. **Crear un repositorio público en GitHub** sin conectar la cuenta

---

### Paso 5: Configuración del Worker

Una vez conectado el repositorio:

**Name:** `instagram-quote-bot`  
**Region:** Frankfurt (o el más cercano)  
**Branch:** main  
**Root Directory:** (dejar vacío)

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
python telegram_bot.py
```

**Plan:** Free

---

### Paso 6: Variables de Entorno

Antes de crear el worker, agrega la variable de entorno:

Click en **"Advanced"** → **"Add Environment Variable"**

- **Key:** `TELEGRAM_BOT_TOKEN`
- **Value:** `8573033645:AAG7CC8OB7KgymvZDjaTDS-yJKS0M60Wrg8`

---

### Paso 7: Crear y Deploy

1. Click en **"Create Background Worker"**
2. Render empezará a construir el proyecto
3. Espera 2-3 minutos

---

## ✅ Verificar que Funciona

### En los Logs de Render:
Deberías ver:
```
Iniciando bot...
✅ Bot iniciado correctamente
Presiona Ctrl+C para detener
Application started
```

### En Telegram:
1. Abre Telegram
2. Busca tu bot
3. Envía: `/start`
4. Escribe una frase
5. Selecciona un estilo
6. ¡Deberías recibir tu imagen!

---

## 🐛 Solución de Problemas

### "No git repository found"
→ Render NECESITA un repositorio Git. Opciones:
- Conecta tu GitHub a la nueva cuenta de Render
- Sube el código a GitLab/Bitbucket
- Crea un repo público en GitHub

### "Build failed"
→ Verifica que `requirements.txt` esté en la raíz del proyecto

### "Module not found"
→ Verifica el Build Command: `pip install -r requirements.txt`

### "Bot no responde"
→ Verifica que el token sea correcto en las Environment Variables

---

## 💡 Recomendación

**La forma más fácil es conectar GitHub:**

1. En Render → Account Settings → Connected Accounts
2. Connect GitHub
3. Autoriza Render
4. Luego podrás hacer deploy desde tu repositorio

Esto permite:
- ✅ Actualización automática al hacer `git push`
- ✅ Ver commits en el dashboard
- ✅ Rollback fácil si algo falla
- ✅ No necesitas subir archivos manualmente

---

## 🚀 Alternativa: Railway

Si Render te da problemas sin GitHub, Railway también es gratis y muy fácil:
Ver: [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md)
