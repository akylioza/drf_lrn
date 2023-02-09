from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies_quantity(self):
        return self.movie_director.count()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name="movie_director")

    def __str__(self):
        return self.title

    @property
    def rate(self):
        star = self.movie_review.count()
        if star == 0:
            return 0
        total = 0
        for i in self.movie_review.all():
            total += i.stars
        return total/star

CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_review")
    stars = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return self.text




