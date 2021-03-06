# Generated by Django 2.1.7 on 2020-03-12 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrocerListContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GroceryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(default='test@test.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('securityQuestion', models.CharField(max_length=200)),
                ('securityQuesAnswer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UsersAndGrocery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canEdit', models.BooleanField(default=False)),
                ('canView', models.BooleanField(default=False)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isCreator', models.BooleanField(default=False)),
                ('groceryListId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceryList_lite.GroceryList')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceryList_lite.User')),
            ],
        ),
        migrations.AddField(
            model_name='grocerlistcontent',
            name='groceryListId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceryList_lite.GroceryList'),
        ),
    ]
