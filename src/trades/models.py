from django.db import models

# Create your models here.

IE_CHOICES = (
    (1, 'Export'),
    (2, 'Import'),
)


class Trade(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    ie_code = models.IntegerField(choices=IE_CHOICES)
    coa_code = models.IntegerField()
    coa_name = models.CharField(max_length=50)
    ccc_code = models.IntegerField()
    ccc_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=50)
    weight = models.IntegerField()
    usd = models.IntegerField()
    twd = models.IntegerField()

    def __str__(self):
        return str(self.__dict__)

