# Generated by Django 3.2.9 on 2021-11-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerpath', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
