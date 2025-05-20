from django.db import models

# Create your models here.
class Roc_Trends(models.Model):
    symbol = models.CharField(max_length=20)
    sector = models.CharField(max_length=100)
    latest_close = models.FloatField(null=True)

    roc_3days = models.FloatField(null=True)
    trend_3days = models.CharField(max_length=20, null=True)

    roc_7days = models.FloatField(null=True)
    trend_7days = models.CharField(max_length=20, null=True)

    roc_12days = models.FloatField(null=True)
    trend_12days = models.CharField(max_length=20, null=True)

    roc_20days = models.FloatField(null=True)
    trend_20days = models.CharField(max_length=20, null=True)

    roc_45days = models.FloatField(null=True)
    trend_45days = models.CharField(max_length=20, null=True)

    roc_60days = models.FloatField(null=True)
    trend_60days = models.CharField(max_length=20, null=True)

    roc_90days = models.FloatField(null=True)
    trend_90days = models.CharField(max_length=20, null=True)

    roc_120days = models.FloatField(null=True)
    trend_120days = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.symbol