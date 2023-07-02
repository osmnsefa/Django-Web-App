from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article (models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")#auth tablosundaki user'a erişiyoruz.on delete ile silinmesi halinde kullanıcıya ait tüm verilerin silinmesini sağlıyoruz.
    title=models.CharField(max_length=50,verbose_name="Başlık")#verbose_name admin panelindeki adını değiştirmemizi sağlar.
    content=RichTextField()
    created_date=models.DateTimeField( auto_now_add=True,verbose_name="Oluşturma Tarihi")
    article_image=models.FileField( blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin") #blank ve null kısmı boş ya da dolu olabilir demek
    
    def __str__(self):
        return self.title   #bu fonksiyon makale'nin üzerinde title bilgisinin bulunmasını sağlar.
    
    class Meta:
        ordering=['-created_date'] #en son eklenen makaleyi ilk sıraya getirsin diye yaptık.
    
    
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="İsim")
    comment_content=models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_author
    
    class Meta:
        ordering=['-comment_date']
    

    
    