def calculate_bmi(height, weight):
    """
    Calculate BMI given height (in meters) and weight (in kilograms).

   """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values.")
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def interpret_bmi(bmi):
    """
    Interpret the BMI and provide a classification.

    Args:
        bmi (float): Calculated BMI.

    Returns:
        str: BMI interpretation.
    """
    if bmi <= 0:
        return "Invalid BMI. Height and weight must be positive values."
    elif bmi < 16:
        return "Very severely underweight"
    elif bmi < 16.9:
        return "Severely underweight"
    elif bmi < 18.4:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    elif bmi < 34.9:
        return "Obese (Class I)"
    elif bmi < 39.9:
        return "Obese (Class II)"
    else:
        return "Obese (Class III)"


def main():
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))

        bmi = calculate_bmi(height, weight)
        print(f"Your BMI is {bmi}, indicating that you are {interpret_bmi(bmi)}.")

    except ValueError as ve:
        print("Error:", ve)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
