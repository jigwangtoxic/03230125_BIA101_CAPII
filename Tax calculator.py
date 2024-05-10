class Employee:
    def __init__(self, name, total_income, position, organization_type, children_in_school=False):
        """
        Constructor to initialize an Employee object.
        
        Args:
            name (str): The name of the employee.
            total_income (float): Total income of the employee for 1 year.
            position (str): The position of the employee (Regular or Contract).
            organization_type (str): Type of organization (Government, Private, Corporate).
            children_in_school (bool): True if the employee has children in school, False otherwise.
        """
        self.name = name
        self.total_income = total_income
        self.position = position
        self.organization_type = organization_type
        self.children_in_school = children_in_school

    def calculate_tax(self):
        """
        Method to calculate the tax for the employee.
        
        Returns:
            float: The calculated tax amount.
        """
        if self.total_income < 0:
            raise ValueError("Total income cannot be negative")

        # Define tax slabs and rates (Progressive Income Tax - PIT)
        tax_slabs = [(0, 50000, 0.0), (50000, 100000, 0.1), (100000, 200000, 0.15), (200000, float('inf'), 0.20)]
        
        # Initialize tax
        tax = 0
        
        # Calculate tax based on income slabs
        for slab in tax_slabs:
            min_income, max_income, tax_rate = slab
            if min_income <= self.total_income < max_income:
                tax += (self.total_income - min_income) * tax_rate
                break
            elif self.total_income >= max_income:
                tax += (max_income - min_income) * tax_rate
        
        # Deductibles
        if self.organization_type == "Government":
            # Government employees don't have PF deductions
            nppf = 0
        else:
            # Corporate and private employees have PF deductions
            nppf = 0.05 * self.total_income

        # Deduct tax for children
        if self.children_in_school:
            tax -= 500  # Assuming 500 tax deduction per child in school

        # Deduct GIS for corporate employees
        if self.organization_type == "Corporate":
            gis = 0.02 * self.total_income
            tax -= gis

        # Net tax after deductions
        net_tax = tax - nppf
        
        return net_tax

# Example usage
employee1 = Employee("Dorji", 600000, "Regular", "Corporate", children_in_school=True)
print(f"{employee1.name} has to pay ${employee1.calculate_tax()} in taxes.")

employee2 = Employee("Kinley", 400000, "Contract", "Government")
print(f"{employee2.name} has to pay ${employee2.calculate_tax()} in taxes.")
