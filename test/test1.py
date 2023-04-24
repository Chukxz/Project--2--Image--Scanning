# import perbackendconfig,re
# from PIL import Image

# perbackendconfig.configure()


# # #Define the pizel data
# pixel_data1 = [(255,0,0),(0,255,0),(0,0,255)]
# pixel_data2 = [(255,240,142),(89,255,90),(149,212,255)]



# #Create an new image with the desired dimensions
# image = Image.new('RGB',(3,2))


# #Set the pixel values for the image
# image.putdata(pixel_data1)

# image.putdata(pixel_data2)

# #Save the image file
# image.save('test3.png')

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


# import time
# start = time.time()

# total_sum = 0
# for i in range(100000000):
#     total_sum +=1
#     print('Done')

# print(f'Sum: {total_sum}')
# print(f"For loop: {time.time() - start} seconds")

# total_sum = sum(range(100000000)) 

# print(f'Sum: {total_sum}')
# print(f"For loop: {time.time() - start} seconds")

# import  numpy as np
# total_sum = np.sum(np.arange(1000000))

# print(f'Sum: {total_sum}')
# print(f"For loop: {time.time() - start} seconds")

import math,numpy as np,time
from PIL import Image

# def expr(x,y,sigma=1,scale=1):
#     # Mean (mu) = 0, so it is not included in the variables,
#     # but Standard deviation (sigma) is included

#     base_expr = 1/(2*(math.pow(sigma,2))*math.pi)

#     power_expr_x = math.pow(x,2)/math.pow(sigma,2)
#     expr_x = math.pow(math.e,-power_expr_x)

#     power_expr_y = math.pow(y,2)/math.pow(sigma,2)
#     expr_y = math.pow(math.e,-power_expr_y)

#     final_expr = scale * base_expr * expr_x * expr_y
#     return final_expr

# def kernel(kernel_size,sigma = 1, scale = 1):
#     try:
#         if kernel_size >= 0:
#             if kernel_size %2 == 1:
#                 val = (kernel_size-1)/2
#                 row = []
#                 for i in range(kernel_size):
#                     column = []
#                     for j in range(kernel_size):
#                         column.append(expr(i-val,j-val,sigma,scale))
#                     row.append(column)
#                 return row
#             else:print("Even number as Kernel size is not supported")
#         else:print('Negative values not allowed')
#     except TypeError:
#         print('Only integers are allowed')

# try:
#     start = time.time()
#     values = kernel(3,0.2)
#     print(values)
#     print(np.sum(values))
#     print(round(np.sum(values)))
# except NameError:
#     print('Only integers are allowed')
# finally:
#     print(f"Time taken : {time.time()-start}")

# def pixel_neighbourhood(x,y,kernel_size,sigma,scale,width,height,pixels):
#     try:
#         values = kernel(kernel_size,sigma,scale)
#         if kernel_size >= 0:
#             if kernel_size %2 == 1:
#                 val = (kernel_size-1)/2
#                 row = []
#                 for j in range(kernel_size):
#                     val_y = j - val
#                     coord_y = val_y + y
#                     if coord_y>=0 or coord_y<height:
#                         column = []
#                         for i in range(kernel_size):
#                             val_x = i - val
#                             coord_x = val_x + x
#                             if coord_x>=0 or coord_x<width:
#                                 column.append(pixels[coord_x,coord_y]*values(val_x,val_y))
#                     row.append()
#                 pixel_value = round(np.sum(row))
#                 return (int(pixel_value))
#     except BaseException as base_err:
#         print(base_err)

import numpy as np


# t = 255*np.random.rand(5,5)

t = [
    [214, 212, 123, 213, 200],
    [211, 210, 128, 214, 198],
    [207, 200, 255, 210, 190],
    [213, 202, 125, 211, 193],
    [213, 201, 126, 210, 192]
]

for i in t:
    print(i)

def expr(x,y,sigma,scale):
    # start = time.time()
    # Mean (mu) = 0, so it is not included in the variables,
    # but Standard deviation (sigma) is included

    base_expr = 1/(2*(math.pow(sigma,2))*math.pi)

    power_expr_x = math.pow(x,2)/math.pow(sigma,2)
    expr_x = math.pow(math.e,-power_expr_x)

    power_expr_y = math.pow(y,2)/math.pow(sigma,2)
    expr_y = math.pow(math.e,-power_expr_y)

    final_expr = scale * base_expr * expr_x * expr_y
    # end = time.time() - start
    # print(f'Time taken: {end} seconds')
    return final_expr

def kernel(kernel_size,sigma = 10, scale = 100):
    if kernel_size >=0 and kernel_size%2==1:
        val = (kernel_size-1)/2
        row = []
        for i in range(kernel_size):
            column = []
            for j in range(kernel_size):
                column.append(expr(i-val,j-val,sigma,scale))
            row.append(column)
        return row
    
kernel_set = kernel(kernel_size=5,sigma=4.5,scale=100)
for i in kernel_set:
    print(i)

def pixel_neighbourhood(pixels,x=0,y=0,width=1,height=1,kernel_size=5,sigma=1,scale=1):
    kernel_set = kernel(kernel_size,sigma,scale)

    if kernel_size>=0 and kernel_size<=min(width,height) and kernel_size%2==1:
        val = int((kernel_size-1)/2)
        row = []
        for j in range(kernel_size):
            column = []
            val_x = int(j-val)
            coord_x = val_x+x
            if coord_x<0:
                coord_x=0
            elif coord_x>=width:
                coord_x = width-1
            for i in range(kernel_size):
                val_y = int(i-val)
                coord_y = val_y+y
                if coord_y<0:
                    coord_y=0
                elif coord_y>=height:   
                    coord_y = height-1
                column.append(pixels[coord_y][coord_x]*kernel_set[i][j])
            row.append(column)
        result = round(np.sum(row)/(math.pow(kernel_size,2)))
        if result>255:
            result = 255
        return result
    
for i in range(len(t)):
    for j in range(len(t)):
        print(pixel_neighbourhood(t,i,j,5,5))

# print(pixel_neighbourhood(t,1,2,5,5))

