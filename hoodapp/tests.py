from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class TestLocation(TestCase):
    def setUp(self):
        self.location1 = Location.objects.create(location='Mombasa')

    def tearDown(self):
        Location.objects.all().delete()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.location1, Location))

    def test_save_location(self):
        self.location2 = Location.objects.create(location='Nairobi')
        self.assertEqual(len(Location.objects.all()), 2)
        
        
        
        

class TestNeighbourhood(TestCase):
  def setUp(self):
    self.location = Location.objects.create(location='Mombasa')
    self.hood1 = Neighbourhood.objects.create(name='Langata', location=self.location, police_num= '0722000000', hospital_num= '0722000000', occupants_count=2)


  def tearDown(self):
        Location.objects.all().delete()
        Neighbourhood.objects.all().delete()
        

  def test_isinstance(self):
       self.assertTrue(isinstance(self.hood, Neighbourhood))

  def test_deletehood(self):
    self.hood2 = Neighbourhood.objects.create(name='Langata', location=self.location, police_num= '0722000000', hospital_num= '0722000000', occupants_count=2)
    self.assertEqual(len(Neighbourhood.objects.all()),2)
    Neighbourhood.delete_neigbourhood(self.hood.id)
    self.assertEqual(len(Neighbourhood.objects.all()),1)

  def test_findneighborhood(self):
    searchterm = 'Langata'
    self.hood2 = Neighbourhood.objects.create(name='Langata', location=self.location, police_num= '0722000000', hospital_num= '0722000000', occupants_count=2)
    results = Neighbourhood.find_neigborhood(searchterm)
    self.assertTrue(len(results), 1)

  def test_updateneighbourhood(self):
    self.hood2 = Neighbourhood.objects.create(name='Langata', location=self.location, police_num= '0722000000', hospital_num= '0722000000', occupants_count=2)
    Neighbourhood.update_neighbourhood(self.hood2.id, name='Uthiru')
    updated = Neighbourhood.objects.get(id = self.hood2.id)
    self.assertEqual(updated.name, 'Uthiru')
    
    
    
    
class TestBusiness(TestCase):
  def setUp(self):
    self.location = Location.objects.create(location='Nairobi')
    self.newuser = User.objects.create(username = 'Ollie')
    self.hood = Neighbourhood.objects.create(name='Langata', location=self.location, police_num= '0722000000', hospital_num= '0722000000', occupants_count=2)
    self.business = Business.objects.create(name = 'mintgadgets', description='huawei phones', email='mintgadget@gmail.com', username=self.newuser, neighbourhood=self.hood)

  def tearDown(self):
    User.objects.all().delete()
    Neighbourhood.objects.all().delete()
    Business.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.business, Business))  

  def test_save_business(self):
    self.business2 = Business.objects.create(name = 'Furywrld', description='photography', email='wrld@gmail.com', username=self.newuser, neighbourhood=self.hood)
    self.assertEqual(len(Business.objects.all()), 2)


  def test_delete_business(self):
    self.business2 = Business.objects.create(businessname = 'trial2', description='description for trial2', email='sammaingi5@gmail.com', username=self.newuser, neighbourhood=self.hood)
    self.assertEqual(len(Business.objects.all()), 2)
    Business.delete_business(self.business2.id)
    self.assertEqual(len(Business.objects.all()), 1)

  def test_searchbusiness(self):
    self.business2 = Business.objects.create(name = 'mintgadgets', description='huawei phones', email='mintgadget@gmail.com', username=self.newuser, neighbourhood=self.hood)
    searchterm = 'mintgadgets'
    search_results = Business.searchbusiness(searchterm)
    self.assertEqual(len(search_results), 1)    
