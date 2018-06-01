from django.shortcuts import render,render_to_response

# Create your views here.

def main_page(request):
    return render(request,"index.html",None)
