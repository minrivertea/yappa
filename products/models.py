from django.db import models

from tinymce import models as tinymce_models




class ShopSettings(models.Model):
    homepage_promo_text = tinymce_models.HTMLField(
        help_text="The text in the top feature area (not including the button)")
    homepage_intro_text = tinymce_models.HTMLField(blank=True, null=True,
        help_text="The text that appears under the feature area, above the games list")
    homepage_feature_image = models.ImageField(upload_to='images/homepage',
        help_text="The main feature image on the homepage")
    games_page_intro_text = tinymce_models.HTMLField(blank=True, null=True,
        help_text="The intro text on the games listing page")
    logo = models.ImageField(upload_to='images/homepage',
        help_text="Make sure it's a clear logo, JPG or GIF only")
    google_code = models.TextField(blank=True, null=True,
        help_text="The Google Analytics tracking code (including script tags")
    homepage_featured_games = models.ManyToManyField('Product', blank=True, null=True,
        help_text="Choose 3 games that will appear on the homepage")
    is_active = models.BooleanField(default=True,
        help_text="Is this the active settings model? Be careful with this...")
    

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=80)
    order = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/categories', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
    
    def get_games(self):
        games = Product.objects.filter(category=self)
        return games

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=80)
    category = models.ForeignKey(Category)
    short_description = tinymce_models.HTMLField()
    description = tinymce_models.HTMLField()
    body = tinymce_models.HTMLField()
    image = models.ImageField(upload_to='images/products')
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name
        
    