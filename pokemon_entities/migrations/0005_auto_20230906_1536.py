# Generated by Django 3.2.21 on 2023-09-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20230906_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(default=1, verbose_name='Атака'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(default=1, verbose_name='Защита'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(default=1, verbose_name='Здоровье'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Уровень'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(default=1, verbose_name='Выносливость'),
            preserve_default=False,
        ),
    ]