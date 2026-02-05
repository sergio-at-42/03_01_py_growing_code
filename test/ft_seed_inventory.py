def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	print(seed_type.capitalize(), "seeds:", end=" ")
	if unit == "packets" :
		print(quantity, "packets available")
	elif unit == "grams" :
		print(quantity, "grams total")
	elif unit == "area" :
		print("covers", quantity, "square meters")
	else :
		print(quantity, "Unknown unit type")
