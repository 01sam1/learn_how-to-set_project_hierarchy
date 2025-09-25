#include<stdio.h>
#include<string.h>
#include<conio.h>

char* (check)(char* ip,char cmp,int accept,int* a_var,int repeat){
    if(repeat==0 || ip==NULL ||*ip=='\0') return ip;
    int temp_r=0;//use for limited repetition
    char al;
        if(repeat==-1 ){
            int cou=0;
            while (1)
            {
                al=*(ip+cou++);
                if (cmp!=al)
                {  
                    if (al!='\0')
                    {
                        // printf("%c\n",al);
                        return ip+--cou;
                    }
                    *a_var=accept; 
                    return ip+--cou;
                }
            }
        }
        else{
        // int cou=0;
        while (temp_r<repeat)
        {
            al=*(ip+temp_r++);
                if (cmp!=al)
                {  
                    *a_var=0;
                    return NULL;
                }
        }
        *a_var=accept;
        if(*(ip+temp_r)!='\0' && accept==1){
            *a_var=0;
            // printf("\n%d",*(ip+temp_r));
            return ip+temp_r;    
        }
        return ip+temp_r;
        }
        
}
void remove_new_line(char* str){
    int length =strlen(str);
    if (str[length-1]=='\n')
    {
        // printf("executed");
        str[length-1]='\0';
    }
    
    // printf("\n%d",length);
}

int automata()
{
    char str[100],*ch;
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    // int length =strlen(str);
    remove_new_line(str);
    // printf("%d",str[3]);
    int accept=0;
    int poi=0;
    // while (poi<length);
    // {
    //     //something happens
    //     ch=str[poi];
    //     if(accept!=0){
    //         exit(0);
    //     }
    //     accept =check(ch,'a',0);
    // }
    ch=check(str,'a',0,&accept,-1);
    if (ch==NULL)
    {
        printf("entered string is not in language\n");
    }
    // printf("%c",*ch);
    ch=check(ch,'b',1,&accept,2);
    ch=check(ch,'c',1,&accept,-1);
    // if (ch==NULL)
    // {
    //     printf("entered string is not in language\n");
    // }

    // final step
    if(accept==1){
        printf("entered string is in language\n");
    }
    else{
        printf("entered string is not in language\n");
    }
    
    

    // algorithm

    // printf("%s",str);


    return 0;
}

int main(){
    while (1)
    {
        automata();
    }
    
}