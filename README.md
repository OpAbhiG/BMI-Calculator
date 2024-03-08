# BMI-Calculator

```markdown

This Python script calculates Body Mass Index (BMI) based on a person's height and weight, providing a classification from underweight to clinically obese.

## How to Use

1. Ensure Python is installed on your system.
2. Clone or download the repository.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the script:

   ```bash
   python bmi_script.py
   ```

5. Follow on-screen instructions to input your height (in meters) and weight (in kilograms).
6. The program will display your BMI and the corresponding classification.

## Code Structure

- **bmi_script.py**: Main script for BMI calculation and interpretation.
- **README.md**: Overview and usage instructions.

## Functions

### `compute_bmi(height, weight)`

Calculate BMI given height (in meters) and weight (in kilograms).

- Parameters:
  - `height` (float): Height in meters.
  - `weight` (float): Weight in kilograms.

- Returns:
  - float: Calculated BMI.

### `interpret_bmi(bmi)`

Interpret the BMI and provide a classification.

- Parameters:
  - `bmi` (float): Calculated BMI.

- Returns:
  - str: BMI interpretation.

### `execute()`

Main function to run BMI calculation and interpretation.

## Error Handling

The script ensures only numerical values for height and weight are accepted, handling invalid input.
