from django.db import models
class Department(models.Model):
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Doctor(models.Model):
    dname=models.CharField(max_length=20)
    spe=models.CharField(max_length=20)
    dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='upload')
    def __str__(self):
        return self.dname
class Booking(models.Model):
    p_name=models.CharField(max_length=20)
    p_phone=models.CharField(max_length=20)
    doc_name=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    bookeddate=models.DateField(auto_now_add=True)
    booking=models.DateField()
    def __str__(self):
        return self.p_name

