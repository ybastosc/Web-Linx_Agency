from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.filemanager import MDFileManager
import json
import os

# Caminho para armazenar os dados dos usuários
DATA_FILE = "users.json"

# Função para carregar os dados existentes
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Função para salvar os dados
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Gerenciador de Telas
class LoginScreen(Screen):
    def do_login(self):
        username = self.ids.username.text
        password = self.ids.password.text
        users = load_data()
        if username in users and users[username]['password'] == password:
            self.manager.current = "notes"
        else:
            self.show_error("Usuário ou senha inválidos!")

    def show_error(self, message):
        dialog = MDDialog(text=message)
        dialog.open()

class RegisterScreen(Screen):
    def register_user(self):
        username = self.ids.new_username.text
        password = self.ids.new_password.text
        users = load_data()
        if username in users:
            self.show_error("Usuário já existe!")
        else:
            users[username] = {"password": password, "notes": [], "files": [], "images": []}
            save_data(users)
            self.manager.current = "login"

    def show_error(self, message):
        dialog = MDDialog(text=message)
        dialog.open()

class NotesScreen(Screen):
    def save_note(self):
        note = self.ids.note_input.text.strip()
        if not note:
            return
        username = self.manager.get_screen("login").ids.username.text
        users = load_data()
        if username in users:
            users[username]['notes'].append(note)
            save_data(users)
            self.ids.note_input.text = ""
            self.load_notes()

    def load_notes(self):
        username = self.manager.get_screen("login").ids.username.text
        users = load_data()
        if username in users:
            self.ids.notes_display.text = "\n".join(users[username]['notes'])

    def select_file(self):
        self.file_manager = MDFileManager(select_path=self.file_selected, exit_manager=self.close_manager)
        self.file_manager.show('/')

    def file_selected(self, path):
        username = self.manager.get_screen("login").ids.username.text
        users = load_data()
        if username in users:
            users[username]['files'].append(path)
            save_data(users)
        self.close_manager()

    def select_image(self):
        self.file_manager = MDFileManager(select_path=self.image_selected, exit_manager=self.close_manager)
        self.file_manager.show('/')

    def image_selected(self, path):
        username = self.manager.get_screen("login").ids.username.text
        users = load_data()
        if username in users:
            users[username]['images'].append(path)
            save_data(users)
        self.close_manager()

    def close_manager(self, *args):
        self.file_manager.close()

class ResetPasswordScreen(Screen):
    def reset_password(self):
        username = self.ids.reset_username.text
        new_password = self.ids.new_password.text
        users = load_data()
        if username in users:
            users[username]['password'] = new_password
            save_data(users)
            self.manager.current = "login"
        else:
            self.show_error("Usuário não encontrado!")

    def show_error(self, message):
        dialog = MDDialog(text=message)
        dialog.open()

class WindowManager(ScreenManager):
    pass

KV = """
ScreenManager:
    LoginScreen:
    RegisterScreen:
    NotesScreen:
    ResetPasswordScreen:

<LoginScreen>:
    name: "login"
    MDLabel:
        text: "Bem-vindo ao Cofre Seguro"
        font_style: "H4"
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .8}
    MDTextField:
        id: username
        hint_text: "Usuário"
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: .8
    MDTextField:
        id: password
        hint_text: "Senha"
        password: True
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .8
    MDRaisedButton:
        text: "Entrar"
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .5
        on_release: root.do_login()
    MDRaisedButton:
        text: "Esqueceu a senha?"
        pos_hint: {"center_x": .5, "center_y": .35}
        size_hint_x: .5
        on_release: app.root.current = "reset_password"
    MDRaisedButton:
        text: "Cadastrar"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .5
        on_release: app.root.current = "register"

<NotesScreen>:
    name: "notes"
    MDLabel:
        text: "Minhas Notas"
        font_style: "H4"
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .9}
    MDTextField:
        id: note_input
        hint_text: "Digite sua nota"
        pos_hint: {"center_x": .5, "center_y": .7}
        size_hint_x: .8
    MDRaisedButton:
        text: "Salvar Nota"
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: .5
        on_release: root.save_note()
    MDRaisedButton:
        text: "Adicionar Arquivo"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .5
        on_release: root.select_file()
    MDRaisedButton:
        text: "Adicionar Foto"
        pos_hint: {"center_x": .5, "center_y": .45}
        size_hint_x: .5
        on_release: root.select_image()
    ScrollView:
        MDLabel:
            id: notes_display
            text: ""
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
    MDRaisedButton:
        text: "Sair"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .5
        on_release: app.root.current = "login"
"""

class SecureApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

if __name__ == "__main__":
    SecureApp().run()
