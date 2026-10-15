/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 17:22:24 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/13 17:30:15 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf_utils.h"
#include "utils.h"

int	ft_putstr_fd(char *s, int fd)
{
	if (!s)
		return ((int)write(fd, "(null)", 6));
	return ((int)write(fd, s, ft_strlen(s)));
}

int	ft_putchar_fd(char c, int fd)
{
	return ((int)write(fd, &c, 1));
}

void	*ft_memset(void *s, int c, size_t n)
{
	size_t			i;
	unsigned char	*tmp;

	i = 0;
	tmp = (unsigned char *)s;
	while (i < n)
		tmp[i++] = c;
	return (s);
}
