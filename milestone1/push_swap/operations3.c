/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations3.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 21:27:55 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/02 16:58:30 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "operations_utils.h"

void	rra(t_pushswap *ps)
{
	set_current_op(&ps->info, RRA);
	if (!ps->a || !ps->a->next)
		return ;
	reverse_rotate(&ps->a);
	increment_opscnt(&ps->info, RRA);
	put_current_operation(ps->info);
}

void	rrb(t_pushswap *ps)
{
	set_current_op(&ps->info, RRB);
	if (!ps->b || !ps->b->next)
		return ;
	reverse_rotate(&ps->b);
	increment_opscnt(&ps->info, RRB);
	put_current_operation(ps->info);
}

void	rrr(t_pushswap *ps)
{
	set_current_op(&ps->info, RRR);
	if (!ps->a || !ps->a->next)
		return ;
	if (!ps->b || !ps->b->next)
		return ;
	reverse_rotate(&ps->a);
	reverse_rotate(&ps->b);
	increment_opscnt(&ps->info, RRR);
	put_current_operation(ps->info);
}
