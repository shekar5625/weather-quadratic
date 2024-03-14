import numpy as np  # for quadratic solutions


def calculate_weather(a, b, c):
  
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots" 
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Single real root: {root}"
    else:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
        return f"Two real roots: {root1}, {root2}"

def read_weather_from_keyboard():
    a = float(input("Enter coefficient 'a': "))
    b = float(input("Enter coefficient 'b': "))
    c = float(input("Enter coefficient 'c': "))
    return a, b, c


def read_weather_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        weather_data = []
        for line in lines:
            a, b, c = map(float, line.strip().split())
            weather_data.append((a, b, c))
    return weather_data


def main():
 
    
   
    a, b, c = 1, -3, 2
    print("Weather parameters from hard coded values:")
    print(calculate_weather(a, b, c))
    

    print("\nWeather parameters from keyboard input:")
    a, b, c = read_weather_from_keyboard()
    print(calculate_weather(a, b, c))
    

    print("\nWeather parameters from file:")
    filename = "weather_data.txt"  
    weather_data = read_weather_from_file(filename)
    for idx, (a, b, c) in enumerate(weather_data):
        print(f"Set {idx+1}: {calculate_weather(a, b, c)}")

if _name_ == "_main_":
    main()
