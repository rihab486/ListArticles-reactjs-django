from django.urls import path
from . views import *

from . import views

urlpatterns = [
 path('articles/', ArticleListCreate.as_view(), name="list and create article"),
 path('articles/<int:pk>', ArticleupdateDelete.as_view(), name="list and update articles"),
  path('classification/', ClassificationListCreate.as_view(), name="list and create classification"),
 path('classification/<int:pk>', ClassificationupdateDelete.as_view(), name="list and update classification"),


]