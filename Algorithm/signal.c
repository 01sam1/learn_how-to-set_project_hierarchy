#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<unistd.h>
#include<time.h>
#include<sys/wait.h>    

int main()
{
printf("run first process");
int pid =fork();
if(pid==-1){
    return 1;
}
if(pid==0){
    while(1){
        usleep(600000); 
        printf("I am on printing mood");

    }
}
else{
    sleep(2);
    kill(pid,SIGNKILL);
    wait(NULL);
}

return 0;
}