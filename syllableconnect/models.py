from django.db import models
from django.contrib.postgres.fields import ArrayField


class WordBank(models.Model):
    word = models.CharField(max_length=50, unique=True)
    jp_word = models.CharField(max_length=20, null=True)
    syllable_count = models.IntegerField()
    level = models.IntegerField()
    connect_app = models.BooleanField(null=False, default=False)
    image_filename = models.CharField(null=False, default="")
    audio_filename = models.CharField(null=False, default="")

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"


class SyllableBank(models.Model):
    word = models.ForeignKey("WordBank", to_field="word", db_column="word", on_delete=models.CASCADE)
    syllables = ArrayField(models.CharField(max_length=19, blank=False))
    audio = ArrayField(models.CharField(), default=[])
    audio_json = models.JSONField(default=dict, blank=True)


