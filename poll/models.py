from django.db import models

# Create your models here.
class Poll(models.Model):
    message=models.CharField(max_length=500,null=True,blank=True)
    poll_one=models.CharField(max_length=500,null=True,blank=True)
    poll_two=models.CharField(max_length=500,null=True,blank=True)
    poll_third=models.CharField(max_length=500,null=True,blank=True)
    poll_one_count=models.IntegerField(default=0)
    poll_two_count=models.IntegerField(default=0)
    poll_third_count=models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)
    @property
    def total(self):
        total=self.poll_one_count+self.poll_two_count+self.poll_third_count
        return total

