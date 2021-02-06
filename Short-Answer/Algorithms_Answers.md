#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - Linear time. It doesn't matter if there are O(1) inside the loop. If n changes it affects the number of loops the while makes.

b) O(nlogn) - Log linear time. There are two loops that will get affected according to the n value.

c) O(logn) - Logaritmic time. The number of operations increases verry little in comparison to the variable. The function logn increases very slowly. = O(logn)

## Exercise II

Linear complexity O(n)

- Building hight changes with n input
- Egg number is unknown but plenty so it doesn't matter
- Egg get broken if thrown out of f hight or higher, survives if hight is lower than f
- Find a strategy to determine the value of f. Number of dropped + broken eggs is minimal.

levels_high = n
dropped eggs = d
broken eggs = d - f
safe point = f

- if same number of eggs gets dropped, how we can make it that more survive the falling from f higher grounds

- We have to make a conditional if the egg brakes that would be the f point and then another conditional to have the egg survive if it goes below f point.

- Since we will have to throw the eggs from all the levels to find the safe point, it makes it logaritmic complexity O(logn)
- Binary search - start in the middle,
