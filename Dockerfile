# Dockerfile para Instagram Quote Generator
# Optimizado para Fly.io

FROM python:3.12-slim

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

# Instalar dependencias del sistema necesarias para Pillow
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar requirements primero (para cache de Docker)
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Crear carpetas necesarias
RUN mkdir -p output output/carousels

# Exponer puerto
EXPOSE 8080

# Comando por defecto (arrancar aplicación web)
# Para bot de Telegram, cambiar a: CMD ["python", "telegram_bot.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "120", "app:app"]
