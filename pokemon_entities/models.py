from django.db import models


class Pokemon(models.Model):
    title = models.CharField("название (рус.)", max_length=200)
    title_en = models.CharField("название (анг.)", max_length=200, blank=True, default="")
    title_jp = models.CharField("название (яп.)", max_length=200, blank=True, default="")
    image = models.ImageField("изображение", null=True)
    description = models.TextField("описание", blank=True, default="")

    def __str__(self):
        return f"{self.title}"


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name="покемон", on_delete=models.CASCADE, related_name="entities")
    lat = models.FloatField("широта")
    lon = models.FloatField("долгота")
    appeared_at = models.DateTimeField("время появления")
    disappeared_at = models.DateTimeField("время исчезновения")
    level = models.IntegerField("уровень")
    health = models.IntegerField("здоровье")
    attack = models.IntegerField("атака")
    defence = models.IntegerField("защита")
    stamina = models.IntegerField("выносливость")
