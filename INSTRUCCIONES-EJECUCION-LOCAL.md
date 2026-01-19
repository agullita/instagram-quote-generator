# 🚀 Instrucciones para Ejecutar Localmente

## ✅ Estado del Proyecto
**El proyecto está 100% listo para ejecutarse localmente**

---

## 📋 Requisitos Previos
- ✅ Python 3.12.2 (instalado)
- ✅ Todas las dependencias instaladas
- ✅ Estructura de carpetas completa

---

## 🎯 Ejecutar la Aplicación Web

### Opción 1: Script de Inicio (Recomendado)
```bash
cd instagram-quote-generator
start.bat
```

### Opción 2: Comando Directo
```bash
cd instagram-quote-generator
python app.py
```

**El servidor iniciará en:** `http://localhost:5000`

---

## 🌐 Usar la Aplicación Web

1. **Abre tu navegador** y ve a: `http://localhost:5000`
2. **Escribe una frase** en el campo de texto
3. **Añade el autor** (opcional)
4. **Selecciona una plantilla**:
   - 🎯 Minimalista
   - 🌙 Oscuro
   - 🎨 Vibrante
   - 🌊 Océano
   - 🌅 Atardecer
   - 🌲 Bosque
   - 🔶 Geométrico Naranja
   - 📐 Geométrico Limpio
5. **Haz clic en "Generar Imagen"**
6. **Descarga tu imagen** (1080x1080px lista para Instagram)

---

## 🤖 Ejecutar el Bot de Telegram (Opcional)

### 1. Obtener Token de Telegram
1. Abre Telegram y busca **@BotFather**
2. Envía `/newbot`
3. Sigue las instrucciones (nombre y username del bot)
4. **Copia el token** que te proporciona

### 2. Configurar Token
Edita el archivo `.env` en la carpeta `instagram-quote-generator`:
```bash
TELEGRAM_BOT_TOKEN=TU_TOKEN_AQUI
```

### 3. Iniciar Bot
```bash
cd instagram-quote-generator
start_telegram_bot.bat
```

### 4. Usar el Bot
1. Busca tu bot en Telegram
2. Envía `/start` para ver las instrucciones
3. Envía cualquier frase y sigue el asistente

**Ejemplos de uso:**
- `"La vida es bella"` - Frase simple
- `"La vida es bella | Roberto"` - Con autor
- `"La vida es bella | Roberto #vida,bella"` - Con palabras destacadas

---

## 📁 Archivos Generados
Las imágenes se guardan en: `instagram-quote-generator/output/`

---

## 🛑 Detener el Servidor
Presiona **CTRL+C** en la terminal donde está corriendo

---

## 🔧 Solución de Problemas

### Puerto 5000 ocupado
Edita `app.py` línea 329:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Cambiar a 5001
```

### Error de permisos
Ejecuta la terminal como **Administrador**

### No se generan imágenes
Verifica que la carpeta `output/` existe y tiene permisos de escritura

---

## ✅ Verificación de Instalación

### Probar generación de imagen:
```bash
cd instagram-quote-generator
python -c "from image_generator import InstagramQuoteGenerator; g = InstagramQuoteGenerator(); print(g.generate_image('Prueba exitosa', 'minimal'))"
```

Deberías ver: `✅ output/quote_minimal_TIMESTAMP.png`

---

## 📊 Características Disponibles

### Aplicación Web:
- ✅ Generación de imágenes únicas
- ✅ Generación de carruseles
- ✅ 8 plantillas de diseño
- ✅ Palabras destacadas
- ✅ Preview en tiempo real
- ✅ Descarga directa

### Bot de Telegram:
- ✅ Generación desde chat
- ✅ Interfaz interactiva con botones
- ✅ Carruseles de hasta 10 imágenes
- ✅ Mismas plantillas que la web

---

## 🌍 Siguiente Paso: Subir a Servidor

Una vez que compruebes que funciona localmente, estarás listo para:
- 🚀 Desplegar en Render
- 🚀 Desplegar en Railway
- 🚀 Desplegar en Vercel
- 🚀 Desplegar en servidor propio

**El proyecto incluye guías de deployment para todas estas plataformas.**

---

## 💡 Consejos

1. **Para desarrollo**: Usa `python app.py` (modo debug activo)
2. **Para pruebas de producción**: Usa `gunicorn app:app`
3. **Bot de Telegram**: Puede correr simultáneamente con la web
4. **Imágenes pesadas**: Revisa la carpeta `output/` periódicamente

---

## 📞 Soporte
Si tienes problemas, verifica:
1. ✅ Python instalado: `python --version`
2. ✅ Dependencias instaladas: `pip list | findstr Flask`
3. ✅ Carpetas existen: `output/`, `backgrounds/`
4. ✅ Puerto disponible: 5000

---

**¡Todo listo para empezar! 🎉**
