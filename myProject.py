from math import*
from myplot import plot 
# x = float (input("Введите действительную часть "))
# y = float (input("Введите мнимую часть "))
# print ("z = ",x,"+",y,"i")


arr_x50 = []
arr_y50 = []

arr_x30 = []
arr_y30 = []

arr_x20 = []
arr_y20 = []

arr_x10 = []
arr_y10 = []

arr_x5 = []
arr_y5 = []

iRe = -2
while iRe < 2:
    iIm = -2
    while iIm < 2:
        x = iRe
        y = iIm
        i = 0
        z = complex(0)
        arr = []
        while i < 10:
            z = z*z + complex (x, y)
            arr.append(z)
            i+=1
       # print (arr)  
        arr_new = []
        # print (z)
        for i in arr:
            Im_y = z.imag
            Re_x = z.real
            z_modull = sqrt (Im_y * Im_y + Re_x * Re_x)
            arr_new.append(z_modull)
        if arr_new[-1] > 15:
            print (" > 50")
        else:
            arr_y50.append(y)
            arr_x50.append(x)
            c50 = 'pink'
            if arr_new[-1] > 3:
                print (" > 30")
            else:
                arr_y30.append(y)
                arr_x30.append(x)
                c30 = 'yellow'
                if arr_new[-1] > 1.5:
                    print(" > 20")
                else:
                    arr_y20.append(y)
                    arr_x20.append(x)
                    c20 = 'red'
                    if arr_new[-1] > 0.75:
                        print(" > 10")
                    else:
                        arr_y10.append(y)
                        arr_x10.append(x)
                        c10 = 'blue'
                        if arr_new[-1] > 0.325:
                            print(" > 5")
                        else:
                            arr_y5.append(y)
                            arr_x5.append(x)
                            c5 = 'black' 
        iIm += 0.01
    iRe += 0.01

plot(arr_x50, arr_y50, c50, arr_x30, arr_y30, c30, arr_x20, arr_y20, c20, arr_x10, arr_y10, c10, arr_x5, arr_y5, c5)