#include<stdio.h>
#include<conio.h>
int fact(int y)
{
  if(y==1)
  return(1)
else 
return (y*fact (y-1))
}
main()
{
    int num ,f ;
    clrscr()
    printf("enter a number ");
    scanf("%d,&num")
    f=fact(num);
    printf("factorial is %d",f);
    return(0)
}

