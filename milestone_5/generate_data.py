from faker import Faker
import csv
import sys
faker = Faker()

def generate_data(num_employees):
    with open('database.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Hiring Date', 'Department', 'Birthday'])
        for _ in range(num_employees):
            name = faker.name()
            hire_date = faker.date()
            department = faker.random_element(elements=('HR', 'Finance', 'Engineering', 'R&D'))
            birthday = faker.date_of_birth(minimum_age=21, maximum_age=65)
            writer.writerow([name, hire_date, department, birthday])

def read_csv(filename):
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def filter_data(data, month):
    filtered_data = [row for row in data if row['Birthday'].split('-')[1] == month]
    return filtered_data

def generate_report(data, month, verbose=False):
    print(f"Report for {month} generated")
    print("--- Birthdays ---")
    print(f"Total: {len(data)}")
    if verbose:
        print("Employee Names:")
        for row in data:
            print(f"- {row['Name']}")
    print("By department:")
    departments = {}
    for row in data:
        department = row['Department']
        departments[department] = departments.get(department, 0) + 1
    for department, count in departments.items():
        print(f"- {department}: {count}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python report.py database.csv <month> [-v]")
        sys.exit(1)
    filename = sys.argv[1]
    month = sys.argv[2].capitalize()
    verbose = False
    if len(sys.argv) == 4 and sys.argv[3] == '-v':
        verbose = True
    data = read_csv(filename)
    filtered_data = filter_data(data, month)
    generate_report(filtered_data, month, verbose)