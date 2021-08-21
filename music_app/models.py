from django.db import models
from django.contrib.auth.models import User
class albumCategory(models.Model):
    category_name = models.CharField(max_length = 200,null=True,blank=False)
    category_image= models.FileField(null=True)
    def __str__(self):
        return self.category_name
class album(models.Model):
    category = models.ForeignKey(albumCategory,related_name="category_album",on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=True,blank=False)  
    picture = models.FileField(null=True)
    genre = models.CharField(max_length=150,null=True,blank=False)
    album_added = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    def __str__(self):
        return self.name + "-" + self.category.category_name 
class song(models.Model):
    song_album = models.ForeignKey(album,related_name="song_album",on_delete=models.PROTECT)
    is_visible = models.BooleanField(default=False)#if is_visible == False then show as requested song. If admin accepts is_visible= True, and not a part of requested from last condition.If deleted then no question of song object
    song_name = models.CharField(max_length=150,null=True,blank=False) 
    song_file = models.FileField(null=True)
    dedicated_by = models.CharField(max_length=40,null=True,blank=False)
    dedicated_for = models.CharField(max_length=40,null=True,blank=False)
    date_added= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.song_name + "-" + self.song_album.name
class extendedUser(models.Model):
    belongs_to = models.OneToOneField(User,related_name="extended_reverse",on_delete=models.CASCADE)
    songs_list = models.ManyToManyField(song,related_name="fav_song")
    def __str__(self):
        return  self.belongs_to.username +"'s favorite song"

# Create your models here.
### if song_object in request.user.extendUser.songs_list.all:
####FAVORITE