/* Data race demo for parallel debugging (EPA Ex4).
 * Build buggy:  gcc -g -O0 -pthread race.c -o race
 * Detect:       gcc -g -O0 -pthread -fsanitize=thread race.c -o race_tsan && ./race_tsan
 *               valgrind --tool=helgrind ./race
 * Fix:          compile with -DFIXED to use a mutex.
 * Expect: buggy run often prints less than 400000.
 */
#include <pthread.h>
#include <stdio.h>

#define THREADS 4
#define ITERS 100000

static long counter = 0;
static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

static void *worker(void *arg) {
    (void)arg;
    for (int i = 0; i < ITERS; i++) {
#ifdef FIXED
        pthread_mutex_lock(&lock);
        counter++;
        pthread_mutex_unlock(&lock);
#else
        counter++;                  /* BUG: read-modify-write is not atomic */
#endif
    }
    return NULL;
}

int main(void) {
    pthread_t t[THREADS];
    for (int i = 0; i < THREADS; i++) pthread_create(&t[i], NULL, worker, NULL);
    for (int i = 0; i < THREADS; i++) pthread_join(t[i], NULL);
    printf("counter = %ld (expected %d)\n", counter, THREADS * ITERS);
    return counter == (long)THREADS * ITERS ? 0 : 1;
}
