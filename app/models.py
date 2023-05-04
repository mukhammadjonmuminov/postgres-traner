from django.db import models

# class Status:
#     class PersonSex(models.TextChoices):
#         MALE = 'm', 'Male'
#         FEMALE = 'f', 'Female'

class Passenger(models.Model):
    # passenger_id = models.PositiveBigIntegerField()
    survived = models.IntegerField()
    p_class = models.IntegerField()
    full_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.PositiveIntegerField(blank=True, null=True)
    sib_sp = models.IntegerField()
    parch = models.IntegerField()
    ticket = models.CharField(max_length=50)
    fare = models.FloatField()
    cabin = models.CharField(max_length=20)
    embarked = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name