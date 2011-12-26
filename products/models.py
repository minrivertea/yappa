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
    name = models.CharField(max_length=200, 
        help_text="The full name of the game")
    slug = models.SlugField(max_length=80,
        help_text="No special characters, spaces etc. only letters, numbers and '-' dashes")
    order = models.PositiveIntegerField(blank=True, null=True, 
        help_text="The order of the category ont the listing page. 1 is top, 10 is bottom. Optional")
    image = models.ImageField(upload_to='images/categories', blank=True, null=True, 
        help_text="An image to represent the category. Should be 200px wide.")
    is_active = models.BooleanField(default=True, 
        help_text="If unticked, it won't appear on the site.")
    
    def __unicode__(self):
        return self.name
    
    def get_games(self):
        games = Product.objects.filter(category=self)
        return games

class Product(models.Model):
    name = models.CharField(max_length=200, 
        help_text="The full name of this game")
    slug = models.SlugField(max_length=80, 
        help_text="No special characters, spaces etc. only letters, numbers and '-' dashes")
    category = models.ForeignKey(Category, 
        help_text="Which category does it belong to?")
    direct_link = models.URLField(blank=True, null=True, 
        help_text="If the game is directly playable online, link to it. Optional.")
    short_description = tinymce_models.HTMLField(help_text="Very short descr. only 70 characters.")
    description = tinymce_models.HTMLField(help_text="Slightly longer description, maybe 200 characters.")
    body = tinymce_models.HTMLField(help_text="Full description, unlimited.")
    image = models.ImageField(upload_to='images/products', 
        help_text="The small 'thumbnail' image for the game. ")
    big_promo_image = models.ImageField(upload_to="images/products", blank=True, null=True,
        help_text="A large image which appears on the game description page. 400px wide.")
    is_active = models.BooleanField(default=True, 
        help_text="If unticked, the game won't appear on the site.")
    
    def __unicode__(self):
        return self.name
        
    