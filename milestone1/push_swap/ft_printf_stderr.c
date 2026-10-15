/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_stderr.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/04 22:30:32 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/29 13:25:27 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdarg.h>
#include <stdlib.h>
#include "ft_printf_utils.h"
#include "ft_putnbr.h"

static int	ft_putconv(va_list ap, char type)
{
	if (type == 'c')
		return (ft_putchar_fd(va_arg(ap, int), 2));
	else if (type == '%')
		return (ft_putchar_fd('%', 2));
	else if (type == 's')
		return (ft_putstr_fd(va_arg(ap, char *), 2));
	else if (type == 'd' || type == 'i')
		return (ft_putnbr((long)va_arg(ap, int), 2));
	else if (type == 'f')
		return (ft_putfloat(va_arg(ap, double), 2));
	else if (type == 'u')
		return (ft_putnbr(va_arg(ap, unsigned int), 2));
	else if (type == 'x' || type == 'X')
		return (ft_puthex(va_arg(ap, unsigned int), type, 2));
	else if (type == 'p')
		return (ft_putptr(va_arg(ap, void *), 2));
	return (ft_putchar_fd('%', 2) + ft_putchar_fd(type, 2));
}

int	ft_printf_stderr(const char *fmt, ...)
{
	int		ret;
	int		tmp;
	va_list	ap;

	ret = 0;
	if (!fmt)
		return (-1);
	va_start(ap, fmt);
	while (*fmt)
	{
		if (*fmt == '%')
		{
			tmp = ft_putconv(ap, *(fmt + 1));
			ret += tmp;
			fmt += 2;
		}
		else
		{
			write(2, fmt++, 1);
			ret++;
		}
	}
	va_end(ap);
	return (ret);
}
