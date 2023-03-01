Problem Statement
Alexa will turn on the air conditioner if, and only if, the temperature of the room is 30 degrees Celsius or above. The current temperature of the room is X degrees Celsius. Will she turn on the air conditioner?
Input
The input consists of a single integer X.

Constraints
−40≤X≤40
X is an integer.
Output
Print Yes if you will turn on the air conditioner; print No otherwise.
Example
Sample Input 1
25
Sample Output 1
No

Sample Input 2
30
Sample Output 2
Yes

#include <stdio.h> // header file for Standard Input Output
#include <stdlib.h> // header file for Standard Library

int main() {
    int x;
    scanf("%d",&x);
    if(x>=30){printf("Yes");}
    else{printf("No");}
    return 0;
}