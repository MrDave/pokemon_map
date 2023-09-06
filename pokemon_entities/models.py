from django.db import models


class Pokemon(models.Model):
    title = models.CharField("название", max_length=200)
    image = models.ImageField("изображение", null=True)

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name="покемон", on_delete=models.CASCADE)
    lat = models.FloatField("широта")
    lon = models.FloatField("долгота")
    appeared_at = models.DateTimeField("время появления")
    disappeared_at = models.DateTimeField("время исчезновения")
    level = models.IntegerField("уровень")
    health = models.IntegerField("здоровье")
    attack = models.IntegerField("атака")
    defence = models.IntegerField("защита")
    stamina = models.IntegerField("выносливость")
