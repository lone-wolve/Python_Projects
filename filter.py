
def filterfunc1(x):
    if (x % 2 == 0):
        return False
    return True


def filterfunc2(x):
    if x.isupper():
        return False
    return True


def squarefunc(x):

    return x ** 2

# def convert_cel_farh(temp):

#     return (temp * 9/5) + 32


# def convert_farh_cel(temp):

#     return (temp - 32) * 5/9


    


# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# characters = "abcdDEfGHIJmnop"

temprature = [40,60,50,33,45,60,70]

# odd = list(filter(filterfunc1, numbers))
# print(odd)

# lowercase = list(filter(filterfunc2,characters))
# print(lowercase)

# square = list(map(squarefunc, numbers))
# print(square)
#TODO: Map fuction used 
# celcious_to_Farenhite = list(map(convert_cel_farh, temprature))
# print(celcious_to_Farenhite)

# farenhite_to_celcius = list(map(convert_farh_cel, temprature))
# print(farenhite_to_celcius)

#TODO: USE LAMBDA INSIDE OF MAP FUCTION
celcious_to_Farenhite = list(map(lambda temp: (temp *9/5) + 32, temprature))
print(celcious_to_Farenhite)

farenhite_to_celcius = list(map(lambda temp: (temp -32) * 5/9, temprature))
print(farenhite_to_celcius)