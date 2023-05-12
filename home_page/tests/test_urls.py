from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home_page.views import home_view

class TestUrls(SimpleTestCase):
    
    def test_home_view_url_is_resolved(self):
        url = reverse('home_view')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,home_view)
        
        
# Here, reverse function will convert home_view variable to actual url
# resolve function will return the value gets when we execute a particular url
# assertEquals function checks two values same or not
