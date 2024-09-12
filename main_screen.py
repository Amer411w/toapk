from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Rectangle
import arabic_reshaper
from kivy.core.text import LabelBase  # استيراد LabelBase
from kivy.uix.widget import Widget


LabelBase.register(name='Arabic', fn_regular='/storage/emulated/0/nmadgecollge/Amiri/Amiri-Bold.ttf')

def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return reshaped_text[::-1]  # عكس النص بعد إعادة تشكيله

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical', padding=5, spacing=20)
        
        # إضافة النص أعلى مربع الأزرار
        title_label = Label(
            text=reshape_text('اجابات تقاويم ثالث ثانوي'),
            font_name='Arabic',
            font_size='40sp',
            size_hint=(1, 0.1),
            halign='center',
            valign='middle'
        )
        
        button_box = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(0.9, None), height=800, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        with button_box.canvas.before:
            Color(0.16, 0.16, 0.17, 1)  # لون الخلفية
            self.rect = Rectangle(size=button_box.size, pos=button_box.pos)
        
        button_box.bind(size=self._update_rect, pos=self._update_rect)
        
        button_box.add_widget(Button(
            text=reshape_text('المفضلات'),
            font_name='Arabic',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.6, 0, 0.4, 0.5),
            color=(1, 1, 1, 1),
            on_press=self.show_favorites
        ))
        button_box.add_widget(Button(
            text=reshape_text('المشاريع'),
            font_name='Arabic',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.6, 0, 0.4, 1),
            color=(1, 1, 1, 1),
            on_press=self.show_projects
        ))
        button_box.add_widget(Button(
            text=reshape_text('المبادرات'),
            font_name='Arabic',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.6, 0, 0.4, 0.5),
            color=(1, 1, 1, 1),
            on_press=self.show_initiatives
        ))
        button_box.add_widget(Button(
            text=reshape_text('الإعدادات'),
            font_name='Arabic',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.6, 0, 0.4, 1),
            color=(1, 1, 1, 1),
            on_press=self.show_settings
        ))
        
        # إضافة العناصر إلى `main_layout`
        main_layout.add_widget(title_label)  # إضافة النص أعلى مربع الأزرار
        main_layout.add_widget(Widget(size_hint=(1, 0.1)))  # إضافة مساحة فارغة
        main_layout.add_widget(button_box)
        main_layout.add_widget(Widget(size_hint=(1, 0.2)))  # إضافة مساحة فارغة في الأسفل
        
        self.add_widget(main_layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def show_favorites(self, instance):
        self.manager.current = 'favorites'

    def show_projects(self, instance):
        self.manager.current = 'projects'

    def show_initiatives(self, instance):
        self.manager.current = 'initiatives'

    def show_settings(self, instance):
        self.manager.current = 'settings'
