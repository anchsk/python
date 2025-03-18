total_days = 0
total_rainy_days = 0
total_rain = 0
max_rain = 0


while True:
    rainfall_today = input("Enter a number: ")
    
    if rainfall_today == '9999' or rainfall_today == 'q':
        break
    
    try:
        val = int(rainfall_today)
        if val < 0:
            raise Exception()                                 
    except:
        print("Please, enter a valid number!")
    else: 
        if val > 0:
            total_rainy_days += 1
            total_rain += val
        total_days += 1
        
        if val > max_rain:
            max_rain = val

print(f' Total: {total_days} \n Rainy days: {total_rainy_days} \n Max rain: {max_rain} \n Total rain: {total_rain}')
