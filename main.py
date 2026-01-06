from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Dark background color
Window.clearcolor = (0.1, 0.15, 0.2, 1)


class FinalPriceApp(App):

    def build(self):
        self.title = "FinalPrice Pro"
        self.icon = "icon.png"

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        layout.add_widget(
            Label(
                text="FinalPrice Pro Mobile",
                font_size=30,
                color=(0, 1, 0.5, 1)
            )
        )

        self.ek = TextInput(
            hint_text="Einkaufspreis (€)",
            multiline=False,
            input_filter="float",
            font_size=20
        )
        layout.add_widget(self.ek)

        self.vk = TextInput(
            hint_text="Verkaufspreis (€)",
            multiline=False,
            input_filter="float",
            font_size=20
        )
        layout.add_widget(self.vk)

        self.rabatt = TextInput(
            hint_text="Rabatt (%)",
            multiline=False,
            input_filter="float",
            font_size=20
        )
        layout.add_widget(self.rabatt)

        btn = Button(
            text="BERECHNEN",
            background_color=(0, 0.6, 1, 1),
            font_size=25,
            size_hint_y=0.3
        )
        btn.bind(on_press=self.berechnen)
        layout.add_widget(btn)

        self.result = Label(
            text="Endpreis: 0.00 €",
            font_size=25
        )
        layout.add_widget(self.result)

        return layout

    def berechnen(self, instance):
        try:
            vk = float(self.vk.text)
            r = float(self.rabatt.text)

            endpreis = vk - (vk * r / 100)
            self.result.text = f"Endpreis: {endpreis:.2f} €"

        except ValueError:
            self.result.text = "Error: Enter Numbers!"


# Main Entry Point
FinalPriceApp().run()
