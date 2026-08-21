from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

from ai_hub import AIHub
from geo_module import GeoModule
from asset_store import AssetStore
from anim_player import AnimationPlayer

class AuraEngineApp(App):
    def build(self):
        self.title = "Aura Engine - AAA Mobile Studio"
        
        root_layout = BoxLayout(orientation='vertical', padding=15, spacing=12)
        
        header = Label(text='[b]AURA ENGINE 2026[/b] - Mobile AI Workspace', markup=True, font_size=20, size_hint_y=None, height=40)
        root_layout.add_widget(header)
        
        self.ai_hub = AIHub()
        self.geo = GeoModule()
        self.store = AssetStore()
        self.animator = AnimationPlayer()
        
        self.console = TextInput(text='Системата е инициализирана успешно.\nГотово за работа в Termux / Android.', readonly=True, background_color=(0.1, 0.1, 0.15, 1), foreground_color=(0.8, 0.9, 1, 1))
        root_layout.add_widget(self.console)
        
        btn_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        b1 = Button(text='Обнови AI Модели')
        b1.bind(on_press=self.action_fetch_ai)
        
        b2 = Button(text='Зареди OSM Град')
        b2.bind(on_press=self.action_load_geo)
        
        b3 = Button(text='Магазин Активи')
        b3.bind(on_press=self.action_open_store)
        
        btn_layout.add_widget(b1)
        btn_layout.add_widget(b2)
        btn_layout.add_widget(b3)
        
        root_layout.add_widget(btn_layout)
        return root_layout

    def action_fetch_ai(self, instance):
        self.console.text += "\n[AI Hub] Извличане на модели от OpenRouter..."
        models = self.ai_hub.fetch_free_models()
        if models:
            top_model = models[0].get('name', 'Unknown')
            self.console.text += f"\n[AI Hub] Успешно! Намерени: {len(models)}. Топ модел (Безплатен): {top_model}"
        else:
            self.console.text += "\n[AI Hub Грешка] Неуспешна връзка или липса на интернет."

    def action_load_geo(self, instance):
        self.console.text += "\n[Geo Module] Изтегляне на данни от OpenStreetMap (Larnaca Box)..."
        bbox = (34.90, 33.60, 34.93, 33.64)
        data = self.geo.load_city_skeleton(bbox)
        if data:
            self.console.text += f"\n[Geo Module] Заредени улици: {len(data['roads'])}, Сгради: {len(data['buildings'])}"
        else:
            self.console.text += "\n[Geo Module Грешка] Проблем при изпълнение на Overpass заявката."

    def action_open_store(self, instance):
        assets = self.store.fetch_store_catalog("3d_models")
        self.console.text += f"\n[Asset Store] Налични активи в облака: {len(assets)}. Категории анимации: {len(self.animator.categories)}"

if __name__ == '__main__':
    AuraEngineApp().run()
