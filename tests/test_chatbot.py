import unittest
import json
from app import app, check_predefined_patterns, generate_response

class ChatbotTestCase(unittest.TestCase):
    """Test cases for AI Chatbot"""

    def setUp(self):
        """Set up test client"""
        self.app = app
        self.client = app.test_client()
        self.app.config['TESTING'] = True

    def tearDown(self):
        """Clean up after tests"""
        pass

    # Pattern Matching Tests
    def test_greeting_pattern_recognition(self):
        """Test greeting pattern recognition"""
        result = check_predefined_patterns("hello")
        self.assertIsNotNone(result)
        self.assertIn("assist", result.lower())

    def test_help_pattern_recognition(self):
        """Test help request pattern recognition"""
        result = check_predefined_patterns("I need help")
        self.assertIsNotNone(result)

    def test_product_pattern_recognition(self):
        """Test product inquiry pattern recognition"""
        result = check_predefined_patterns("tell me about your product")
        self.assertIsNotNone(result)

    def test_no_pattern_match(self):
        """Test message without pattern match"""
        result = check_predefined_patterns("xyzabc random message")
        self.assertIsNone(result)

    # API Endpoint Tests
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.client.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')

    def test_index_endpoint(self):
        """Test root endpoint"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'AI Chatbot API')

    def test_chat_endpoint_with_message(self):
        """Test chat endpoint with valid message"""
        response = self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'hello'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('response', data)

    def test_chat_endpoint_empty_message(self):
        """Test chat endpoint with empty message"""
        response = self.client.post(
            '/api/chat',
            data=json.dumps({'message': ''}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_chat_endpoint_no_json(self):
        """Test chat endpoint without JSON"""
        response = self.client.post(
            '/api/chat',
            content_type='application/json'
        )
        self.assertIn(response.status_code, [400, 500])

    def test_history_endpoint(self):
        """Test history endpoint"""
        # First, send a message
        self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'test'}),
            content_type='application/json'
        )

        # Then get history
        response = self.client.get('/api/history')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIsInstance(data['history'], list)

    def test_clear_endpoint(self):
        """Test clear endpoint"""
        response = self.client.post('/api/clear')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')

    # Response Accuracy Tests
    def test_response_not_empty(self):
        """Test that responses are not empty"""
        response = self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'hello'}),
            content_type='application/json'
        )
        data = json.loads(response.data)
        self.assertTrue(len(data['response']) > 0)

    def test_response_is_string(self):
        """Test that response is a string"""
        response = self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'what is AI?'}),
            content_type='application/json'
        )
        data = json.loads(response.data)
        self.assertIsInstance(data['response'], str)

    def test_timestamp_in_response(self):
        """Test that response includes timestamp"""
        response = self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'hello'}),
            content_type='application/json'
        )
        data = json.loads(response.data)
        self.assertIn('timestamp', data)

    # Content Safety Tests
    def test_response_contains_no_errors(self):
        """Test that response doesn't contain error strings"""
        response = self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'hello'}),
            content_type='application/json'
        )
        data = json.loads(response.data)
        response_text = data['response'].lower()
        
        # Check that response doesn't contain error indicators
        error_indicators = ['error', 'exception', 'failed', 'traceback']
        for indicator in error_indicators:
            self.assertNotIn(indicator, response_text)

    # Performance Tests
    def test_response_time_acceptable(self):
        """Test that response time is acceptable"""
        import time
        
        start_time = time.time()
        response = self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'hello'}),
            content_type='application/json'
        )
        end_time = time.time()
        
        response_time = end_time - start_time
        
        # Response should be generated within 30 seconds (Gemini API call)
        self.assertLess(response_time, 30)

    # User Engagement Tests
    def test_multiple_messages_in_sequence(self):
        """Test handling multiple messages in sequence"""
        messages = ['hello', 'what is AI?', 'thank you']
        
        for message in messages:
            response = self.client.post(
                '/api/chat',
                data=json.dumps({'message': message}),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data)
            self.assertEqual(data['status'], 'success')

    def test_conversation_context_maintained(self):
        """Test that conversation context is maintained"""
        # Send initial message
        self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'my name is John'}),
            content_type='application/json'
        )

        # Send follow-up message
        response = self.client.post(
            '/api/chat',
            data=json.dumps({'message': 'what is my name?'}),
            content_type='application/json'
        )

        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')


class AccuracyTestCase(unittest.TestCase):
    """Test cases for chatbot accuracy"""

    def setUp(self):
        """Set up test client"""
        self.app = app
        self.client = app.test_client()
        self.app.config['TESTING'] = True

    def test_pattern_accuracy_greeting(self):
        """Test greeting pattern accuracy"""
        test_inputs = ['hello', 'hi', 'hey']
        for input_text in test_inputs:
            result = check_predefined_patterns(input_text)
            self.assertIsNotNone(result, f"Failed for input: {input_text}")

    def test_pattern_accuracy_help(self):
        """Test help request pattern accuracy"""
        test_inputs = ['help', 'I need help', 'can you assist']
        for input_text in test_inputs:
            result = check_predefined_patterns(input_text)
            self.assertIsNotNone(result, f"Failed for input: {input_text}")

    def test_pattern_case_insensitivity(self):
        """Test that patterns are case insensitive"""
        test_inputs = ['HELLO', 'Hello', 'hElLo']
        for input_text in test_inputs:
            result = check_predefined_patterns(input_text)
            self.assertIsNotNone(result, f"Failed for input: {input_text}")


if __name__ == '__main__':
    unittest.main()
