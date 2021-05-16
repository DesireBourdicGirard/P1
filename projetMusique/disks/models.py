from django.db import models

class Track(models.Model):
    name = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=4, decimal_places=2)
    composer = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "track"
        ordering = ['composer']

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "album"
        ordering = ['title']

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "artist"
        ordering = ['name']

    def __str__(self):
        return self.name
