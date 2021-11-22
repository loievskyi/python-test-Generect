# Generated by Django 3.2.5 on 2021-11-22 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='company.name')),
                ('location', models.CharField(max_length=50, verbose_name='company.location')),
                ('revenue', models.PositiveIntegerField(verbose_name='company.revenue')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='person.full_name')),
                ('job_title', models.CharField(max_length=50, verbose_name='person.job_title')),
                ('location', models.CharField(max_length=50, verbose_name='person.location')),
                ('email', models.EmailField(max_length=50, verbose_name='person.email')),
                ('phone_number', models.CharField(max_length=50, verbose_name='person.phone_number')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persons', to='core.company')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
    ]