#!/usr/bin/env python3
""" Test SUITE Unittest module Task """

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception_msg):
        """Test that access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_msg)

class TestGetJson(unittest.TestCase):
    """Test case for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected result."""
        with patch('utils.requests.get') as mocked_get:
            # Create a Mock response object with the json method returning test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mocked_get.return_value = mock_response

            # Call get_json with the test_url
            result = get_json(test_url)

            # Ensure the mocked get method was called once with test_url
            mocked_get.assert_called_once_with(test_url)

            # Check if the result is as expected
            self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches the result of a_property."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            obj = TestClass()
            # Call a_property twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Check that the method was called once
            mock_method.assert_called_once()

            # Check that the result is as expected
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
