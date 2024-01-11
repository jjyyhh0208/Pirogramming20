from django.db import models

# Create your models here.
class Reviews(models.Model):
    title = models.CharField(max_length=200)
    createdDate = models.DateTimeField(blank = True, null = True)

    class Genre(models.Choices):
        science_fiction = 'SF'
        romance = 'Romance'
        action = 'Action'
        horror = 'Horror'
        crime = 'Crime'
        comedy = 'Comedy'
        
    genre = models.CharField(max_length=200, choices=Genre.choices)

    class Rank(models.IntegerChoices):
        BAD = 1, '1'
        NOTBAD = 2, '2'
        SOSO = 3, '3'
        GOOD = 4, '4'
        PERFECT = 5, '5'
    rank = models.IntegerField(choices=Rank.choices)

    running_time = models.TimeField()
    content = models.TextField()
    director = models.CharField(max_length=200)
    actors = models.CharField(max_length=200)