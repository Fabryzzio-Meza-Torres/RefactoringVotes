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

## Tests Development:
Our team developed two tests: one for the case of a tie between candidates and another for the case of {Insert Aaroncito Salvame}.
