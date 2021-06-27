def atm():
    pin = 1234
    ava_bal = 1000000
    a = int(input(' \nPRESS 1 TO INDICATE THAT THE CARD IS INSERTED:'))
    if a == 1:
        b = int(input('\nPlease select the banking operations:\n1-CASH WITHDRAWAL :\n2-BALANCE ENQUIRY\n3-CHANGE PIN'))
        if b == 1:
            c = int(input("\n\n1-SAVINGS ACCOUNT\n2-CURRENT ACCOUNT"))
            if c == 1:
                d = int(input("\nENTER THE AMOUNT IN MULTIPLES OF 100 ONLY:"))
                if d % 100 == 0 and d <= 20000:
                    p = int(input('\nENTER THE 4 DIGITS PIN NUMBER:'))
                    if p == pin:
                        print('\nPLEASE WAIT!! YOUR TRANSACTION IS ON PROCESS:\n')
                        print('\nCOLLECT THE CASH OF RS', d)
                        e = int(input('\nDO YOU WANT THE RECEIPT?,\n press 1 if you want'))
                        if e == 1:
                            print('\nCOLLECT THE RECEIPT')
                            f = int((input('\nDO YOU WANT TO MAKE ANOTHER TRANSACTION?\n if yes press 1\t if not press 0')))
                            if f == 1:
                                atm()
                            else:
                                print('\nCOLLECT YOUR CARD:')
                                print('\nTHANKS FOR BANKING WITH AXIS BANK,MEET YOU SOON!!!!!!!!!!!')

                        else:
                            f = int((input('\nDO YOU WANT TO MAKE ANOTHER TRANSACTION?\n if yes press 1\t if not press 0 ')))
                            if f == 1:
                                atm()
                            else:
                                print('\nCOLLECT YOUR CARD:')
                                print('\nTHANKS FOR BANKING WITH AXIS BANK,MEET YOU SOON!!!!!!!!!!!')

                    else:
                        print('\nENTER CORRECT 4 DIGITS NUMBER:')
                else:
                    print('\nPLEASE ENTER THE AMOUNT IN MULTIPLES OF 100 ONLY AND LESSER THAN 20000 RS:')
            else:
                print('\nYOU HAVE SELECTED CURRENT ACCOUNT')
                d = int(input("\nENTER THE AMOUNT IN MULTIPLES OF 100 ONLY:"))
                if d % 100 == 0 and d <= 20000:
                    p = int(input('\nENTER THE 4 DIGITS PIN NUMBER:'))
                    if p == pin:
                        print('\nPLEASE WAIT!! YOUR TRANSACTION IS ON PROCESS:\n')
                        print('\nCOLLECT THE CASH OF RS', d)
                        e = int(input('\nDO YOU WANT THE RECEIPT?,\n press 1 if you want'))
                        if e == 1:
                            print('\nCOLLECT THE RECEIPT')
                            f = int(
                                (input('\nDO YOU WANT TO MAKE ANOTHER TRANSACTION?\n if yes press 1\t if not press 0 ')))
                            if f == 1:
                                atm()
                            else:
                                print('\nCOLLECT YOUR CARD:')
                                print('\nTHANKS FOR BANKING WITH AXIS BANK,MEET YOU SOON!!!!!!!!!!!')

                        else:
                            f = int(
                                (input('\nDO YOU WANT TO MAKE ANOTHER TRANSACTION?\n if yes press 1\t if not press 0 ')))
                            if f == 1:
                                atm()
                            else:
                                print('\nCOLLECT YOUR CARD:')
                                print('\nTHANKS FOR BANKING WITH AXIS BANK,MEET YOU SOON!!!!!!!!!!!')

                    else:
                        print('\nINCORRECT PIN:')
                else:
                    print('\nPLEASE ENTER THE AMOUNT IN MULTIPLES OF 100 ONLY AND LESSER THAN 20000:')
        elif b == 2:
            print('\nYOU HAVE SELECTED THE OPTION FOR BALANCE ENQUIRY:')
            g = int(input('\nENTER THE 4 DIGITS PIN NUMBER:'))
            if g == pin:
                print('\nTHE AVAILABLE BALANCE IN YOUR ACCOUNT IS \t:'" "'rs', ava_bal)
                print('\nTHANKS FOR BANKING WITH AXIS BANK,MEET YOU SOON!!!!!!!!!!!')
            else:
                print('\nPIN MISMATCH,PLEASE ENTER CORRECT PIN')

        else:
            print('\nYOU HAVE SELECTED THE OPTION FOR PIN CHANGE REQUEST: ')
            old_pin = int(input('\nENTER THE OLD PIN NUMBER '))
            if old_pin == pin:
                new_pin = input("\nENTER NEW FOUR DIGITS PIN NUMBER")
                if len(new_pin) == 4:
                    pin = new_pin
                    print("\nTHE PIN HAVE BEEN SUCCESSFULLY UPDATED as", pin)
                    print('\nTHANKS FOR BANKING WITH AXIS BANK,MEET YOU SOON!!!!!!!!!!!')

                else:
                    print('\nENTER ONLY FOUR DIGITS:')
            else:
                print('\nPIN MISMATCH,PLEASE ENTER CORRECT PIN NUMBER:')
    else:
        print(" \nPLEASE INSERT THE CARD PROPERLY:")


print(" WELCOME TO AXIS BANK \n "
      "\nPLEASE INSERT YOUR CARD")
atm()
