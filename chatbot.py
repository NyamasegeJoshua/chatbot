# CREATE A CHATBOT WITH 'openai'
# Import packages and dependencies
import openai
import sys
from PyQt5 import QtWidgets, QtCore
from config import API_KEY

# Import unique apikey
openai.api_key = API_KEY

# Build interface
class ChatBotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(50, 50, 450, 450)
        self.setWindowTitle('JoshBot')

        self.chat_history = QtWidgets.QTextEdit(self)
        self.chat_history.setReadOnly(True)

        self.user_input = QtWidgets.QLineEdit(self)

        self.send_button = QtWidgets.QPushButton('Send', self)
        self.send_button.clicked.connect(self.send_message)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.chat_history)
        vbox.addWidget(self.user_input)
        vbox.addWidget(self.send_button)

        self.setLayout(vbox)

    def send_message(self):
        user_message = self.user_input.text()
        self.user_input.clear()
        self.update_chat_history('You: ' + user_message)

        bot_message = chatBot(user_message)
        self.update_chat_history('Bot: ' + bot_message)

    def update_chat_history(self, message):
        self.chat_history.append(message)
        self.chat_history.verticalScrollBar().setValue(self.chat_history.verticalScrollBar().maximum())

def chatBot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    ).choices[0].text.strip()

    return response

app = QtWidgets.QApplication(sys.argv)
window = ChatBotWindow()
window.show()
sys.exit(app.exec_())
