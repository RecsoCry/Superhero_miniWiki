# Generated by Django 4.2.1 on 2023-07-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='movie',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Film'), (2, 'Serial')], verbose_name='movies'),
        ),
    ]
