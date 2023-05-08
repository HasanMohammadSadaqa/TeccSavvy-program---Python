import csv
import re


class InvalidDataError(Exception):
    pass


def validate_data(row):
    name_pattern = r'^[A-Za-z ]+$'
    age_pattern = r'^\d+$'
    salary_pattern = r'^\d+(\.\d+)?$'

    name = row[0].strip()
    age = row[1].strip()
    salary = row[2].strip()

    if not re.match(name_pattern, name):
        raise InvalidDataError(f"Invalid name '{name}' in row {row}. Name must contain only letters and spaces.")

    if not re.match(age_pattern, age):
        raise InvalidDataError(f"Invalid age '{age}' in row {row}. Age must be a positive integer.")

    age = int(age)
    if age < 18 or age > 120:
        raise InvalidDataError(f"Invalid age '{age}' in row {row}. Age must be between 18 and 120.")

    if not re.match(salary_pattern, salary):
        raise InvalidDataError(f"Invalid salary '{salary}' in row {row}. Salary must be a positive float or integer.")

    salary = float(salary)
    if salary >= 1000000:
        raise InvalidDataError(f"Invalid salary '{salary}' in row {row}. Salary must be less than $1 million.")

    return name, age, salary


def read_csv_file(filename):
    data = []

    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip the header row

            for row_num, row in enumerate(csv_reader, start=2):
                if len(row) != 3:
                    print(f"Warning: Skipping row {row_num}. Expected 3 columns, found {len(row)} columns.")
                    continue

                try:
                    validated_row = validate_data(row)
                    data.append(validated_row)
                except InvalidDataError as e:
                    print(f"Invalid data in row {row_num}: {e}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to read file '{filename}'.")

    return data


# Example usage
filename = 'data.csv'
data = read_csv_file(filename)
print(data)
