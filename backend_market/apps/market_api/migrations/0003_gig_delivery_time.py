# Generated by Django 4.2.3 on 2023-08-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0002_remove_gig_likes_remove_review_buyer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='delivery_time',
            field=models.IntegerField(default=1),
        ),
    ]