STYLES = {
    "h1": {
        "char": "=",
        "center": True,
    },
    "h2": {
        "char": "=",
        "center": False,
    },
    "h3": {
        "char": "-",
        "center": False,
    },
    "h4": {
        "prefix": "> ",
    },
    "h5": {
        "prefix": "  • ",
    },
}


def show(text: str, style: str = "h2", width: int = 80) -> None:
    if style not in STYLES:
        raise ValueError(f"Estilo inválido: {style}")

    config = STYLES[style]

    print()

    if style == "h1":
        print(config["char"] * width)
        print(text.center(width))
        print(config["char"] * width)

    elif style in ("h2", "h3"):
        print(text)
        print(config["char"] * len(text))

    else:
        print(config["prefix"] + text)

    print()