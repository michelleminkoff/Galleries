# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Galleries1990	(models.Model):
    name = models.TextField(blank=True) # Field name made lowercase. This field type is a guess.
    address_number = models.TextField(blank=True) # This field type is a guess.
    address_direction = models.TextField(blank=True) # This field type is a guess.
    address_street = models.TextField(blank=True) # This field type is a guess.
    address_type = models.TextField(blank=True) # This field type is a guess.
    address_zip = models.TextField(blank=True) # This field type is a guess.
    start_year = models.TextField(blank=True) # This field type is a guess.
    end_year = models.TextField(blank=True) # This field type is a guess.
    count_90 = models.TextField(blank=True) # This field type is a guess.
    count_95 = models.TextField(blank=True) # This field type is a guess.
    count_00 = models.TextField(blank=True) # This field type is a guess.
    count_05 = models.TextField(blank=True) # This field type is a guess.
    count_10 = models.TextField(blank=True) # This field type is a guess.
    director = models.TextField(blank=True) # This field type is a guess.
    painting = models.TextField(blank=True) # This field type is a guess.
    outcome = models.TextField(blank=True) # This field type is a guess.
    sculpture = models.TextField(blank=True) # This field type is a guess.
    notes = models.TextField(blank=True) # This field type is a guess.
    three_d_construction = models.TextField(blank=True) # This field type is a guess.
    pastels = models.TextField(blank=True) # This field type is a guess.
    furniture = models.TextField(blank=True) # This field type is a guess.
    ceramics = models.TextField(blank=True) # This field type is a guess.
    glass = models.TextField(blank=True) # This field type is a guess.
    metal = models.TextField(blank=True) # This field type is a guess.
    prints = models.TextField(blank=True) # This field type is a guess.
    photography = models.TextField(blank=True) # This field type is a guess.
    drawing = models.TextField(blank=True) # This field type is a guess.
    jewelry = models.TextField(blank=True) # This field type is a guess.
    wearables = models.TextField(blank=True) # This field type is a guess.
    accessories = models.TextField(blank=True) # This field type is a guess.
    cards = models.TextField(blank=True) # This field type is a guess.
    lithography = models.TextField(blank=True) # This field type is a guess.
    etching = models.TextField(blank=True) # This field type is a guess.
    serigraphy = models.TextField(blank=True) # This field type is a guess.
    monoprints = models.TextField(blank=True) # This field type is a guess.
    folk_art = models.TextField(db_column=u'folk art', blank=True) # Field renamed to remove spaces. Field name made lowercase. This field type is a guess.
    graphics = models.TextField(blank=True) # This field type is a guess.
    fiber = models.TextField(blank=True) # This field type is a guess.
    handcrafts = models.TextField(blank=True) # This field type is a guess.
    mixed_media = models.TextField(blank=True) # This field type is a guess.
    all = models.TextField(blank=True) # This field type is a guess.
    tapestry = models.TextField(blank=True) # This field type is a guess.
    clay_ = models.TextField(db_column=u'clay ', blank=True) # Field renamed to remove spaces. Field name made lowercase. This field type is a guess.
    wood = models.TextField(blank=True) # This field type is a guess.
    kaleidoscopes = models.TextField(blank=True) # This field type is a guess.
    silkscreen = models.TextField(blank=True) # This field type is a guess.
    mobiles = models.TextField(blank=True) # This field type is a guess.
    assemblage = models.TextField(blank=True) # This field type is a guess.
    neon = models.TextField(blank=True) # This field type is a guess.
    collage = models.TextField(blank=True) # This field type is a guess.
    enamel = models.TextField(blank=True) # This field type is a guess.
    porcelain = models.TextField(blank=True) # This field type is a guess.
    books = models.TextField(blank=True) # This field type is a guess.
    fresco = models.TextField(blank=True) # This field type is a guess.
    pottery = models.TextField(blank=True) # This field type is a guess.
    weaving = models.TextField(blank=True) # This field type is a guess.
    basketry = models.TextField(blank=True) # This field type is a guess.
    leather = models.TextField(blank=True) # This field type is a guess.
    batik = models.TextField(blank=True) # This field type is a guess.
    paper = models.TextField(blank=True) # This field type is a guess.
    move1 = models.TextField(blank=True) # This field type is a guess.
    move2 = models.TextField(blank=True) # This field type is a guess.
    move3 = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'galleries1990'

