# 🚀 Guía de Inicio Rápido

## Instalación en 3 Pasos

### 1️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2️⃣ Iniciar la Aplicación

**Opción A - Usando el script de inicio (Windows):**
```bash
start.bat
```

**Opción B - Usando el script de inicio (macOS/Linux):**
```bash
chmod +x start.sh
./start.sh
```

**Opción C - Directamente con Python:**
```bash
python app.py
```

### 3️⃣ Abrir en el Navegador

Abre tu navegador y ve a: **http://localhost:5000**

---

## 🎨 Cómo Usar

1. **Escribe tu frase** en el área de texto
2. **Añade el autor** (opcional)
3. **Selecciona una plantilla** de diseño
4. **Haz clic en "Generar Imagen"**
5. **Descarga tu imagen** lista para Instagram

---

## 💡 Ejemplos de Frases

- "La vida es aquello que te va sucediendo mientras te empeñas en hacer otros planes." - John Lennon
- "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito." - Albert Schweitzer
- "No cuentes los días, haz que los días cuenten." - Muhammad Ali
- "La mejor manera de predecir el futuro es creándolo." - Peter Drucker

---

## 🎨 Plantillas Disponibles

- **Minimalista**: Fondo blanco, texto oscuro (profesional)
- **Oscuro Elegante**: Fondo oscuro, texto blanco (sofisticado)
- **Vibrante**: Naranja brillante (energético)
- **Océano**: Azul relajante (tranquilo)
- **Atardecer**: Tonos cálidos (romántico)
- **Bosque**: Verde natural (ecológico)

---

## ❓ Problemas Comunes

**Error: ModuleNotFoundError**
```bash
pip install Flask Pillow Werkzeug
```

**Error: Puerto 5000 ocupado**
- Edita `app.py` y cambia el puerto en la última línea
- Usa otro puerto como 5001, 8000, etc.

**Las imágenes no se generan**
- Verifica que la carpeta `output/` existe
- Asegúrate de tener permisos de escritura

---

## 📱 Especificaciones de las Imágenes

- **Tamaño**: 1080x1080 píxeles
- **Formato**: PNG
- **Calidad**: Alta (95%)
- **Peso aproximado**: 20-40 KB
- **Optimizado para**: Instagram Feed Posts

---

¿Necesitas más ayuda? Consulta el archivo `README.md` para documentación completa.
