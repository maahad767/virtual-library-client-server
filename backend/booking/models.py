from django.db import models

class BookingPlan(models.Model):
    book = models.ForeignKey("product.Book", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    recurring = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}: {self.price}"
    

class Booking(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)
    plan = models.ForeignKey("booking.BookingPlan", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} - {self.plan}"
    