ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

#         LIST         #

ft_list[1] = "World!"

#         TUPLE         #

ft_tuple = ("Hello", "France!")

# or :

tmp_list = list(ft_tuple)
tmp_list[1] = "France!"
ft_tuple = tuple(tmp_list)

#         SET         #

tmp_list = list(ft_set)
tmp_list[1] = "Nice!"
ft_set = set(tmp_list)

#         Dict         #

ft_dict['Hello'] = "42Nice!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
