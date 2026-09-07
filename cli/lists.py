def show(
    items: list,
    style: str = "bullet"
) -> None:

    if style == "bullet":
        for item in items:
            print(f"  • {item}")

    elif style == "numbered":
        for index, item in enumerate(items, 1):
            print(f"  {index}. {item}")

    else:
        raise ValueError(f"Estilo inválido: {style}")