from flask import Flask, request, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John Doe", "birthday": "april 18", "department": "HR"},
    {"id": 2, "name": "Jane Smith", "birthday": "april 20", "department": "Engineering"},
    {"id": 3, "name": "Tom Brown", "birthday": "april 25", "department": "HR"},
    {"id": 4, "name": "Alice Johnson", "birthday": "april 30", "department": "HR"}
]

@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    
    filtered_employees = [employee for employee in employees if employee['department'] == department and employee['birthday'].split(' ')[0].lower() == month.lower()]
    
    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }
    
    return jsonify(response)

@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    
    filtered_employees = [employee for employee in employees if employee['department'] == department and employee['birthday'].split(' ')[0].lower() == month.lower()]
    
    response = {
        "total": len(filtered_employees),
        "employees": filtered_employees
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5008)