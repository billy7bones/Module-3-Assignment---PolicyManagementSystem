class Policyholder:
    def __init__(self, policyholder_id, name, email, status="Active"):
        """
        Initialize a Policyholder object.

        Args:
            policyholder_id (int): Unique ID of the policyholder.
            name (str): Name of the policyholder.
            email (str): Email of the policyholder.
            status (str): Current status of the policyholder. Default is 'Active'.
        """
        self.policyholder_id = policyholder_id
        self.name = name
        self.email = email
        self.status = status
        self.products = []

    def register_policyholder(self):
        """Register the policyholder by setting the status to 'Active'."""
        self.status = "Active"
        return f"Policyholder {self.name} registered successfully."

    def suspend_policyholder(self):
        """Suspend the policyholder by setting the status to 'Suspended'."""
        self.status = "Suspended"
        return f"Policyholder {self.name} has been suspended."

    def reactivate_policyholder(self):
        """Reactivate the policyholder by setting the status to 'Active'."""
        self.status = "Active"
        return f"Policyholder {self.name} has been reactivated."

    def add_product(self, product):
        """Add a product to the policyholder's account."""
        self.products.append(product)
        return f"Product {product.name} added to {self.name}'s account."

    def get_details(self):
        """Retrieve the policyholder's details."""
        return {
            "ID": self.policyholder_id,
            "Name": self.name,
            "Email": self.email,
            "Status": self.status,
            "Products": [product.name for product in self.products],
        }
