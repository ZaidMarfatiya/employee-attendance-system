# Employee Attendance System

This is a Django web application that allows you to manage employee records and track their attendance. It provides functionality to add, edit, and delete employee details, as well as mark their daily attendance.

## Features

- **Employee Management**
  - Add new employees with name, email, mobile number, and department
  - Edit existing employee details
  - Delete employees
  - View a list of all employees

- **Attendance Tracking**
  - Mark today's attendance for each employee
  - View today's attendance records
  - View a list of all attendance records

## Technologies Used

- Python
- Django
- JavaScript
- jQuery
- Ajax
- Bootstrap
- DataTables

## Installation

1. Clone the repository:
    git clone https://github.com/ZaidMarfatiya/employee-attendance-system.git

2. Navigate to the project directory:
    cd employee-attendance-system

3. Create a virtual environment and activate it:
    python -m venv env
    source env/bin/activate  # On Windows, use env\Scripts\activate

4. Install the required packages:
    pip install -r requirements.txt

5. Apply the database migrations:
    python manage.py migrate

6. Start the development server:
    python manage.py runserver

7. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage

1. **Add Employees**
- Click on the "Add Employee" button to open the employee creation form.
- Fill in the required details (name, email, mobile, department) and click "Save".

2. **Edit Employees**
- In the employee list, click the "Edit" button next to the employee you want to modify.
- Update the employee details and click "Save".

3. **Delete Employees**
- In the employee list, click the "Delete" button next to the employee you want to remove.
- Confirm the deletion by clicking the "Delete" button in the confirmation modal.

4. **Mark Attendance**
- Click on the "Today's Attendance" link in the navigation bar.
- For employees who are present, click the "Edit" button and mark the "Present" checkbox.
- For employees who are absent, click the "Add" button and leave the "Present" checkbox unchecked.
- Click "Save" to update the attendance records.

5. **View Attendance**
- Click on the "All Attendance" link in the navigation bar to view a list of all attendance records.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.
