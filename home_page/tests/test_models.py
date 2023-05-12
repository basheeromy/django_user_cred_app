from django.test import TestCase
from home_page.models import Products

class TestModels(TestCase):
    
    def setUp(self):
        self.product1 = Products.objects.create(title = 'Toys',price = 300.00, rating = 4)
    
    def test_object_name_from_dunder_str(self):
        self.assertEquals(str(self.product1),'Toys')
        
        
# Here we can see the error if we change Toys to something different like Toys1