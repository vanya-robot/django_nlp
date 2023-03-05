from django.db import models


class PredResults(models.Model):

    review_text = models.CharField(max_length=5000)
    classification = models.CharField(max_length=30)
    bi_class = models.CharField(max_length=30)

    def __str__(self):
        return self.classification
