CFLAGS = -g -O0 -Wall -Wextra

all: memory_bugs memory_bugs_fixed race race_fixed

memory_bugs: memory_bugs.c
	$(CC) $(CFLAGS) -fno-stack-protector -o $@ $<

memory_bugs_fixed: memory_bugs_fixed.c
	$(CC) $(CFLAGS) -o $@ $<

race: race.c
	$(CC) $(CFLAGS) -pthread -o $@ $<

race_fixed: race.c
	$(CC) $(CFLAGS) -pthread -DFIXED -o $@ $<

tsan: race.c
	$(CC) $(CFLAGS) -pthread -fsanitize=thread -o race_tsan $<

asan: memory_bugs.c
	$(CC) $(CFLAGS) -fsanitize=address,undefined -o memory_bugs_asan $<

clean:
	rm -f memory_bugs memory_bugs_fixed race race_fixed race_tsan memory_bugs_asan

# GDB cheat sheet:
#   gdb ./memory_bugs        (gdb) run 2      (gdb) bt      (gdb) frame 1     (gdb) print *p
#   break use_after_free     next / step      watch counter     info locals      x/16xb buf
#   Valgrind: valgrind --leak-check=full --track-origins=yes ./memory_bugs 4
