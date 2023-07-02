from django import forms 

class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı")
    password=forms.CharField(label="Parola",widget=forms.PasswordInput)
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label="Parolayı Doğrulayın",widget=forms.PasswordInput)
    
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        
        if password and confirm and password != confirm:    #burada confirm,password alanlarının doldurulup doldurulmadığını ve paraloların eşit olup olmadığını kontrol ettik.
            raise forms.ValidationError("Parolalar Eşleşmiyor...")
        
        values={        # Aldığımız bilgileri kullanabilmek için sözlük yapısında tutmamız gerekiyor.
            "username":username,
            "password": password,
            
        }
        return values    
    
    