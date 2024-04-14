"""
URL configuration for bookr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import reviews.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('booksearch/', reviews.views.book_search, name='book_search'),
    path("publishers/new/", reviews.views.publisher_edit, name="publisher_create"),
    path("publishers/<int:pk>/", reviews.views.publisher_edit, name="publisher_edit"),
    path("books/<int:book_pk>/reviews/new/", reviews.views.review_edit, name="review_create"),
    path(
        "books/<int:book_pk>/reviews/<int:review_pk>/",
        reviews.views.review_edit,
        name="review_edit",
    ),
    path('books/<int:pk>/', reviews.views.book_detail, name='book_detail'),
    # path('accounts/', reviews.views.include(('django.contrib.auth.urls', 'auth'),namespace='accounts')),
    path('accounts/profile/', reviews.views.profile, name='profile'),

]
