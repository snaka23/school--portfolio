/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/23 21:19:43 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/26 17:30:08 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STACK_H
# define STACK_H

# include <stdlib.h>

typedef struct s_stack
{
	int				value;
	int				index;
	struct s_stack	*next;
}	t_stack;

t_stack				*stack_new(int data);
void				stackadd_back(t_stack **stc, t_stack *new);
void				assign_index(t_stack *a);
size_t				stack_size(t_stack *stc);
t_stack				*stack_at(t_stack *stc, size_t nbr);
void				stack_free(t_stack *a);

#endif