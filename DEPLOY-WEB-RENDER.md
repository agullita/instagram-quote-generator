# 🌐 Deploy Web en Render - Guía Completa

## 🎯 Lo Que Vamos a Hacer

Publicar tu aplicación web de generación de imágenes para Instagram en Render, accesible desde cualquier lugar con una URL pública.

**Resultado final:** `https://tu-app.onrender.com`

---

## ⏱️ Tiempo Estimado: 5 minutos

---

## 📋 Antes de Empezar

Verifica que tengas:
- ✅ Cuenta en Render.com (gratis, sin tarjeta)
- ✅ El código está en GitHub: `https://github.com/agullita/instagram-quote-generator.git`

---

## 🚀 PASO A PASO

### 1️⃣ Ir a Render

1. Abre: https://render.com/dashboard
2. Inicia sesión con tu cuenta

---

### 2️⃣ Crear Web Service

1. Click en **"New +"** (arriba a la derecha)
2. Selecciona **"Web Service"** ⚠️ (Esta vez SÍ Web Service, NO Worker)

---

### 3️⃣ Conectar Repositorio

**Opción A: Si Render NO está conectado con GitHub**
1. Busca la opción "Public Git repository"
2. Pega la URL: `https://github.com/agullita/instagram-quote-generator.git`
3. Click "Continue"

**Opción B: Si puedes conectar GitHub**
1. Click "Connect a repository"
2. Busca: `agullita/instagram-quote-generator`
3. Click "Connect"

---

### 4️⃣ Configuración del Servicio

Copia y pega exactamente estos valores:

#### **Información Básica**

| Campo | Valor |
|-------|-------|
| **Name** | `instagram-quote-generator` |
| **Region** | `Frankfurt` (o el más cercano a ti) |
| **Branch** | `main` |
| **Root Directory** | *(dejar vacío)* |

#### **Build & Deploy**

| Campo | Valor |
|-------|-------|
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |

⚠️ **IMPORTANTE**: El Start Command debe ser `gunicorn app:app` (NO `python app.py`)

#### **Instance Type**

| Campo | Valor |
|-------|-------|
| **Plan** | `Free` |

---

### 5️⃣ Variables de Entorno (Opcional)

No necesitas configurar variables de entorno para la versión web.

Si en el futuro quieres agregar alguna:
1. Click en **"Advanced"**
2. Busca **"Environment Variables"**
3. Add Environment Variable

---

### 6️⃣ Crear el Servicio

1. Revisa que todo esté correcto
2. Click en **"Create Web Service"**
3. ☕ Espera 2-3 minutos mientras Render:
   - Descarga el código
   - Instala las dependencias
   - Inicia el servidor

---

### 7️⃣ Verificar el Deploy

#### En Render - Ver el Progreso:

Verás una pantalla con logs en tiempo real. Busca:

```
==> Downloading Repo...
==> Building...
==> Installing dependencies from requirements.txt
==> Starting server...
[INFO] Starting gunicorn
[INFO] Listening at: http://0.0.0.0:10000
==> Your service is live 🎉
```

#### Obtener tu URL:

En la parte superior verás tu URL pública:
```
https://instagram-quote-generator-XXXX.onrender.com
```

---

### 8️⃣ Probar la Aplicación

1. **Copia la URL** que te dio Render
2. **Ábrela en tu navegador**
3. Deberías ver la interfaz del generador de imágenes
4. **Prueba:**
   - Escribe una frase: "La vida es bella"
   - Elige un estilo: 🌈 Gradient
   - Click en "Generar"
   - ¡Descarga tu imagen!

---

## ✅ ¡LISTO! Tu Web está Online

Tu aplicación ahora está disponible en:
```
https://tu-app.onrender.com
```

Compártela con quien quieras 🎉

---

## 🔄 Actualizaciones Automáticas

Cada vez que hagas `git push` a GitHub, Render detectará los cambios y actualizará tu web automáticamente.

```bash
# En tu computadora
cd instagram-quote-generator
git add .
git commit -m "Nueva funcionalidad"
git push origin main

# Render automáticamente hará re-deploy
```

---

## ⚠️ Importante: Plan Gratuito

### Limitaciones del Plan Free:

- **Se "duerme" tras 15 minutos sin uso**
  - Primera visita después de dormir: tarda 30-60 segundos en despertar
  - Después funciona normal
  
- **Tiempo de construcción:** 750 horas/mes (más que suficiente)

### ¿Cómo Evitar que se Duerma?

**Opción 1: Upgrade a plan Starter ($7/mes)**
- No se duerme nunca
- Más rápido

**Opción 2: Usar un "pinger"** (gratuito)
- UptimeRobot.com
- Hace ping cada 5 minutos
- Mantiene la app despierta

---

## 🐛 Solución de Problemas

### Error: "Build failed"

**Causa:** Problemas instalando dependencias

**Solución:**
1. Ve a los logs
2. Busca qué dependencia falló
3. Verifica que `requirements.txt` esté correcto

---

### Error: "Application failed to respond"

**Causa:** La app no está escuchando en el puerto correcto

**Solución:**
1. Verifica que Start Command sea: `gunicorn app:app`
2. No uses `python app.py` en producción

---

### Error: "ModuleNotFoundError"

**Causa:** Falta alguna dependencia en requirements.txt

**Solución:**
1. Verifica que `gunicorn==21.2.0` esté en requirements.txt
2. Haz un nuevo deploy manual si es necesario

---

### La web carga pero no genera imágenes

**Causa:** Faltan las carpetas o archivos

**Solución:**
1. Verifica que existan estas carpetas en GitHub:
   - `backgrounds/`
   - `output/`
   - `templates/`
2. Verifica que haya archivos en `backgrounds/`

---

### "Service Unavailable" al abrir la URL

**Causa:** La app está "dormida" (plan gratuito)

**Solución:**
- Espera 30-60 segundos
- Recarga la página
- Debería despertar automáticamente

---

## 📊 Monitoreo

### Ver Logs en Tiempo Real:

1. Ve a tu servicio en Render
2. Click en **"Logs"** (pestaña superior)
3. Verás todas las peticiones y errores

### Ver Métricas:

1. Pestaña **"Metrics"**
2. CPU, memoria, requests

---

## 🎨 Personalizar el Dominio (Opcional)

Si quieres tu propio dominio (ej: `migenera dor.com`):

1. Compra un dominio (Namecheap, GoDaddy, etc.)
2. En Render → Settings → Custom Domain
3. Agrega tu dominio
4. Configura los DNS según las instrucciones

**Costo:** Solo el dominio (~$10/año), Render sigue siendo gratis

---

## 📱 Compartir tu Aplicación

Ahora puedes compartir tu generador:

- ✅ En redes sociales
- ✅ Con amigos y familia
- ✅ En tu portfolio
- ✅ En tu CV como proyecto

**Ejemplo:**
"Creé un generador de imágenes para Instagram: https://mi-app.onrender.com"

---

## 🚀 Próximos Pasos (Opcional)

### Mejoras que puedes hacer:

1. **Agregar más estilos** de diseño
2. **Más fondos personalizados**
3. **Login de usuarios** (guardar diseños favoritos)
4. **API pública** para otros desarrolladores
5. **Analytics** (Google Analytics)
6. **Compartir directo a Instagram** (usando su API)

---

## 💡 Resumen de URLs Importantes

| Recurso | URL |
|---------|-----|
| **Dashboard Render** | https://render.com/dashboard |
| **Tu Web** | https://tu-app.onrender.com |
| **Logs** | Dashboard → Tu servicio → Logs |
| **Settings** | Dashboard → Tu servicio → Settings |
| **GitHub Repo** | https://github.com/agullita/instagram-quote-generator |

---

## 🎯 Checklist Final

- [ ] Web Service creado en Render
- [ ] Build completado exitosamente
- [ ] URL pública funcionando
- [ ] Probado generar una imagen
- [ ] Guardada la URL de tu app
- [ ] (Opcional) Configurado pinger para evitar sleep
- [ ] (Opcional) Compartida en redes sociales

---

## 🎉 ¡Felicidades!

Tu aplicación web está online y lista para usar. Ahora cualquiera puede generar imágenes para Instagram desde tu web.

---

## ❓ ¿Necesitas Ayuda?

Si tienes problemas:
1. Revisa los logs en Render
2. Busca el error específico en esta guía
3. Verifica que seguiste todos los pasos

**Tu app está lista para compartir al mundo** 🌍✨
