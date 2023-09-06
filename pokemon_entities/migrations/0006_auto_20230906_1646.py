# Generated by Django 3.2.21 on 2023-09-06 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20230906_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(verbose_name='время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(verbose_name='атака'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(verbose_name='защита'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(verbose_name='время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(verbose_name='здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(verbose_name='уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon', verbose_name='покемон'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(verbose_name='выносливость'),
        ),
    ]