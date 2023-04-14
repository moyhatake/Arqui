#include <stdio.h>

int main() {
   int n, i, t1 = 0, t2 = 1, nextVal;
   printf("Fibonacci numbers to show: ");
   scanf("%d", &n);
   if (n <= 0) printf("Must be a positive integer");
   else {
       printf("Fibonacci series:\n");
       for (i = 1; i <= n; ++i) {
            printf("%d ", t1);
            nextVal = t1 + t2;
            t1 = t2;
            t2 = nextVal;
        }
   }
   printf("\n");
   return 0;
}
