# Generated by Django 3.0.1 on 2020-01-17 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100, unique=True)),
                ('Mobile', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('Room_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Room_Image', models.ImageField(default='', upload_to='')),
                ('Room_Type', models.CharField(choices=[('Single Room', 'Single Room'), ('Double Room', 'Double Room'), ('Double Double Room', 'Double Double Room'), ('Twin Room', 'Twin Room'), ('Interconnecting Rooms', 'Interconnecting Rooms'), ('Adjoining Rooms', 'Adjoining Rooms'), ('Duplex', 'Duplex'), ('Cabana', 'Cabana'), ('Studio Room', 'Studio Room'), ('Parlor', 'Parlor'), ('Lanai', 'Lanai'), ('Efficiency Room', 'Efficiency Room'), ('Hospitality Room', 'Hospitality Room'), ('Suite Room', 'Suite Room'), ('King Bedroom', 'King Bedroom'), ('Queen Bedroom', 'Queen Bedroom')], default='', max_length=50)),
                ('Location', models.CharField(max_length=200)),
                ('Price', models.CharField(max_length=10)),
                ('Description', models.TextField(default='', max_length=500)),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('Booking_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('No_of_Rooms_Booked', models.CharField(max_length=2)),
                ('Total_Price', models.CharField(max_length=10)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_booking_app.Customer')),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_booking_app.Room')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
