from django import forms

from . import models

class login_form(forms.Form):

    email = forms.EmailField()

    # 패스워드를 숨기기 위해서 widget 설정
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        """
        * 사용자 ID, Password 유효성 검사 
        """
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        try:
            user = models.User.objects.get(username=email)
            
            if user.check_password(password):
                # 유효성 모두 통과
                return self.cleaned_data
            else:
                # password가 틀릴시 password에 오류 표시
                self.add_error("password",forms.ValidationError('비밀번호가 틀립니다.'))
        except models.User.DoesNotExist: 
            # 모델 내 사용자 계정이 없으면 오류발생
            # ID가 틀릴시 ID에 오류 표시
            self.add_error("email",forms.ValidationError('계정이 없습니다.'))