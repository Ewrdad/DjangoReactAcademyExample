# Generated by Django 4.1.1 on 2022-09-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='astro',
            fields=[
                ('astroID', models.AutoField(primary_key=True, serialize=False)),
                ('astroName', models.CharField(max_length=200)),
                ('astroCraft', models.CharField(max_length=400)),
                ('astroDay', models.IntegerField(default=50)),
                ('astroMonth', models.IntegerField(default=50)),
                ('astroYear', models.IntegerField(default=50)),
            ],
        ),
    ]
