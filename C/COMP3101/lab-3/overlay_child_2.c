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
        printf("\nThis is the child process. About to run an 'ps' command.\n");
        fflush(stdout);
        execl("/bin/ps", "ps", "au", "-u", (char *)NULL);
        perror("execl");
        return 1;
    }

    /* the parent replaces its code with ls */
    execl("/bin/ls", "ls", "-l", (char *)NULL);
    perror("execl");
    return 1;
}
