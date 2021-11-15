from django.db import models

class Bond(models.Model):

    username = models.CharField(max_length=30) 
    isin = models.CharField(max_length=30) 
    size = models.CharField(max_length=30)
    currency = models.CharField(max_length=30) 
    maturity = models.CharField(max_length=30)
    lei = models.CharField(max_length=30) 
    legal_name = models.CharField(max_length=30) 

    def get_json(self):
      return {
        "isin": self.isin,
        "size":  self.size,
        "currency": self.currency, 
        "maturity": self.maturity,
        "lei": self.lei,
        "legal_name": self.legal_name
      }
