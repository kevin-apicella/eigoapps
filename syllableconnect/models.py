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
        try:
            if self.jp_word:
                return f"{self.word} ({self.jp_word}) - Level {self.level}"
            return f"{self.word} - Level {self.level}"
        except:
            return f"WordBank #{self.pk}"

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"


class SyllableBank(models.Model):
    word = models.ForeignKey("WordBank", to_field="word", db_column="word", on_delete=models.CASCADE)
    syllables = ArrayField(models.CharField(max_length=19, blank=False))

    def __str__(self):
        try:
            word_display = str(self.word) if self.word else "Unknown word"
            if self.syllables and len(self.syllables) > 0:
                syllables_str = "-".join(str(s) for s in self.syllables if s)
                return f"{word_display}: {syllables_str}"
            return f"{word_display}: No syllables"
        except:
            return f"SyllableBank #{self.pk}"

    class Meta:
        verbose_name = "Syllable Breakdown"
        verbose_name_plural = "Syllable Breakdowns"