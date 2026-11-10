
# 4) შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს 5 სტუდენტის სახელსა და ქულას.
# თითოეული სტუდენტის ქულის მიხედვით განსაზღვრეთ მისი შედეგი:
# თუ ქულა 90 ან მეტია - "შესანიშნავი", თუ 70-დან 89-მდეა - "კარგი",
# თუ 50-დან 69-მდეა - "დამაკმაყოფილებელი", 
# ხოლო 50-ზე ნაკლები ქულის შემთხვევაში - "ჩაჭრილი".
# საბოლოოდ გამოიტანეთ ყველა სტუდენტის სახელი და შესაბამისი შედეგი.

all_results = ""

for i in range(5):
    name = input("Enter student name: ")
    score = int(input("Enter score: "))

    if score >= 90:
        result = "excellent"
    elif score >= 70:
        result = "good"
    elif score >= 50:
        result = "satisfactory"
    else:
        result = "failed"

    all_results = all_results + name + " - " + result + ", "

print(all_results)


