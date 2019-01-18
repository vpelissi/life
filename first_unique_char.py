# **************************************************************************** #
#                                                                              #
#                                                       ::::::::   ::::::::    #
#    first_unique_char.py                             :+:    :+: :+:    :+:    #
#                                                          +:+         +:+     #
#    By: vpelissi <vpelissi@23.us.org>                  +#+        +#++:       #
#                                                    +#+             +#+       #
#    Created: 2019/01/15 01:56:10 by vpelissi      #+#       #+#    #+#        #
#    Updated: 2019/01/15 01:56:15 by vpelissi     #########  ########.io       #
#                                                                              #
# **************************************************************************** #


def first_unique_char(value):
    if (len(value) == 1):
        return 0
    ban = []

    for i in range(len(value)):
        if all(value[i] != value[k] for k in range(i + 1, len(value))) == True and value[i] not in ban:
            return value[i]
        else:
            ban.append(value[i])
    return -1

