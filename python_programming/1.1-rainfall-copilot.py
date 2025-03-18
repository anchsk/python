def main():
    total_days = 0
    rainy_days = 0
    total_rainfall = 0
    max_rainfall = 0

    while True:
        try:
            rainfall = float(input("Enter the amount of rainfall (9999 to exit): "))
            if rainfall == 9999:
                break
            if rainfall < 0:
                print("Negative rainfall value is not allowed. Please try again.")
                continue
            total_days += 1
            if rainfall > 0:
                rainy_days += 1
                total_rainfall += rainfall
                if rainfall > max_rainfall:
                    max_rainfall = rainfall
        except ValueError:
            print("Please enter a numeric value.")

    print(f"Total number of recorded days: {total_days}")
    print(f"Number of rainy days: {rainy_days}")
    print(f"Total rainfall over the period: {total_rainfall}")
    print(f"Maximum rainfall in one day: {max_rainfall}")

if __name__ == "__main__":
    main()