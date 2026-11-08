# safe_copy.asm - bounds-checked string copy (the defensive-programming version of strcpy).
# Concepts: lb/sb, byte loops, checking length against buffer size BEFORE copying, always NUL-terminating.
# The destination buffer is 8 bytes. The source is 20 chars, so the copy is truncated to 7 chars + NUL.
# Expected output:
#   copied: AAAAAAA
#   truncated: 1

        .data
src:    .asciiz "AAAAAAAAAAAAAAAAAAAA"
dst:    .space 8
guard:  .asciiz "OK"           # sits after dst; must still read "OK" after the copy (no overflow)
m1:     .asciiz "copied: "
m2:     .asciiz "\ntruncated: "
m3:     .asciiz "\nguard: "
nl:     .asciiz "\n"

        .text
        .globl main
main:
        la   $a0, dst
        la   $a1, src
        li   $a2, 8             # size of destination buffer
        jal  safe_strcpy        # v0 = 1 if truncated, 0 otherwise
        move $s0, $v0

        li   $v0, 4
        la   $a0, m1
        syscall
        li   $v0, 4
        la   $a0, dst
        syscall
        li   $v0, 4
        la   $a0, m2
        syscall
        li   $v0, 1
        move $a0, $s0
        syscall
        li   $v0, 4
        la   $a0, m3
        syscall
        li   $v0, 4
        la   $a0, guard
        syscall
        li   $v0, 4
        la   $a0, nl
        syscall
        li   $v0, 10
        syscall

# int safe_strcpy(char *dst, const char *src, int size)
# Copies at most size-1 bytes, always terminates, returns 1 if the source was truncated.
safe_strcpy:
        blez $a2, ss_fail       # size <= 0: nothing safe to do
        addi $t0, $a2, -1       # t0 = max chars to copy
        li   $t1, 0             # i = 0
ss_loop:
        beq  $t1, $t0, ss_limit # reached the limit
        add  $t2, $a1, $t1
        lb   $t3, 0($t2)        # c = src[i]
        add  $t4, $a0, $t1
        sb   $t3, 0($t4)        # dst[i] = c
        beqz $t3, ss_done_ok    # copied the terminator: finished without truncation
        addi $t1, $t1, 1
        j    ss_loop
ss_limit:
        add  $t4, $a0, $t1
        sb   $zero, 0($t4)      # force NUL terminator
        add  $t2, $a1, $t1
        lb   $t3, 0($t2)        # was there more source left?
        beqz $t3, ss_done_ok
        li   $v0, 1             # truncated
        jr   $ra
ss_done_ok:
        li   $v0, 0
        jr   $ra
ss_fail:
        li   $v0, 1
        jr   $ra
