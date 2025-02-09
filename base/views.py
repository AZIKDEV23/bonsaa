from django.shortcuts import render

def home(request):
    return render(request=request, template_name='pages/home.html')

def error(request):
    return render(request=request, template_name='pages/404.html')

def about(request):
    return render(request=request, template_name='pages/about.html')

def blog_details(request):
    return render(request=request, template_name='pages/blog-details.html')

def blog(request):
    return render(request=request, template_name='pages/blog.html')

def contact(request):
    return render(request=request, template_name='pages/contact.html')

def faq(request):
    return render(request=request, template_name='pages/faq.html')

# def index3(request):
#     return render(request=request, template_name='pages/index-three.html')

# def index2(request):
#     return render(request=request, template_name='pages/index-two.html')

def members(request):
    return render(request=request, template_name='pages/members.html')

def portfolio(request):
    return render(request=request, template_name='pages/portfolio.html')

def pricing(request):
    return render(request=request, template_name='pages/pricing.html')

def privacy(request):
    return render(request=request, template_name='pages/privacy-police.html')

def recover(request):
    return render(request=request, template_name='pages/recover-password.html')

def service_details(request):
    return render(request=request, template_name='pages/service-details.html')

def service(request):
    return render(request=request, template_name='pages/services.html')

def sign_in(request):
    return render(request=request, template_name='pages/sign-in.html')

def sign_up(request):
    return render(request=request, template_name='pages/sign-up.html')

def terms(request):
    return render(request=request, template_name='pages/terms.html')

def testimonial(request):
    return render(request=request, template_name='pages/testimonial.html')