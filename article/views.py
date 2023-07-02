from django.shortcuts import render,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):
    keyword=request.GET.get('keyword')
    
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    
    articles=Article.objects.all()
    
    return render(request,"articles.html",{"articles":articles})


def index(request):
    return render(request,"index.html")#parametre olarak request vermeliyiz.
def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    
    
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")# giriş yapma kontrolünü djangodaki decorator ile yapıp login url'sine yönlendiriyoruz.
def addarticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None) #request.FILES'i dosya yüklenip yüklenmeme durumu için koyduk.
    
    if form.is_valid():
        article=form.save(commit=False)# model formlardaki otomatik kaydetmeyi false yapıp obje oluşturuyoz.çünkü model formlara yazar bilgisinide vermemiz gerekiyor.
        
        article.author=request.user
        article.save()
        
        messages.success(request,"Makale Başarıyla Oluşturuldu...")
        return redirect("article:dashboard") #name=dahboard article'ın altında olduğu için bu şekilde çağırıyoruz.
    
    return render(request,"addarticle.html",{"form":form})
def detail(request,id):
    article=get_object_or_404(Article,id=id)# olmayan bir makale çağırılırsa 404 sayfasına gönderir,makale varsa obje haline getirir.
    
    comments=article.comments.all()
    
    
    return render(request,"detail.html",{"article":article,"comments":comments})
@login_required(login_url="user:login")
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article) #instance parametresi ile article objesi içindeki bligileri forma aktarırız.
    
    if form.is_valid():
        article=form.save(commit=False)# model formlardaki otomatik kaydetmeyi false yapıp obje oluşturuyoz.çünkü model formlara yazar bilgisinide vermemiz gerekiyor.
        
        article.author=request.user
        article.save()
        
        messages.success(request,"Makale Başarıyla Güncellendi...")
        return redirect("article:dashboard") #name=dahboard article'ın altında olduğu için bu şekilde çağırıyoruz.
    
    
    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    
    article.delete()
    
    messages.success(request,"Makale Başarıyla Silindi...")
    return redirect("article:dashboard") #name=dahboard article'ın altında olduğu için bu şekilde çağırıyoruz.

def addComment(request,id):
    article=get_object_or_404(Article,id=id)
    
    if request.method == "POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        
        newComment.article=article
        
        newComment.save()
        
    return redirect(reverse("article:detail",kwargs={"id":id}))

