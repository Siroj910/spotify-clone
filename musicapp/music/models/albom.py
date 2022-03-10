from django.db import models

class Albom(models.Model):
	artist = models.ForeignKey('music.Artist', on_delete=models.CASCADE)
	name = models.CharField(max_length=150, blank=False, null=False)
	cover = models.URLField(blank=True)
