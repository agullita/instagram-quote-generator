# 🚀 Guía de Despliegue en Render

## ⚠️ ERROR COMÚN: "Port binding failed"

Si ves este error es porque seleccionaste **Web Service** en lugar de **Background Worker**.

**Solución:**
1. Elimina el servicio actual
2. Crea uno nuevo pero selecciona **"Background Worker"**
3. Los bots de Telegram NO exponen puertos HTTP, por eso deben ser Background Workers

---

## 📋 Ventajas de Render

- ✅ **100% GRATIS** (no necesita tarjeta)
- ✅ **Actualización automática** con Git
- ✅ **Fácil de usar**
- ✅ **Logs en tiempo real**
- ⚠️ Nota: El servicio gratuito puede "dormir" tras 15 min de inactividad, pero se reactiva automáticamente cuando llega un mensaje

---

## 🎯 Pasos para Desplegar

### **Paso 1: Crear Cuenta en Render**

1. Ve a https://render.com
2. Click en **"Get Started"**
3. Selecciona **"Sign in with GitHub"**
4. Autoriza Render para acceder a tus repositorios

---

### **Paso 2: Crear Nuevo Background Worker**

⚠️ **IMPORTANTE**: Un bot de Telegram debe ser **Background Worker**, NO Web Service.

1. En el Dashboard de Render, click en **"New +"**
2. Selecciona **"Background Worker"** (NO Web Service)
3. Click en **"Connect a repository"**
4. Busca y selecciona tu repositorio
5. Click en **"Connect"**

---

### **Paso 3: Configurar el Servicio**

En la página de configuración, ajusta lo siguiente:

#### **Información Básica:**
- **Name**: `instagram-quote-bot` (o el que prefieras)
- **Region**: `Frankfurt` (o el más cercano a ti)
- **Branch**: `main`
- **Root Directory**: (dejar vacío)

#### **Build & Deploy:**
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python telegram_bot.py`

⚠️ **NOTA**: Los Background Workers NO necesitan configurar puerto, eso es solo para Web Services.

#### **Plan:**
- Selecciona **"Free"** ($0/month)

---

### **Paso 4: Configurar Variables de Entorno** ⚠️ **MUY IMPORTANTE**

Antes de hacer deploy, configura la variable de entorno:

1. Baja hasta la sección **"Environment Variables"**
2. Click en **"Add Environment Variable"**
3. Añade:
   - **Key**: `TELEGRAM_BOT_TOKEN`
   - **Value**: `8573033645:AAG7CC8OB7KgymvZDjaTDS-yJKS0M60Wrg8`
4. **NO marques** "Secret File" (déjalo como está)

---

### **Paso 5: Deploy**

1. Click en **"Create Web Service"**
2. Render comenzará a desplegar tu bot
3. Esto toma 2-3 minutos la primera vez

---

### **Paso 6: Verificar que Funciona**

1. Espera a que el estado cambie a **"Live" 🟢**
2. Click en **"Logs"** en el menú lateral
3. Deberías ver: `✅ Bot iniciado correctamente`

4. **Prueba el bot en Telegram:**
   - Abre Telegram
   - Busca tu bot
   - Envía `/start`
   - ¡Debería responder! 🎉

---

## 🔄 Actualizar el Bot

Una vez desplegado, actualizar es muy fácil:

1. **Haz cambios** en tu código local
2. **Commit y push:**
   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   git push
   ```
3. **Render detecta el push** y redespliega automáticamente ✨
4. **En 2-3 minutos** tu bot tiene los cambios

---

## 📊 Monitoreo

### **Ver Logs:**
1. Ve a Render Dashboard → Tu Servicio
2. Click en **"Logs"**
3. Verás todos los mensajes en tiempo real

### **Verificar Estado:**
- **🟢 Live**: Bot funcionando
- **🟡 Building**: Desplegando cambios
- **🔴 Failed**: Error (revisa los logs)

### **Restart Manual:**
Si necesitas reiniciar:
1. Ve a tu servicio
2. Click en **"Manual Deploy"** → **"Deploy latest commit"**

---

## ⚠️ Limitaciones del Plan Gratuito

### **"Sleep" después de 15 minutos:**
- El servicio gratuito "duerme" tras 15 min sin actividad
- Se reactiva **automáticamente** cuando llega un mensaje
- Primera respuesta puede tardar 30-60 segundos (luego es instantáneo)

### **Solución:**
Si quieres evitar el "sleep", puedes:
1. **Usar un servicio de ping** (UptimeRobot) que haga ping cada 10 min
2. **Upgrade a plan pagado** ($7/mes) - el bot estará 100% activo

### **Horas mensuales:**
- Plan gratuito: 750 horas/mes
- Suficiente para un bot que funcione 24/7

---

## 🛠️ Solución de Problemas

### **El bot no responde:**
1. Verifica los logs en Render
2. Asegúrate de que `TELEGRAM_BOT_TOKEN` esté configurado correctamente
3. Verifica que el estado sea "Live" 🟢

### **Error "Token inválido":**
- Ve a Environment → Edita `TELEGRAM_BOT_TOKEN`
- Verifica que no haya espacios extra

### **El servicio falla al iniciar:**
- Revisa los logs
- Verifica que `requirements.txt` tenga todas las dependencias
- Asegúrate de que el Start Command sea: `python telegram_bot.py`

### **Primera respuesta muy lenta:**
- Es normal en plan gratuito (el servicio estaba "dormido")
- Respuestas siguientes serán instantáneas
- Considera usar UptimeRobot para mantenerlo activo

---

## 💡 Tips Adicionales

### **Mantener el Bot Activo (sin upgrade):**

1. Ve a https://uptimerobot.com (gratis)
2. Crea cuenta
3. Add New Monitor:
   - **Type**: HTTP(s)
   - **URL**: Tu URL de Render (ej: `https://instagram-quote-bot.onrender.com`)
   - **Interval**: 10 minutos
4. Esto hace "ping" al bot cada 10 min y evita que duerma

### **Variables de Entorno Adicionales:**

Si en el futuro necesitas más variables:
1. Ve a Environment
2. Add Environment Variable
3. El servicio se redesplegará automáticamente

---

## 📈 Upgrade Opcional

Si necesitas:
- ✅ Sin "sleep" (100% uptime)
- ✅ Más recursos (RAM/CPU)
- ✅ Prioridad en soporte

Puedes hacer upgrade a **Starter Plan** ($7/mes)

---

## 🎯 Resumen Rápido

1. ✅ Crear cuenta en Render (con GitHub)
2. ✅ New Web Service → Conectar repositorio
3. ✅ Configurar: Build Command y Start Command
4. ✅ Añadir variable: `TELEGRAM_BOT_TOKEN`
5. ✅ Deploy
6. ✅ ¡Bot funcionando 24/7 gratis!

---

## 🆘 Ayuda

- **Documentación Render**: https://render.com/docs
- **Soporte Render**: https://render.com/support
- **Telegram Bot API**: https://core.telegram.org/bots/api

---

**¡Tu bot estará en la nube 24/7 completamente gratis! 🚀**
