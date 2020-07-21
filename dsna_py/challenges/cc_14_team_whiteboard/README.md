# Interview 01
__Max stack__. Write a method that returns the “biggest” element in a stack.

## Specifications
Read all of the following instructions carefully. <br>
- Act as an interviewer, giving a candidate a code challenge <br>
- Score the candidate according to the Whiteboard Rubric <br>
- You are free to offer suggestions or guidance (and see how they respond), but don’t solve it for the candidate

## Feature Tasks
Ask the candidate to write a __'Max Stack'__ which is defined as a __Stack__ with an additional __`getMax()`__ member function which returns the 'biggest' element in the Stack.
- The candidate can assume that only numeric values will be stored in the Stack, *but she/he has to ask before the interviewer can state this*.
- The internal memory of the Stack can be approached in different ways.
	- Using a __Linked List__
		- This approach uses __O(n)__ space.
	- Using an __Array__
		- This approach can either use __O(n)__ space *(or O(c) where c is the size of the array in static-size arrays)*.
		- If your language doesn't support dynamic arrays, inquire about the candidate's decision of using a limited amount of storage for the Stack.
	- Using a __Node__ class and manually creating connections by maintaining a reference to the __'top'__ of the stack.
		- This approach uses __O(n)__ space.
- This __`getMax()`__ member function can be approached in several ways as well:
	- Modifying the traditional `push` and `pop` methods to keep track on the maximum value so far.
	- Use a __`maxStack`__ instance variable, and each time you push a number, you check if it's >= the peek on `maxStack`; if so, push it onto both `maxStack` and the actual stack. Then when popping, check if equal to max on `maxStack`, and if so, also pop `maxStack`.
		- This solution takes __O(1)__ time to both maintain and retrieve the maximum value.
	- Traversing the entire Stack to calculate the maximum value.
		- This solution takes __O(n)__ time.
		- If the candidate is considering this approach, comment on the fact that there might be a more efficient way to calculate the maximum value, but avoid providing specific details.
 <br>
## Structure
Familiarize yourself with the grading rubric, so you know how to score the interview.

Look for effective problem solving, efficient use of time, and effective communication with the whiteboard space available. <br>

Every solution might look a little different, but the candidate should be able to test their solution with different inputs to verify correctness. <br>

Assign points for each item on the Rubric, according to how well the candidate executed on that skill. <br>

Add up all the points at the end, and record the total at the bottom of the page. <br>

## Documentation
Record detailed notes on the rubric, to share with the candidate when the interview is complete. <br>

[Whiteboard rubric on me here](./assets/2020-07-20_cc_14_WB-Rubric.png) <br>
