from django.shortcuts import render


def index(request):
  """/トップページ"""
  context = {
    'name':'Kei',
  }
  return render(request,'paa/index.html',context)
    #render関数の第一引数には必ずrequestを渡し、第二引数にはhtmlファイルの場所を書く。
    #djangoフレームワークはアプリケーション内のtemplatesフォルダの内容を自動で読み込んでくれる。

def about(request):
    """/about アバウトページ"""
    return render(request,'paa/about.html')

def info(request):
    """/info インフォページ"""
    return render(request,'paa/info.html')
