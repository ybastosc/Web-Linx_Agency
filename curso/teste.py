from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.imagelist import MDSmartTile
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
import json
import os
import shutil

# Caminho para armazenar os dados dos usuários e arquivos
DATA_FILE = "users.json"
IMAGE_FOLDER = "user_images"

# Criar pasta para armazenar imagens se não existir
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

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
        note = self.ids.note_input.text
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
            notes = "\n".join(users[username]['notes'])
            self.ids.notes_display.text = notes

    def select_file(self):
        self.file_manager = MDFileManager(select_path=self.file_selected)
        self.file_manager.show('/')

    def file_selected(self, path):
        username = self.manager.get_screen("login").ids.username.text
        users = load_data()
        if username in users:
            users[username]['files'].append(path)
            save_data(users)

    def select_image(self):
        self.file_manager = MDFileManager(select_path=self.image_selected)
        self.file_manager.show('/')

    def image_selected(self, path):
        username = self.manager.get_screen("login").ids.username.text
        users = load_data()
        if username in users:
            image_filename = os.path.basename(path)
            new_path = os.path.join(IMAGE_FOLDER, image_filename)
            shutil.copy(path, new_path)
            users[username]['images'].append(new_path)
            save_data(users)
            self.load_images()

    def load_images(self):
        username = self.manager.get_screen("login").ids.username.text
        users = load_data()
        self.ids.image_gallery.clear_widgets()
        if username in users:
            for img_path in users[username]['images']:
                self.ids.image_gallery.add_widget(Image(source=img_path, size_hint=(None, None), size=(100, 100)))

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

<NotesScreen>:
    name: "notes"
    BoxLayout:
        orientation: "vertical"
        MDTextField:
            id: note_input
            hint_text: "Digite sua nota"
        MDRaisedButton:
            text: "Salvar Nota"
            on_release: root.save_note()
        MDRaisedButton:
            text: "Adicionar Arquivo"
            on_release: root.select_file()
        MDRaisedButton:
            text: "Adicionar Imagem"
            on_release: root.select_image()
        ScrollView:
            GridLayout:
                id: image_gallery
                cols: 3
                size_hint_y: None
                height: self.minimum_height
        MDRaisedButton:
            text: "Sair"
            on_release: app.root.current = "login"
"""

class SecureApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

if __name__ == "__main__":
    SecureApp().run()
