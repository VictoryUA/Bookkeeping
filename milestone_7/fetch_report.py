import requests
import sys

def fetch_report(month, department):
    url = f'http://127.0.0.1:5008/birthdays?month={month}&department={department}'
    response = requests.get(url)
    
    if response.status_code == 200:
        report = response.json()
        print(f"Total: {report['total']}")
        print("Employees:")
        for employee in report['employees']:
            print(f"{employee['id']}, {employee['name']}, {employee['birthday']}")
    else:
        print("Error fetching report.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 fetch_report.py <month> <department>")
    else:
        month = sys.argv[1]
        department = sys.argv[2]
        fetch_report(month, department)
        