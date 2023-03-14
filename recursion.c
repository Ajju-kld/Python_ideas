#include<stdio.h>
void reverse_string(char *a){
if (*a == '\0')
{
return ;
}
reverse_string(a+1);
printf("%c",*a);
}

void main(){
  char s[100];
   printf("enter the string to be reversed");
   scanf("%s",s);
   printf("string before reversing %s \n",s);
   printf("after the reversing :  ");
   reverse_string(s);
  printf("\n");



}