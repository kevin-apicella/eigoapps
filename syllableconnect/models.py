from django.db import models
from django.contrib.postgres.fields import ArrayField

#
# class WordBank(models.Model):
#     word = models.CharField(max_length=50, unique=True)
#     jp_word = models.CharField(max_length=20, null=True)
#     syllable_count = models.IntegerField()
#     level = models.IntegerField()
#     connect_app = models.BooleanField(null=False, default=False)
#
#
# class SyllableBank(models.Model):
#     word = models.ForeignKey("WordBank", to_field="word", db_column="word", on_delete=models.CASCADE)
#     syllables = ArrayField(models.CharField(max_length=19, blank=False))
#

class WordBank(models.Model):
    word = models.CharField(max_length=50, unique=True)
    jp_word = models.CharField(max_length=20, null=True)
    syllable_count = models.IntegerField()
    level = models.IntegerField()
    connect_app = models.BooleanField(null=False, default=False)

    def __str__(self):
        if self.jp_word:
            return f"{self.word} ({self.jp_word}) - Level {self.level}"
        return f"{self.word} - Level {self.level}"

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"


class SyllableBank(models.Model):
    word = models.ForeignKey("WordBank", to_field="word", db_column="word", on_delete=models.CASCADE)
    syllables = ArrayField(models.CharField(max_length=19, blank=False))

    def __str__(self):
        syllables_str = "-".join(self.syllables) if self.syllables else "No syllables"
        return f"{self.word.word}: {syllables_str}"

    class Meta:
        verbose_name = "Syllable Breakdown"
        verbose_name_plural = "Syllable Breakdowns"