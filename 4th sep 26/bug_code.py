def reverse_string(text: str) -> str:
   """Return the reverse of the input string."""
   characters = list(text)
   left_index = 0
   right_index = len(characters)
   def swap_elements(sequence: list, index_a: int, index_b: int) -> None:
       sequence[index_a], sequence[index_b] = sequence[index_b], sequence[index_a]
   while left_index < right_index:
       swap_elements(characters, left_index, right_index)
       left_index += 1
       right_index -= 1
   return "".join(characters)