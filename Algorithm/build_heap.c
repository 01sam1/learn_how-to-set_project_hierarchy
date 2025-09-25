#include<stdio.h>
#include<math.h>
void build_heap(int*,int,int);
void make_heap(int*,int);
int extract_key(int*,int*);
int main()
{
    int ar[]={0,10,1,50,48,57,32,98};
    int length =8;
    // build_heap(ar,1,length);
    // make_heap(ar,length-1,length);
    make_heap(ar,length);
    int extracted_key =extract_key(ar,&length);
    printf("%d  %d\n",extracted_key,length);
    extracted_key =extract_key(ar,&length);
    printf("%d  %d\n",extracted_key,length);
    for (int i = 0; i < length; i++)
    {
        printf("%d  ",ar[i]);
    }
    

return 0;
}

void build_heap(int *ar,int lg,int length){
    // printf("hello akshit");
    // length =length-1;
    int l=2*lg;
    int r=2*lg+1,temp_lg=lg;
    if (r<length && *(ar+r)> *(ar+temp_lg))
    {
        temp_lg = r;
    }
    if (l<length && *(ar+l)> *(ar+temp_lg))
    {
        temp_lg = l;
    }

    if (temp_lg!=lg)
    {
        l = ar[lg];
        ar[lg] =ar[temp_lg];
        ar[temp_lg] =l;
        lg=temp_lg;
        build_heap(ar,lg,length);
    }
    
}

void make_heap(int *ar,int length){
    int i;
    // length-=1;
   for (i=(int)floor((length-1)/2); i > 0; i--)
   {
    /* code */
    printf("%d\n",i);
    build_heap(ar,i,length);
   }
   
}

int extract_key(int *ar,int* length){
    if (*length<=1){
        printf("already heap\n");
        return 0;
    }
    int key=ar[1];
    ar[1]=ar[*length-1];
    build_heap(ar,1,*length);
    *length =*length-1;
    return key;


}