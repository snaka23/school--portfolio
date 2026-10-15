/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   operations_utils.h                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 14:53:05 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/02 15:30:11 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef OPERATIONS_UTILS_H
# define OPERATIONS_UTILS_H

# include "push_swap.h"

void	rotate(t_stack **stc);
void	reverse_rotate(t_stack **stc);
void	swap(t_stack **stc);
void	put_current_operation(t_sortinfo info);

#endif