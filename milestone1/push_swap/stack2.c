/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack2.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 19:14:34 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/28 17:17:09 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

size_t	stack_size(t_stack *stc)
{
	t_stack	*ptr;
	size_t	count;

	ptr = stc;
	count = 0;
	while (ptr)
	{
		ptr = ptr->next;
		count++;
	}
	return (count);
}

t_stack	*stack_at(t_stack *stc, size_t nbr)
{
	t_stack	*tmp;
	size_t	size;
	size_t	i;

	i = 0;
	size = stack_size(stc);
	if (nbr > size)
		return (NULL);
	tmp = stc;
	while (i < nbr)
	{
		tmp = tmp->next;
		i++;
	}
	return (tmp);
}
