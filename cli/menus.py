def select(
    title: str,
    items: list
):
    print()
    print(title)
    print("=" * len(title))
    print()

    for index, item in enumerate(items, 1):
        print(f"  {index}. {item}")

    print()

    while True:
        try:
            choice = int(input("Opção: "))

            if 1 <= choice <= len(items):
                return items[choice - 1]

            print("[ERROR] Opção inválida.")

        except ValueError:
            print("[ERROR] Digite um número.")