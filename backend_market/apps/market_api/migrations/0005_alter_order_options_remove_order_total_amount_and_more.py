# Generated by Django 4.2.3 on 2023-08-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_api', '0004_alter_order_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['total_cost', 'order_date']},
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Total Cost'),
        ),
    ]