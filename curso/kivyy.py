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
        text: "Cadastrar"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .5
        on_release: app.root.current = "register"

<RegisterScreen>:
    name: "register"
    MDLabel:
        text: "Cadastre novo usuário"
        font_style: "H4"
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .8}
    MDTextField:
        id: new_username
        hint_text: "Usuário"
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: .8
    MDTextField:
        id: new_password
        hint_text: "Senha"
        password: True
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .8
    MDRaisedButton:
        text: "Cadastrar"
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .5
        on_release: root.register_user()

<ResetPasswordScreen>:
    name: "reset"
    MDLabel:
        text: "Esquecer senha"
        font_style: "H4"
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .8}
    MDTextField:
        id: reset_username
        hint_text: "Usuário"
        pos_hint: {"center_x": .5, "center_y": .6}
        size_hint_x: .8
    MDTextField:
        id: new_password
        hint_text: "Nova Senha"
        password: True
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint_x: .8
    MDRaisedButton:
        text: "Resetar Senha"
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .5
        on_release: root.reset_password()

<NotesScreen>:
    name: "notes"
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
    MDLabel:
        id: file_display
        text: ""
        pos_hint: {"center_x": .5, "center_y": .45}
    MDRaisedButton:
        text: "Adicionar Foto"
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .5
        on_release: root.select_photo()
    MDLabel:
        id: photo_display
        text: ""
        pos_hint: {"center_x": .5, "center_y": .35}
    MDRaisedButton:
        text: "Sair"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .5
        on_release: app.root.current = "login"
"""