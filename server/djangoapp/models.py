from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

# Car Model model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]
    
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.car_type}, {self.year})"
