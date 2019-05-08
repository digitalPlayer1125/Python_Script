from PIL import Image

def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()

if __name__ == '__main__':
    print("Input the x of the origin")
    x1= int(input())
    print("Input the y of the origin")
    y1= int(input())
    print("Input the x of the end")
    x2= int(input())
    print("Input the y of the end")
    y2= int(input())
    for i in range(1, j): #Set j as the number of images with the number of images with the same name
        image = 'Name_Of_Your_Image(%s).png' %i
        crop(image, (x1, y1, x2, y2), 'Final_Name_Of_The_Image(%s).png'%i)
