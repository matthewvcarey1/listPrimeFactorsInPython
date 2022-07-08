#!/usr/bin/env python3

import sys
import time
import numpy as numpy


# sieve from numpy
def sieve(n):
    flags = numpy.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, n):
        # We could use a lower upper bound for this loop, but I don't want to bother with
        # getting the rounding right on the sqrt handling.
        if flags[i]:
            flags[i * i::i] = False
    return numpy.flatnonzero(flags)


def prime_factors(num, primes, factors):
    if num < 2:
        return factors
    for p in primes:
        if num % p == 0:
            res = factors.append(p)
            return prime_factors(num // p, primes, factors)
    return factors


def list_base_exponents(nums):
    nums.sort()
    lbe = []
    last_num = -1
    lbe_index = -1
    first = True
    for n in nums:
        if first is False and n == last_num:
            base, exponent = lbe[lbe_index]
            exponent += 1
            lbe[lbe_index] = (base, exponent)
        else:
            lbe_index += 1
            be = (n, 1)
            lbe.append(be)
            last_num = n
        first = False
    return lbe


def num_to_superscript(num):
    superscript_digits = [
        "\u2070",
        "\u00B9",
        "\u00B2",
        "\u00B3",
        "\u2074",
        "\u2075",
        "\u2076",
        "\u2077",
        "\u2078",
        "\u2079"]
    super_string_list = []
    while num > 0:
        value = num % 10
        s = superscript_digits[value]
        super_string_list.append(s)
        num = num // 10
    # The list is back to front lets reverse it.
    super_string_list.reverse()
    return ''.join(super_string_list)


def generate_index_format_string(lbe):
    string_list = []
    first = True
    for be in lbe:
        if first is False:
            string_list.append(" \u00D7 ")
        first = False
        base, exponent = be
        string_list.append(str(base))
        if exponent > 1:
            string_list.append(num_to_superscript(exponent))
    return ''.join(string_list)


def main(n):
    primes = sieve(n // 2)
    factors = []
    factors = prime_factors(n, primes, factors)
    lbe = list_base_exponents(factors)
    print(generate_index_format_string(lbe))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("missing natural number parameter")
        sys.exit(1)
    start = time.perf_counter()
    arg = sys.argv[1]
    val = int(arg)
    main(val)
    end = time.perf_counter()
    print(f"Time taken {end - start:0.4f} seconds")

