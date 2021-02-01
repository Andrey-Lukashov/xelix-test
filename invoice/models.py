from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    """ Model representing an invoice. """

    internal_reference = models.CharField(max_length=36)
    gross_amount = models.DecimalField("Total Invoice Amount",
                                       decimal_places=2,
                                       max_digits=20,
                                       blank=True, null=True, default=0)
    supplier_reference = models.CharField(max_length=36)
    date_posted = models.DateField()
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
