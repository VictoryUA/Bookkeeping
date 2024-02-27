from faker import Faker
import csv

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

if __name__ == "__main__":
    generate_data(100) 