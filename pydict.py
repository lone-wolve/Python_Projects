
# import csv
# with open ('Country.csv' , mode= 'r') as infile:
#     reader = csv.reader(infile)

#     mydict= {}

#     for row in reader:

#         key = row[0]
#         mydict[key] = row[1] 
#         print(f"{row[0]} ,{row[1]} ,{row[2]} ,{row[3]}")

sals_info_keys = ["Adams","Hibba","Therse"]
sals_info_value = ["3087","408954","58849"]
sal_info = {}
indx = 0
for key, values in zip(sals_info_keys,sals_info_value):

    sal_info[key] = values
print(sal_info)

print("*" * 5)

sals_info = {sals_info_keys[indx]:sals_info_value[indx] for indx in range(0, len(sals_info_keys))}
print(sal_info)

new_dict = {k:v for k,v in sal_info.items()  }

print(new_dict)

    
