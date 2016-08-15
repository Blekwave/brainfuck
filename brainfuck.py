#!/usr/bin/env python3

import sys


def bracket_matches(program):
    """Returns a dict with positions for matching brackets.

    e.g.:
    >>> bracket_matches("++[-,.[+>>]]")
    {
        2: 11,
        6: 10
    }
    """
    opening_pos = []
    matches = {}
    for pos, instr in enumerate(program):
        if instr == "[":
            opening_pos.append(pos)
        if instr == "]":
            opening = opening_pos.pop()
            matches[opening] = pos
            matches[pos] = opening
    return matches


def run_program(program, memory=None, debug_mode=False):
    """Runs a Brainfuck program.

    Parameters:
    - program: the program itself.
    - debug_mode: when enabled, read values will be printed to stdout.
    - memory: initial memory array. (if None, a 30000-large array of
              zeroes is created)

    Returns the memory array after finishing execution."""

    DEFAULT_MEMORY_SIZE = 30000

    cell = 0
    if not memory:
        memory = [0] * DEFAULT_MEMORY_SIZE
    pos = 0
    matches = bracket_matches(program)

    while pos < len(program):
        instruction = program[pos]

        if instruction == "+":
            memory[cell] += 1
        elif instruction == "-":
            memory[cell] -= 1
        elif instruction == ">":
            cell += 1
        elif instruction == "<":
            cell -= 1
        elif instruction == ".":
            print(chr(memory[cell]), end="")
        elif instruction == ",":
            read = ord(sys.stdin.read(1))
            if debug_mode:
                print("Read:", read)
            memory[cell] = read
        elif instruction == "[":
            if memory[cell] == 0:
                pos = matches[pos]
        elif instruction == "]":
            if memory[cell] != 0:
                pos = matches[pos]

        pos += 1
    return memory


def main():
    program_path = sys.argv[1]
    debug_mode = len(sys.argv) >= 3 and sys.argv[2] == "debug"

    with open(program_path) as f:
        program = f.read()
        cells = run_program(program, debug_mode=debug_mode)
        if debug_mode:
            print(cells[:10])


if __name__ == "__main__":
    main()
