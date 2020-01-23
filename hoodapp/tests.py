from django.test import TestCase
from .models import Hood, Biz, Posts
# Create your tests here.

class TestHood(TestCase):
    def setUp(self):
        self.new_hood=Hood(name='test', location='test_loc', occupants_count=9, police_contact=900, hospital_contact=100)
        self.new_hood.save_hood()

    def test_hood_instance(self):
        self.assertTrue(isinstance(self.new_hood, Hood))

    def test_hood_delete(self):
        self.test_hood=Hood(name='test1', location='test_loc1', occupants_count=9, police_contact=900, hospital_contact=100)
        self.test_hood.save_hood()
        self.new_hood.delete_hood()
        self.assertTrue(len(Hood.objects.all()), 1)

class TestBiz(TestCase):
    def setUp(self):
        self.new_biz=Biz(name='b_test', description='test potatoes')
        self.new_biz.save_biz()

    def test_biz_instance(self):
        self.assertTrue(isinstance(self.new_biz, Biz))

    def test_search_by_name(self):
        self.test_biz=Biz(name='b_test1', description='test appols')
        self.test_biz.save_biz()
        search=Biz.search_by_name(name='b')
        self.assertEqual(search, test_biz)
