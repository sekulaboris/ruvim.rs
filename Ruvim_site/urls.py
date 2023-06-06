from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from Blog.sitemaps import PostSitemap



sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Base.urls', namespace='base')),
    path('', include('Contact.urls', namespace='contact')),
    path('', include('Blog.urls', namespace='blog')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),
    path('account/', include ('django.contrib.auth.urls')),
    path('account/', include('account.urls', namespace='account')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),      
    path('payment/', include('payment.urls', namespace='payment')),  
    path('', include('OnlineShop.urls', namespace='onlineshop')),
   
]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
