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

        /* the child replaces its code with ps */
        execl("/bin/ps", "ps", "au", "-u", (char *)NULL);
        perror("execl");
        return 1;
    }

    printf("\nThis is the parent process. The child was created with process id: %d\n",
           (int)process_id);
    return 0;
}
