from django.db import models

class Song(models.Model):
	album = models.ForeignKey('music.Albom', on_delete=models.CASCADE,  null=True, blank=True)
	title = models.CharField(max_length=150, blank=False, null=False)
	cover = models.URLField(blank=True)
	source = models.URLField(blank=False, null=False)

	listened = models.PositiveIntegerField(default=0)