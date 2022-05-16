from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class UserManager(BaseUserManager):
#     # 일반 user 생성
#     def create_user(self, user_id, sex, age, vege_type, alle_type, password=None):
#         if not user_id:
#             raise ValueError('must have user user_id')
#         if not sex:
#             raise ValueError('must have user sex')
#         if not age:
#             raise ValueError('must have user age')
#         user = self.model(
#             user_id=user_id,
#             sex=sex,
#             age=age,
#             vege_type=vege_type,
#             alle_type=alle_type
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     # 관리자 user 생성
#     def create_superuser(self, user_id, sex, age, password=None):
#         user = self.create_user(
#             user_id,
#             password=password,
#             sex=sex,
#             age=age
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     id = models.AutoField(primary_key=True)
#     user_id = models.CharField(
#         default='', max_length=100, null=False, blank=False, unique=True)
#     sex = models.BooleanField(default=False, null=False)
#     age = models.SmallIntegerField(
#         default='', null=False, blank=False)
#     vege_type = models.CharField(
#         default='', max_length=50, null=False, blank=False, unique=False)
#     alle_type = models.CharField(
#         default='', max_length=50, null=False, blank=False, unique=False)

#     # User 모델의 필수 field
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     # 헬퍼 클래스 사용
#     objects = UserManager()

#     # 사용자의 usernamefield는 user_id로 설정
#     USERNAME_FIELD = 'user_id'
#     # 필수로 작성해야하는 field
#     REQUIRED_FIELDS = ['user_id', 'age', 'sex']

#     def __str__(self):
#         return self.user_id

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(
        default='', max_length=100, null=False, blank=False, unique=True)
    sex = models.BooleanField(default=False, null=False)
    age = models.SmallIntegerField(
        default='', null=False, blank=False)
    vege_type = models.CharField(
        default='', max_length=50, null=False, blank=False, unique=False)
    alle_type = models.CharField(
        default='', max_length=50, null=False, blank=False, unique=False)
    password = models.CharField(max_length=200)
