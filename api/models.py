from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class movie(models.Model):
	name = models.CharField(max_length=100)
	_99popularity = models.FloatField()
	director = models.CharField(max_length=100)
	imdb_score = models.DecimalField(max_digits=4, decimal_places=2)
	genre = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
    )

	def __str__(self):
		return self.name