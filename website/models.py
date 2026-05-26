from django.db import models


class EmissionRecord(models.Model):

    company_name = models.CharField(max_length=100)

    amount = models.FloatField()

    facility_name = models.CharField(max_length=100)

    status = models.CharField(max_length=20)

    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('Utility', 'Utility'),
        ('Travel', 'Travel'),
    ]

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        default='SAP'
    )

    # ADD THIS
    is_suspicious = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name