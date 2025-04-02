
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    
    def setUp(self): #the setUp method is called before every test method
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self): #Test for a single response
        """Test that a single response is stored correctly."""
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses) #the assertIn method checks if the first argument is in the second argument
    
    def test_store_multiple_responses(self): #Test for multiple responses
            """Test that multiple responses are stored correctly."""
            for response in self.responses:
                self.my_survey.store_response(response)
            for response in self.responses:
                self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()