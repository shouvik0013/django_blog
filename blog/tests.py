from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


from .models import Post


class BlogTests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@tmail.com',
            password='secret',
        )

        self.post = Post.objects.create(
            title='New title',
            body='New body',
            author=self.user,
        )


    def test_string_representation(self):
        self.assertEqual(str(self.post), 'New title')

    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'New title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'New body')
    

    def test_post_list_view(self):
        response    = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New body')
        self.assertTemplateUsed(response, 'home.html')

    
    def test_post_detail_view(self):
        response    = self.client.get('/post/1/')
        no_response  = self.client.get('/post/7/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'New title')
        self.assertTemplateUsed(response, 'post_detail.html')
        
    
    def test_post_create_view(self):
        response = self.client.post(path=reverse('post_new'), data={
            'title': 'New title',
            'body': 'New text body',
            'author': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text body')


    def test_post_delete_view(self):

        response = self.client.get(path=reverse('post_delete', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    
    def test_post_update_view(self):
        response = self.client.post(path=reverse('post_edit', kwargs={"pk": 1}), data={
            'title': 'Updated title',
            'body': 'Updated body',
        })
        
        
        #self.assertContains(response, 'Updated title')
        #self.assertContains(response, 'Updated body')
        #self.assertEqual(response.status_code, 302)
        print('Status code of post_update_view: ' + str(response.status_code))
