/* Fixed versions of memory_bugs.c. Diff the two files: `diff memory_bugs.c memory_bugs_fixed.c` */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void heap_overflow(void) {
    const char *src = "this string is far too long";
    size_t n = strlen(src) + 1;
    char *buf = malloc(n);                          /* FIX: size from the data */
    if (!buf) return;
    memcpy(buf, src, n);
    printf("%s\n", buf);
    free(buf);
}

static void use_after_free(void) {
    int *p = malloc(sizeof *p);
    if (!p) return;
    *p = 42;
    printf("%d\n", *p);                             /* FIX: use before free */
    free(p);
    p = NULL;                                       /* FIX: no dangling pointer */
}

static void leak(void) {
    for (int i = 0; i < 3; i++) {
        char *s = malloc(100);
        if (!s) return;
        snprintf(s, 100, "item %d", i);
        puts(s);
        free(s);                                    /* FIX: release each allocation */
    }
}

static void uninit(void) {
    int total = 0;                                  /* FIX: initialise */
    for (int i = 0; i < 5; i++) total += i;
    if (total > 5) puts("big"); else puts("small");
}

static void double_free(void) {
    char *p = malloc(16);
    free(p);
    p = NULL;                                       /* FIX: free(NULL) is a safe no-op */
    free(p);
}

static void stack_overflow(const char *input) {
    char name[8];
    snprintf(name, sizeof name, "%s", input);       /* FIX: bounded copy (truncates safely) */
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
