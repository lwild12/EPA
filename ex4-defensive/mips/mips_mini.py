#!/usr/bin/env python3
"""Tiny MIPS32 interpreter for the instruction subset used in these exercises.

It exists so the .asm files in this folder could be tested without SPIM/MARS. It is NOT a replacement for
MARS or SPIM (the EPA machine will have its own). Differences: no delay slots, no .macro, no floats, no file
syscalls; syscalls supported: 1 print int, 4 print string, 5 read int, 10 exit, 11 print char.
Usage: python3 mips_mini.py program.asm
"""
import re
import sys

REGS = {"zero": 0, "at": 1, "v0": 2, "v1": 3, "a0": 4, "a1": 5, "a2": 6, "a3": 7,
        **{f"t{i}": 8 + i for i in range(8)}, **{f"s{i}": 16 + i for i in range(8)},
        "t8": 24, "t9": 25, "k0": 26, "k1": 27, "gp": 28, "sp": 29, "fp": 30, "ra": 31}
DATA_BASE, STACK_TOP = 0x10010000, 0x7FFFEFFC
M32 = 0xFFFFFFFF


def s32(x):
    x &= M32
    return x - (1 << 32) if x & 0x80000000 else x


class MIPS:
    def __init__(self, src, stdin=""):
        self.mem = {}
        self.reg = [0] * 32
        self.reg[29] = STACK_TOP
        self.labels = {}
        self.prog = []
        self.out = []
        self.stdin = [int(x) for x in stdin.split()]
        self.halted = False
        self._load(src)

    # ---- assembling ----
    def _load(self, src):
        section, dptr = "text", DATA_BASE
        for raw in src.splitlines():
            line = raw.split("#")[0] if '"' not in raw else self._strip_comment(raw)
            line = line.strip()
            while True:
                m = re.match(r"^([A-Za-z_.$][\w.$]*):\s*(.*)$", line)
                if not m:
                    break
                lab, line = m.group(1), m.group(2)
                self.labels[lab] = dptr if section == "data" else len(self.prog)
            if not line:
                continue
            if line.startswith("."):
                d, _, rest = line.partition(" ")
                rest = rest.strip()
                if d == ".data":
                    section = "data"
                elif d == ".text":
                    section = "text"
                elif d == ".globl":
                    pass
                elif d == ".word":
                    dptr += (-dptr) % 4
                    for v in rest.split(","):
                        self._w32(dptr, int(v.strip(), 0))
                        dptr += 4
                elif d == ".byte":
                    for v in rest.split(","):
                        self.mem[dptr] = int(v.strip(), 0) & 0xFF
                        dptr += 1
                elif d in (".asciiz", ".ascii"):
                    s = bytes(rest[1:-1], "utf-8").decode("unicode_escape")
                    for ch in s:
                        self.mem[dptr] = ord(ch)
                        dptr += 1
                    if d == ".asciiz":
                        self.mem[dptr] = 0
                        dptr += 1
                elif d == ".space":
                    for _ in range(int(rest, 0)):
                        self.mem[dptr] = 0
                        dptr += 1
                else:
                    raise ValueError(f"unsupported directive {d}")
                continue
            op, _, args = line.partition(" ")
            self.prog.append((op.lower(), [a.strip() for a in args.split(",")] if args.strip() else []))

    @staticmethod
    def _strip_comment(raw):
        out, inq = [], False
        for ch in raw:
            if ch == '"':
                inq = not inq
            if ch == "#" and not inq:
                break
            out.append(ch)
        return "".join(out)

    # ---- memory ----
    def _w32(self, a, v):
        for i in range(4):
            self.mem[a + i] = (v >> (8 * i)) & 0xFF

    def _r32(self, a):
        return s32(sum(self.mem.get(a + i, 0) << (8 * i) for i in range(4)))

    # ---- helpers ----
    def r(self, name):
        return self.reg[REGS[name.lstrip("$")] if not name.lstrip("$").isdigit() else int(name.lstrip("$"))]

    def w(self, name, v):
        i = REGS[name.lstrip("$")]
        if i:
            self.reg[i] = s32(v)

    def val(self, tok):
        tok = tok.strip()
        if tok.startswith("$"):
            return self.r(tok)
        if tok in self.labels:
            return self.labels[tok]
        return int(tok, 0)

    def addr(self, tok):
        m = re.match(r"^(-?\w*)\((\$\w+)\)$", tok.strip())
        off = int(m.group(1), 0) if m.group(1) else 0
        return (self.r(m.group(2)) + off) & M32

    # ---- execution ----
    def run(self, max_steps=2_000_000):
        pc = self.labels.get("main", 0)
        steps = 0
        while not self.halted:
            if pc >= len(self.prog):
                raise RuntimeError("fell off the end of the program (missing exit syscall?)")
            steps += 1
            if steps > max_steps:
                raise RuntimeError("step limit exceeded (infinite loop?)")
            op, a = self.prog[pc]
            nxt = pc + 1
            R = self.r
            if op == "li": self.w(a[0], int(a[1], 0))
            elif op == "la": self.w(a[0], self.labels[a[1]])
            elif op == "move": self.w(a[0], R(a[1]))
            elif op in ("add", "addu"): self.w(a[0], R(a[1]) + R(a[2]))
            elif op in ("addi", "addiu"): self.w(a[0], R(a[1]) + int(a[2], 0))
            elif op in ("sub", "subu"): self.w(a[0], R(a[1]) - R(a[2]))
            elif op == "mul": self.w(a[0], R(a[1]) * R(a[2]))
            elif op == "and": self.w(a[0], R(a[1]) & R(a[2]))
            elif op == "or": self.w(a[0], R(a[1]) | R(a[2]))
            elif op == "andi": self.w(a[0], R(a[1]) & int(a[2], 0))
            elif op == "ori": self.w(a[0], R(a[1]) | int(a[2], 0))
            elif op == "sll": self.w(a[0], (R(a[1]) << int(a[2], 0)) & M32)
            elif op == "srl": self.w(a[0], (R(a[1]) & M32) >> int(a[2], 0))
            elif op == "slt": self.w(a[0], int(R(a[1]) < R(a[2])))
            elif op == "slti": self.w(a[0], int(R(a[1]) < int(a[2], 0)))
            elif op == "lw": self.w(a[0], self._r32(self.addr(a[1])))
            elif op == "sw": self._w32(self.addr(a[1]), R(a[0]) & M32)
            elif op == "lb":
                b = self.mem.get(self.addr(a[1]), 0)
                self.w(a[0], b - 256 if b > 127 else b)
            elif op == "lbu": self.w(a[0], self.mem.get(self.addr(a[1]), 0))
            elif op == "sb": self.mem[self.addr(a[1])] = R(a[0]) & 0xFF
            elif op in ("beq", "bne", "blt", "bgt", "ble", "bge"):
                x, y = R(a[0]), self.val(a[1])
                t = {"beq": x == y, "bne": x != y, "blt": x < y, "bgt": x > y, "ble": x <= y, "bge": x >= y}[op]
                if t: nxt = self.labels[a[2]]
            elif op in ("beqz", "bnez", "blez", "bgtz", "bltz", "bgez"):
                x = R(a[0])
                t = {"beqz": x == 0, "bnez": x != 0, "blez": x <= 0, "bgtz": x > 0, "bltz": x < 0, "bgez": x >= 0}[op]
                if t: nxt = self.labels[a[1]]
            elif op == "j": nxt = self.labels[a[0]]
            elif op == "jal":
                self.reg[31] = pc + 1
                nxt = self.labels[a[0]]
            elif op == "jr": nxt = R(a[0])
            elif op == "nop": pass
            elif op == "syscall": self._syscall()
            else: raise ValueError(f"unsupported instruction: {op} {a}")
            pc = nxt
        return "".join(self.out)

    def _syscall(self):
        v = self.reg[2]
        a0 = self.reg[4]
        if v == 1: self.out.append(str(a0))
        elif v == 4:
            p, s = a0 & M32, []
            while self.mem.get(p, 0):
                s.append(chr(self.mem[p]))
                p += 1
            self.out.append("".join(s))
        elif v == 5: self.reg[2] = self.stdin.pop(0)
        elif v == 10: self.halted = True
        elif v == 11: self.out.append(chr(a0 & 0xFF))
        else: raise ValueError(f"unsupported syscall {v}")


if __name__ == "__main__":
    print(MIPS(open(sys.argv[1]).read()).run(), end="")
