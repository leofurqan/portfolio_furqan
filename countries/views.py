from django.shortcuts import render
import requests

# Create your views here.
def countries(request):
    if request.method == "POST":
        search_query = request.POST.get('search').lower()
        region = request.POST.get('region').lower()
        subregion = request.POST.get('subregion')
        
        response = requests.get("https://restcountries.com/v3.1/all")
        countries = response.json()
        
        if(len(search_query) > 0 and len(region) > 0):
            filtered_name = []
            filtered = []
            
            for country in countries:
                if country["name"]["common"].lower().find(search_query) != -1:
                    filtered_name.append(country)
            
            for country in filtered_name:
                if country["region"].lower() == region:
                    filtered.append(country)
                
            context = {'countries': filtered, 'search': search_query, 'region': region}
        elif(len(search_query) > 0):
            filtered = []
            
            for country in countries:
                if country["name"]["common"].lower().find(search_query) != -1:
                    filtered.append(country)
                    
            context = {'countries': filtered, 'search': search_query}
        elif(len(region) > 0):
            filtered = []
            
            for country in countries:
                if country["region"].lower() == region:
                    filtered.append(country)
            
            context = {'countries': filtered, 'region': region}
    else:
        response = requests.get("https://restcountries.com/v3.1/all")
        countries = response.json()
        context = {'countries': countries}
    
    
    return render(request, 'countries/index.html', context)