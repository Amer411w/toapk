from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
import arabic_reshaper

def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return reshaped_text[::-1]  # عكس النص بعد إعادة تشكيله

class FavoritesScreen(Screen):
    def __init__(self, **kwargs):
        super(FavoritesScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(
            text=reshape_text('هذه هي نافذة المفضلات'),
            font_name='Arabic',
            halign='right',  # محاذاة النص لليمين
            valign='middle'  # محاذاة النص عموديًا
        ))
        
        layout.add_widget(Button(
            text=reshape_text('المفضلات 1'),
            font_name='Arabic',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.6, 0, 0.4, 0.5),
            color=(1, 1, 1, 1),
            on_press=self.show_favorites_1
        ))
        layout.add_widget(Button(
            text=reshape_text('المفضلات 2'),
            font_name='Arabic',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.6, 0, 0.4, 1),
            color=(1, 1, 1, 1),
            on_press=self.show_favorites_2
        ))
        layout.add_widget(Button(
            text=reshape_text('المفضلات 3'),
            font_name='Arabic',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.6, 0, 0.4, 0.5),
            color=(1, 1, 1, 1),
            on_press=self.show_favorites_3
        ))
        
        self.add_widget(layout)

    def show_favorites_1(self, instance):
        self.manager.current = 'favorites_1'

    def show_favorites_2(self, instance):
        self.manager.current = 'favorites_2'

    def show_favorites_3(self, instance):
        self.manager.current = 'favorites_3'
