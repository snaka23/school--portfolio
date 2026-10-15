/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nshuhei <nshuhei@student.42.jp>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 17:32:26 by nshuhei           #+#    #+#             */
/*   Updated: 2026/05/28 17:52:44 by nshuhei          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PUTNBR_H
# define FT_PUTNBR_H

int	ft_putnbr(long num, int fd);
int	ft_puthex(unsigned int dec, char type, int fd);
int	ft_putptr(void *ptr, int fd);
int	ft_putfloat(double n, int fd);

#endif