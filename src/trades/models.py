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
    coa_code = models.CharField(max_length=10)
    coa_name = models.CharField(max_length=50)
    ccc_code = models.CharField(max_length=10)
    ccc_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=50)
    weight = models.IntegerField()
    usd = models.IntegerField(null=True, blank=True)
    twd = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.__dict__)

