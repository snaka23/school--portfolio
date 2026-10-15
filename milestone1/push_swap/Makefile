NAME = push_swap

CC = cc
CFLAGS = -Wall -Wextra -Werror

RM = rm -f

SRCS = \
	push_swap.c \
	parse.c \
	stack.c \
	stack2.c \
	operations.c \
	operations2.c \
	operations3.c \
	operations_utils.c \
	sort.c \
	sort_small.c \
	sort_simple.c \
	sort_medium.c \
	sort_complex.c \
	sort_utils.c \
	sortinfo.c \
	sortinfo2.c \
	sortinfo3.c \
	utils.c \
	ft_printf_stderr.c \
	ft_printf_utils.c \
	ft_putnbr.c \
	ft_itoa.c \
	ft_itoa_hex.c

OBJS = $(SRCS:.c=.o)

HEADERS = \
	push_swap.h \
	stack.h \
	operations.h \
	operations_utils.h \
	sort.h \
	sort_utils.h \
	sortinfo.h \
	parse.h \
	utils.h \
	ft_printf_stderr.h \
	ft_printf_utils.h \
	ft_putnbr.h \
	ft_itoa.h

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re