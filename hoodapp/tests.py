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
    searchterm = 'Embakasi'
    self.hood2 = Neighbourhood.objects.create(name='Langata', location=self.location, police_num= '0722000000', hospital_num= '0722000000', occupants_count=2)
    results = Neighbourhood.find_neigborhood(searchterm)
    self.assertTrue(len(results), 1)

  def test_updateneighbor(self):
    self.hood2 = Neighbourhood.objects.create(name='Langata', location=self.location, police_num= '0722000000', hospital_num= '0722000000', occupants_count=2)
    Neighbourhood.update_neighborhood(self.hood2.id, name='Uthiru')
    updated = Neighbourhood.objects.get(id = self.hood2.id)
    self.assertEqual(updated.name, 'Uthiru')
