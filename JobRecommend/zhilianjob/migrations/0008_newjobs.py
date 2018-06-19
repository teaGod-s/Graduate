# Generated by Django 2.0.2 on 2018-05-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhilianjob', '0007_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.TextField()),
                ('link', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('workplace', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('attribute', models.CharField(max_length=255)),
                ('field', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]