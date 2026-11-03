# 3) მომხმარებელს შეაყვანინეთ რიცხვი. თუ რიცხვი დადებითია და ლუწია,
#  გამოიტანეთ "Positive Even". თუ დადებითია და კენტია, გამოიტანეთ "Positive Odd".
#  თუ უარყოფითია, გამოიტანეთ "Negative", სხვა შემთხვევაში — "Zero".

num = int(input("enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num < 0:
    print("Negative")
else:
    print("Zero")









