/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/12 11:34:10 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/12 11:44:18 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include <unistd.h>
# include <stdarg.h>

int	ft_printf_char(int c);
int	ft_printf_str(const char *str);
int	ft_printf_nbr(int nb);
int	ft_printf_unbr(unsigned int nb);
int	ft_printf_ptr(void *ptr);
int	ft_printf_hex_low(unsigned int nb);
int	ft_printf_hex_upp(unsigned int nb);
int	ft_printf(const char *format, ...);

#endif
