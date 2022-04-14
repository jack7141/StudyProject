from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):

    # FIXME: What is the difference between setUp() and setUpClass() in the Python unittest framework?
    # python unittest setUp method override
    def setUp(self):
        """슈퍼유저 생성, 로그인 후 일반 유저 생성"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='aravind@gmail.com',
            password='1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='silent@retreat.com',
            password='1234',
            name='Test user name'
        )

    def test_users_listed(self):
        """ 생성한 유저가 user 페이지에 있는지 유무 파악 """
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        self.assertContains(response, self.user.name)


    def test_user_page_change(self):
        """ 유저 수정 페이지 테스트"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """ 유저 추가 테스트 """
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)