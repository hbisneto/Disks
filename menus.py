import disks
import info
from action import (
    eject, 
    format, 
    mount, 
    unmount
)

def menu_disk(path):
    disco = disks.get_disks()[path]

    while True:
        print()
        print("="*80)
        print("[!]: What would you like to do with this disk?")
        print("="*80)
        print(f"[DISCO]: {disco['nome']}")
        print(f"[CAMINHO]: {path}")
        print(f"[FileSystem]: {disco['fs']}")
        print("="*80)
        print("[1] Disk Information")
        print("[2] Format...")
        print("[3] Eject...")
        print("[4] Mount")
        print("[5] Unmount")
        print("[0] Back")
        print("="*80)
        opt = input("[ConsoleOS/User]: ")
        print("="*80)

        if opt == "1":
            info.drive_info(path)
            # informacoes(path)

        elif opt == "2":
            format.trigger_action(path)

        elif opt == "3":
            eject.trigger_action(path)

        elif opt == "4":
            mount.trigger_action(path)

        elif opt == "5":
            unmount.trigger_action(path)

        elif opt == "0":
            break

        else:
            print("\nOpção inválida.")