/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/09 19:54:58 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/28 17:50:59 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_itoa.h"
#include "ft_printf_utils.h"

int	ft_putnbr(long num, int fd)
{
	int		ret;
	char	*str;

	str = ft_itoa(num);
	if (!str)
		return (-1);
	ret = ft_putstr_fd(str, fd);
	if (str)
		free(str);
	return (ret);
}

int	ft_puthex(unsigned int dec, char type, int fd)
{
	int			ret;
	char		*str;
	const char	*lowhex;
	const char	*uphex;

	lowhex = "0123456789abcdef";
	uphex = "0123456789ABCDEF";
	if (type == 'x')
		str = ft_itoa_hexa(dec, lowhex);
	if (type == 'X')
		str = ft_itoa_hexa(dec, uphex);
	if (!str)
		return (-1);
	ret = ft_putstr_fd(str, fd);
	if (str)
		free(str);
	return (ret);
}

int	ft_putptr(void *ptr, int fd)
{
	int				ret;
	char			*str;
	unsigned long	adress;
	const char		*lowhex;

	if (!ptr)
		return ((int)write(fd, "(nil)", 5));
	lowhex = "0123456789abcdef";
	adress = (unsigned long)ptr;
	str = ft_itoa_ptr(adress, lowhex);
	if (!str)
		return (-1);
	ret = ft_putstr_fd(str, fd);
	if (str)
		free(str);
	return (ret);
}

int	ft_putfloat(double n, int fd)
{
	long	int_part;
	long	frac_part;
	int		ret;

	ret = 0;
	if (n < 0)
	{
		ret += write(fd, "-", 1);
		n *= -1;
	}
	int_part = (long)n;
	frac_part = (long)((n - int_part) * 100);
	if (frac_part == 100)
	{
		int_part++;
		frac_part = 0;
	}
	ret += ft_putnbr(int_part, fd);
	ret += write(fd, ".", 1);
	if (frac_part < 10)
		ret += write(fd, "0", 1);
	ret += ft_putnbr(frac_part, fd);
	return (ret);
}
