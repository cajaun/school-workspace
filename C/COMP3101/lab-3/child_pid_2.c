#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(void)
{
    pid_t process_id = fork();

    if (process_id < 0) {
        perror("fork");
        return 1;
    }

    /* parent and child receive different return values from fork */
    printf("fork returned %d\n", (int)process_id);
    return 0;
}
