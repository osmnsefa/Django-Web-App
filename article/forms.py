from django import forms 
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title","content","article_image"] #biz burda title,content ve article_image alanından input oluşturmasını söylüyoruz.
        
        
        