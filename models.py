
class Employee:
    def __init__ (self, employee_id, employee_name, assigned_job):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.assigned_job = assigned_job
        
    def to_dict(self):
            return {
                "_id": self.employee_id,
                "employee_name": self.employee_name,
                "assigned_job": self.assigned_job
            }