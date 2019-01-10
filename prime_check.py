# **************************************************************************** #
#                                                                              #
#                                                       ::::::::   ::::::::    #
#    prime_check.py                                   :+:    :+: :+:    :+:    #
#                                                          +:+         +:+     #
#    By: vpelissi <vpelissi@23.us.org>                  +#+        +#++:       #
#                                                    +#+             +#+       #
#    Created: 2019/01/10 19:12:29 by vpelissi      #+#       #+#    #+#        #
#    Updated: 2019/01/10 19:13:30 by vpelissi     #########  ########.io       #
#                                                                              #
# **************************************************************************** #


def prime_check(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            return False
        j += 6
    return True


print(prime_check(42))

