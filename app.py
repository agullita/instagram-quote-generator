"""
Servidor Flask para la aplicación de generación de imágenes de Instagram
"""
from flask import Flask, render_template, request, jsonify, send_file
from image_generator import InstagramQuoteGenerator
from carousel_generator import CarouselGenerator
import os
from datetime import datetime
import traceback
import zipfile
import io

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

# Inicializar los generadores
generator = InstagramQuoteGenerator(output_dir='output')
carousel_generator = CarouselGenerator(output_dir='output/carousels')


@app.route('/')
def index():
    """Página principal de la aplicación"""
    return render_template('index.html')


@app.route('/api/templates', methods=['GET'])
def get_templates():
    """
    Endpoint para obtener las plantillas disponibles
    
    Returns:
        JSON con la lista de plantillas y sus detalles
    """
    try:
        templates = generator.get_available_templates()
        return jsonify({
            'success': True,
            'templates': templates
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate', methods=['POST'])
def generate_image():
    """
    Endpoint para generar una imagen con una frase
    
    Request JSON:
        - quote: Texto de la frase (requerido)
        - template: Nombre de la plantilla (opcional, default: 'minimal')
        - author: Autor de la frase (opcional)
    
    Returns:
        JSON con la ruta de la imagen generada o error
    """
    try:
        # Obtener datos del request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No se proporcionaron datos'
            }), 400
        
        quote = data.get('quote', '').strip()
        template = data.get('template', 'minimal')
        author = data.get('author')
        if author:
            author = author.strip()
        highlight_words = data.get('highlight_words', None)
        
        # Validaciones
        if not quote:
            return jsonify({
                'success': False,
                'error': 'La frase no puede estar vacía'
            }), 400
        
        if len(quote) > 500:
            return jsonify({
                'success': False,
                'error': 'La frase es demasiado larga (máximo 500 caracteres)'
            }), 400
        
        if template not in generator.TEMPLATES:
            return jsonify({
                'success': False,
                'error': f'Plantilla inválida. Opciones: {list(generator.TEMPLATES.keys())}'
            }), 400
        
        # Generar la imagen
        output_path = generator.generate_image(
            quote=quote,
            template=template,
            author=author if author else None,
            highlight_words=highlight_words
        )
        
        # Obtener nombre del archivo
        filename = os.path.basename(output_path)
        
        return jsonify({
            'success': True,
            'message': 'Imagen generada exitosamente',
            'filename': filename,
            'download_url': f'/api/download/{filename}'
        })
        
    except Exception as e:
        app.logger.error(f'Error generando imagen: {str(e)}')
        app.logger.error(traceback.format_exc())
        return jsonify({
            'success': False,
            'error': f'Error al generar la imagen: {str(e)}'
        }), 500


@app.route('/api/download/<filename>', methods=['GET'])
def download_image(filename):
    """
    Endpoint para descargar una imagen generada
    
    Args:
        filename: Nombre del archivo a descargar
        
    Returns:
        Archivo de imagen
    """
    try:
        # Validar que el archivo existe y está en el directorio correcto
        file_path = os.path.join('output', filename)
        
        if not os.path.exists(file_path):
            return jsonify({
                'success': False,
                'error': 'Archivo no encontrado'
            }), 404
        
        # Verificar que es un archivo PNG
        if not filename.endswith('.png'):
            return jsonify({
                'success': False,
                'error': 'Tipo de archivo no válido'
            }), 400
        
        return send_file(
            file_path,
            mimetype='image/png',
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        app.logger.error(f'Error descargando imagen: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/preview/<filename>', methods=['GET'])
def preview_image(filename):
    """
    Endpoint para previsualizar una imagen generada
    
    Args:
        filename: Nombre del archivo a previsualizar
        
    Returns:
        Archivo de imagen (sin forzar descarga)
    """
    try:
        file_path = os.path.join('output', filename)
        
        if not os.path.exists(file_path):
            return jsonify({
                'success': False,
                'error': 'Archivo no encontrado'
            }), 404
        
        return send_file(
            file_path,
            mimetype='image/png'
        )
        
    except Exception as e:
        app.logger.error(f'Error previsualizando imagen: {str(e)}')
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate-carousel', methods=['POST'])
def generate_carousel():
    """
    Endpoint para generar un carrusel de imágenes
    
    Request JSON:
        - content: Texto o lista de textos (requerido)
        - carousel_type: 'auto', 'manual', o 'list' (opcional, default: 'auto')
        - template: Nombre de la plantilla (opcional, default: 'minimal')
        - title: Título para slide de portada (opcional)
        - subtitle: Subtítulo para slide de portada (opcional)
        - cta_text: Call to action para slide final (opcional)
        - highlight_words: Lista de palabras a destacar (opcional)
        - size: 'square', 'vertical', o 'horizontal' (opcional, default: 'square')
    
    Returns:
        ZIP con todas las imágenes del carrusel
    """
    try:
        # Obtener datos del request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No se proporcionaron datos'
            }), 400
        
        content = data.get('content')
        carousel_type = data.get('carousel_type', 'auto')
        template = data.get('template', 'minimal')
        title = data.get('title')
        subtitle = data.get('subtitle')
        cta_text = data.get('cta_text')
        highlight_words = data.get('highlight_words')
        size_type = data.get('size', 'square')
        
        # Validaciones
        if not content:
            return jsonify({
                'success': False,
                'error': 'El contenido no puede estar vacío'
            }), 400
        
        # Convertir tipo de tamaño
        size_map = {
            'square': CarouselGenerator.SQUARE,
            'vertical': CarouselGenerator.VERTICAL,
            'horizontal': CarouselGenerator.HORIZONTAL
        }
        size = size_map.get(size_type, CarouselGenerator.SQUARE)
        
        # Generar carrusel
        output_paths = carousel_generator.generate_carousel(
            content=content,
            carousel_type=carousel_type,
            template=template,
            title=title,
            subtitle=subtitle,
            cta_text=cta_text,
            highlight_words=highlight_words,
            size=size
        )
        
        # Crear archivo ZIP con todas las imágenes
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            for i, path in enumerate(output_paths, start=1):
                filename = os.path.basename(path)
                zf.write(path, filename)
        
        memory_file.seek(0)
        
        # Nombre del archivo ZIP
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_filename = f'carousel_{template}_{timestamp}.zip'
        
        return send_file(
            memory_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name=zip_filename
        )
        
    except Exception as e:
        app.logger.error(f'Error generando carrusel: {str(e)}')
        app.logger.error(traceback.format_exc())
        return jsonify({
            'success': False,
            'error': f'Error al generar el carrusel: {str(e)}'
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar que la aplicación está funcionando"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })


@app.errorhandler(404)
def not_found(error):
    """Manejador de errores 404"""
    return jsonify({
        'success': False,
        'error': 'Endpoint no encontrado'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Manejador de errores 500"""
    return jsonify({
        'success': False,
        'error': 'Error interno del servidor'
    }), 500


if __name__ == '__main__':
    print("=" * 60)
    print("🎨 Instagram Quote Generator - Servidor Web")
    print("=" * 60)
    print("\n📍 Servidor iniciado en: http://localhost:5000")
    print("📝 Abre tu navegador y visita la URL anterior\n")
    print("Presiona CTRL+C para detener el servidor")
    print("=" * 60 + "\n")
    
    # Ejecutar en modo debug para desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)
