# Generated by Django 2.0.2 on 2018-04-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sales', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('detail', models.CharField(max_length=255)),
            ],
        ),
    ]
