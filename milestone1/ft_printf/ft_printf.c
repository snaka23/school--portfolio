/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/11 11:40:16 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/13 17:27:40 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	check_char(char c)
{
	if (c == 'c' || c == 's' || c == 'p')
		return (1);
	else if (c == 'd' || c == 'i' || c == 'u')
		return (1);
	else if (c == 'x' || c == 'X' || c == '%')
		return (1);
	else
		return (0);
}

static int	printf_write(const char *format, int i, va_list ap)
{
	int		count;

	count = 0;
	if (format[i + 1] == 'c')
		count = ft_printf_char(va_arg(ap, int));
	else if (format[i + 1] == 's')
		count = ft_printf_str(va_arg(ap, const char *));
	else if (format[i + 1] == 'p')
		count = ft_printf_ptr(va_arg(ap, void *));
	else if (format[i + 1] == 'd')
		count = ft_printf_nbr(va_arg(ap, int));
	else if (format[i + 1] == 'i')
		count = ft_printf_nbr(va_arg(ap, int));
	else if (format[i + 1] == 'u')
		count = ft_printf_unbr(va_arg(ap, unsigned int));
	else if (format[i + 1] == 'x')
		count = ft_printf_hex_low(va_arg(ap, unsigned int));
	else if (format[i + 1] == 'X')
		count = ft_printf_hex_upp(va_arg(ap, unsigned int));
	else if (format[i + 1] == '%')
		count = ft_printf_char('%');
	return (count);
}

static int	count_write(const char *format, int *i, va_list ap)
{
	int	res;

	res = 0;
	if (format[*i] == '%' && check_char(format[*i + 1]))
	{
		res = printf_write(format, *i, ap);
		*i = *i + 2;
	}
	else
	{
		res = write(1, &format[*i], 1);
		*i = *i + 1;
	}
	return (res);
}

int	ft_printf(const char *format, ...)
{
	va_list	ap;
	int		i;
	int		count;
	int		res;

	va_start(ap, format);
	i = 0;
	count = 0;
	while (format[i])
	{
		res = count_write(format, &i, ap);
		if (res == -1)
		{
			va_end(ap);
			return (-1);
		}
		count = count + res;
	}
	va_end(ap);
	return (count);
}
/*#include <stdio.h>

int main(void)
{
     int ft_ret, std_ret;
     char *str = "Gemini";

     printf("--- Test: String & Char ---\n");
     ft_ret = ft_printf("MINE: %s is %c\n", str, 'G');
     std_ret = printf("REAL: %s is %c\n", str, 'G');
     printf("Return: [FT: %d] | [STD: %d]\n\n", ft_ret, std_ret);

     printf("--- Test: Integer Limits ---\n");
     ft_ret = ft_printf("MINE: %d, %d\n", -2147483648, 2147483647);
     std_ret = printf("REAL: %d, %d\n", -2147483648, 2147483647);
     printf("Return: [FT: %d] | [STD: %d]\n\n", ft_ret, std_ret);

     printf("--- Test: NULL Pointer ---\n");
     ft_ret = ft_printf("MINE: %s, %p\n", (char *)NULL, NULL);
     std_ret = printf("REAL: %s, %p\n", (char *)NULL, NULL);
     printf("Return: [FT: %d] | [STD: %d]\n\n", ft_ret, std_ret);

     return (0);
}*/
