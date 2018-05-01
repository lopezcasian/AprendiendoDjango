# Generated by Django 2.0.1 on 2018-05-01 03:58

from django.db import migrations, models
import django.db.models.deletion

def create_continent(apps, schema_editor):
    Continent = apps.get_model("contients", "Continent")
    Contient.objects.create(name="asia", color="red", translate="asia")
    Contient.objects.create(name="américa", color="blue", translate="america")
    Contient.objects.create(name="antártida", color="green", translate="antarctica")
    Contient.objects.create(name="europa", color="brown", translate="europe")
    Contient.objects.create(name="áfrica", color="yellow", translate="africa")
    Contient.objects.create(name="oceanía", color="pink", translate="oceania")

class Migration(migrations.Migration):

    dependencies = [
        ('continents', '0001_initial'),
        ('countries', '0002_auto_20180423_2349'),
    ]

    operations = [
    migrations.RunPython(create_continent),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='continents.Continent'),
            preserve_default=False,
        ),
    ]
