# 2) შექმენით ორი ცვლადი: age და has_ticket.
# age-ში შეინახეთ მომხმარებლის ასაკი, ხოლო has_ticket-ში — True ან False.
# გამოიყენეთ and ოპერატორი და შეამოწმეთ, შეუძლია თუ არა მომხმარებელს კინოში შესვლა.
# შესვლა შესაძლებელი უნდა იყოს მხოლოდ იმ შემთხვევაში, თუ მომხმარებელი მინიმუმ 12 წლისაა და ბილეთი აქვს.
# (მონაცემები, ანუ age-იც და has_ticket-იც უნდა შემოაყვანინოთ მომხმარებელს.)

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (True/False): ") == "True"

can_enter = age >= 12 and has_ticket

print("Can enter the cinema:", can_enter)







