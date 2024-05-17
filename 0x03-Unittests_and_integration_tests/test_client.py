#!/usr/bin/env python3
"""A module for testing the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"login": "google"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"login": "google"})

    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url returns the correct value."""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct list of repos."""
        # Define the mock payload for get_json
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]
        mock_get_json.return_value = mock_payload
        mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos property
        repos = client.public_repos

        # Check that the mocked property and get_json were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

        # Check that the list of repos is as expected
        expected_repos = ["repo1", "repo2", "repo3"]
        self.assertEqual(repos, expected_repos)

if __name__ == '__main__':
    unittest.main()
