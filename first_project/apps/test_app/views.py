from django.shortcuts import render, HttpResponse

def index(request):
	context = {
		"name": "Noell",
		"color": "turquoise",
		"pets": ["Bruce", "Fits", "Gergie"]
	}
	return render(request, "test_app/index.html", context)

# def index(request):
#     return HttpResponse("placeholder to later display a list of all blogs")

# def new(request):
# 	return HttpResponse("placeholder to display a new form to create a new blog")

# def create(request):
# 	return HttpResponse()

# def show(request,number):
# 	return HttpResponse("placeholder to display blog number: 15")

# def edit(request,number,edit):
# 	return HttpResponse("placeholder to edit blog number: 15")

# def destroy(request,number,delete):
# 	return HttpResponse("placeholder to delete blog number: 15")