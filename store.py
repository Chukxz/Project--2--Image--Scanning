#import os
# print(os.name," ",os.curdir," ",os.pardir," ",os.sep," ",os.linesep)


# arr1 = np.random.random(100000) #100k random values
# arr2 = np.random.random(100000) #100k random values

# arr1 = [1,2,3]
# arr2 = [4,5,6]

# #Faster in operation
# res1 = sg.fftconvolve(arr1,arr2)
# print("Done",res1,type(res1))


# # Slower in operation
# res2 = np.convolve(arr1,arr2)
# print("final",res2,type(res2))


#Use gaussian blur
#Convert to greyscale 
#Use Sobel edge detector in x and y direction
#Also get gradient and orientation
#Use canny edge

# #Define the pizel data
# pixel_data = [(255,0,0),(0,255,0),(0,0,255)]

# #Create an new image with the desired dimensions
# image = Image.new('RGB',(3,1))

# #Set the pixel values for the image
# image.putdata(pixel_data)

# #Save the image file
# image.save('test1.png')

# o = Image.open('test1.png')
# p = o.load()

# for i in range(o.size[0]):
#     for j in range(o.size[1]):
#         print(p[i,j])



# #get the column names from the Pixels table in the ImagePixelValue database
# table_name = 'Pixels'

# columns = []
# for row in conn.execute(f"PRAGMA table_info('{table_name}')"):
#     columns.append(row[1])

# new_values = ['hey','hi','there'] #Values to set

# i = 0
# for column in columns:
#     cursor.execute(f"UPDATE {table_name} SET {column} = ? WHERE id = ?",(new_values[i],1)) #Set
#     i+1



#Insert into database
# cursor.execute('''
#     INSERT INTO Pixels (name,email)
#     VALUES (?,?)
# ''',('John Doe','johndoe@example.com')
# )



# # Join tables
# def join(index):
#     name = "image_row_"+str(index)
#     nameId = name+'.id'
#     nameR = name+'.value_R'
#     nameG = name+'.value_G'
#     nameB = name+'.value_B'
#     queryJoin = f"""SELECT {nameId}, {nameR}, {nameG}, {nameB}
#     FROM Pixels
#     JOIN {name} ON Pixels.id = {nameId}"""
#     cursor.execute(queryJoin)
#     rows = cursor.fetchall()

#     for row in rows:
#         print(row[1],row[2],row[3])

import re
test = '-gg'

resfindall = re.findall(r"-",test)
resmatch = re.match(r'-',test)

if not resmatch == None:
    if resfindall.count("-") == 1:
        res = re.sub("-","",test)
        print(res)
    else: raise TypeError
else:
    raise TypeError

