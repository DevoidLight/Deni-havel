# Generated by Django 4.2.7 on 2025-06-26 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовано')], default='draft', max_length=20)),
                ('required_investment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('business_plan', models.FileField(blank=True, null=True, upload_to='business_plans')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
