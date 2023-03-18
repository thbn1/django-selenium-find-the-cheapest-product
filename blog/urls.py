from django.urls import path, include
from . import views
# http://127.0.0.1:8000/         =>index
# http://127.0.0.1:8000/index    =>index
# http://127.0.0.1:8000/blogs    =>blogs
# http://127.0.0.1:8000/blogs/3  =>blog-details
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path("",views.index),
    path("index",views.index),
    path("blogs",views.blogs),
    path("blogs/<str:id>",views.blog_details),
    path("getproducts",views.getproducts),
    path("urunara",views.urunara),

    path("register",views.register_request),
    path("login",views.login_request, name="login"),
    path("logout",views.logout_request, name="logout"),

]

urlpatterns += staticfiles_urlpatterns()
