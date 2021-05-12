from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestclass(TestCase):
    # Set up method
    def setUp(self):
        self.alvynah=Editor(first_name='Alvynah',last_name='Wabwoba',email='alvynah@moringaschool.com')
    # To tear down instance
    def tearDown(self):
        Editor.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.alvynah,Editor))
    # Testing save method
    def test_save_method(self):
        self.alvynah.save_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)>0)
    # Testing delete method
    def test_delete_method(self):
        self.alvynah.delete_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)== 0)
    def test_get_all(self):
        self.alvynah.get_all()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)==1)
    def test_update_editor(self):
        self.alvynah.save_editor()
        self.alvynah.update_editor(self.alvynah.id,'Vee')
        vee=Editor.objects.get(first_name='Vee')
        self.assertEqual(vee.first_name, 'Vee')

class ArticleTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.alvynah = Editor(first_name='Alvynah', last_name='Wabwoba', email='alvynah@moringaschool.com')
        self.alvynah.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.alvynah)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)
    def test_get_news_by_date(self):
        test_date='2017-03-17'
        date=dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date =Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
