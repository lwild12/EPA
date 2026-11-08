/* Deliberately buggy program for practising GDB and Valgrind (EPA Ex4).
 * Build: make memory_bugs       Run under Valgrind: valgrind --leak-check=full ./memory_bugs <n>
 * Pick a bug with the argument:
 *   1 heap buffer overflow   2 use-after-free   3 memory leak
 *   4 uninitialised read     5 double free      6 stack overflow (strcpy)
 * For each: (a) reproduce, (b) find the line with Valgrind/GDB, (c) fix it, (d) re-run clean.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void heap_overflow(void) {
    char *buf = malloc(8);
    strcpy(buf, "this string is far too long");   /* BUG: writes past the 8-byte block */
    printf("%s\n", buf);
    free(buf);
}

static void use_after_free(void) {
    int *p = malloc(sizeof *p);
    *p = 42;
    free(p);
    printf("%d\n", *p);                            /* BUG: reads freed memory */
}

static void leak(void) {
    for (int i = 0; i < 3; i++) {
        char *s = malloc(100);                      /* BUG: never freed */
        snprintf(s, 100, "item %d", i);
        puts(s);
    }
}

static void uninit(void) {
    int total;                                      /* BUG: never initialised */
    for (int i = 0; i < 5; i++) total += i;
    if (total > 5) puts("big"); else puts("small"); /* conditional jump depends on uninit value */
}

static void double_free(void) {
    char *p = malloc(16);
    free(p);
    free(p);                                        /* BUG: second free of same pointer */
}

static void stack_overflow(const char *input) {
    char name[8];
    strcpy(name, input);                            /* BUG: no bounds check */
    printf("hello %s\n", name);
}

int main(int argc, char **argv) {
    int which = argc > 1 ? atoi(argv[1]) : 0;
    switch (which) {
        case 1: heap_overflow(); break;
        case 2: use_after_free(); break;
        case 3: leak(); break;
        case 4: uninit(); break;
        case 5: double_free(); break;
        case 6: stack_overflow("AAAAAAAAAAAAAAAAAAAAAAAA"); break;
        default: fprintf(stderr, "usage: %s <1-6>\n", argv[0]); return 2;
    }
    return 0;
}
