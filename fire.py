import tkinter as tk, random, math

w, h = 500, 500
root = tk.Tk()
root.title("Fireworks")
canvas = tk.Canvas(root, width=w, height=h, bg="black")
canvas.pack()

def launch_firework():
    x = random.randint(100, 400)
    y = h
    rocket = canvas.create_oval(x-2, y-10, x+2, y, fill="white")
    trail = []

    # Rocket rising with tail
    for _ in range(40):
        canvas.move(rocket, 0, -5)
        pos = canvas.coords(rocket)
        tx, ty = (pos[0]+pos[2])//2, (pos[1]+pos[3])//2
        spark = canvas.create_oval(tx, ty, tx+2, ty+2, fill="orange", outline="")
        trail.append(spark)
        if len(trail) > 12:
            canvas.delete(trail.pop(0))
        root.update()
        canvas.after(20)

    for t in trail: canvas.delete(t)
    pos = canvas.coords(rocket)
    canvas.delete(rocket)
    cx, cy = (pos[0]+pos[2])//2, (pos[1]+pos[3])//2
    explode(cx, cy)

def explode(cx, cy):
    sparks = []
    for _ in range(60):
        angle = random.uniform(0, 2*math.pi)
        speed = random.uniform(2, 6)
        dx, dy = math.cos(angle)*speed, math.sin(angle)*speed
        color = random.choice(["red","yellow","blue","green","orange","purple","white"])
        spark = canvas.create_line(cx, cy, cx+dx*2, cy+dy*2, fill=color, width=2)
        sparks.append((spark, dx, dy, color))

    # Glow effect: expanding circles
    glow = canvas.create_oval(cx-10, cy-10, cx+10, cy+10, outline="", fill="yellow")
    for r in range(10, 80, 10):
        canvas.coords(glow, cx-r, cy-r, cx+r, cy+r)
        canvas.itemconfig(glow, fill=random.choice(["yellow","orange","gold"]))
        root.update()
        canvas.after(30)
    canvas.delete(glow)

    # Animate sparks outward with fading
    for step in range(25):
        for spark, dx, dy, color in sparks:
            canvas.move(spark, dx, dy)
            coords = canvas.coords(spark)
            if len(coords) == 4:
                x1,y1,x2,y2 = coords
                canvas.coords(spark, x1,y1, (x1+x2)//2, (y1+y2)//2)
        root.update()
        canvas.after(50)

    for spark,_,_,_ in sparks:
        canvas.delete(spark)

def show_fireworks():
    canvas.delete("all")
    for _ in range(3):
        launch_firework()
    root.after(2000, show_fireworks)

show_fireworks()
root.mainloop()


