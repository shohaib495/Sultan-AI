from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

try:
    from plyer import tts
except ImportError:
    tts = None

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 20
    spacing: 15

    canvas.before:
        Color:
            rgba: 0.01, 0.02, 0.07, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        text: "S U L T A N"
        font_size: "34sp"
        bold: True
        color: 0.1, 0.7, 1, 1
        size_hint_y: 0.2

    Label:
        text: "AI ASSISTANT"
        font_size: "18sp"
        color: 0.4, 0.8, 1, 1

    Label:
        id: greeting
        text: "Hi Azhar Sir!\\nAssalam-o-Alaikum.\\nSultan is online."
        font_size: "23sp"
        halign: "center"
        color: 1, 1, 1, 1

    TextInput:
        id: message
        hint_text: "Talk to Sultan..."
        multiline: False
        size_hint_y: 0.15

    Button:
        text: "SEND MESSAGE"
        on_release: app.send_message()

    Button:
        text: "VOICE GREETING"
        on_release: app.speak()

    Button:
        text: "SETTINGS"
        on_release: app.settings()
"""

class SultanAI(App):

    def build(self):
        self.title = "SULTAN AI"
        Window.clearcolor = (0.01, 0.02, 0.07, 1)
        Clock.schedule_once(self.startup, 2)
        return Builder.load_string(KV)

    def startup(self, dt):
        self.speak()

    def speak(self):
        text = (
            "Hi Azhar Sir. "
            "Assalam-o-Alaikum. "
            "Sultan is online. "
            "How can I assist you today?"
        )
        if tts:
            try:
                tts.speak(text)
            except Exception:
                pass

    def send_message(self):
        msg = self.root.ids.message.text.strip()
        if msg:
            self.root.ids.greeting.text = (
                "Your message received!\\n"
                "AI connection is not configured yet."
            )
            self.root.ids.message.text = ""

    def settings(self):
        self.root.ids.greeting.text = (
            "SULTAN SETTINGS\\n\\n"
            "Gemini: Not connected\\n"
            "ChatGPT: Not connected"
        )

if __name__ == "__main__":
    SultanAI().run()
