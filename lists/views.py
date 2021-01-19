from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    
    if request.method == 'POST':
        return HttpResponse('<html><title>a list item</title></html>')
    #     print('request.POST[=>', request)
    #     #return render(request,  'home.html', {'new_item_text': request.POST['item_text']})
    #     return render(request,  'home.html')
    return render(request,  'home.html')
