from django.db import models

# Footwear Model
class Footwear(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='footwear_images/')

    def __str__(self):
        return self.name


# Order Model
class Order(models.Model):
    footwear = models.ForeignKey(Footwear, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} - {self.footwear.name}'