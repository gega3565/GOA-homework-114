# 2) შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს პროდუქტების რაოდენობას,
#  შემდეგ კი for ციკლის გამოყენებით თითოეული პროდუქტის ფასს. 
# პროგრამამ უნდა დაითვალოს ყველა პროდუქტის საერთო ღირებულება. 
# თუ თანხა 200 ლარზე მეტია, მომხმარებელს მიეცით 15%-იანი ფასდაკლება, თუ 100-დან 200 ლარამდეა - 10%,
#  ხოლო სხვა შემთხვევაში ფასდაკლება არ მოქმედებს. საბოლოოდ გამოიტანეთ გადასახდელი თანხა.

count = int(input("How many products? "))
total = 0

for i in range(count):
    price = int(input("Enter price: "))
    total = total + price

if total > 200:
    discount = 15
elif total >= 100:
    discount = 10
else:
    discount = 0

to_pay = total - total * discount / 100

print("Total:", total)
print("Discount:", discount, "%")
print("To pay:", to_pay)





