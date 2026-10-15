/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 17:33:46 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/28 17:07:49 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_ITOA_H
# define FT_ITOA_H

# include <stdlib.h>

char			*ft_itoa(long n);
char			*ft_itoa_hexa(long n, const char *hex);
char			*ft_itoa_ptr(unsigned long n, const char *hex);

#endif