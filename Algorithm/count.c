#include<stdio.h>
#include<stdlib.h>
int min_max(int *ar,int len,int* a ,int *b){
    *a=*ar; //for max element
    *b=*ar; //for min element
    for (int i = 1; i < len; i++)
    {
       if (ar[i]> *a)
       {
            *a=ar[i];
       }

       if (ar[i]< *b)
       {//for min element
            *b=ar[i];
       }
        
    }
    return 1;
    

}
int count_sort(int *ar,int len){
    int max,min,offset;
    min_max(ar,len,&max,&min);
    int *bucket;
    printf("%d %d\n",max,min);

    if(min<0 || max>100){
        printf("this algorithm is not work for element range more than 100\n");
        return 0;
    }
    bucket =(int*)calloc(sizeof(int),(max-min+1));
    printf("\nspace allocated\n");
    for (int i = 0; i < len; i++)
    {
        *(bucket+(ar[i]-min))+=1;
    }


    // for (int i = 0; i<=(max-min); i++)
    // {
    //     printf("%d ",*(bucket+i));
    // }
    int j=0;
    for (int i = 0;  i<=(max-min); i++)
    {
        while (*(bucket+i)!=0)
        {
            ar[j]=min+i;
            j++;
            bucket[i]-=1;

        }
        
    }
    
    free(bucket);


}

int main()
{
    int a[]={2,2,3,4,1,5,1,5};
    int length=8;
    count_sort(a,length);
    printf("\n");
    for (int i = 0; i <length; i++)
    {
        printf("%d ",a[i]);
    }
    return 0;
}