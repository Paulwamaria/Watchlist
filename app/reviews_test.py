import unittest

from models import reviews

Review = reviews.Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.new_review =  Review(1234,'Dark Phoenix',"https://image.tmdb.org/t/p/w500/jdjdjdjn",'My oh my!, what a movie!')

    def tearDown(self):
        Review.clear_reviews()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))

    def test_instance_variables(self):
        self.assertEqual(self.new_review.movie_id, 1234)
        self.assertEqual(self.new_review.title, 'Dark Phoenix')
        self.assertEqual(self.new_review.imageurl, "https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEqual(self.new_review.review, 'My oh my!, what a movie!')

    def test_save_reviews(self):
        self.new_review.save_review()
        self.assertEqual(len(Review.all_reviews),1)


if __name__ ==  '__main__':
    unittest.main()

        
