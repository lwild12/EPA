# size_check.asm - defensive length check written directly in assembler.
# Mirrors the first check in sync_validator.py: reject a request body that is empty, negative or over 65536 bytes.
# Concepts: function with jal/jr, arguments in $a0, result in $v0, reject-by-default, checking BOTH ends of the range
# (a negative length would sneak past a one-sided "length > max" test, a classic integer bug).
# Expected output:
#   -1 REJECT
#   0 REJECT
#   1 ACCEPT
#   65536 ACCEPT
#   65537 REJECT
#   2147483647 REJECT

        .data
lens:   .word -1, 0, 1, 65536, 65537, 2147483647
count:  .word 6
sp1:    .asciiz " "
acc:    .asciiz "ACCEPT\n"
rej:    .asciiz "REJECT\n"

        .text
        .globl main
main:
        la   $s0, lens          # s0 = address of the list of lengths
        la   $t0, count
        lw   $s1, 0($t0)        # s1 = how many
        li   $s2, 0             # s2 = index i
next:
        bge  $s2, $s1, finish   # while (i < count)
        sll  $t1, $s2, 2        # byte offset = i * 4
        add  $t1, $s0, $t1
        lw   $s3, 0($t1)        # s3 = lens[i]

        li   $v0, 1             # print the length
        move $a0, $s3
        syscall
        li   $v0, 4             # print a space
        la   $a0, sp1
        syscall

        move $a0, $s3
        jal  check_size         # v0 = 1 accept, 0 reject
        beqz $v0, say_reject
        li   $v0, 4
        la   $a0, acc
        syscall
        j    advance
say_reject:
        li   $v0, 4
        la   $a0, rej
        syscall
advance:
        addi $s2, $s2, 1        # i++
        j    next
finish:
        li   $v0, 10            # exit
        syscall

# check_size(length) -> 1 if 1 <= length <= 65536, else 0. Default is reject.
check_size:
        li   $v0, 0             # assume reject
        blez $a0, cs_done       # zero or negative: reject
        li   $t0, 65536
        bgt  $a0, $t0, cs_done  # too large: reject
        li   $v0, 1             # only now accept
cs_done:
        jr   $ra
