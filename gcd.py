# **************************************************************************** #
#                                                                              #
#                                                       ::::::::   ::::::::    #
#    gcd.py                                           :+:    :+: :+:    :+:    #
#                                                          +:+         +:+     #
#    By: vpelissi <vpelissi@23.us.org>                  +#+        +#++:       #
#                                                    +#+             +#+       #
#    Created: 2019/01/11 00:11:48 by vpelissi      #+#       #+#    #+#        #
#    Updated: 2019/01/11 00:12:03 by vpelissi     #########  ########.io       #
#                                                                              #
# **************************************************************************** #



def gcd(a, b):
    """Computes the greatest common divisor of integers a and b using
    Euclid's Algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a
