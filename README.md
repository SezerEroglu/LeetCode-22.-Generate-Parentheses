# LeetCode-22.-Generate-Parentheses

We add an open paranthesis and then a closed paranthesis to the stack. If the open and closed paran count is equal to n, we return.
We can make two decisions, add an opening paran or closed paran. Close paran count must be equal or less than closed. Also open paran
count must be equal or less than n. If both the open and closed paran icount is n, this means we are done and we can return.
After every backtack call, we pop the lement we added so the other condition can flow with an unaltered stack.