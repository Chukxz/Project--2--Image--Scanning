import perbackendconfig,re
from PIL import Image

perbackendconfig.configure()


# #Define the pizel data
pixel_data1 = [(255,0,0),(0,255,0),(0,0,255)]
pixel_data2 = [(255,240,142),(89,255,90),(149,212,255)]



#Create an new image with the desired dimensions
image = Image.new('RGB',(3,2))


#Set the pixel values for the image
image.putdata(pixel_data1)

image.putdata(pixel_data2)

#Save the image file
image.save('test3.png')

# o = Image.open('test2.png')
# p = o.load()

# for i in range(o.size[0]):
#     for j in range(o.size[1]):
#         print(p[i,j])







# #Create an new image with the desired dimensions
# image = Image.new('RGB',(width,height))

# #Set the pixel values for the image
# image.putdata(pixel_data)

# #Save the image file
# image.save('Pipe Puzzle GrayScale.png')



