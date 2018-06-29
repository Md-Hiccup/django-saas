from django.db import models

# Create your models here.
class AddModule(models.Model):
    module_name = models.CharField(max_length=200, unique=True)
    order_no = models.IntegerField()
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return self.module_name
    
class EditModule(models.Model):
    module_name = models.ForeignKey(AddModule, on_delete=models.CASCADE)
    submodule_name = models.CharField(max_length= 200)
    path = models.CharField(max_length=200)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        filename = str(self.submodule_name)
        return filename