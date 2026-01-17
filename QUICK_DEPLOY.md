# 🚀 Despliegue Rápido en Railway

## ⚡ Comandos Rápidos (Copiar y Pegar)

### **1. Inicializar Git y Subir a GitHub**

```bash
cd instagram-quote-generator

# Inicializar Git
git init

# Añadir todos los archivos
git add .

# Hacer commit
git commit -m "Initial commit - Instagram Quote Generator Bot"

# Conectar con GitHub (REEMPLAZA con tu usuario y repo)
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git

# Subir a GitHub
git branch -M main
git push -u origin main
```

---

### **2. Desplegar en Railway**

1. Ve a https://railway.app
2. Login con GitHub
3. Click en "New Project" → "Deploy from GitHub repo"
4. Selecciona tu repositorio
5. **Configura la variable de entorno:**
   - Nombre: `TELEGRAM_BOT_TOKEN`
   - Valor: `8573033645:AAG7CC8OB7KgymvZDjaTDS-yJKS0M60Wrg8`

---

### **3. Actualizar el Bot (después del despliegue inicial)**

```bash
# Hacer cambios en tu código
# Luego:

git add .
git commit -m "Descripción de tus cambios"
git push
```

**¡Railway desplegará automáticamente!** ✨

---

## 📋 Archivos Creados para Railway

✅ `Procfile` - Define cómo ejecutar el bot
✅ `runtime.txt` - Versión de Python
✅ `railway.json` - Configuración de Railway
✅ `.gitignore` - Archivos a ignorar
✅ `requirements.txt` - Dependencias actualizadas
✅ `.env` - Variables locales (NO se sube a Git)

---

## 🎯 Checklist Rápido

- [ ] Crear repositorio en GitHub
- [ ] Subir código con `git push`
- [ ] Crear cuenta en Railway
- [ ] Conectar repositorio
- [ ] Configurar `TELEGRAM_BOT_TOKEN`
- [ ] ¡Verificar que funciona!

---

## 🆘 Si algo falla

1. **Verifica los logs** en Railway → View Logs
2. **Verifica el token** esté bien configurado
3. **Lee la guía completa** en `DEPLOY_RAILWAY.md`

---

**Tiempo estimado: 10-15 minutos** ⏱️
**Costo: GRATIS** ($5 de crédito incluido) 💰
