import random
from tkinter import (
    Canvas,
    Tk,
)

N, M, SCREEN_HEIGHT = 10, 10, 1080


def create_window(
    screen_height
):
    window = Tk()
    window_height = int(screen_height)
    window.geometry(f"{window_height}x{window_height}")
    return window


def create_canvas(
    window,
    window_height
):
    canvas = Canvas(window,
                    width=window_height * .95,
                    height=window_height * .95,
                    bg="white")
    canvas.pack()
    return canvas


def draw_grid(
    canvas,
    n,
    m
):
    width = canvas.winfo_reqwidth() / n
    height = canvas.winfo_reqheight() / m
    
    for y in range(m):
        for x in range(n):
            canvas.create_rectangle(x * width,
                                    y * height,
                                    x * width + width,
                                    y * height + height,
                                    outline="black",
                                    fill="white")


def generate_grid(
    n,
    m
):
    """
    Génère une grille de n lignes et m colonnes composé de nombre aléatoire entre -15 et 15, on favorise des nombres proches de 0
    :param n: nombre de lignes
    :param m: nombre de colonnes
    :return: la grille générée
    """
    return [[random.randint(-15,
                            15) for _ in range(n)] for _ in range(m)]


def main():
    window = create_window(SCREEN_HEIGHT)
    canvas = create_canvas(window,
                           SCREEN_HEIGHT)
    draw_grid(canvas,
              N,
              M)
    
    grid = generate_grid(N,
                         M)
    print(grid)
    
    window.mainloop()


if __name__ == "__main__":
    main()
