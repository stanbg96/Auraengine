from kivy.graphics import RenderContext, Rectangle, Color
from kivy.uix.widget import Widget

class EngineRenderer(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Използваме Kivy RenderContext за мобилни GLSL шейдъри
        self.canvas = RenderContext(use_parent_modelview=True)
        
        with self.canvas:
            # Базов цвят и геометрия за процедурните обекти
            Color(0.12, 0.53, 0.9, 1.0)
            self.rect = Rectangle(pos=self.pos, size=self.size)
            
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.init_procedural_shaders()

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def init_procedural_shaders(self):
        # Мобилни GLSL шейдъри, съвместими с Kivy и OpenGL ES
        vert_shader = '''
            precision mediump float;
            attribute vec4 v_position;
            attribute vec2 v_texcoord;
            uniform mat4 modelview_mat;
            uniform mat4 projection_mat;
            varying vec2 texcoord;
            
            void main() {
                texcoord = v_texcoord;
                gl_Position = projection_mat * modelview_mat * v_position;
            }
        '''
        
        frag_shader = '''
            precision mediump float;
            varying vec2 texcoord;
            uniform vec4 color;
            
            void main() {
                // Кибернетичен син цвят за процедурните обекти на телефона
                gl_FragColor = vec4(0.12, 0.53, 0.9, 1.0);
            }
        '''
        
        # Прилагаме шейдърите към Kivy контекста безопасно
        try:
            self.canvas.shader.vs = vert_shader
            self.canvas.shader.fs = frag_shader
        except Exception as e:
            print(f"Shader compilation warning: {e}")
