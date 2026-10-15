/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations2.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 17:00:04 by snakagaw          #+#    #+#             */
/*   Updated: 2026/06/02 16:58:30 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "operations_utils.h"

void	ra(t_pushswap *ps)
{
	set_current_op(&ps->info, RA);
	if (!ps->a || !ps->a->next)
		return ;
	rotate(&ps->a);
	increment_opscnt(&ps->info, RA);
	put_current_operation(ps->info);
}

void	rb(t_pushswap *ps)
{
	set_current_op(&ps->info, RB);
	if (!ps->b || !ps->b->next)
		return ;
	rotate(&ps->b);
	increment_opscnt(&ps->info, RB);
	put_current_operation(ps->info);
}

void	rr(t_pushswap *ps)
{
	set_current_op(&ps->info, RR);
	if (!ps->a || !ps->a->next)
		return ;
	if (!ps->b || !ps->b->next)
		return ;
	rotate(&ps->a);
	rotate(&ps->b);
	increment_opscnt(&ps->info, RR);
	put_current_operation(ps->info);
}

//====
// #include "operations.h"
//
// void	ra(t_pushswap *ps)
// {
// 	t_stack	*ptr;
//
// 	if (!ps->a || !ps->a->next)
// 		return ;
// 	ptr = ps->a;
// 	ps->a = ps->a->next;
// 	ptr->next = NULL;
// 	stackadd_back(&ps->a, ptr);
// 	put_current_operation(RA);
// 	increment_opscnt(&ps->info, RA);
// }
//
// void	rb(t_pushswap *ps)
// {
// 	t_stack	*ptr;
//
// 	if (!ps->b || !ps->b->next)
// 		return ;
// 	ptr = ps->b;
// 	ps->b = ps->b->next;
// 	ptr->next = NULL;
// 	stackadd_back(&ps->b, ptr);
// 	put_current_operation(RB);
// 	increment_opscnt(&ps->info, RB);
// }
//
// void	rra(t_pushswap *ps)
// {
// 	t_stack	*ptr1;
// 	t_stack	*ptr2;
//
// 	if (!ps->a || !ps->a->next)
// 		return ;
// 	ptr1 = ps->a;
// 	while (ptr1->next->next)
// 		ptr1 = ptr1->next;
// 	ptr2 = ptr1->next;
// 	ptr1->next = NULL;
// 	ptr2->next = ps->a;
// 	ps->a = ptr2;
// 	put_current_operation(RRA);
// 	increment_opscnt(&ps->info, RRA);
// }
//
// void	rrb(t_pushswap *ps)
// {
// 	t_stack	*ptr1;
// 	t_stack	*ptr2;
//
// 	if (!ps->b || !ps->b->next)
// 		return ;
// 	ptr1 = ps->b;
// 	while (ptr1->next->next)
// 		ptr1 = ptr1->next;
// 	ptr2 = ptr1->next;
// 	ptr1->next = NULL;
// 	ptr2->next = ps->b;
// 	ps->b = ptr2;
// 	put_current_operation(RRB);
// 	increment_opscnt(&ps->info, RRB);
// }
//=============

//------
// #include "stack.h"
// #include "sortinfo.h"
// #include <unistd.h>
//
// void	ra(t_stack **stc)
// {
// 	t_stack	*ptr;
//
// 	if (!stc || !*stc || !(*stc)->next)
// 		return ;
// 	ptr = *stc;
// 	*stc = (*stc)->next;
// 	ptr->next = NULL;
// 	stackadd_back(stc, ptr);
// 	put_current_operation(RA);
// 	increment_opscnt(&g_sortinfo, RA);
// }
//
// void	rb(t_stack **stc)
// {
// 	t_stack	*ptr;
//
// 	if (!stc || !*stc || !(*stc)->next)
// 		return ;
// 	ptr = *stc;
// 	*stc = (*stc)->next;
// 	ptr->next = NULL;
// 	stackadd_back(stc, ptr);
// 	put_current_operation(RB);
// 	increment_opscnt(&g_sortinfo, RB);
// }
//
// void	rra(t_stack **stc)
// {
// 	t_stack	*ptr1;
// 	t_stack	*ptr2;
//
// 	if (!stc || !*stc || !(*stc)->next)
// 		return ;
// 	ptr1 = *stc;
// 	while ((ptr1->next)->next)
// 		ptr1 = ptr1->next;
// 	ptr2 = ptr1->next;
// 	ptr1->next = NULL;
// 	ptr2->next = *stc;
// 	*stc = ptr2;
// 	put_current_operation(RRA);
// 	increment_opscnt(&g_sortinfo, RRA);
// }
//
// void	rrb(t_stack **stc)
// {
// 	t_stack	*ptr1;
// 	t_stack	*ptr2;
//
// 	if (!stc || !*stc || !(*stc)->next)
// 		return ;
// 	ptr1 = *stc;
// 	while (ptr1->next->next)
// 		ptr1 = ptr1->next;
// 	ptr2 = ptr1->next;
// 	ptr1->next = NULL;
// 	ptr2->next = *stc;
// 	*stc = ptr2;
// 	put_current_operation(RRB);
// 	increment_opscnt(&g_sortinfo, RRB);
// }
//---------