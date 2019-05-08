from PIL import Image

def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()

if __name__ == '__main__':
    for i in range(1, j): #Set j as the number of images with the number of images with the same name
        image = 'Name_Of_Your_Image(%s).png' %i
        crop(image, (0, 180, 1000, 620), 'Final_Name_Of_The_Image(%s).png'%i)
