import os


def clear_terminal():
    """Limpa a tela do terminal, verificando o sistema operacional."""
    if os.name == 'nt':  # Verifica se o sistema é Windows
        os.system('cls')
    else:  # Para Linux, macOS e outros Unix-like
        os.system('clear')
