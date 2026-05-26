import threading
import time
import speech_recognition as sr
from googletrans import Translator
import pyttsx3
from plyer import tts

class TranslationEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        self.is_recording = False
        self.callback = None
        # 尝试初始化本地 TTS，如果是在安卓上则优先使用 plyer
        try:
            self.tts_engine = pyttsx3.init()
        except:
            self.tts_engine = None

    def speak(self, text):
        try:
            # 优先使用安卓原生 TTS (通过 plyer)
            tts.speak(text)
        except Exception:
            # 备选方案：pyttsx3
            if self.tts_engine:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()

    def start_live_translation(self, source_lang='zh-CN', target_lang='en'):
        self.is_recording = True
        threading.Thread(target=self._listen_loop, args=(source_lang, target_lang), daemon=True).start()

    def stop(self):
        self.is_recording = False

    def _listen_loop(self, source_lang, target_lang):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.is_recording:
                try:
                    # 监听一小段语音
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    # 识别
                    text = self.recognizer.recognize_google(audio, language=source_lang)
                    if text:
                        # 翻译
                        translated = self.translator.translate(text, src=source_lang, dest=target_lang)
                        if self.callback:
                            self.callback(text, translated.text)
                        # 自动播放翻译后的语音
                        self.speak(translated.text)
                except sr.WaitTimeoutError:
                    continue
                except Exception as e:
                    print(f"Error in listen loop: {e}")
                    time.sleep(1)
