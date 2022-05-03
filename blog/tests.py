from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone
from .views import post_list, post_details
from .models import Post
# Create your tests here.

class HomeTest(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='test user', email = 'test@mail.com', password='xyz')
        self.post = Post.objects.create(author=user, title='Test', text='Something.', created_date=timezone.now())
        url = reverse('post_list')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, post_list) 
    
    def test_home_view_contains_links_to_post_details(self):
        post_details_url = reverse('post_details', kwargs={'pk': self.post.pk})
        print(self.response)
        self.assertContains(self.response, 'href="{}"'.format(post_details_url))

class PostDetailsTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='test user', email = 'test@mail.com', password='xyz')
        Post.objects.create(author=user, title='Test', text='Something.', created_date=timezone.now())
    
    def test_pd_view_success_status_code(self):
        url = reverse('post_details', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    
    def test_pd_view_not_found_status_code(self):
        url = reverse('post_details' ,kwargs={'pk':43})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
    
    def test_pd_url_resolves_pd_view(self):
        view = resolve('/post/1/')
        self.assertEquals(view.func, post_details)
