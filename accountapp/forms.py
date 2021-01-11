from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 부모의 초기값 그대로 생성
        self.fields['username'].disabled = True # 속성 비활성화/수정, update 불가능하게 변경됨