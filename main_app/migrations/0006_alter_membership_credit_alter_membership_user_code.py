# Generated by Django 4.1.3 on 2022-12-05 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_membership_credit_alter_membership_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='credit',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='membership',
            name='user_code',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
