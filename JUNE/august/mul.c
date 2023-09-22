// // #include<stdio.h>
// // int main()
// // {
// //     int n, i, value = 0,sum = 0;
// //     printf("enter the number");
// //     scanf("%d", &n);
// //     for(i=1;i<=10;i++)
// //     {
// //         value = n * i;
// //         printf("%d\n", value);
// //         sum += value;
// //     }
// //     printf("%d", sum);
// //     return 0;
// // }


// #include<stdio.h>
// int main()
// {
//     int i, d, n, rev, f, l;
//     printf("enter the start");
//     scanf("%d", &f);
//     printf("enter the end");
//     scanf("%d", &l);

//     for(i=f;i<=l;i++)
//     {
//         rev = 0;
//         n = i;
//         while (n !=0 )
//         {
//             d = n%10;
//             rev = rev * 10 + d;
//             n = n / 10;
//         }

//         if (i == rev)
//         {
//             printf("%d,", i);
//         }
//     }
//     return 0;
// }   
