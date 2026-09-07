# Disks

import disks
import menus

def main():
    while True:
        path = disks.selecionar_disco()

        if path is None:
            print("\nSaindo...")
            break

        menus.menu_disk(path)


if __name__ == "__main__":
    main()