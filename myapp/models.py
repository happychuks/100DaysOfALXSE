from django.db import models

# Menu model
class Menu(models.Model):
    item_name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
        