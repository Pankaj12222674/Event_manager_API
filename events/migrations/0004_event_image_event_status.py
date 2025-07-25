# Generated by Django 5.2.4 on 2025-07-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_booking_options_booking_booked_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_images/'),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
    ]
