# Refactorization of Code of Votes in Elections

## Colaborators:
- Fabryzzio Meza
- Aaron Navarro

## Refactorization Methods Applied:
1. **Method Extraction**:
   - We extracted methods from the global function `count_votes`. We developed four different functions that encapsulate the methods of the old global functions to simplify and improve the reusability of the code.

2. **Rename of Variables**:
   - We renamed functions and variables for better understanding of the code.

3. **Delete Duplicate Code**:
   - During the method extraction process, we deleted some code with the same purposes.

4. **Conditional Simplification**:
   - In the conditional part of the global function, we simplified it by using a function that retains the same logic but improves code comprehensibility.

5. **Division of Methods**:
   - We divided the global function into four different functions to improve the code's readability and reusability.

## Tests Development:

### 1. Valid File Test (`test_count_votes_valid_file`)
- **Purpose**: Verify the correct vote counting with valid data
- **Scenario**: Multiple cities with votes for different candidates
- **Expected Results**: 
  - Correct sum of votes per candidate
  - Proper winner declaration
- **Test Data**:
  ```python
  mock_csv = """city,candidate,votes
  Springfield,Alice,1200
  Springfield,Bob,750
  Shelbyville,Alice,2000
  Shelbyville,Bob,2500"""
  ```
  - Alice: 3200 votes (1200 + 2000)
  - Bob: 3250 votes (750 + 2500)
  - Winner: Bob with 3250 votes

### 2. Invalid Votes Test (`test_count_votes_invalid_votes`)
- **Purpose**: Verify system handling of invalid vote entries
- **Scenario**: File contains an invalid vote count
- **Expected Behavior**: 
  - Invalid votes are counted as 0
  - System continues processing remaining valid votes
- **Test Data**:
  ```python
  mock_csv = """city,candidate,votes
  Springfield,Bob,750
  Shelbyville,Alice,2000
  Springfield,Alice,invalid
  Shelbyville,Bob,2500"""
  ```
  - Alice: Invalid vote counted as 0
  - Final count: Alice 2000, Bob 3250

### 3. Tie Votes Test (`test_count_votes_tie`)
- **Purpose**: Verify system behavior in case of a tie
- **Scenario**: Two candidates with equal vote counts
- **Expected Behavior**: 
  - Winner determined alphabetically
  - Both vote counts displayed correctly
- **Test Data**:
  ```python
  mock_csv = """city,candidate,votes
  Springfield,Alice,1500
  Shelbyville,Bob,1500
  Capital,Alice,500
  Metro,Bob,500"""
  ```
  - Alice: 2000 votes (1500 + 500)
  - Bob: 2000 votes (1500 + 500)
  - Winner: Alice (alphabetically first)

### 4. Empty File Test (`test_empty_file`)
- **Purpose**: Verify system handling of empty input files
- **Scenario**: CSV file contains only headers
- **Expected Behavior**: 
  - System displays "No votes were cast"
  - No vote counting attempted
- **Test Data**:
  ```python
  mock_csv = """city,candidate,votes"""
  ```

### 5. Single Candidate Test (`test_single_candidate`)
- **Purpose**: Verify system behavior with only one candidate
- **Scenario**: All votes cast for the same candidate
- **Expected Behavior**: 
  - Correct vote sum for single candidate
  - Proper winner declaration
- **Test Data**:
  ```python
  mock_csv = """city,candidate,votes
  Springfield,Alice,1500
  Shelbyville,Alice,500"""
  ```
  - Alice: 2000 votes (1500 + 500)

### 6. Negative Votes Test (`test_process_votes_negative_votes`)
- **Purpose**: Verify system handling of negative vote counts
- **Scenario**: File contains negative vote values
- **Expected Behavior**: 
  - System accepts and processes negative votes
  - Correct arithmetic with negative values
- **Test Data**:
  ```python
  mock_csv = """city,candidate,votes
  Springfield,Alice,-100
  Shelbyville,Bob,500"""
  ```
  - Alice: -100 votes
  - Bob: 500 votes

### Test Execution Instructions

To run all tests:
```bash
python -m unittest test_vote_counter.py
```

To run a specific test:
```bash
python -m unittest test_vote_counter.TestVoteCounter.test_count_votes_tie
```

### Implementation Details
- **Mocking Strategy**: Used `unittest.mock.patch` for:
  - File operations (`mock_open`)
  - Print function output verification
- **Assertions**: Combination of:
  - `assert_any_call` for multiple print verifications
  - `assertEqual` for direct value comparisons
  - `assert_called_once_with` for single print verifications