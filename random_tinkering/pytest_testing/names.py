from name_funtion import get_formatted_name

print("enter q to quit")
while True:
   first = input("\nGive a first name: ")
   if first == 'q':
      break

   last = input("\nGive a last name: ")
   if last == 'q':
      break

   formatted_name = get_formatted_name(first, last)
   print(f"\nFormatted full name: {formatted_name}. ")

