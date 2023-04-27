from django.shortcuts import render

# Create your views here.

from covid.models import  Country_Code, Country_Continent, Country, Hosp_defence, Hosp_gov, Hosp_railways, India_cases, India_tests, India_vaccine, Patients, State_cases, State_tests, State_vaccine, World_cases, World_tests, World_vaccine

def home_page(request):
    return render(request, "index.html", {})

def state_queries(request):
    countries = Country_Code.objects.filter(name="Belgium")
    context = {"cnt": countries}
    return render(request, "states.html", context)

def india_queries(request):
    countries = Country_Code.objects.filter(name="India")
    context = {"cnt": countries}
    return render(request, "india.html", context)

def world_queries(request):
    countries = Country_Code.objects.filter(code="AFG")
    context = {"cnt": countries}
    return render(request, "world.html", context)

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = Person.objects.get(name = search_id)
            #do something with user
            html = ("<H1>%s</H1>", user)
            return HttpResponse(html)
        except Person.DoesNotExist:
            return HttpResponse("no such user")  
    else:
        return render(request, 'form.html')