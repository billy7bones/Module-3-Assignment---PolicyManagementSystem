class Product:
    def __init__(self, product_id, name, description, price, status="Available"):
        """
        Initialize a Product object.

        Args:
            product_id (int): Unique ID of the product.
            name (str): Name of the product.
            description (str): Description of the product.
            price (float): Price of the product.
            status (str): Current status of the product. Default is 'Available'.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.status = status

    def create_product(self):
        """Create the product by setting the status to 'Available'."""
        self.status = "Available"
        return f"Product {self.name} created successfully."

    def update_product(self, name=None, description=None, price=None):
        """Update the product details."""
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        return f"Product {self.product_id} updated successfully."

    def suspend_product(self):
        """Suspend the product by setting the status to 'Suspended'."""
        self.status = "Suspended"
        return f"Product {self.name} has been suspended."
