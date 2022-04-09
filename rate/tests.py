from django.test import TestCase

from .models import Profile, Project
from django.contrib.auth.models import User

# Create your tests here.

class ProjectTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user('testuser')

        self.project = Project(title='Test Project', description='Test Description', link='https://www.google.com', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_method(self):
        self.project.save_project()
        project = Project.objects.filter(title='Test Project').delete()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)

    def test_update_method(self):
        self.project.save_project()
        project = Project.objects.filter(title='Test Project').update(title='Test Project Updated')
        projects = Project.objects.filter(title='Test Project Updated')
        self.assertTrue(len(projects) > 0)

    def test_search_by_title(self):
        self.project.save_project()
        project = Project.objects.filter(title__icontains='Test')
           
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user('testuser')

        self.profile = Profile(bio='Test Bio', job_title='Test Job Title', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        profile = Profile.objects.filter(bio='Test Bio').delete()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_update_method(self):
        self.profile.save_profile()
        profile = Profile.objects.filter(bio='Test Bio').update(bio='Test Bio Updated')
        profiles = Profile.objects.filter(bio='Test Bio Updated')
        self.assertTrue(len(profiles) > 0)
   
