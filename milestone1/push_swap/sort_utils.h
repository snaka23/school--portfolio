/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_utils.h                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 15:41:42 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/01 23:10:04 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SORT_UTILS_H
# define SORT_UTILS_H

# include "push_swap.h"

int		min_value(t_stack *stc);
size_t	min_position(t_stack *a);
void	a_move_min_top(t_pushswap *ps);
int		max_value(t_stack *stc);
size_t	max_position(t_stack *stc);

#endif