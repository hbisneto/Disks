def get_disks():
    disks = {
        "/": {
            "nome": "SSD Interno",
            "particao": "/dev/nvme0n1p2",
            "total": "476 GB",
            "ocupado": "231 GB",
            "livre": "245 GB",
            "fs": "ext4",
            "tipo": "Interno"
        },

        "/dev/sda1": {
            "nome": "HD Externo",
            "particao": "/dev/sda1",
            "total": "931 GB",
            "ocupado": "542 GB",
            "livre": "389 GB",
            "fs": "ntfs",
            "tipo": "Externo"
        },

        "/dev/sdb1": {
            "nome": "Pendrive",
            "particao": "/dev/sdb1",
            "total": "64 GB",
            "ocupado": "12 GB",
            "livre": "52 GB",
            "fs": "vfat",
            "tipo": "Externo"
        }
    }

    return disks

def listar_discos():
    print()
    print("-"*80)
    print("DISPOSITIVOS DE ARMAZENAMENTO")
    print("-"*80)

    paths = list(get_disks().keys())

    for indice, caminho in enumerate(paths, start=1):
        disco = get_disks()[caminho]

        print(f"[{indice}] {disco['nome']}")
        print(f"    Caminho:   {caminho}")
        print(f"    Partição:  {disco['particao']}")
        print(f"    Tipo:      {disco['tipo']}")
        print(f"    Total:     {disco['total']}")
        print(f"    Ocupado:   {disco['ocupado']}")
        print(f"    Livre:     {disco['livre']}")
        print(f"    FileSystem: {disco['fs']}")
        print("-"*80)
    print()


def selecionar_disco():
    paths = list(get_disks().keys())

    while True:
        listar_discos()
        print("="*80)
        opt = input("[!]: Select a disk (number) or 'q' to quit: ")
        print("="*80)

        if opt.lower() == "q":
            return None

        try:
            index = int(opt)

            if 1 <= index <= len(paths):
                return paths[index - 1]

            print("\nOpção inválida.\n")

        except ValueError:
            print("\nDigite um número válido.\n")