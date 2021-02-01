from django.db import models


class Invoice(models.Model):
    """ Model representing an invoice. """

    internal_reference = models.CharField(max_length=36)
    gross_amount = models.DecimalField("Total Invoice Amount",
                                       decimal_places=2,
                                       max_digits=20,
                                       blank=True, null=True, default=0)
    supplier_reference = models.CharField(max_length=36)
    date_posted = models.DateField()
