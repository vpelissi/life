# **************************************************************************** #
#                                                                              #
#                                                       ::::::::   ::::::::    #
#    factorial.py                                     :+:    :+: :+:    :+:    #
#                                                          +:+         +:+     #
#    By: vpelissi <vpelissi@23.us.org>                  +#+        +#++:       #
#                                                    +#+             +#+       #
#    Created: 2019/01/10 20:19:45 by vpelissi      #+#       #+#    #+#        #
#    Updated: 2019/01/10 20:20:10 by vpelissi     #########  ########.io       #
#                                                                              #
# **************************************************************************** #


def factorial(n, mod=None):
    """Calculates factorial iteratively.
    If mod is not None, then return (n! % mod)
    Time Complexity - O(n)"""
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("'n' must be a non-negative integer.")
    if mod is not None and not (isinstance(mod, int) and mod > 0):
        raise ValueError("'mod' must be a positive integer")
    result = 1
    if n == 0:
        return 1
    for i in range(2, n+1):
        result *= i
        if mod:
            result %= mod
    return result

print(factorial(42))
