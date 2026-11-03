# 8) მომხმარებელს შეაყვანინეთ ორი რიცხვი: start და end.
#  while ციკლის გამოყენებით გამოიტანეთ ყველა რიცხვი start-დან end-ის ჩათვლით.
#  თუ რიცხვი დადებითია და ლუწია, გამოიტანეთ "Positive Even", სხვა შემთხვევაში გამოიტანეთ თავად რიცხვი.

start = int(input("enter start: "))
end = int(input("enter end: "))

while start <= end:
    if start > 0 and start % 2 == 0:
        print(start, "positive even")
    else:
        print(start)
    start += 1








