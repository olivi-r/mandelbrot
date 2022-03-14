import tkinter


pixel_size = 1

width = 400
height = 400
inf_limit = 10000
rec = 200

data = [["#000000" for _ in range(width)] for _ in range(height)]


# calculate if each pixel is in the set
# f(z) = z ** 2 + c
# where c is the original point in the complex plane
# new_z = f(prev_z)
# when abs(z) does not tend to infinity, it is in the set
for y in range(height):
    for x in range(width):
        x_val = 5 * (x / width) - 3
        y_val = 5 * (y / height) - 2.5
        z = c = complex(x_val, y_val)

        brightness = 0
        for n in range(rec):
            z = (z ** 2) + c
            if abs(z) > inf_limit:
                brightness = 255 * n / rec
                break

        else:
            brightness = 255

        colour = "#" + f"{int(brightness):02x}" * 3
        data[y][x] = colour


root = tkinter.Tk()
root.title("Mandelbrot Set")
root.geometry(f"{pixel_size * width}x{pixel_size * height}")
root.resizable(0, 0)
canvas = tkinter.Canvas(
    root, highlightthickness=0, bg="#000000", width=pixel_size * width, height=pixel_size * height
)


# draw pixels
for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val != "#000000":
            canvas.create_rectangle(
                pixel_size * x, pixel_size * y, pixel_size * (x + 1), pixel_size * (y + 1), fill=val,
                outline=""
            )


canvas.pack(fill="both", expand=1)
root.mainloop()
