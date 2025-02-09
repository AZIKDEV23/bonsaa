from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('error/', error, name='error'),
    path('about/', about, name='about'),
    path('blog_details/', blog_details, name='blog_details'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    # path('index_three/', index3, name='index3'),
    # path('index_two/', index2, name='index2'),
    path('members/', members, name='members'),
    path('portfolio/', portfolio, name='portfolio'),
    path('pricing/', pricing, name='pricing'),
    path('privacy/', privacy, name='privacy'),
    path('recover/', recover, name='recover'),
    path('service_details/', service_details, name='service_details'),
    path('service/', service, name='service'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('terms/', terms, name='terms'),
    path('testimonial/', testimonial, name='testimonial')
]
