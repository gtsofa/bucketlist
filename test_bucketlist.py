# test_bucketlist.py

import unittest
import os
import json
from app import create_app, db

class BucketlistTestCase(unittest.TestCase):
    """
    This class represents the bucketlist test case
    """
    def setUp(self):
        """
        Define test variable and initialize app
        """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.bucketlist = {'name': 'Go to Borabora for vacation'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_bucketlist_creation(self):
        """
        Test API can create a bucketlist(POST request)
        """
        response = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Go to Borabora', str(response.data))

    def test_api_can_get_all_bucketlists(self):
        """
        Test API if it can get a bucketlist(GET request)
        """
        response = self.client().post('/bucketlist/', data=self.bucketlist)
        self.assertEqual(response.status_code, 201)
        response = self.client().get('/bucketlist/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Go to Borabora', str(response.data))

    def test_api_can_get_bucketlist_by_id(self):
        """
        Test API can get a single bucketlist by using it's id.
        """
        results = self.client().post('/bucketlist/', data=self.bucketlist)
        self.assertEqual(results.status_code, 201)
        result_in_json = json.loads(results.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/bucketlist/{}'.format(result_in_json['id'])
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn('Go to Borabora', str(result.data))

    def test_bucket_can_be_edited(self):
        """
        Test API can edit an existing bucketlist. (PUT request)
        """
        resultvalue = self.client().post(
            '/bucketlists', data={'name': 'Eat, pray and love'})
        self.assertEqual(resultvalue.status_code, 201)
        resultvalue = self.client().put(
            '/bucketlist/1', data={'name': 'Dont just eat, but also pray and love :-)'}
        )
        self.assertEqual(resultvalue.status_code, 200)
        results = self.client().get('/bucketlists/1')
        self.assertIn('Dont just eat', str(results.data))

    def test_bucketlist_deletion(self):
        """
        Test API can delete an existing bucketlist. (Delete request)
        """
        resultvalue = self.client().post('/bucketlist', data={'name': 'Eat, pray and love'})
        self.assertEqual(resultvalue.status_code, 201)
        response = self.client().delete('/bucketlist/1')
        self.assertEqual(response.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/bucketlist/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """
        Tear down all initialized variables.
        """
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# make the tests conveniently executable
if __name__=='__main__':
    unittest.main()
