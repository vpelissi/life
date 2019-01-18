# **************************************************************************** #
#                                                                              #
#                                                       ::::::::   ::::::::    #
#    fibonacci.py                                     :+:    :+: :+:    :+:    #
#                                                          +:+         +:+     #
#    By: vpelissi <vpelissi@23.us.org>                  +#+        +#++:       #
#                                                    +#+             +#+       #
#    Created: 2019/01/12 13:40:35 by vpelissi      #+#       #+#    #+#        #
#    Updated: 2019/01/12 13:41:46 by vpelissi     #########  ########.io       #
#                                                                              #
# **************************************************************************** #


def fibonacci(x):
	sequence_list = []

	current = 0
	next = 1
	
	for i in range (x):
	
		sequence_list.append(current)
		current = next
		if i > 0:
			next = sequence_list[i] + current
		else:
			next = 1
	return sequence_list	
