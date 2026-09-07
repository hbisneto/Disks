import disks

def drive_info(path):
    disco = disks.get_disks()[path]
    print()
    print("-"*80)
    print("> DISK INFORMATION")
    print("-"*80)
    print(f"Nome:       {disco['nome']}")
    print(f"Caminho:    {path}")
    print(f"Partição:   {disco['particao']}")
    print(f"Tipo:       {disco['tipo']}")
    print(f"Total:      {disco['total']}")
    print(f"Ocupado:    {disco['ocupado']}")
    print(f"Livre:      {disco['livre']}")
    print(f"FileSystem: {disco['fs']}")
    print("-"*80)