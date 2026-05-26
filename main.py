from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.menu import MDDropdownMenu
from core import TranslationEngine
import threading

class TranslatorApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.src_lang = 'zh-CN'
        self.dest_lang = 'en'
        self.lang_menu = None

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.engine = TranslationEngine()
        self.engine.callback = self.on_translation_result
        return Builder.load_file("translator.kv")

    def select_language(self, type):
        languages = [
            {"text": "中文", "code": "zh-CN"},
            {"text": "英语", "code": "en"},
            {"text": "日语", "code": "ja"},
            {"text": "韩语", "code": "ko"},
            {"text": "法语", "code": "fr"},
        ]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": lang["text"],
                "on_release": lambda x=lang: self.set_language(type, x),
            } for lang in languages
        ]
        caller = self.root.ids.src_lang_btn if type == 'src' else self.root.ids.dest_lang_btn
        self.lang_menu = MDDropdownMenu(caller=caller, items=menu_items, width_mult=4)
        self.lang_menu.open()

    def set_language(self, type, lang):
        if type == 'src':
            self.src_lang = lang['code']
            self.root.ids.src_lang_btn.text = f"{lang['text']} ({lang['code']})"
        else:
            self.dest_lang = lang['code']
            self.root.ids.dest_lang_btn.text = f"{lang['text']} ({lang['code']})"
        self.lang_menu.dismiss()

    def toggle_recording(self):
        if not self.engine.is_recording:
            self.root.ids.mic_button.icon = "stop"
            self.root.ids.status_label.text = "正在录音并翻译..."
            self.engine.start_live_translation(self.src_lang, self.dest_lang)
        else:
            self.engine.stop()
            self.root.ids.mic_button.icon = "microphone"
            self.root.ids.status_label.text = "已停止"

    def on_translation_result(self, original, translated):
        # 使用 Clock.schedule_once 确保 UI 更新在主线程执行
        Clock.schedule_once(lambda dt: self.update_ui(original, translated))

    def update_ui(self, original, translated):
        item = ThreeLineListItem(
            text=f"原文: {original}",
            secondary_text=f"译文: {translated}",
            tertiary_text="点击播放语音",
            on_release=lambda x: self.engine.speak(translated)
        )
        # 将新翻译置顶
        self.root.ids.chat_list.add_widget(item, index=len(self.root.ids.chat_list.children))

if __name__ == "__main__":
    TranslatorApp().run()
