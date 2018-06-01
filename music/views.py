from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album


# Homepage
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    
    def get_queryset(self):
        return Album.objects.all()
# Detail Page     
class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

# Giving the user the ability to create new albums
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']






























# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song


# # Create your views here.
# def index(request):
#     all_albums = Album.objects.all() #Connect to database and get albums
#     return render(request, 'music/index.html',{'all_albums': all_albums})
    
    
#     # html =''     
#     # for album in all_albums:
#     #         url = '/music/' + str(album.id) +'/'
#     #         html += '<a href="'  + url + '">'  + album.album_title + '</a><br>'
#     # return HttpResponse(html)
    
    
# def detail(request, album_id):
#     album = get_object_or_404(Album,pk=album_id)
#     return render(request, 'music/detail.html',{'album': album})
    
    
    
    
    
    
    
    
    
# def favorite(request, album_id):
#     album = get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html',{
#             'album': album,
#             'error_message': "You did not select valid song",
#         })
#     else:
#         if selected_song.is_favorite:
#             selected_song.is_favorite = False
#             selected_song.save()
#         else:
#             selected_song.is_favorite = True
#             selected_song.save()
#         return render(request, 'music/detail.html',{'album': album})

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    