# ⚡ Deploy Web en Render - Versión Rápida

## 🎯 5 Pasos - 5 Minutos

### 1️⃣ Ir a Render
👉 https://render.com/dashboard → **New +** → **Web Service**

---

### 2️⃣ Conectar Repo
📦 Pega esta URL:
```
https://github.com/agullita/instagram-quote-generator.git
```

---

### 3️⃣ Configuración (Copiar/Pegar)

| Campo | Valor |
|-------|-------|
| **Name** | `instagram-quote-generator` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Plan** | Free |

---

### 4️⃣ Crear
✅ Click **"Create Web Service"**  
⏱️ Espera 2-3 minutos

---

### 5️⃣ Probar
🌐 Abre la URL que te da Render  
🎨 Genera tu primera imagen

---

## 🎉 ¡LISTO!

Tu web está en: `https://tu-app.onrender.com`

---

## 📚 ¿Necesitas Más Detalles?

Ver guía completa: [DEPLOY-WEB-RENDER.md](DEPLOY-WEB-RENDER.md)

---

## ⚠️ Importante

- ✅ Se "duerme" tras 15 min sin uso (plan gratuito)
- ✅ Primera visita después de dormir: tarda ~30s en despertar
- ✅ Actualizaciones automáticas con cada `git push`

---

## 🐛 Si Algo Falla

**Build failed?**
→ Verifica que `gunicorn==21.2.0` esté en requirements.txt

**App no responde?**
→ Verifica Start Command: `gunicorn app:app` (NO `python app.py`)

**404 Not Found?**
→ Espera 30s, la app está despertando
