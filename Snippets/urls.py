from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin

urlpatterns = [
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet, name="snippet-add"),
    # path('snippets/create', views.snippet_create, name="snippet-create"),
    path('snippets/delete/<int:snippet_id>', views.snippet_delete, name="snippet-delete"),
    path('snippets/list', views.snippets_page, name="snippets-list"),
    path('snippets/my', views.snippets_my, name="snippets-my"),
    path('snippet/<int:snippet_id>', views.snippet_detail, name="snippet-detail"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.registration, name='registration'),
    path('comment/add', views.comment_add, name="comment-add"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
