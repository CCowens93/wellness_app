# Generated by Django 2.2.7 on 2019-11-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellness_app', '0005_dietarygoal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietarygoal',
            name='elimination',
            field=models.CharField(choices=[('dairy', 'dairy'), ('soy', 'soy'), ('red meat', 'red meat'), ('pork', 'pork'), ('processed sugar', 'processed sugar'), ('alcohol', 'alcohol'), ('gluten', 'gluten')], default='n/a', max_length=500),
        ),
    ]
