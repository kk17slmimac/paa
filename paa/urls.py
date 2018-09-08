from django.urls import path
from.import views

app_name='paa'

urlpatterns = [
    path('',views.index,name='index'),
    #第一引数を空にしているのは/paid_acquisition_app以降が空の場合という意味
    #第二引数のviews.indexは実際に呼び出し処理を指定
    #第三引数は名前、今までurlに対して処理を呼び出す'(正引き)'と考えていたが逆にurlの文字列が欲しい場合(逆引き)にnameに指定した名前と
    path('about/',views.about,name='about'),
    path('info/',views.info,name='info'),


]
