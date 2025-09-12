from modules.menu import Menu

if __name__ == "__main__":
    try:
        Menu.apresentacao()
        Menu.login()
        Menu.menuPrincipal()
    except KeyboardInterrupt:
        print("\n\n⛔  Programa interrompido pelo usuário. Até logo!")
    except Exception as e:
        print(f"\n⚠️  Ocorreu um erro inesperado: {e}")