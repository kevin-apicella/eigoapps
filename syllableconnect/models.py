from django.db import models
from django.contrib.postgres.fields import ArrayField


class WordBank(models.Model):
    word = models.CharField(max_length=50, unique=True)
    syllable_count = models.IntegerField()
    level = models.IntegerField()
    connect_app = models.BooleanField(null=False, default=False)


class SyllableBank(models.Model):
    word = models.ForeignKey("WordBank", to_field="word", db_column="word", on_delete=models.CASCADE)
    syllables = ArrayField(models.CharField(max_length=19, blank=False))
