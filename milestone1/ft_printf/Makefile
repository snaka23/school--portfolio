# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: snakagaw <snakagaw@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/12 11:51:05 by snakagaw          #+#    #+#              #
#    Updated: 2026/05/13 17:19:08 by snakagaw         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME	= libftprintf.a
CC		= cc
CFLAGS	= -Wall -Wextra -Werror
SRCS	= ft_printf.c \
		  ft_printf_utils.c \
		  ft_printf_utils_2.c
OBJS	= $(SRCS:.c=.o)
all:	$(NAME)
$(NAME):	$(OBJS)
	ar rcs	$(NAME)	$(OBJS)
%.o:%.c
	$(CC) $(CFLAGS) -c $< -o $@
clean:
	rm -f $(OBJS)
fclean:	clean
	rm -f $(NAME)
re:	fclean all
.PHONY:	all clean fclean re
