# import re,numpy as np,scipy as sc
import imagetodatabase as imgdb,imagetograyscale as imggray,perbackendconfig as  perbconf,re,localfileoperations as lfo,os,sqlite3,time,numpy as np,loctuple,math
from PIL import Image

#Create error classes inheriting from the built in UserWarning class
class NoresmatchWarning(UserWarning): ...
class ExcessiveresfindallWarning(UserWarning): ...
class NotinvallistWarning(UserWarning): ...
class NoresValue(UserWarning): ...
class ExitProgram(UserWarning): ...
class NotexactlyvallistWarning(UserWarning): ...
class EmptyString(UserWarning): ...

parentdir = os.getcwd()


row = [(3,), (2,), (4), (9), (4), (7), (6,), (13,), (6,)]

test = (242)

print(loctuple.tupletolist(row))


#Configure file location for my system, modify it on yours
perbconf.configure()

def setImgFilePath(parentdir,inputimg,ext):
    inputimg_file = inputimg + '.' + ext
    img_file_path =os.path.join(parentdir,'Resources','Generated_Images',inputimg,inputimg_file)
    return img_file_path

def setImgFolderPath(parentdir,inputimg):
    img_folder_path = os.path.join(parentdir,'Resources','Generated_Images',inputimg)
    return img_folder_path

def expr(x,y,sigma,scale):
    # Mean (mu) = 0, so it is not included in the variables,
    # but Standard deviation (sigma) is included

    base_expr = 1/(2*(math.pow(sigma,2))*math.pi)

    power_expr_x = math.pow(x,2)/math.pow(sigma,2)
    expr_x = math.pow(math.e,-power_expr_x)

    power_expr_y = math.pow(y,2)/math.pow(sigma,2)
    expr_y = math.pow(math.e,-power_expr_y)

    final_expr = scale * base_expr * expr_x * expr_y
    return final_expr

def kernel(kernel_size=3,sigma=3, scale=10):
    try:
        if kernel_size >= 0:
            if kernel_size %2 == 1:
                val = (kernel_size-1)/2
                row = []
                for i in range(kernel_size):
                    column = []
                    for j in range(kernel_size):
                        column.append(expr(i-val,j-val,sigma,scale))
                    row.append(column)
                return row
            else:print("Even number as Kernel size is not supported")
        else:print('Negative values not allowed')
    except TypeError:
        print('Only integers are allowed')
try:
    start = time.time()
    values = kernel()
    print(values)
    print(np.sum(values))
    print(round(np.sum(values)))
except NameError:
    print('Only integers are allowed')
finally:
    print(f"Time taken : {time.time()-start}")

def pixel_neighbourhood(x=0,y=0,pixels=0,kernel_size=3,sigma=3,scale=10,width=1920,height=1920):
    try:
        values = kernel(kernel_size,sigma,scale)
        if kernel_size >= 0:
            if kernel_size %2 == 1:
                val = (kernel_size-1)/2
                row = []
                for j in range(kernel_size):
                    val_y = int(j - val)
                    coord_y = val_y + y
                    if coord_y>=0 or coord_y<height:
                        column = []
                        for i in range(kernel_size):
                            val_x = int(i - val)
                            coord_x = val_x + x
                            if coord_x>=0 or coord_x<width:
                                column.append(pixels*values[val_x][val_y])
                    row.append(column)
                pixel_value = round(np.sum(row))
                return (pixel_value)
    except BaseException as base_err:
        print(base_err)

print(pixel_neighbourhood(3,0,232))

def tupletolist(tuple):
        """
        Custom function for converting tuple to list
        """
        tuple_string = str(tuple)
        tuple_string_list = re.split(r'[\[]|[\(]|[, ]|[\)]|[\]]',tuple_string)
        return_list =  [j for j in tuple_string_list if j!='']
        return return_list

# refrow = tupletolist(row)

# res = [ for j in refrow]

# print(res)






