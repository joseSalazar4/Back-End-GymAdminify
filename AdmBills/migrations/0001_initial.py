from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('paid', models.IntegerField(db_column='Paid')),
                ('paymentday', models.DateField(blank=True, db_column='PaymentDay', null=True)),
                ('issuedate', models.DateField(db_column='IssueDate')),
                ('cost', models.DecimalField(db_column='Cost', decimal_places=2, max_digits=15)),
            ],
            options={
                'db_table': 'Bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PayMethod',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=45)),
            ],
            options={
                'db_table': 'PayMethod',
                'managed': False,
            },
        ),
    ]
