# test_vote_counter.py

import unittest
from unittest.mock import patch, mock_open
from vote_counter import count_votes, process_votes, define_winner

class TestVoteCounter(unittest.TestCase):

    @patch("builtins.print")
    def test_count_votes_valid_file(self, mock_print):
        mock_csv = """city,candidate,votes
        Springfield,Alice,1200
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")
        
        # Expected output after tallying votes
        mock_print.assert_any_call("Alice:3200 votes")
        mock_print.assert_any_call("Bob:3250 votes")
        mock_print.assert_any_call("The winner is Bob with 3250 votes")

    @patch("builtins.print")
    def test_count_votes_invalid_votes(self, mock_print):
        # Simulate a CSV file with invalid votes data
        mock_csv = """city,candidate,votes
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Springfield,Alice,invalid
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Expect Alice's invalid vote to be counted as 0
        mock_print.assert_any_call("Alice:2000 votes")
        mock_print.assert_any_call("Bob:3250 votes")
        mock_print.assert_any_call("The winner is Bob with 3250 votes")

    @patch("builtins.print")
    def test_count_votes_tie(self, mock_print):
        # Test case for a tie between candidates
        mock_csv = """city,candidate,votes
        Springfield,Alice,1500
        Shelbyville,Bob,1500
        Capital,Alice,500
        Metro,Bob,500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Both candidates should have equal votes
        mock_print.assert_any_call("Alice:2000 votes")
        mock_print.assert_any_call("Bob:2000 votes")
        # In case of tie, the first candidate alphabetically wins
        mock_print.assert_any_call("The winner is Alice with 2000 votes")

    @patch("builtins.print")
    def test_empty_file(self, mock_print):
        # Test case for empty file with only headers
        mock_csv = """city,candidate,votes"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")
        
        # Should print "No votes were cast"
        mock_print.assert_called_once_with("No votes were cast")

    @patch("builtins.print")
    def test_single_candidate(self, mock_print):
        # Test case for single candidate
        mock_csv = """city,candidate,votes
        Springfield,Alice,1500
        Shelbyville,Alice,500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        mock_print.assert_any_call("Alice:2000 votes")
        mock_print.assert_any_call("The winner is Alice with 2000 votes")

    def test_process_votes_negative_votes(self):
        # Test case for negative votes
        mock_csv = """city,candidate,votes
        Springfield,Alice,-100
        Shelbyville,Bob,500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            results = process_votes("votes.csv")
            
        self.assertEqual(results["Alice"], -100)
        self.assertEqual(results["Bob"], 500)

if __name__ == "__main__":
    unittest.main()