def mail_control(mail):
    if '@' and '.' in mail:
        valid=True
        return valid
    else:
        valid=False
        return valid
valid=False
mail=input("Enter the mail")
if mail_control(mail):
    print("your mail is  correct:")
else:
     print("your mail is not correct:")


