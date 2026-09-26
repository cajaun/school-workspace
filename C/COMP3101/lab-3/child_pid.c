#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
    pid_t process_id;

    printf("\nThis line is printed before the call to fork()\n");
    fflush(stdout);

    process_id = fork();
    if (process_id < 0) {
        perror("fork");
        return 1;
    }

    if (process_id == 0) {
        printf("\nThis is the child process saying hello!\n");
        printf("%d is pid of this child\n", (int)getpid());
    } else {
        printf("\nThis is the parent process. The child was created with process id: %d\n",
               (int)process_id);
        printf("%d is pid of this parent\n", (int)getpid());
    }

    return 0;
}
