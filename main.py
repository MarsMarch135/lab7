from PIL import Image, ImageFilter
def z1():
 Filename = "ars.jpg"
 with Image.open('ars.jpg') as img:
    img.load()
 img.show()
 width, height = img.size

 format = img.format
 mode = img.mode
 print("Width:", width)
 print("Height:", height)
 print("Format:", format)
 print("Color Model:", mode)
z1()
def z2():

    img=Image.open('ars.png')
    img.show()
    new = img.resize((img.width // 3, img.height // 3))
    new.save("new.png")
    con = img.rotatre(188)
    con.save('newflip.png')
    con = img.transpose(Image.Flip_left_right)
    con.save("newflip1.png")
z2()
def z3():
 name = ["1.jpg", "2.jpg", "3.jpg"]
 for file in name:
     with Image.open(file) as img:
         img.load()
         new1 = img.filter(ImageFilter.CONTOUR)
         new1.show()
         new1.save('new' + file)


z3()
def z4():
    image1 = Image.open("ars.jpg")
    new1 = image1.resize((image1.width // 4, image1.height // 4))
    img = Image.open("1.jpg")
    img.paste(new1)
    img.save("arsf.jpg")
z4()

