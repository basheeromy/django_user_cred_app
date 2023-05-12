from django.test import TestCase, Client
from django.urls import reverse
from home_page.models import Products

class TestViews(TestCase):
    
    def test_products_GET(self):
        
        client = Client()
        response = client.get(reverse('home_view'))
        self.assertEquals(response.status_code,302)
        

# as this view will automatically redirect to login_page view as there 
# is no session data, we are not going to test this with assertTemplateUsed function
        
# The test client is a Python class that acts as a dummy web browser, 
# allowing you to test your views and interact with your Django-powered 
# application programmatically.     


# The HyperText Transfer Protocol (HTTP) 302 Found redirect status 
# response code indicates that the resource requested has been temporarily 
# moved to the URL given by the Location header.