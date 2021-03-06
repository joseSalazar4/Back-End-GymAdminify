# Generated by Django 3.2 on 2021-05-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('effectivedate', models.DateField(db_column='EffectiveDate')),
                ('capacitypercentage', models.DecimalField(db_column='CapacityPercentage', decimal_places=4, max_digits=5)),
                ('timeperday', models.JSONField(db_column='TimePerDay')),
            ],
            options={
                'db_table': 'Config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('tuitioncost', models.DecimalField(db_column='TuitionCost', decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'Gym',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
                ('capacity', models.IntegerField(db_column='Capacity')),
            ],
            options={
                'db_table': 'Room',
                'managed': False,
            },
        ),
    ]
