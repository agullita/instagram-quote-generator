"""
Generador de imágenes para Instagram con frases personalizadas
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from datetime import datetime


class InstagramQuoteGenerator:
    """Genera imágenes de Instagram con frases y diferentes plantillas de diseño"""
    
    # Tamaño estándar de Instagram (cuadrado)
    WIDTH = 1080
    HEIGHT = 1080
    
    # Plantillas de diseño predefinidas
    TEMPLATES = {
        'minimal': {
            'name': 'Minimalista',
            'bg_color': (255, 255, 255),
            'text_color': (30, 30, 30),
            'accent_color': (200, 200, 200),
            'font_size': 60,
            'description': 'Diseño limpio y simple con fondo blanco',
            'bg_image': None
        },
        'dark': {
            'name': 'Oscuro Elegante',
            'bg_color': (20, 20, 30),
            'text_color': (255, 255, 255),
            'accent_color': (100, 100, 120),
            'font_size': 60,
            'description': 'Fondo oscuro con texto blanco elegante',
            'bg_image': None
        },
        'vibrant': {
            'name': 'Vibrante',
            'bg_color': (255, 87, 51),
            'text_color': (255, 255, 255),
            'accent_color': (255, 195, 0),
            'font_size': 62,
            'description': 'Colores brillantes y llamativos',
            'bg_image': None
        },
        'ocean': {
            'name': 'Océano',
            'bg_color': (52, 152, 219),
            'text_color': (255, 255, 255),
            'accent_color': (41, 128, 185),
            'font_size': 60,
            'description': 'Tonos azules relajantes inspirados en el mar',
            'bg_image': None
        },
        'sunset': {
            'name': 'Atardecer',
            'bg_color': (255, 111, 97),
            'text_color': (255, 255, 255),
            'accent_color': (253, 203, 110),
            'font_size': 60,
            'description': 'Degradado cálido de atardecer',
            'bg_image': None
        },
        'forest': {
            'name': 'Bosque',
            'bg_color': (39, 174, 96),
            'text_color': (255, 255, 255),
            'accent_color': (46, 204, 113),
            'font_size': 60,
            'description': 'Tonos verdes naturales',
            'bg_image': None
        },
        'geometric1': {
            'name': 'Geométrico Naranja',
            'bg_color': (255, 255, 255),
            'text_color': (30, 30, 30),
            'accent_color': (255, 152, 0),
            'font_size': 60,
            'description': 'Diseño geométrico con formas naranjas y amarillas',
            'bg_image': 'backgrounds/background1.png'
        },
        'geometric2': {
            'name': 'Geométrico Minimalista',
            'bg_color': (255, 255, 255),
            'text_color': (30, 30, 30),
            'accent_color': (255, 152, 0),
            'font_size': 60,
            'description': 'Diseño geométrico limpio con detalle naranja',
            'bg_image': 'backgrounds/background2.png'
        }
    }
    
    def __init__(self, output_dir='output'):
        """
        Inicializa el generador
        
        Args:
            output_dir: Directorio donde se guardarán las imágenes generadas
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def _get_font(self, size=60):
        """
        Obtiene la fuente a usar, intentando usar fuentes del sistema
        
        Args:
            size: Tamaño de la fuente
            
        Returns:
            ImageFont object
        """
        # Lista de fuentes a intentar (en orden de preferencia)
        font_options = [
            # Windows
            'C:/Windows/Fonts/arial.ttf',
            'C:/Windows/Fonts/calibri.ttf',
            'C:/Windows/Fonts/segoeui.ttf',
            # Linux
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
            # macOS
            '/System/Library/Fonts/Helvetica.ttc',
            '/Library/Fonts/Arial.ttf',
        ]
        
        for font_path in font_options:
            if os.path.exists(font_path):
                try:
                    return ImageFont.truetype(font_path, size)
                except:
                    continue
        
        # Si no encuentra ninguna fuente, usa la predeterminada
        return ImageFont.load_default()
    
    def _calculate_adaptive_font_size(self, text, base_size, max_width, max_height):
        """
        Calcula el tamaño de fuente óptimo según la longitud del texto
        
        Args:
            text: Texto a evaluar
            base_size: Tamaño base de la fuente
            max_width: Ancho máximo disponible
            max_height: Altura máxima disponible
            
        Returns:
            Tamaño de fuente óptimo
        """
        text_length = len(text)
        
        # Ajustar el tamaño base según la longitud del texto
        if text_length < 50:
            # Texto corto: aumentar tamaño
            size_multiplier = 1.5
        elif text_length < 100:
            # Texto medio: tamaño normal a ligeramente mayor
            size_multiplier = 1.2
        elif text_length < 200:
            # Texto largo: tamaño normal
            size_multiplier = 1.0
        else:
            # Texto muy largo: reducir tamaño
            size_multiplier = 0.8
        
        adaptive_size = int(base_size * size_multiplier)
        
        # Iterar para encontrar el tamaño que mejor se ajusta
        for size in range(adaptive_size, 20, -2):
            font = self._get_font(size)
            lines = self._wrap_text(text, font, max_width)
            
            # Calcular altura total
            line_height = size + 20
            total_height = len(lines) * line_height
            
            # Si cabe en la altura máxima, usar este tamaño
            if total_height <= max_height:
                return size
        
        # Si no encuentra un tamaño adecuado, retornar el mínimo
        return 30
    
    def _wrap_text(self, text, font, max_width):
        """
        Divide el texto en múltiples líneas para que quepa en el ancho máximo
        
        Args:
            text: Texto a dividir
            font: Fuente a usar
            max_width: Ancho máximo en píxeles
            
        Returns:
            Lista de líneas de texto
        """
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = font.getbbox(test_line)
            width = bbox[2] - bbox[0]
            
            if width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    # La palabra sola es más ancha que max_width
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def _draw_gradient(self, draw, start_color, end_color):
        """
        Dibuja un gradiente vertical sutil
        
        Args:
            draw: ImageDraw object
            start_color: Color inicial (RGB)
            end_color: Color final (RGB)
        """
        for y in range(self.HEIGHT):
            ratio = y / self.HEIGHT
            r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
            g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
            b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
            draw.line([(0, y), (self.WIDTH, y)], fill=(r, g, b))
    
    def generate_image(self, quote, template='minimal', author=None, highlight_words=None, output_filename=None):
        """
        Genera una imagen con la frase proporcionada
        
        Args:
            quote: Frase a incluir en la imagen
            template: Nombre de la plantilla a usar ('minimal', 'dark', 'vibrant', etc.)
            author: Autor de la frase (opcional)
            highlight_words: Lista de palabras a destacar en otro color (opcional)
            output_filename: Nombre del archivo de salida (opcional, se genera automáticamente si no se proporciona)
            
        Returns:
            Ruta del archivo generado
        """
        if template not in self.TEMPLATES:
            raise ValueError(f"Plantilla '{template}' no existe. Opciones: {list(self.TEMPLATES.keys())}")
        
        template_config = self.TEMPLATES[template]
        
        # Verificar si la plantilla usa imagen de fondo
        if template_config.get('bg_image'):
            bg_image_path = template_config['bg_image']
            try:
                # Intentar cargar la imagen de fondo
                image = Image.open(bg_image_path)
                # Asegurar que tenga el tamaño correcto
                if image.size != (self.WIDTH, self.HEIGHT):
                    image = image.resize((self.WIDTH, self.HEIGHT), Image.Resampling.LANCZOS)
                # Convertir a RGB si es necesario
                if image.mode != 'RGB':
                    image = image.convert('RGB')
            except Exception as e:
                print(f"⚠️ No se pudo cargar la imagen de fondo: {e}")
                print(f"   Usando color de fondo alternativo")
                # Usar color sólido como fallback
                image = Image.new('RGB', (self.WIDTH, self.HEIGHT), template_config['bg_color'])
        else:
            # Crear imagen con fondo de color sólido
            image = Image.new('RGB', (self.WIDTH, self.HEIGHT), template_config['bg_color'])
        
        draw = ImageDraw.Draw(image)
        
        # Opcionalmente añadir gradiente sutil para algunos templates (solo si no hay imagen de fondo)
        if template in ['sunset', 'ocean'] and not template_config.get('bg_image'):
            bg_color = template_config['bg_color']
            # Crear un gradiente más oscuro hacia abajo
            end_color = tuple(max(0, c - 30) for c in bg_color)
            self._draw_gradient(draw, bg_color, end_color)
        
        # Preparar el texto de la frase
        max_width = self.WIDTH - 160  # Margen de 80px a cada lado
        max_height = self.HEIGHT - 400  # Espacio para decoraciones y autor
        
        # Calcular tamaño de fuente adaptativo
        adaptive_font_size = self._calculate_adaptive_font_size(
            quote, 
            template_config['font_size'], 
            max_width, 
            max_height
        )
        
        # Obtener fuentes con el tamaño adaptativo
        quote_font = self._get_font(adaptive_font_size)
        author_font = self._get_font(max(20, adaptive_font_size - 20))
        
        lines = self._wrap_text(quote, quote_font, max_width)
        
        # Calcular altura total del texto
        line_height = adaptive_font_size + 20
        total_text_height = len(lines) * line_height
        
        if author:
            total_text_height += 100  # Espacio para el autor
        
        # Posición inicial del texto (centrado verticalmente)
        y = (self.HEIGHT - total_text_height) // 2
        
        # Dibujar líneas decorativas superiores
        line_y = y - 60
        draw.rectangle(
            [(self.WIDTH // 2 - 40, line_y), (self.WIDTH // 2 + 40, line_y + 4)],
            fill=template_config['accent_color']
        )
        
        # Preparar lista de palabras a destacar (en minúsculas para comparación)
        highlight_set = set()
        if highlight_words:
            highlight_set = {word.lower().strip() for word in highlight_words}
        
        # Dibujar cada línea de texto centrada con palabras destacadas
        for line in lines:
            # Calcular posición x inicial (centrada)
            bbox = quote_font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            x = (self.WIDTH - text_width) // 2
            
            # Si no hay palabras a destacar, dibujar la línea completa
            if not highlight_set:
                draw.text((x, y), line, font=quote_font, fill=template_config['text_color'])
            else:
                # Dibujar palabra por palabra con colores diferentes
                current_x = x
                words = line.split()
                
                for i, word in enumerate(words):
                    # Limpiar palabra de puntuación para comparación
                    word_clean = word.strip('.,;:!?¡¿"\'()[]{}').lower()
                    
                    # Determinar el color
                    if word_clean in highlight_set:
                        color = template_config['accent_color']
                    else:
                        color = template_config['text_color']
                    
                    # Dibujar la palabra
                    draw.text((current_x, y), word, font=quote_font, fill=color)
                    
                    # Calcular el ancho de la palabra más el espacio
                    word_bbox = quote_font.getbbox(word + ' ')
                    word_width = word_bbox[2] - word_bbox[0]
                    current_x += word_width
            
            y += line_height
        
        # Dibujar autor si existe
        if author:
            y += 40
            author_text = f"— {author}"
            bbox = author_font.getbbox(author_text)
            author_width = bbox[2] - bbox[0]
            x = (self.WIDTH - author_width) // 2
            draw.text((x, y), author_text, font=author_font, fill=template_config['accent_color'])
        
        # Dibujar líneas decorativas inferiores
        line_y = y + 80 if author else y + 40
        draw.rectangle(
            [(self.WIDTH // 2 - 40, line_y), (self.WIDTH // 2 + 40, line_y + 4)],
            fill=template_config['accent_color']
        )
        
        # Generar nombre de archivo si no se proporciona
        if not output_filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_filename = f'quote_{template}_{timestamp}.png'
        
        # Asegurar que tiene extensión .png
        if not output_filename.endswith('.png'):
            output_filename += '.png'
        
        # Guardar imagen
        output_path = os.path.join(self.output_dir, output_filename)
        image.save(output_path, 'PNG', quality=95)
        
        return output_path
    
    def get_available_templates(self):
        """
        Retorna información sobre las plantillas disponibles
        
        Returns:
            Diccionario con información de todas las plantillas
        """
        return {
            key: {
                'name': config['name'],
                'description': config['description']
            }
            for key, config in self.TEMPLATES.items()
        }


# Ejemplo de uso si se ejecuta directamente
if __name__ == '__main__':
    generator = InstagramQuoteGenerator()
    
    # Ejemplos de uso
    examples = [
        {
            'quote': 'La vida es aquello que te va sucediendo mientras te empeñas en hacer otros planes.',
            'template': 'minimal',
            'author': 'John Lennon'
        },
        {
            'quote': 'El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.',
            'template': 'vibrant',
            'author': 'Albert Schweitzer'
        },
        {
            'quote': 'No cuentes los días, haz que los días cuenten.',
            'template': 'dark',
            'author': 'Muhammad Ali'
        }
    ]
    
    print("Generando imágenes de ejemplo...")
    for i, example in enumerate(examples, 1):
        output_path = generator.generate_image(**example)
        print(f"{i}. Generada: {output_path}")
    
    print("\n✓ ¡Imágenes generadas exitosamente!")
