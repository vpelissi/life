# **************************************************************************** #
#                                                                              #
#                                                       ::::::::   ::::::::    #
#    palindrome.py                                    :+:    :+: :+:    :+:    #
#                                                          +:+         +:+     #
#    By: vpelissi <vpelissi@23.us.org>                  +#+        +#++:       #
#                                                    +#+             +#+       #
#    Created: 2019/01/15 01:34:21 by vpelissi      #+#       #+#    #+#        #
#    Updated: 2019/01/15 01:35:13 by vpelissi     #########  ########.io       #
#                                                                              #
# **************************************************************************** #

from string import ascii_letters


def palindrome(value):
    i = 0
    j = len(value)-1
    
    while i < j:
        while i < j and not value[i].isalnum():
            	i += 1
        while i < j and not value[j].isalnum():
            	j -= 1
        if value[i].lower() != value[j].lower():
            	return False
        i, j = i+1, j-1
    return True
