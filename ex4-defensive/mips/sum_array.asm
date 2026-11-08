# sum_array.asm - sums a word array and prints the result (MARS / SPIM syscalls).
# Concepts: .data, la, lw with offset, loop with a counter, syscall 1 (print int), syscall 4 (print string), syscall 10 (exit)
# Expected output: Sum = 150

        .data
nums:   .word 10, 20, 30, 40, 50
count:  .word 5
msg:    .asciiz "Sum = "
nl:     .asciiz "\n"

        .text
        .globl main
main:
        la   $t0, nums          # t0 = address of array
        la   $t1, count
        lw   $t1, 0($t1)        # t1 = number of elements
        li   $t2, 0             # t2 = running sum
        li   $t3, 0             # t3 = index i
loop:
        bge  $t3, $t1, done     # while (i < count)
        sll  $t4, $t3, 2        # byte offset = i * 4
        add  $t4, $t0, $t4      # address of nums[i]
        lw   $t5, 0($t4)
        add  $t2, $t2, $t5      # sum += nums[i]
        addi $t3, $t3, 1        # i++
        j    loop
done:
        li   $v0, 4             # print "Sum = "
        la   $a0, msg
        syscall
        li   $v0, 1             # print integer
        move $a0, $t2
        syscall
        li   $v0, 4
        la   $a0, nl
        syscall
        li   $v0, 10            # exit
        syscall
