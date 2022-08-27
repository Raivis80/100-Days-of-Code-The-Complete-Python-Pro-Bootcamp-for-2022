#Welcome to band name generator


def band_name_generator():
    print("Welcome to band name generator") # Welcome message
    city = input("What is name of the city you are from?\n") #input city name
    pet = input("What is name of your pet?\n") #input pet name

    return "Your band name is", city, pet #print band name

print(band_name_generator()) #call function