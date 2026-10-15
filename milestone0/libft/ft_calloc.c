/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/01 16:26:38 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/04 17:36:24 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t nmemb, size_t size)
{
	unsigned char	*res;
	size_t			sum;
	size_t			i;

	if (nmemb != 0 && size > (size_t)-1 / nmemb)
		return (NULL);
	sum = nmemb * size;
	res = (unsigned char *)malloc(sum);
	if (res == NULL)
		return (NULL);
	i = 0;
	while (i < sum)
	{
		res[i] = 0;
		i++;
	}
	return (res);
}
