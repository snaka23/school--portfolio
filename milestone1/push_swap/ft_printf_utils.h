/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.h                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 17:20:36 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/13 17:55:59 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_UTILS_H
# define FT_PRINTF_UTILS_H

# include <stdlib.h>
# include <unistd.h>

void				*ft_memset(void *b, int c, size_t len);
int					ft_putchar_fd(char c, int fd);
int					ft_putstr_fd(char *s, int fd);

#endif