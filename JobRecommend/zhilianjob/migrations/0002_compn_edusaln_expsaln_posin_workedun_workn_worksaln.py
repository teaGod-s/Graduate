# Generated by Django 2.0.2 on 2018-04-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhilianjob', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EduSalN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpSalN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PosiN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkEduN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(max_length=255)),
                ('education', models.CharField(max_length=255)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(max_length=255)),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkSalN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('num', models.IntegerField()),
            ],
        ),
    ]
