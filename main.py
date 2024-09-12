from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import mainthread, Clock
from kivy.logger import Logger
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from jnius import autoclass
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from main_screen import MainScreen  # استيراد الشاشة من الملف الجديد
from favorites_screen import FavoritesScreen  # استيراد شاشة المفضلات
from favorites1_screen import Favorites1Screen  # استيراد شاشة المفضلات 1
from favorites2_screen import Favorites2Screen  # استيراد شاشة المفضلات 2
from favorites3_screen import Favorites3Screen  # استيراد شاشة المفضلات 3
from projects_screen import ProjectsScreen  # استيراد شاشة المشاريع
from initiatives_screen import InitiativesScreen  # استيراد شاشة المبادرات
from settings_screen import SettingsScreen  # استيراد شاشة الإعدادات
from favorites_screen import FavoritesScreen  # استيراد شاشة المفضلات
from favorites1_screen import Favorites1Screen  # استيراد شاشة المفضلات 1
from favorites2_screen import Favorites2Screen  # استيراد شاشة المفضلات 2
from favorites3_screen import Favorites3Screen  # استيراد شاشة المفضلات 3
import arabic_reshaper
from kivy.uix.button import Button

def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return reshaped_text[::-1]  # عكس النص بعد إعادة تشكيله

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FavoritesScreen(name='favorites'))
        sm.add_widget(Favorites1Screen(name='favorites_1'))
        sm.add_widget(Favorites2Screen(name='favorites_2'))
        sm.add_widget(Favorites3Screen(name='favorites_3'))
        sm.add_widget(ProjectsScreen(name='projects'))
        sm.add_widget(InitiativesScreen(name='initiatives'))
        sm.add_widget(SettingsScreen(name='settings'))
        
        # جدولة دالة منع التقاط الشاشة
        Clock.schedule_once(self.prevent_screenshot, 5)
        return sm

    @mainthread
    def prevent_screenshot(self, dt):
        try:
            WindowManager = autoclass('android.view.WindowManager$LayoutParams')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            activity = PythonActivity.mActivity
            activity.getWindow().addFlags(WindowManager.FLAG_SECURE)
            Logger.info('Screenshot prevention flag set successfully')
        except Exception as e:
            Logger.error(f'Error setting screenshot prevention flag: {e}')

    def on_key(self, window, key, *args):
        if key == 27:  # 27 هو كود زر الرجوع في الأندرويد
            if self.root.current == 'main':
                self.show_exit_popup()
                return True
            else:
                self.root.current = self.root.previous()
                return True
        return False

    def show_exit_popup(self):
        layout = FloatLayout()
        with layout.canvas.before:
            Color(0.6, 0, 0.4, 0.5)  # لون الخلفية
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.bind(size=self._update_rect, pos=self._update_rect)
        
        title_label = Label(
            text=reshape_text('تأكيد الخروج'),
            font_name='Arabic',
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'top': 1}
        )
        popup_label = Label(
            text=reshape_text('هل تريد الخروج من التطبيق؟'),
            font_name='Arabic',
            size_hint=(0.6, 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        no_button = Button(
            text=reshape_text('لا'),
            font_name='Arabic',
            size_hint=(0.3, 0.2),
            pos_hint={'center_x': 0.3, 'center_y': 0.3},
            background_normal='',
            background_color=(0.6, 0, 0.4, 0.5),
            color=(1, 1, 1, 1),
            on_press=lambda *args: exit_popup.dismiss()
        )
        yes_button = Button(
            text=reshape_text('نعم'),
            font_name='Arabic',
            size_hint=(0.3, 0.2),
            pos_hint={'center_x': 0.7, 'center_y': 0.3},
            background_normal='',
            background_color=(0.6, 0, 0.4, 0.5),
            color=(1, 1, 1, 1),
            on_press=self.stop
        )
        layout.add_widget(title_label)
        layout.add_widget(popup_label)
        layout.add_widget(no_button)
        layout.add_widget(yes_button)
        
        exit_popup = Popup(
            title='',
            content=layout,
            size_hint=(0.8, 0.4),
            auto_dismiss=False
        )
        
        exit_popup.open()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_start(self):
        Window.bind(on_keyboard=self.on_key)

if __name__ == '__main__':
    MyApp().run()
