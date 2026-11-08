# bubble_sort.asm - sorts a word array in place and prints it.
# Concepts: nested loops, array indexing, swapping through registers, printing with syscall 1 / 11.
# Expected output: 1 2 3 5 8 9

        .data
arr:    .word 5, 2, 9, 1, 8, 3
n:      .word 6
sp_:    .asciiz " "
nl:     .asciiz "\n"

        .text
        .globl main
main:
        la   $s0, arr
        la   $t0, n
        lw   $s1, 0($t0)        # s1 = n
        li   $s2, 0             # i = 0
outer:
        addi $t0, $s1, -1
        bge  $s2, $t0, print    # for i in 0..n-2
        li   $s3, 0             # j = 0
        sub  $s4, $t0, $s2      # limit = n-1-i
inner:
        bge  $s3, $s4, next_i
        sll  $t1, $s3, 2
        add  $t1, $s0, $t1      # &arr[j]
        lw   $t2, 0($t1)        # arr[j]
        lw   $t3, 4($t1)        # arr[j+1]
        ble  $t2, $t3, no_swap
        sw   $t3, 0($t1)
        sw   $t2, 4($t1)
no_swap:
        addi $s3, $s3, 1
        j    inner
next_i:
        addi $s2, $s2, 1
        j    outer
print:
        li   $s2, 0
ploop:
        bge  $s2, $s1, end
        sll  $t1, $s2, 2
        add  $t1, $s0, $t1
        lw   $a0, 0($t1)
        li   $v0, 1
        syscall
        beq  $s2, $t0, noSpace  # no trailing space after the last element (t0 = n-1)
        li   $v0, 4
        la   $a0, sp_
        syscall
noSpace:
        addi $s2, $s2, 1
        j    ploop
end:
        li   $v0, 4
        la   $a0, nl
        syscall
        li   $v0, 10
        syscall
