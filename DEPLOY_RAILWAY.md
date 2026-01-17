# 🚀 Guía de Despliegue en Railway

## 📋 Requisitos Previos
- Cuenta de GitHub (gratuita)
- Cuenta de Railway (gratuita - $5 de crédito inicial)

---

## 🎯 Pasos para Desplegar

### **Paso 1: Preparar el Repositorio en GitHub**

1. **Crear repositorio en GitHub:**
   - Ve a https://github.com/new
   - Nombre: `instagram-quote-generator` (o el que prefieras)
   - Público o Privado (ambos funcionan)
   - NO inicialices con README (ya tienes archivos)
   - Click en "Create repository"

2. **Subir tu código a GitHub:**
   ```bash
   cd instagram-quote-generator
   
   # Inicializar git (si no está inicializado)
   git init
   
   # Añadir todos los archivos
   git add .
   
   # Hacer commit
   git commit -m "Initial commit - Instagram Quote Generator Bot"
   
   # Conectar con tu repositorio (reemplaza con tu usuario)
   git remote add origin https://github.com/TU_USUARIO/instagram-quote-generator.git
   
   # Subir a GitHub
   git branch -M main
   git push -u origin main
   ```

---

### **Paso 2: Crear Cuenta en Railway**

1. Ve a https://railway.app
2. Click en "Login" → "Login with GitHub"
3. Autoriza Railway para acceder a tu GitHub
4. ¡Listo! Tienes $5 de crédito gratis

---

### **Paso 3: Crear Nuevo Proyecto en Railway**

1. En Railway, click en "New Project"
2. Selecciona "Deploy from GitHub repo"
3. Autoriza Railway a acceder a tus repositorios
4. Selecciona tu repositorio `instagram-quote-generator`
5. Railway empezará a desplegar automáticamente

---

### **Paso 4: Configurar Variables de Entorno**

⚠️ **MUY IMPORTANTE**: Debes configurar el token del bot

1. En Railway, ve a tu proyecto
2. Click en la pestaña "Variables"
3. Click en "New Variable"
4. Añade:
   - **Variable**: `TELEGRAM_BOT_TOKEN`
   - **Value**: `8573033645:AAG7CC8OB7KgymvZDjaTDS-yJKS0M60Wrg8`
5. Click en "Add"

Railway redesplegará automáticamente con la nueva variable.

---

### **Paso 5: Verificar que Funciona**

1. Ve a la pestaña "Deployments" en Railway
2. Verifica que el estado sea "Success" ✅
3. Click en "View Logs" para ver los logs en tiempo real
4. Deberías ver: `✅ Bot iniciado correctamente`

5. **Probar el bot:**
   - Abre Telegram
   - Busca tu bot
   - Envía `/start`
   - ¡Debería responder! 🎉

---

## 🔄 Actualizar el Bot (Despliegue Continuo)

Una vez configurado, actualizar es MUY fácil:

1. **Haz cambios** en tu código local
2. **Commit y push:**
   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   git push
   ```
3. **Railway detecta el push** y redespliega automáticamente ✨
4. **En 1-2 minutos** tu bot ya tiene los cambios

---

## 📊 Monitoreo

### **Ver Logs en Tiempo Real:**
1. Ve a Railway → Tu Proyecto
2. Click en "View Logs"
3. Verás todos los mensajes y errores

### **Verificar Uso de Recursos:**
1. Ve a Railway → Tu Proyecto
2. Click en "Metrics"
3. Verás uso de CPU, RAM, y créditos

### **Crédito Gratuito:**
- Railway da $5/mes gratis
- Un bot de Telegram consume ~$0.50-1/mes
- ¡Suficiente para mantenerlo gratis! 🎉

---

## 🛠️ Solución de Problemas

### **El bot no responde:**
1. Verifica los logs en Railway
2. Asegúrate de que `TELEGRAM_BOT_TOKEN` esté configurado
3. Verifica que el deployment sea exitoso (✅)

### **Error "Token inválido":**
- Revisa que el token en Variables sea correcto
- Copia el token completo sin espacios

### **Se acabó el crédito:**
- Railway te notificará por email
- Puedes añadir una tarjeta para continuar (~$1/mes)
- O migrar a Render (plan gratuito con limitaciones)

### **El bot se detiene después de un tiempo:**
- Railway mantiene el bot activo 24/7
- Si se detiene, revisa los logs para ver el error
- Puede ser un error en el código o falta de memoria

---

## 🎨 Funcionalidades Desplegadas

✅ Bot de Telegram con todas las funcionalidades:
- Generación de imágenes únicas
- Palabras destacadas
- 8 plantillas (incluyendo fondos personalizados)
- Generación de carruseles
- Respuestas en tiempo real

✅ Despliegue automático con Git
✅ Logs en tiempo real
✅ 99.9% uptime
✅ Gratis (con $5 de crédito)

---

## 📈 Próximos Pasos (Opcional)

### **Añadir la App Web:**
1. En Railway, click en "New Service"
2. Selecciona el mismo repositorio
3. En Variables, añade:
   - `PORT` = `5000`
4. En Settings, cambia el Start Command a: `python app.py`
5. Railway te dará una URL pública para la web

### **Dominio Personalizado:**
1. En Railway, ve a Settings
2. Click en "Generate Domain"
3. Railway te da un dominio: `tu-bot.up.railway.app`
4. O conecta tu propio dominio

---

## 💰 Costos Estimados

- **Plan Gratuito**: $5/mes de crédito
- **Bot solo**: ~$0.50-1/mes
- **Bot + Web**: ~$2-3/mes
- **Con tráfico alto**: ~$5-10/mes

**Recomendación**: Empieza con el plan gratuito. Si necesitas más, Railway es muy económico.

---

## 🎯 Resumen

1. ✅ Sube código a GitHub
2. ✅ Conecta Railway con GitHub
3. ✅ Configura `TELEGRAM_BOT_TOKEN`
4. ✅ ¡Tu bot está en la nube 24/7!
5. ✅ Para actualizar: solo haz `git push`

---

## 🆘 Ayuda

- **Documentación Railway**: https://docs.railway.app
- **Soporte Railway**: https://railway.app/discord
- **Telegram Bot API**: https://core.telegram.org/bots/api

---

**¡Tu bot estará funcionando 24/7 sin necesidad de tu ordenador! 🚀**
