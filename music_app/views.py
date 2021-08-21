from django.shortcuts import render,redirect
from .models import albumCategory,album,song,extendedUser
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required#beat-master
from django.contrib.auth.models import User,auth
from django.contrib import messages

def category(request):
    all_category_objects = albumCategory.objects.all()
    return render(request,'all_categories.html',{'all_category_objects':all_category_objects})

def category_album(request,id):
    requested_category = albumCategory.objects.get(id=id)
    filtered_albums= album.objects.filter(category= requested_category)
    return render(request,'allAlbum.html',{'all_album':filtered_albums})

def allsong(request,id):
    filtered_songs = None
    requested_album = album.objects.get(id=id)
    
    #all_songs=requested_album.song_album.all()
    #filtered_songs = all_songs.filter(is_visisble=True)

    if 'addSong' in request.POST :
        print('exec')
        print(request.POST)
        print(request.FILES)
        song_name=  request.POST['song_name']
        song_file = request.FILES['song_file']
        dedicated_by=  request.POST['dedicated_by']
        dedicated_for=  request.POST['dedicated_for']
        new_song = song(song_album=requested_album,song_name = song_name, song_file = song_file,dedicated_by= dedicated_by,dedicated_for=dedicated_for)
        new_song.save()
    filtered_song= song.objects.filter(song_album= requested_album,is_visible = True)
    if 'search' in request.POST:
        name_song = request.POST['name_song']
        filtered_song = song.objects.filter(song_name__contains = name_song,song_album=requested_album )
    return render(request,'song.html',{'Allsong':filtered_song,'album':requested_album})
def addCategory(request):#only admin
    if request.user.is_staff:
        if 'add' in request.POST and request.FILES:
            name=  request.POST['category_name']
            img = request.FILES['image']
            new_category = albumCategory(category_name = name, category_image = img)
            new_category.save()
        return render(request,'categoryAdd.html')   
    else:
        raise Http404("You are not an admin")
def addAlbum(request):#only admin
    if request.user.is_staff:
        all_category = albumCategory.objects.all()
        if 'add' in request.POST and request.FILES:
            category_id = request.POST['cat_id_value']
            category_object = albumCategory.objects.get(id=category_id)
            name=  request.POST['album_name']
            picture = request.FILES['image']
            genre = request.POST['genre']
            age= request.POST['age']
            new_album=album(category= category_object,name=name,picture=picture,genre=genre,age=age)
            new_album.save()
            message = "Successfully added"
            return render(request,'albumadd.html',{'all_category':all_category,'message':message})
        return render(request,'albumadd.html',{'all_category':all_category})
    else:
        raise Http404("You are not admin")  


@login_required
def addsong(request):
    all_album= album.objects.all()
    if 'add' in request.POST and request.FILES:
            album_id = request.POST['album_id']
            album_object = album.objects.get(id=album_id)
            song_name=  request.POST['song_name']
            song_file = request.FILES['song_file']
            dedicated_by=  request.POST['dedicated_by']
            dedicated_for=  request.POST['dedicated_for']
            new_song = song(song_album=album_object,song_name = song_name, song_file = song_file,dedicated_by= dedicated_by,dedicated_for=dedicated_for)
            new_song.save()
            #message = "Successfully added"
            return redirect('/')
    return redirect('/') 

def login(request):#copied frm beat-connect master
    if 'login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user != None:
            auth.login(request,user)
            messages.add_message(request, messages.INFO, 'Logged In')
            return redirect('/home/')
        else:
            messages.add_message(request, messages.INFO, 'Invalid Credential')
            return redirect('/home/')
            #return render(request, 'login.html', {'error_message': "Invalid Credentials"})
    #return render(request, 'login.html')
def register(request):
    if 'register' in request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                return render(request,'home.html',{'error_message':"Username already taken"})
            elif User.objects.filter(email = email).exists():
                return render(request,'home.html',{'error_message':"Email already taken"})
            else:
                user= User.objects.create_user(username = username, password = password1, email = email, first_name= first_name, last_name = last_name)
                user.save()
                extended_user = extendedUser(belongs_to= user)
                extended_user.save()
                return redirect('/')
        else:
            return render(request,'home.html',{'error_message':"Password does not match"})
    return render(request,'home.html')
def favourite(request,album_id):
    try:
        requested_album = album.objects.get(id=album_id)
        filtered_song= song.objects.filter(song_album= requested_album)
    except:
        raise Http404("Album Does not exist")
    if 'favourite' in request.POST:
        try:
            song_id = request.POST['song']
            song_object = song.objects.get(id= song_id)
            #print(song_object.song_name)
            extend_user_object = extendedUser.objects.get(belongs_to= request.user)
            extend_user_object.songs_list.add(song_object)
            for x in extend_user_object.songs_list.all():
                print(x.song_name)
        except:
            pass
    return render(request,'song.html',{'Allsong':filtered_song,'album':requested_album})
# Create your views here
@login_required
def favsong(request):
    extend_user_object = extendedUser.objects.get(belongs_to= request.user)
    return render(request,'favsong.html',{'extend_user_object':extend_user_object})
     
@login_required     
def songrequest(request):
    if request.user.is_staff:
        rsong=song.objects.filter(is_visible= False)
        return render(request,'requestsong.html',{'allsong':rsong})   
    else:
        raise Http404("You are not an admin")

def accept(request,song_id):
    song_object = song.objects.get(id =song_id )
    song_object.is_visible=True
    song_object.save()
    rsong=song.objects.filter(is_visible= False)
    return render(request,'requestsong.html',{'allsong':rsong})

def reject(request,song_id):
    songobj=song.objects.get(id=song_id)
    songobj.delete()
    rsong=song.objects.filter(is_visible= False)
    return render(request,'requestsong.html',{'allsong':rsong})  

def home(request):
    return render(request,'home.html')

def home1(request):
    return render(request,'home1.html')          

        