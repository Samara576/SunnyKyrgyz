# Generated by Django 4.2.3 on 2023-09-06 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('favorite', '0001_initial'),
        ('travel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlistalbum',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='housefavorite',
            name='housing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='housing', to='travel.housing'),
        ),
        migrations.AddField(
            model_name='housefavorite',
            name='wishlist_album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houseFavorite', to='favorite.wishlistalbum'),
        ),
    ]
