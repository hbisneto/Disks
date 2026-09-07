from cli import headings
from cli import messages
from cli import lists
from cli import tables
from cli import menus
from cli import separators


headings.show("DISK CLEANER", style="h1")

headings.show("Discos disponíveis", style="h2")

disks = [
    {
        "path": "/",
        "name": "SSD",
        "total": "500 GB",
        "used": "380 GB",
        "free": "120 GB",
    },
    {
        "path": "/dev/sdb",
        "name": "HD",
        "total": "1 TB",
        "used": "220 GB",
        "free": "780 GB",
    },
]

tables.show(disks)

separators.show()

messages.info("Selecione um disco.")

selected = menus.select(
    "Discos",
    [disk["path"] for disk in disks]
)

headings.show("Disco selecionado", style="h3")

messages.success(f"Você selecionou {selected}")