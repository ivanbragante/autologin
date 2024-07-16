import tkinter as tk
from tkinter import messagebox
import json
import os

# Definição das variáveis
guid = ''
id_tcs = ''
senha_tcs = ''
senha_ramal = ''
ramal = ''
senha_cyber = ''
senha_entrust = ''

selected_functions = {}
config_file = "config.json"

def load_config():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return json.load(file)
    return {}

def save_config(config):
    with open(config_file, "w") as file:
        json.dump(config, file)

def save_checkbox_states():
    config_data = {
        "bate_ponto": var_bate_ponto.get(),
        "login_cisco": var_login_cisco.get(),
        "abrir_snowchat": var_abrir_snowchat.get(),
        "gchat": var_gchat.get(),
        "cyberark": var_cyberark.get(),
        "open_entrust": var_open_entrust.get(),
        "guid": guid,
        "id_tcs": id_tcs,
        "senha_tcs": senha_tcs,
        "senha_ramal": senha_ramal,
        "ramal": ramal,
        "senha_cyber": senha_cyber,
        "senha_entrust": senha_entrust
    }
    save_config(config_data)

def show_gui():
    global selected_functions
    global guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust

    # Carregar configurações
    config = load_config()
    guid = config.get("guid", "")
    id_tcs = config.get("id_tcs", "")
    senha_tcs = config.get("senha_tcs", "")
    senha_ramal = config.get("senha_ramal", "")
    ramal = config.get("ramal", "")
    senha_cyber = config.get("senha_cyber", "")
    senha_entrust = config.get("senha_entrust", "")

    # Inicializar a janela
    root = tk.Tk()
    root.title("BR-SD Auto Login")

    # Obtém a largura e altura da tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Define o tamanho da janela
    window_width = int(screen_width * 0.2)
    window_height = int(screen_height * 0.25)

    # Centraliza a janela na tela
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Variáveis para os checkboxes
    global var_bate_ponto, var_login_cisco, var_abrir_snowchat, var_gchat, var_cyberark, var_open_entrust
    var_bate_ponto = tk.BooleanVar(value=config.get("bate_ponto", True))
    var_login_cisco = tk.BooleanVar(value=config.get("login_cisco", True))
    var_abrir_snowchat = tk.BooleanVar(value=config.get("abrir_snowchat", True))
    var_gchat = tk.BooleanVar(value=config.get("gchat", True))
    var_cyberark = tk.BooleanVar(value=config.get("cyberark", True))
    var_open_entrust = tk.BooleanVar(value=config.get("open_entrust", True))

    # Criação dos checkboxes
    tk.Checkbutton(root, text="Bater Ponto", variable=var_bate_ponto).pack(anchor='w')
    tk.Checkbutton(root, text="Login Cisco", variable=var_login_cisco).pack(anchor='w')
    tk.Checkbutton(root, text="Abrir Snowchat", variable=var_abrir_snowchat).pack(anchor='w')
    tk.Checkbutton(root, text="Abrir GChat", variable=var_gchat).pack(anchor='w')
    tk.Checkbutton(root, text="Cyberark", variable=var_cyberark).pack(anchor='w')
    tk.Checkbutton(root, text="Abrir Entrust", variable=var_open_entrust).pack(anchor='w')

    def on_yes_click():
        global selected_functions
        selected_functions = {
            'bate_ponto': var_bate_ponto.get(),
            'login_cisco': var_login_cisco.get(),
            'abrir_snowchat': var_abrir_snowchat.get(),
            'gchat': var_gchat.get(),
            'cyberark': var_cyberark.get(),
            'open_entrust': var_open_entrust.get()
        }
        save_checkbox_states()
        root.quit()

    def on_no_click():
        global selected_functions
        selected_functions = None
        root.quit()

    def open_settings():
        settings_window = tk.Toplevel(root)
        settings_window.title("Configurações")

        # Define o tamanho da janela de configurações
        settings_width = int(screen_width * 0.18)
        settings_height = int(screen_height * 0.4)
        settings_window.geometry(f"{settings_width}x{settings_height}")

        # Carregar configurações
        config = load_config()

        # Campos de entrada
        tk.Label(settings_window, text="GUID:").pack(anchor='w')
        entry_guid = tk.Entry(settings_window, width=23)
        entry_guid.insert(0, config.get("guid", ""))
        entry_guid.pack(anchor='w')

        tk.Label(settings_window, text="Login Dicon:").pack(anchor='w')
        entry_id_tcs = tk.Entry(settings_window, width=23)
        entry_id_tcs.insert(0, config.get("id_tcs", ""))
        entry_id_tcs.pack(anchor='w')

        tk.Label(settings_window, text="Senha Dicon:").pack(anchor='w')
        entry_senha_tcs = tk.Entry(settings_window, width=23)
        entry_senha_tcs.insert(0, config.get("senha_tcs", ""))
        entry_senha_tcs.pack(anchor='w')

        tk.Label(settings_window, text="Senha Cisco:").pack(anchor='w')
        entry_senha_ramal = tk.Entry(settings_window, width=23)
        entry_senha_ramal.insert(0, config.get("senha_ramal", ""))
        entry_senha_ramal.pack(anchor='w')

        tk.Label(settings_window, text="Ramal:").pack(anchor='w')
        entry_ramal = tk.Entry(settings_window, width=23)
        entry_ramal.insert(0, config.get("ramal", ""))
        entry_ramal.pack(anchor='w')

        tk.Label(settings_window, text="Senha Cyberark:").pack(anchor='w')
        entry_senha_cyber = tk.Entry(settings_window, width=23)
        entry_senha_cyber.insert(0, config.get("senha_cyber", ""))
        entry_senha_cyber.pack(anchor='w')

        tk.Label(settings_window, text="Senha Entrust:").pack(anchor='w')
        entry_senha_entrust = tk.Entry(settings_window, width=23)
        entry_senha_entrust.insert(0, config.get("senha_entrust", ""))
        entry_senha_entrust.pack(anchor='w')

        def save_settings():
            global guid, id_tcs, senha_tcs, senha_ramal, ramal, senha_cyber, senha_entrust
            guid = entry_guid.get()
            id_tcs = entry_id_tcs.get()
            senha_tcs = entry_senha_tcs.get()
            senha_ramal = entry_senha_ramal.get()
            ramal = entry_ramal.get()
            senha_cyber = entry_senha_cyber.get()
            senha_entrust = entry_senha_entrust.get()

            # Salvar configurações no arquivo JSON
            config_data = {
                "guid": guid,
                "id_tcs": id_tcs,
                "senha_tcs": senha_tcs,
                "senha_ramal": senha_ramal,
                "ramal": ramal,
                "senha_cyber": senha_cyber,
                "senha_entrust": senha_entrust
            }
            save_config(config_data)
            messagebox.showinfo("Configurações", "Configurações salvas com sucesso!")
            settings_window.destroy()

        save_button = tk.Button(settings_window, text="Save", command=save_settings)
        save_button.place(relx=0.75, rely=0.90, anchor='center')

    gear_button = tk.Button(root, text="⚙️", command=open_settings)
    gear_button.pack(side='right', padx=10)

    yes_button = tk.Button(root, text="Run", command=on_yes_click)
    no_button = tk.Button(root, text="Close", command=on_no_click)

    yes_button.pack(side='left', padx=10, pady=10)
    no_button.pack(side='right', padx=10, pady=10)

    # Adicionando a mensagem no rodapé
    footer = tk.Label(root, text="Created by Ivan", font=("Arial", 8))
    footer.place(relx=0.43, rely=0.88, anchor='center')

    root.mainloop()

    return selected_functions, guid, id_tcs, senha_tcs, senha_ramal, senha_cyber, senha_entrust, ramal