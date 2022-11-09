from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product


# Create your tests here.

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='Graphics', slug='graphics')

    def test_category_model_entry(self):
        """
        Test Category Model Data insertion/Types/Field attributes
        """

        data = self.data1
        self.assert_(isinstance(data, Category))
        self.assertEqual(str(data), 'Graphics')


class TestProductsModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='Graphics', slug='graphics')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='graphics beginners',
                                            created_by_id=1, slug='graphics-beginners',
                                            price='20.00', image='graphics')

    def test_products_model_entry(self):
        """
        Test Product model data insetion/types/filed attributes
        :return:
        """

        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'graphics beginners')
