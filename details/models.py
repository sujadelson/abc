from django.db import models

# Create your models here.
  
class Students(models.Model):  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    address = models.CharField(max_length=200)  
    roll_number = models.IntegerField()  
    mobile = models.CharField(max_length=10)
    grade=models.CharField(max_length=10, null=True)

    def __str__(self):  
        return self.first_name + " " + self.last_name


class Marks(models.Model):
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE)
    phy_mark = models.IntegerField()
    chem_mark = models.IntegerField()
    bio_mark = models.IntegerField()


class FullDetail(models.Model):
    student_id = models.IntegerField()
    mark_id = models.IntegerField(null=True)