import flet as ft

name = "Column wrapping"


def example():
    HEIGHT = 400

    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(i)),
                    alignment=ft.alignment.center,
                    width=30,
                    height=30,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items

    async def slider_change(e):
        col.height = float(e.control.value)
        await col.update_async()

    width_slider = ft.Slider(
        min=0,
        max=HEIGHT,
        divisions=20,
        value=HEIGHT,
        label="{value}",
        width=500,
        on_change=slider_change,
    )

    col = ft.Column(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(10),
        height=HEIGHT,
    )

    return ft.Column(
        [
            ft.Column(
                [
                    ft.Text(
                        "Change the column height to see how child items wrap onto multiple columns:"
                    ),
                    width_slider,
                ]
            ),
            ft.Container(content=col, bgcolor=ft.colors.AMBER_100),
        ]
    )
