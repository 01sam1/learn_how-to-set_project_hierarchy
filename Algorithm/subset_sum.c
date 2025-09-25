#include<stdio.h>
int Sum(int *a,int len,int s,int sum){
    if (len<=0 ||sum<=0)
    {
        if (sum==0)
        {
            return 1;
        }
        
        return 0;
    }
    Sum(a,len-1,s,sum);
    Sum(a,len-1,s,sum-a[len-1]);
    
    
    
}
int main()
{
int a[]={1,2};
int len =2;
int e_sum=1;
int ans =Sum(a,len,e_sum,e_sum); 
printf("%d",ans);

return 0;
}