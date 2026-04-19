from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        self.count = 0

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(
            text='Count: 0',
            font_size='32sp'
        )

        increment_btn = Button(
            text='Increment',
            font_size='24sp',
            size_hint=(1, 0.3)
        )
        increment_btn.bind(on_press=self.increment)

        reset_btn = Button(
            text='Reset',
            font_size='24sp',
            size_hint=(1, 0.3),
            background_color=(0.8, 0.2, 0.2, 1)
        )
        reset_btn.bind(on_press=self.reset)

        layout.add_widget(self.label)
        layout.add_widget(increment_btn)
        layout.add_widget(reset_btn)

        return layout

    def increment(self, instance):
        self.count += 1
        self.label.text = f'Count: {self.count}'

    def reset(self, instance):
        self.count = 0
        self.label.text = 'Count: 0'

if __name__ == '__main__':
    CounterApp().run()