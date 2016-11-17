#Example "Big Table" Demo

This is an example of how "big table" might be implemented using Python
data structures

It will ask a series of questions to collect data from the user. Then it
will display the results to the user by dumping the Python data structure
to STDOUT, followed by a very crude tabular representation of the content
of the table.


```
Enter row-id, or just hit ENTER to stop adding data: 
Enter column name (just press ENTER to end row data entry): 
Enter column value (just press ENTER for no value): 
Enter column name (just press ENTER to end row data entry): 
Enter column value (just press ENTER for no value): 
Enter column name (just press ENTER to end row data entry): 
Completed row 'Test1'
Enter row-id, or just hit ENTER to stop adding data: 
Enter column name (just press ENTER to end row data entry): 
Enter column value (just press ENTER for no value): 
Enter column name (just press ENTER to end row data entry): 
Enter column value (just press ENTER for no value): 
Enter column name (just press ENTER to end row data entry): 
Enter column value (just press ENTER for no value): 
Enter column name (just press ENTER to end row data entry): 
Enter column value (just press ENTER for no value): 
Enter column name (just press ENTER to end row data entry): 
Completed row 'Test2'
Enter row-id, or just hit ENTER to stop adding data: 
Nothing entered, ending data entry loop
{'Test1': {'cf:a': '12', 'cf:b': '77', 'row-id': 'Test1'},
 'Test2': {'cr:1': '88', 'cf:c': '77', 'cf:b': '25', 'row-id': 'Test2', 'cf:d': '32'}}

row-id	cf:a	cf:b	cf:c	cf:d	cr:1
Test1	12	77				
Test2		25	77	32	88	
```
