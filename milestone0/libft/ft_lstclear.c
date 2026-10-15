/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: snakagaw <snakagaw@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/04 14:10:50 by snakagaw          #+#    #+#             */
/*   Updated: 2026/05/09 18:06:28 by snakagaw         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*ptr1;
	t_list	*ptr2;

	if (!lst || !*lst || !(*del))
		return ;
	ptr1 = *lst;
	while (ptr1)
	{
		ptr2 = ptr1->next;
		(*del)(ptr1->content);
		free(ptr1);
		ptr1 = ptr2;
	}
	*lst = NULL;
}
