from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader
from galleries.data.models import Gallery1990

def index(request):
   if request.method == 'POST':
        form = SearchForm(request.POST)
   else:
        form = SearchForm()
   return render_to_response('index.html', {'form': form})
 
def search_name(request):
    search_results = Gallery1990.objects.filter(name__icontains=request.POST['name']).order_by('name')
    return render_to_response('search_name.html',{'search_results':search_results, 'name':request.POST['name']})

def search_zipcode(request):
    search_results = Gallery1990.objects.filter(address_zip__icontains=request.POST['zipcode']).order_by('name')
    return render_to_response('search_zipcode.html',{'search_results':search_results, 'zipcode':request.POST['zipcode']})

def search_outcome(request):
    search_results = Gallery1990.objects.filter(outcome__icontains=request.POST['outcome']).order_by('name')
    return render_to_response('search_outcome.html',{'search_results':search_results, 'outcome':request.POST['outcome']})

def search_founded(request):
    founded_1=request.POST['founded_1']
    founded_2=request.POST['founded_2']
    search_results = Gallery1990.objects.filter(start_year__range=(founded_1, founded_2)).order_by('name')
    return render_to_response('gallery/search_founded.html',{'search_results':search_results, 'founded_1':request.POST['founded_1'],  'founded_2':request.POST['founded_2']})
		
def search_closed(request):
    closed_1=request.POST['closed_1']
    closed_2=request.POST['closed_2']
    search_results = Gallery1990.objects.filter(end_year__range=(closed_1, closed_2)).order_by('name')
    return render_to_response('gallery/search_closed.html',{'search_results':search_results, 'closed_1':request.POST['closed_1'],  'closed_2':request.POST['closed_2']})

def search_neighborhood(request):
    search_results = Gallery1990.objects.filter(neighborhood__icontains=request.POST['neighborhood']).order_by('name')
    return render_to_response('gallery/search_neighborhood.html',{'search_results':search_results, 'neighborhood':request.POST['neighborhood']})

def search_media(request):
    media_list = request.POST.getlist('media')
    search_results = Gallery1990.objects.filter(three_d_construction__in= media_list)|Galleries1990.objects.filter(accessories__in= media_list) |Galleries1990.objects.filter(all__in= media_list) |Galleries1990.objects.filter(assemblage__in= media_list)|Galleries1990.objects.filter(basketry__in= media_list)|Galleries1990.objects.filter(batik__in= media_list)|Galleries1990.objects.filter(books__in=media_list)|Galleries1990.objects.filter(cards__in=media_list)|Galleries1990.objects.filter(ceramics__in=media_list)|Galleries1990.objects.filter(clay__in= media_list)|Galleries1990.objects.filter(collage__in= media_list)|Galleries1990.objects.filter(drawing__in= media_list)|Galleries1990.objects.filter(enamel__in= media_list)|Galleries1990.objects.filter(etching__in= media_list)|Galleries1990.objects.filter(fiber__in= media_list)|Galleries1990.objects.filter(folk_art__in= media_list)|Galleries1990.objects.filter(fresco__in= media_list)|Galleries1990.objects.filter(furniture__in= media_list)|Galleries1990.objects.filter(glass__in= media_list)|Galleries1990.objects.filter(graphics__in= media_list)|Galleries1990.objects.filter(handcrafts__in= media_list)|Galleries1990.objects.filter(jewelry__in= media_list)|Galleries1990.objects.filter(kaleidoscopes__in= media_list)|Galleries1990.objects.filter(leather__in= media_list)|Galleries1990.objects.filter(lithography__in= media_list)|Galleries1990.objects.filter(metal__in= media_list)|Galleries1990.objects.filter(mixed_media__in= media_list)|Galleries1990.objects.filter(mobiles__in= media_list)|Galleries1990.objects.filter(monoprints__in= media_list)|Galleries1990.objects.filter(neon__in= media_list)|Galleries1990.objects.filter(painting__in= media_list)|Galleries1990.objects.filter(paper__in= media_list)|Galleries1990.objects.filter(pastels__in= media_list)|Galleries1990.objects.filter(photography__in= media_list)|Galleries1990.objects.filter(porcelain__in= media_list)|Galleries1990.objects.filter(pottery__in= media_list)|Galleries1990.objects.filter(prints__in= media_list)|Galleries1990.objects.filter(sculpture__in= media_list)|Galleries1990.objects.filter(serigraphy__in= media_list)|Galleries1990.objects.filter(silkscreen__in= media_list)|Galleries1990.objects.filter(tapestry__in= media_list)|Galleries1990.objects.filter(wearables__in= media_list)|Galleries1990.objects.filter(weaving__in= media_list)|Galleries1990.objects.filter(wood__in= media_list)
    return render_to_response('gallery/search_media.html',{'search_results':search_results, 'media_list': media_list, 'media':request.POST['media']})

def detail(request, id):
    get_object_or_404(Gallery1990.objects.all(), pk=id)
    return render_to_response('gallery/detail.html', {'galleries1990': p})
 
