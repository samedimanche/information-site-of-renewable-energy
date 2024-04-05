from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class ProfitCalculator(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        # Position type selection buttons
        position_label = Label(text="Position Type:")
        layout.add_widget(position_label)

        position_layout = BoxLayout(orientation='horizontal', spacing=10)
        long_button = Button(text="Long", on_press=self.set_position_type)
        short_button = Button(text="Short", on_press=self.set_position_type)

        position_layout.add_widget(long_button)
        position_layout.add_widget(short_button)

        layout.add_widget(position_layout)

        # Input fields
        coin_amount_label = Label(text="Amount of Coins:")
        layout.add_widget(coin_amount_label)
        self.coin_amount_input = TextInput(multiline=False)
        layout.add_widget(self.coin_amount_input)

        entry_price_label = Label(text="Entry Price:")
        layout.add_widget(entry_price_label)
        self.entry_price_input = TextInput(multiline=False)
        layout.add_widget(self.entry_price_input)

        exit_price_label = Label(text="Exit Price:")
        layout.add_widget(exit_price_label)
        self.exit_price_input = TextInput(multiline=False)
        layout.add_widget(self.exit_price_input)

        # Calculate button
        calculate_button = Button(text="Calculate", on_press=self.calculate_profit)
        layout.add_widget(calculate_button)

        # Result form
        self.result_label = Label(text="")

        return layout

    def set_position_type(self, button):
        self.position_type = button.text.lower()

    def calculate_profit(self, button):
        coin_amount_str = self.coin_amount_input.text.replace(',', '.')
        entry_price_str = self.entry_price_input.text.replace(',', '.')
        exit_price_str = self.exit_price_input.text.replace(',', '.')

        try:
            coin_amount = float(coin_amount_str)
            entry_price = float(entry_price_str)
            exit_price = float(exit_price_str)

            profit = self.perform_profit_calculation(self.position_type, coin_amount, entry_price, exit_price)
            self.result_label.text = f"Profit: {profit}"
        except ValueError:
            self.result_label.text = "Invalid input. Please enter numeric values."

    def perform_profit_calculation(self, position_type, coin_amount, entry_price, exit_price):
        if position_type == "long":
            profit = round(coin_amount * exit_price - coin_amount * entry_price, 3)
        elif position_type == "short":
            profit = round(coin_amount * entry_price - coin_amount * exit_price, 3)
        else:
            profit = "Invalid position type"

        return profit


if __name__ == '__main__':
    ProfitCalculator().run()