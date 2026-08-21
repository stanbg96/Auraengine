import moderngl
import numpy as np

class EngineRenderer:
    def __init__(self, ctx):
        self.ctx = ctx
        self.prog = self.init_procedural_shaders()

    def init_procedural_shaders(self):
        # Напълно работещ GLSL шейдър за процедурно оцветяване и фасади
        vert_shader = '''
            #version 300 es
            in vec3 in_position;
            uniform mat4 u_mvp;
            void main() {
                gl_Position = u_mvp * vec4(in_position, 1.0);
            }
        '''
        frag_shader = '''
            #version 300 es
            precision mediump float;
            out vec4 fragColor;
            void main() {
                // Базов синьо-зелен кибернетичен цвят за процедурните обекти
                fragColor = vec4(0.12, 0.53, 0.9, 1.0);
            }
        '''
        return self.ctx.program(vertex_shader=vert_shader, fragment_shader=frag_shader)
