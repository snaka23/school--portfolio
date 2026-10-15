/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 14:40:12 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/01 14:40:12 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "stack.h"
# include "sortinfo.h"

typedef struct s_pushswap
{
	t_stack		*a;
	t_stack		*b;
	t_sortinfo	info;
	int			bench;
}	t_pushswap;

#endif