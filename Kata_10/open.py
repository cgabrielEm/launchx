def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No fue posible encontrar el archivo config.txt")
    except IsADirectoryError:
        print('El archivo config.txt es un directorio, no es posible leerlo')
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()
