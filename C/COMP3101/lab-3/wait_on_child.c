#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main(void)
{
    pid_t process_id = fork();

    if (process_id < 0) {
        perror("fork");
        return 1;
    }

    if (process_id == 0) {
        for (int index = 0; index < 100000; index++) {
            printf("Child - %d\n", index);
        }
    } else {
        for (int index = 0; index < 100000; index++) {
            printf("Parent - %d\n", index);
        }
    }

    return 0;
}
