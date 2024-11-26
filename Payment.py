class Payment:
    def __init__(self, policyholder, product):
        """
        Initialize a Payment object.

        Args:
            policyholder (Policyholder): Policyholder making the payment.
            product (Product): Product being paid for.
        """
        self.policyholder = policyholder
        self.product = product
        self.status = "Pending"
        self.penalty = 0

    def process_payment(self):
        """Mark the payment as processed and set the status to 'Paid'."""
        self.status = "Paid"
        return f"Payment for {self.product.name} by {self.policyholder.name} processed successfully."

    def send_reminder(self):
        """Send a reminder for the pending payment."""
        return f"Reminder sent to {self.policyholder.name} for {self.product.name} payment."

    def apply_penalty(self, amount):
        """Apply a penalty to the payment."""
        self.penalty += amount
        return f"Penalty of {amount} applied to {self.policyholder.name}."
