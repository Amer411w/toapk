from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
import arabic_reshaper

def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return reshaped_text[::-1]  # عكس النص بعد إعادة تشكيله

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(
            text=reshape_text('هذه هي نافذة الإعدادات'),
            font_name='Arabic',
            halign='right'
        ))
        self.add_widget(layout)
