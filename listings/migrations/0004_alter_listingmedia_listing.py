# Generated by Django 4.1.3 on 2022-12-01 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listings_options_listings_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingmedia',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_media', to='listings.listings'),
        ),
    ]
