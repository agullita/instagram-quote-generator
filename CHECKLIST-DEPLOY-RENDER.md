# ✅ Checklist para Deploy en Render

## 📋 Información que Necesitas

Antes de empezar, ten a mano:

- [ ] **URL del repositorio:** `https://github.com/agullita/instagram-quote-generator.git`
- [ ] **Token del bot:** `8573033645:AAG7CC8OB7KgymvZDjaTDS-yJKS0M60Wrg8`
- [ ] **Acceso a Render:** https://render.com/dashboard (con tu nueva cuenta)

---

## 🚀 Pasos de Deploy (Copiar y Pegar)

### 1️⃣ Crear Background Worker
- [ ] Ir a: https://render.com/dashboard
- [ ] Click: **"New +"**
- [ ] Seleccionar: **"Background Worker"** (NO Web Service)

### 2️⃣ Conectar Repositorio
- [ ] Pegar URL del repo: `https://github.com/agullita/instagram-quote-generator.git`
- [ ] O conectar GitHub si lo pide (solo este proyecto)

### 3️⃣ Configuración Básica
Copiar y pegar exactamente:

| Campo | Valor |
|-------|-------|
| **Name** | `instagram-quote-bot` |
| **Region** | `Frankfurt` |
| **Branch** | `main` |
| **Root Directory** | *(dejar vacío)* |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python telegram_bot.py` |
| **Plan** | `Free` |

### 4️⃣ Variable de Entorno
- [ ] Buscar sección: **"Environment Variables"**
- [ ] Click: **"Add Environment Variable"**
- [ ] **Key:** `TELEGRAM_BOT_TOKEN`
- [ ] **Value:** `8573033645:AAG7CC8OB7KgymvZDjaTDS-yJKS0M60Wrg8`

### 5️⃣ Deploy
- [ ] Click: **"Create Background Worker"**
- [ ] Esperar 2-3 minutos

### 6️⃣ Verificar Logs
- [ ] Click en tu worker
- [ ] Ir a pestaña **"Logs"**
- [ ] Debe mostrar: `✅ Bot iniciado correctamente`

### 7️⃣ Probar en Telegram
- [ ] Abrir Telegram
- [ ] Buscar tu bot
- [ ] Enviar: `/start`
- [ ] Escribir una frase: `Hola mundo | Autor`
- [ ] Seleccionar estilo: 🌈 Gradient
- [ ] **¡Recibir imagen!** 🎉

---

## ⚠️ Si Algo Sale Mal

### Error: "Port binding failed"
❌ Creaste un **Web Service** en lugar de **Background Worker**
✅ Solución: Elimínalo y crea uno nuevo como **Background Worker**

### Error: "Token is invalid"
❌ Token mal copiado o con espacios
✅ Solución: Verifica el token en Environment Variables

### Error: "Module not found"
❌ Build Command incorrecto
✅ Solución: Debe ser exactamente: `pip install -r requirements.txt`

### Bot no responde en Telegram
❌ El bot no está corriendo o hay error en los logs
✅ Solución: Ve a Logs en Render y busca errores en rojo

---

## 📞 ¿Necesitas Ayuda?

Si tienes algún problema:
1. Copia el error de los logs
2. Revisa: [DEPLOY-SIN-GITHUB.md](DEPLOY-SIN-GITHUB.md)
3. O prueba Railway: [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md)

---

## 🎯 Configuración Verificada

✅ `render.yaml` configurado como `worker`  
✅ `requirements.txt` con todas las dependencias  
✅ `telegram_bot.py` listo para ejecutar  
✅ Fondos e imágenes incluidas  
✅ Token configurado  

**Todo está listo para el deploy** 🚀
