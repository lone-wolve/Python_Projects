# with open ('text.txt', 'r') as fp:
#     read = fp.readline,
 
#     for line in iter(read, ''):
#         print(line)

days = ['monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

days_french = ['Leundi', 'Mardi', 'Mecredi', 'Jeudi', 'Vendraudi', 'Samedi', 'Dimache']

for i ,m in enumerate(zip(days, days_french), start=1):
    print (i, m[0], "=", m[1], "in french")

# for i , d in enumerate(days, start= 1):
#     print(i , d)