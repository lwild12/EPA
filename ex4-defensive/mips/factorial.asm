# factorial.asm - recursive factorial showing the stack frame and calling convention.
# Concepts: jal / jr $ra, saving $ra and an argument on the stack, $sp arithmetic, $a0 argument, $v0 result
# Expected output: 6! = 720

        .data
msg:    .asciiz "6! = "
nl:     .asciiz "\n"

        .text
        .globl main
main:
        li   $a0, 6
        jal  fact               # v0 = fact(6)
        move $s0, $v0
        li   $v0, 4
        la   $a0, msg
        syscall
        li   $v0, 1
        move $a0, $s0
        syscall
        li   $v0, 4
        la   $a0, nl
        syscall
        li   $v0, 10
        syscall

# int fact(int n): if (n <= 1) return 1; return n * fact(n-1);
fact:
        addi $sp, $sp, -8       # allocate frame: [sp+4]=ra, [sp+0]=n
        sw   $ra, 4($sp)
        sw   $a0, 0($sp)
        li   $t0, 1
        ble  $a0, $t0, base
        addi $a0, $a0, -1
        jal  fact               # v0 = fact(n-1)
        lw   $a0, 0($sp)        # restore n
        mul  $v0, $a0, $v0      # n * fact(n-1)
        j    epilogue
base:
        li   $v0, 1
epilogue:
        lw   $ra, 4($sp)
        addi $sp, $sp, 8        # free frame
        jr   $ra
