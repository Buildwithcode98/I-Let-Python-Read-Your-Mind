from PIL import Image, ImageFilter, ImageEnhance

img = Image.open("dogs.png").convert("L")

art = (
    img.filter(ImageFilter.FIND_EDGES)
       .filter(ImageFilter.SMOOTH_MORE)
)

art = ImageEnhance.Contrast(art).enhance(3)

art.show()

 
