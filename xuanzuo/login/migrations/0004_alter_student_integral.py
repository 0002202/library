# Generated by Django 4.0.4 on 2022-07-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_student_integral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='integral',
            field=models.IntegerField(default=4, verbose_name='信誉积分'),
        ),
    ]