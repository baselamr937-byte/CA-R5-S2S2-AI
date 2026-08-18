from Person import Person
'''




'''


class Staff(Person):
    '''Class for hospital staff, inheriting from Person.'''
    _total_staff_count =0
    def __init__(self, name: str, age: int, position: str, department: str, shift: str, experience: int, base_salary: float = 7000.0):
        super().__init__(name, age)
        self.position = position
        self.department = department
        self.shift = shift
        self.experience = experience
        self.base_salary = base_salary
        Staff.total_staff_count += 1

    def view_info(self) -> str:
        '''View detailed staff information.'''
        return (
            f"Staff Name: {self.name} | Age: {self.age}\n"
            f"Position: {self.position} | Department: {self.department}\n"
            f"Shift: {self.shift} | Experience: {self.experience} years | Salary: ${self.base_salary}"
        )

    def change_shift(self, new_shift: str) -> None:
        '''Update staff member's working shift.'''
        self.shift = new_shift
        print(f"Shift for {self.name} updated to: {new_shift}")

    def promote(self, new_position: str, salary_increase: float = 0.0) -> None:
        '''Promote staff to a new position with an optional salary raise.'''
        self.position = new_position
        self.base_salary += salary_increase
        print(f"{self.name} has been promoted to {new_position} (New Salary: ${self.base_salary:,.2f})")

    def is_senior(self) -> bool:
        '''Check if staff member is considered senior based on experience.'''
        return self.experience >= 5

    def calculate_bonus(self) -> float:
        '''Calculate annual bonus based on years of experience.'''
        bonus_rate = 0.05 if self.experience < 5 else 0.10
        return self.base_salary * bonus_rate

    def __repr__(self) -> str:
        return f"Staff({self.name}, {self.position}, {self.department})"
    
    def get_staff_by_department(staff_list, department_name):
        """Return all staff members belonging to a specific department."""
        return [member for member in staff_list if member.department.lower() == department_name.lower()]

    def get_night_shift_staff(staff_list):
        """Return all staff working night shifts."""
        return [member for member in staff_list if "night" in member.shift.lower()]

staff_members = [
    # Doctors
    Staff("Dr. Ahmed Mansour", 48, "Consultant Cardiologist", "Cardiology", "Morning Shift", 18, 18000),
    Staff("Dr. Sarah Khalil", 36, "General Surgeon", "Surgery Department", "Rotational Shift", 9, 14000),
    Staff("Dr. Omar Tarek", 31, "Pediatrician", "Pediatrics Department", "Day Shift", 4, 8500),
    Staff("Dr. Laila Hassan", 42, "Radiologist", "X-Ray & Radiology", "Flexible Shift", 12, 13500),

    # Nurses
    Staff("Mona El-Sayed", 34, "Head Nurse", "Intensive Care Unit (ICU)", "Morning Shift", 10, 6500),
    Staff("Ali Mostafa", 23, "Emergency Nurse", "Emergency Department", "Night Shift", 2, 4200),
    Staff("Nourhan Youssef", 27, "Ward Nurse", "Cardiology", "Night Shift", 4, 4800),

    # Technicians and Pharmacists
    Staff("Hassan Mahmoud", 29, "Lab Technician", "Pathology Lab", "Day Shift", 5, 5200),
    Staff("Yasmine Adel", 33, "Clinical Pharmacist", "Pharmacy", "Evening Shift", 7, 7500),
    Staff("Karim Nabil", 40, "Operations Manager", "Hospital Administration", "Morning Shift", 14, 11000)
]

get_staff_by_department = Staff.get_staff_by_department(staff_members, "Emergency Department")