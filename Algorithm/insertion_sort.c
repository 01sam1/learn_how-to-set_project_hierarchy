#include<stdio.h>

int insertion_sort(int *ar,int length){
    printf("start algorithm\n");
    int change;
    for (int i = 1; i < length; i++)
    {
        // printf("running");
        /* code */
        int key =ar[i];
        int j= i-1;
        while (j>=0 && ar[j]>key)
        {
            /* code */
            ar[j+1]=ar[j];
            j--;
            change=1;

        }
        if(change){
        j++;
        ar[j] =key;
        change=0;
        }
        
    }
    
return 1;
}

// int array_size(int ar[]){

//     // printf("%d\n",*(ar));
//     // printf("%d\n",(*ar+1));
//     // // printf("%d\n",(ar)-(ar+1));
//     // printf("%d",sizeof(ar));
//     return (sizeof(ar)/sizeof(ar[0]));
// }

int main()
{
int a[]={1,2,3,4,5,6,7,8};
int length = sizeof(a)/sizeof(a[0]);
// printf("%d",length);
insertion_sort(a,length);
for (int i = 0; i < length; i++)
{
    printf("%d  ",a[i]);
}



return 0;
}