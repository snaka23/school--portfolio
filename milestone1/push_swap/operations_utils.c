/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_utils.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 14:55:17 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/02 15:27:58 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "utils.h"
#include <unistd.h>

void	swap(t_stack **stc)
{
	t_stack	*ptr;

	ptr = *stc;
	*stc = (*stc)->next;
	ptr->next = (*stc)->next;
	(*stc)->next = ptr;
}

void	rotate(t_stack **stc)
{
	t_stack	*ptr;

	ptr = *stc;
	*stc = (*stc)->next;
	ptr->next = NULL;
	stackadd_back(stc, ptr);
}

void	reverse_rotate(t_stack **stc)
{
	t_stack	*ptr1;
	t_stack	*ptr2;

	ptr1 = *stc;
	while (ptr1->next->next)
		ptr1 = ptr1->next;
	ptr2 = ptr1->next;
	ptr1->next = NULL;
	ptr2->next = *stc;
	*stc = ptr2;
}

void	put_current_operation(t_sortinfo info)
{
	t_ops	op;

	op = get_current_op(info);
	if (op == SA)
		write(1, "sa\n", ft_strlen("sa\n"));
	else if (op == SB)
		write(1, "sb\n", ft_strlen("sb\n"));
	else if (op == SS)
		write(1, "ss\n", ft_strlen("ss\n"));
	else if (op == PA)
		write(1, "pa\n", ft_strlen("pa\n"));
	else if (op == PB)
		write(1, "pb\n", ft_strlen("pb\n"));
	else if (op == RA)
		write(1, "ra\n", ft_strlen("ra\n"));
	else if (op == RB)
		write(1, "rb\n", ft_strlen("rb\n"));
	else if (op == RR)
		write(1, "rr\n", ft_strlen("rr\n"));
	else if (op == RRA)
		write(1, "rra\n", ft_strlen("rra\n"));
	else if (op == RRB)
		write(1, "rrb\n", ft_strlen("rrb\n"));
	else if (op == RRR)
		write(1, "rrr\n", ft_strlen("rrr\n"));
}
