# Generated by Django 5.1 on 2024-09-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_designation_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
