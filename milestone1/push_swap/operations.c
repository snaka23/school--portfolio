/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 16:59:10 by snakagaw          #+#    #+#             */
/*   Updated: 2026/06/02 16:58:30 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "operations_utils.h"

void	sa(t_pushswap *ps)
{
	set_current_op(&ps->info, SA);
	if (!ps->a || !ps->a->next)
		return ;
	swap(&ps->a);
	increment_opscnt(&ps->info, SA);
	put_current_operation(ps->info);
}

void	sb(t_pushswap *ps)
{
	set_current_op(&ps->info, SB);
	if (!ps->b || !ps->b->next)
		return ;
	swap(&ps->b);
	increment_opscnt(&ps->info, SB);
	put_current_operation(ps->info);
}

void	ss(t_pushswap *ps)
{
	set_current_op(&ps->info, SS);
	if (!ps->a || !ps->a->next)
		return ;
	if (!ps->b || !ps->b->next)
		return ;
	swap(&ps->a);
	swap(&ps->b);
	increment_opscnt(&ps->info, SS);
	put_current_operation(ps->info);
}

void	pa(t_pushswap *ps)
{
	t_stack	*ptr;

	set_current_op(&ps->info, PA);
	if (!ps->b)
		return ;
	ptr = ps->b;
	ps->b = ps->b->next;
	ptr->next = ps->a;
	ps->a = ptr;
	increment_opscnt(&ps->info, PA);
	put_current_operation(ps->info);
}

void	pb(t_pushswap *ps)
{
	t_stack	*ptr;

	set_current_op(&ps->info, PB);
	if (!ps->a)
		return ;
	ptr = ps->a;
	ps->a = ps->a->next;
	ptr->next = ps->b;
	ps->b = ptr;
	increment_opscnt(&ps->info, PB);
	put_current_operation(ps->info);
}
