def show(
    rows: list[dict],
    columns: list[str] | None = None
) -> None:

    if not rows:
        return

    if columns is None:
        columns = list(rows[0].keys())

    widths = {}

    for column in columns:
        widths[column] = max(
            len(column),
            *[
                len(str(row.get(column, "")))
                for row in rows
            ]
        )

    header = "  ".join(
        column.ljust(widths[column])
        for column in columns
    )

    separator = "  ".join(
        "-" * widths[column]
        for column in columns
    )

    print(header)
    print(separator)

    for row in rows:
        print(
            "  ".join(
                str(row.get(column, "")).ljust(widths[column])
                for column in columns
            )
        )