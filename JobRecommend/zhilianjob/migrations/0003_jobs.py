# Generated by Django 2.0.2 on 2018-05-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhilianjob', '0002_compn_edusaln_expsaln_posin_workedun_workn_worksaln'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('workplace', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
