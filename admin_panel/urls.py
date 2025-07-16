"""
URL configuration for djangoIntegration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('logout',views.logout_view, name='logout'),
    path('productlist', views.productlist, name='productlist'),
    path('page-add-product', views.add_product, name='page-add-product'),
    path('page-list-category', views.category_list, name='page-list-category'),
    path('page-add-category', views.add_category, name='page-add-category'),
    path('page-list-sale', views.list_sale, name='page-list-sale'),
    path('page-add-sale', views.add_sale, name='page-add-sale'),
    path('page-list-purchase', views.list_purchase, name='page-list-purchase'),
    path('page-add-purchase', views.add_purchase, name='page-add-purchase'),
    path('page-list-returns', views.list_returns, name='page-list-returns'),
    path('page-add-return', views.add_returns, name='page-add-return'),
    path('page-list-customers', views.list_customers, name='page-list-customers'),
    path('page-add-customers', views.add_customers, name='page-add-customers'),
    path('page-list-users', views.list_users, name='page-list-users'),
    path('page-add-users', views.add_users, name='page-add-users'),
    path('page-list-suppliers', views.list_suppliers, name='page-list-suppliers'),
    path('page-add-supplier', views.add_supplier, name='page-add-supplier'),
    path('page-report', views.page_report, name='page-report'),
    path('app/user-profile', views.user_profile, name='app/user-profile'),
    path('app/user-add', views.user_add, name='app/user-add'),
    path('app/user-list', views.user_list, name='app/user-list'),
    # New dynamic URLs for category edit and delete
    path('page-delete-category/<int:pk>/', views.delete_category, name='page-delete-category'),
    path('page-edit-category/<int:pk>/', views.edit_category, name='page-edit-category'),
    path('api/signup', views.signup_api, name='signup_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)