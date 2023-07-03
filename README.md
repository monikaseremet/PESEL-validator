# pesel_validator
Polish Personal Identity Code (PESEL) validator

This program validates Polish Personal Identity Codes (PESEL).

Function is_it_valid(pesel: str) returns True or False based on whether the PESEL given as an argument is valid or not, additionaly indicates its gender. 
Polish PESELs follow the format *yymmddpppk*, where *yymmdd* contains the date of birth, including first occurrence of *m* which is the marker for century, *pppp* is the personal identifier where the last occurrence of *p* idicates gender of the person's PESEL, based on wheter the number is even (women) or odd (men), and *k* is a control character.

The program checks the validity by these criteria:
-  The length of the PESEL is correct, wheter it consist of numbers only.
-  The first half of the code is a valid, existing date in the format *yymmdd*.
-  The century marker is either 8 and 9 (1800s), 0 and 1 (1900s) or 2 and 3 (2000s).
-  The control character is valid.
  
The control character is calculated by taking each of the eleven-digit number, multiplying it by its corresponding weight from the string 1-3-7-9-1-3-7-9-1-3. Then the results are added and the ramainder of dividing by 10 is taken. For example, if the result was 63, the remainder of the dividing it by 10 is 3. The control character would be the substarction result of ten and this number.

You will find more examples and explanations of the uses of the PESEL are available at the [Ministry of Digital Affairs](https://www.gov.pl/web/gov/czym-jest-numer-pesel).

NB! Please make sure you do not share your own PESEL, for example in the code you use for testing.

Here are some valid PESELs you can use for testing:

  52060163461
  90010795416
  73080736945
