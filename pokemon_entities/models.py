from django.db import models


class Pokemon(models.Model):
    title = models.CharField("название (рус.)", max_length=200)
    title_en = models.CharField("название (анг.)", max_length=200, blank=True)
    title_jp = models.CharField("название (яп.)", max_length=200, blank=True)
    image = models.ImageField("изображение", null=True)
    description = models.TextField("описание", blank=True)
    previous_evo = models.ForeignKey("self", verbose_name="прошлая эволюция", null=True, on_delete=models.SET_NULL, related_name="next_evo")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name="покемон", on_delete=models.CASCADE, related_name="entities")
    lat = models.FloatField("широта")
    lon = models.FloatField("долгота")
    appeared_at = models.DateTimeField("время появления")
    disappeared_at = models.DateTimeField("время исчезновения")
    level = models.IntegerField("уровень", blank=True)
    health = models.IntegerField("здоровье", blank=True)
    attack = models.IntegerField("атака", blank=True)
    defence = models.IntegerField("защита", blank=True)
    stamina = models.IntegerField("выносливость", blank=True)
