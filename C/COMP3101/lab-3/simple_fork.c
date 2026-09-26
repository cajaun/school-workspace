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

    printf("This line is printed after the call to fork()\n");
    fflush(stdout);
    return 0;
}
