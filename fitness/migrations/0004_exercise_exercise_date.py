# Generated by Django 2.0.2 on 2018-04-12 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0003_auto_20180412_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exercise_date',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
