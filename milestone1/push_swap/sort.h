/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/25 19:53:32 by nshuhei           #+#    #+#             */
/*   Updated: 2026/06/02 19:10:48 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SORT_H
# define SORT_H

# include "push_swap.h"

void	sort_three(t_pushswap *ps);
void	sort_five(t_pushswap *ps);
void	simple_sort(t_pushswap *ps);
void	chunk_sort(t_pushswap *ps);
void	radix_sort(t_pushswap *ps);
void	ft_sort(t_pushswap *ps);

#endif
