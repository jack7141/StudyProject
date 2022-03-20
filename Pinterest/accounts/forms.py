from django import forms

from . import models

class login_form(forms.Form):
    """
    * 로그인시 유효성 검사
    """
    email = forms.EmailField()

    # 패스워드를 숨기기 위해서 widget 설정
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        """
        * 사용자 ID, Password 유효성 검사 
        """
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
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

"""
class sign_up_form(forms.Form):

    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)

    email = forms.EmailField()

    # 패스워드를 숨기기 위해서 widget 설정
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("기존 사용자가 있습니다.")
        except models.User.DoesNotExist: 
            # 기존 DB에 사용자가 이메일이 없을 경우만 회원가입!
            return email

    # 내가 유효성을 검사하고자하는 태그?를 clean뒤에 붙여줘야지 사용가능함
    def clean_confirm_password(self):
        password = self.cleaned_data["password"]

        # 모델?에서 가져오는 password가 아닐시 get으로 가져와야함
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("비밀번호가 동일하지 않습니다.")
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        # 비밀번호 암호화 후 사용자를 가입시키기 위해서 create_user함수 사용
        # parmas: username, email, password 형식으로 지정되어있음
        user = models.User.objects.create_user(email, email, password) 
        user.first_name = first_name
        user.last_name = last_name
        user.save()
"""

# Model Form 형식으로 수정하여 기존에  이메일에서 사용한 유일성 검사 즉, 모델에 내가 지정한 
# 모델의 특성들을 그대로 사용한다. => 기존의 사용하던, clean_email은 자동으로 검사할 수 있게됨
class sign_up_form(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    # 페이지 에러가 생겨서 Email 유효성 체크는 그대로 유지
    # unique constraint failed auth_user.username 
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("기존 사용자가 있습니다.")
        except models.User.DoesNotExist: 
            # 기존 DB에 사용자가 이메일이 없을 경우만 회원가입!
            return email

    # 내가 유효성을 검사하고자하는 태그?를 clean뒤에 붙여줘야지 사용가능함
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")

        # 모델?에서 가져오는 password가 아닐시 get으로 가져와야함
        confirm_password = self.cleaned_data.get("confirm_password")
        print(password, confirm_password)
        if password != confirm_password:
            raise forms.ValidationError("비밀번호가 동일하지 않습니다.")
        else:
            return password

    # Model Form에는 save 함수가 내장 되어있기 때문에 기존의 방식을 취하지 않고
    # Model Form에 있는 기능을 사용해서 저장하면됨
    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        # 비밀번호를 암호화해서 저장한다.
        user.set_password(password)
        user.save()
