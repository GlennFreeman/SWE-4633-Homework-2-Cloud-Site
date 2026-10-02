from django.db import models


# Create your models here.
class Madlib(models.Model):
    adjective1 = models.CharField(max_length=25)
    adjective2 = models.CharField(max_length=25)
    adjective3 = models.CharField(max_length=25)
    adjective4 = models.CharField(max_length=25)

    adverb1 = models.CharField(max_length=25)
    adverb2 = models.CharField(max_length=25)
    adverb3 = models.CharField(max_length=25)
    adverb4 = models.CharField(max_length=25)

    noun1 = models.CharField(max_length=25)
    noun2 = models.CharField(max_length=25)
    noun3 = models.CharField(max_length=25)
    noun4 = models.CharField(max_length=25)
    noun5 = models.CharField(max_length=25)
    noun6 = models.CharField(max_length=25)
    noun7 = models.CharField(max_length=25)

    verb1 = models.CharField(max_length=25)
    verb2 = models.CharField(max_length=25)
    verb3 = models.CharField(max_length=25)
    verb4 = models.CharField(max_length=25)
    verb5 = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.adjective1}, {self.adverb1}, {self.noun1}, {self.verb1}"
