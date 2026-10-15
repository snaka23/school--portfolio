/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/30 19:33:49 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/09 16:33:28 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	const unsigned char	*ptr1;
	unsigned char		*ptr2;

	if (!dest && !src)
		return (NULL);
	ptr1 = (const unsigned char *)src;
	ptr2 = (unsigned char *)dest;
	if (ptr1 < ptr2)
	{
		while (n > 0)
		{
			n--;
			ptr2[n] = ptr1[n];
		}
	}
	else
		ft_memcpy(dest, src, n);
	return (dest);
}
