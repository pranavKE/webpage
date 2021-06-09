# Generated by Django 3.2.1 on 2021-06-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Loc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('address_line1', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('Highest_Education', models.CharField(max_length=200, null=True)),
                ('min_sal', models.CharField(max_length=200)),
                ('Date_Of_Birth', models.DateTimeField()),
                ('photo', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('Experience', models.CharField(max_length=200)),
                ('categories', models.ManyToManyField(to='registrations.Skills')),
                ('pref_loc', models.ManyToManyField(to='registrations.Work_Loc')),
            ],
        ),
    ]
