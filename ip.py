__author__ = 'ankurs'

ip = input('Enter ip address: ')

#print(ip, mask)
a = ip.split('.')
#b = mask.split('.')
#print(a,b)

#if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (0 <= int(a[1]) <=255) and (0 <= int(a[2]) <=255) and (0 <= int(a[3]) <=255) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) :
if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
    print('Valid ip')
else:
    print('Enter a valid ip')

masks = [0,128,192,224,240,248,252,254,255]

mask = input('Enter network mask: ')
b = mask.split('.')
#print(b)
if (len(b) ==4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3]) ) :
    print('Valid mask ')
else:
    print('Invalid mask')

#255.255.255.0 = 11111111.11111111.11111111.00000000

oc1 = bin(int(b[0])).split('b')[1]
print(oc1)



