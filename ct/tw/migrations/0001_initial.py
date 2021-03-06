# Generated by Django 2.0.6 on 2018-06-08 07:12

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import tw.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_key', models.CharField(max_length=100)),
                ('consumer_secret', models.CharField(max_length=100)),
                ('access_token_key', models.CharField(max_length=100)),
                ('access_token_secret', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('text', models.CharField(default='', max_length=280)),
                ('image1', models.ImageField(blank=True, max_length=2000, null=True, upload_to=tw.models.user_directory_path)),
                ('image2', models.ImageField(blank=True, max_length=2000, null=True, upload_to=tw.models.user_directory_path)),
                ('image3', models.ImageField(blank=True, max_length=2000, null=True, upload_to=tw.models.user_directory_path)),
                ('image4', models.ImageField(blank=True, max_length=2000, null=True, upload_to=tw.models.user_directory_path)),
                ('published', models.BooleanField(default=False)),
                ('pub_datetime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_id', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tw.TwitterUser'),
        ),
        migrations.AddField(
            model_name='credential',
            name='twitter_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tw.TwitterUser'),
        ),
        migrations.AlterUniqueTogether(
            name='credential',
            unique_together={('consumer_key', 'consumer_secret', 'access_token_key', 'access_token_secret')},
        ),
    ]
