
# Project: Raw Data Sanitizer
# Goal: Convert messy string input into "AI-ready" floats

def sanitize_data() : 
    # 1. Input (Always returns a string)
    print("Gym AI BMI Sanitizer ")

    input_height = input("Enter you height in cms : ")
    input_weight = input("Enter you  weight in kg : ")
    activity_level = input("Enter your activity level (between 1.0 and 2.0) : ")

    # 2. Cleaning (Removing the 'kg' or 'cm' text)
    clean_height = input_height.replace("cm", "").strip()
    clean_weight = input_weight.replace("kg", "").strip()

    print(f"{clean_height} -- {clean_weight}")

    # 3. Casting (Changing Type from str to float) - try /except 

    try:
        height = float(clean_height)
        weight = float(clean_weight)
        # 4. Logic (BMI Calculation: weight / height_in_meters^2)
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        print(f"\n--- Sanitized Results ---")
        print(f"Weight: {weight} (Type: {type(weight)})")
        print(f"Height: {height} (Type: {type(height)})")
        print(f"Calculated BMI: {round(bmi, 2)}")
        print(f"Adjusted Score: {round(bmi * float(activity_level))}")


    except ValueError:
        print("Input is too messy to clen up.Please enter valid input in cm/kg format")


if __name__ == "__main__":
    sanitize_data()
