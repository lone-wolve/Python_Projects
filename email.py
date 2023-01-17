def main():
    email = input("pls enter your email\n------->")

    (name, domain) = email.split("@")
    domain, extension = domain.split(".")

    print("your user name is:---->", name )
    print("your domain is:---->", domain)
    print("your email extension is: ---->", extension )

main()