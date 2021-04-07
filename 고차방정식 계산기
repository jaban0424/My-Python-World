import math
from sympy import Symbol, solve
import time


run = 1
while run == 1:
    time.sleep(0.5)
    print("\n############################################################################")
    print("################### 방정식 해를 구해주는 프로그램 입니다.###################")
    print("############################################################################\n")
    time.sleep(0.5)
    print("      1 ~ 6차 방정식의 해를 구할 수 있습니다.    \n")
    time.sleep(0.5)
    select = input("해를 구하고 싶은 방정식의 번호를 선택하세요.\n\n 1. 1차 방정식\n 2. 2차 방정식\n 3. 3차 방정식\n 4. 4차 방정식\n 5. 5차 방정식 \n 6. 6차 방정식\n 0. 프로그램 종료 \n\n선택 -> ")
    #1차 방정식
    if select=='1' or select == '2' or select == '3' or select == '4' or select == '5' or select == '6' or select == '0':
        if select == 1:
            time.sleep(0.5)
            print("\n*******************************************")
            print("*******1차 방정식을 선택 하셨습니다.*******")
            print("*******************************************")
            time.sleep(0.5)
            print("\n1차 방정식의 모습은 ax + b = cx + b 입니다. \n각각의 계수를 입력하세요.\n")
            time.sleep(0.5)
            ao=int(input('좌변 x의 계수 a => '))
            bo=int(input('좌변 상수 b => '))
            co=int(input('우변 x의 계수 c => '))
            do=int(input('우변 상수 d => '))
            if ao>co:
                x=(do-bo)/(ao-co)
                time.sleep(0.5)
                print('\n일차방정식의 해 X는 %0.2f입니다.\n'% x )
            elif ao<co:
                x=(bo-do)/(co-ao)
                time.sleep(0.5)
                print('\n일차방정식의 해 X는 %0.2f입니다.\n'% x )
            elif ao==co:
                time.sleep(0.5)
                print('\n해가 없습니다. (x가 소거됨)\n')
            rrun = 1
            while rrun == 1:
                time.sleep(0.5)
                retry=str(input('Q. 다시 하시겠습니까?\nyes : y\nno : n\nA => '))
                time.sleep(0.5)
                if retry=='y' or retry =='n':
                    if retry == 'y':
                        time.sleep(0.5)
                        rrun=0
                    elif retry == 'n':
                        time.sleep(0.5)
                        print("프로그램을 종료합니다.")
                        time.sleep(0.5)
                        rrun=0
                        run=0
                else :
                    time.sleep(0.5)
                    print('문자를 입력해주세요.')
                    time.sleep(0.5)

        #2차 방정식
        elif select == '2':
            time.sleep(0.5)
            print("\n*******************************************")
            print("*******2차 방정식을 선택 하셨습니다.*******")
            print("*******************************************")
            time.sleep(0.5)
            print("\n2차 방정식의 모습은 ax² + bx + c = 0 (a ≠ 0)입니다. \n각각의 계수를 입력하세요.\n")
            x=Symbol('x')
            time.sleep(0.5)
            b=int(input('X²의 계수 b => '))
            c=int(input('x의 계수 => '))
            d=int(input('상수 c => '))
            eq=b*x**2+c*x+d
            a=solve(eq,x)
            if c**2-4*b*d<0:
                time.sleep(0.5)
                print('\n입력한 방정식의 해는')
                time.sleep(0.5)
                print(round(complex(a[0]).real,2),'+(',round(complex(a[0]).imag,2),"i)")
                print(round(complex(a[1]).real,2),'+(',round(complex(a[1]).imag,2),"i)")
                print('입니다.\n')
                time.sleep(0.5)
                time.sleep(0.5)
            elif c**2-4*b*d==0:
                print('입력한 방정식의 중근은')
                time.sleep(0.5)
                print(a[0])
                time.sleep(0.5)
                print('입니다.\n')
                time.sleep(0.5)
            elif c**2-4*b*d>0:
                print('\n입력한 방정식의 해는')
                time.sleep(0.5)
                print(a[0],a[1])
                time.sleep(0.5)
                print('입니다.\n')
                time.sleep(0.5)
            rrun = 1
            while rrun == 1:
                time.sleep(0.5)
                retry=str(input('Q. 다시 하시겠습니까?\nyes : y\nno : n\nA => '))
                time.sleep(0.5)
                if retry=='y' or retry =='n':
                    if retry == 'y':
                        time.sleep(0.5)
                        rrun=0
                    elif retry == 'n':
                        time.sleep(0.5)
                        print("프로그램을 종료합니다.")
                        time.sleep(0.5)
                        rrun=0
                        run=0
                else :
                    time.sleep(0.5)
                    print('문자를 입력해주세요.')
                    time.sleep(0.5)
        #3차 방정식
        elif select == '3':
            time.sleep(0.5)
            print("\n*******************************************")
            print("*******3차 방정식을 선택 하셨습니다.*******")
            print("*******************************************")
            time.sleep(0.5)
            print("\n3차 방정식의 모습은 ax³ + bx² + cx + d = 0 (a ≠ 0) 입니다. \n각각의 계수를 입력하세요.\n")
            x=Symbol('x')
            time.sleep(0.5)
            a=int(input('X³의 계수 a => '))
            b=int(input('X²의 계수 b => '))
            c=int(input('x의 계수 => '))
            d=int(input('상수 c => '))
            eq=a*x**3+b*x**2+c*x+d
            a=solve(eq,x)
            time.sleep(0.5)
            print('\n입력한 방정식의 해는')
            time.sleep(0.5)
            print(round(complex(a[0]).real,2),'+(',round(complex(a[0]).imag,2),"i)")
            print(round(complex(a[1]).real,2),'+(',round(complex(a[1]).imag,2),"i)")
            print(round(complex(a[2]).real,2),'+(',round(complex(a[2]).imag,2),"i)")
            time.sleep(0.5)
            print('입니다.\n')
            rrun = 1
            while rrun == 1:
                time.sleep(0.5)
                retry=str(input('Q. 다시 하시겠습니까?\nyes : y\nno : n\nA => '))
                time.sleep(0.5)
                if retry=='y' or retry =='n':
                    if retry == 'y':
                        time.sleep(0.5)
                        rrun=0
                    elif retry == 'n':
                        time.sleep(0.5)
                        print("프로그램을 종료합니다.")
                        time.sleep(0.5)
                        rrun=0
                        run=0
                else :
                    time.sleep(0.5)
                    print('문자를 입력해주세요.')
                    time.sleep(0.5)


        elif select=='4':
            time.sleep(0.5)
            print("\n*******************************************")
            print("*******4차 방정식을 선택 하셨습니다.*******")
            print("*******************************************")
            time.sleep(0.5)
            print("\n4차 방정식의 모습은 ax⁴ + bx³ + cx² + dx + e = 0 (a ≠ 0)입니다. \n각각의 계수를 입력하세요.\n")
            x=Symbol('x')
            time.sleep(0.5)
            b=int(input('X⁴의 계수 a => '))
            c=int(input('X³의 계수 b => '))
            d=int(input('X²의 계수 c => '))
            e=int(input('x의 계수 d => '))
            f=int(input('상수 e => '))
            eq=b*x**4+c*x**3+d*x**2+e*x+f
            a=solve(eq,x)
            time.sleep(0.5)
            print('\n입력한 방정식의 해는')
            time.sleep(0.5)
            print(round(complex(a[0]).real,2),'+(',round(complex(a[0]).imag,2),"i)")
            print(round(complex(a[1]).real,2),'+(',round(complex(a[1]).imag,2),"i)")
            print(round(complex(a[2]).real,2),'+(',round(complex(a[2]).imag,2),"i)")
            print(round(complex(a[3]).real,2),'+(',round(complex(a[3]).imag,2),"i)")
            time.sleep(0.5)
            print('입니다.\n')
            rrun = 1
            while rrun == 1:
                time.sleep(0.5)
                retry=str(input('Q. 다시 하시겠습니까?\nyes : y\nno : n\nA => '))
                time.sleep(0.5)
                if retry=='y' or retry =='n':
                    if retry == 'y':
                        time.sleep(0.5)
                        rrun=0
                    elif retry == 'n':
                        time.sleep(0.5)
                        print("프로그램을 종료합니다.")
                        time.sleep(0.5)
                        rrun=0
                        run=0
                else :
                    time.sleep(0.5)
                    print('문자를 입력해주세요.')
                    time.sleep(0.5)

        elif select=='5':
            time.sleep(0.5)
            print("\n*******************************************")
            print("*******5차 방정식을 선택 하셨습니다.*******")
            print("*******************************************")
            time.sleep(0.5)
            print("\n5차 방정식의 모습은 ax^5 + bx⁴ + cx³ + dx² + ex + f = 0 (a ≠ 0)입니다. \n각각의 계수를 입력하세요.\n")
            x=Symbol('x')
            time.sleep(0.5)
            a=int(input('X의 5제곱의 계수 a => '))
            b=int(input('X⁴의 계수 b => '))
            c=int(input('X³의 계수 c => '))
            d=int(input('X²의 계수 d => '))
            e=int(input('x의 계수 e => '))
            f=int(input('상수 f => '))
            eq=a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
            a=solve(eq,x)
            time.sleep(0.5)
            print('\n입력한 방정식의 해는')
            time.sleep(0.5)
            print(round(complex(a[0]).real,2),'+(',round(complex(a[0]).imag,2),"i)")
            print(round(complex(a[1]).real,2),'+(',round(complex(a[1]).imag,2),"i)")
            print(round(complex(a[2]).real,2),'+(',round(complex(a[2]).imag,2),"i)")
            print(round(complex(a[3]).real,2),'+(',round(complex(a[3]).imag,2),"i)")
            print(round(complex(a[4]).real,2),'+(',round(complex(a[4]).imag,2),"i)")
            time.sleep(0.5)
            print('입니다.\n')
            rrun = 1
            while rrun == 1:
                time.sleep(0.5)
                retry=str(input('Q. 다시 하시겠습니까?\nyes : y\nno : n\nA => '))
                time.sleep(0.5)
                if retry=='y' or retry =='n':
                    if retry == 'y':
                        time.sleep(0.5)
                        rrun=0
                    elif retry == 'n':
                        time.sleep(0.5)
                        print("프로그램을 종료합니다.")
                        time.sleep(0.5)
                        rrun=0
                        run=0
                else :
                    time.sleep(0.5)
                    print('문자를 입력해주세요.')
                    time.sleep(0.5)

        elif select=='6':
            
            x=Symbol('x')
            time.sleep(0.5)
            print("\n*******************************************")
            print("*******6차 방정식을 선택 하셨습니다.*******")
            print("*******************************************")
            time.sleep(0.5)
            print("\n6차 방정식의 모습은 ax^6 + bx^5 + cx⁴ + dx³ + ex² + fx + g = 0 (a ≠ 0)입니다. \n각각의 계수를 입력하세요.\n")
            time.sleep(0.5)
            q=int(input('X의 6제곱의 계수 a => '))
            a=int(input('X의 5제곱의 계수 b => '))
            b=int(input('X⁴의 계수 c => '))
            c=int(input('X³의 계수 d => '))
            d=int(input('X²의 계수 e => '))
            e=int(input('x의 계수 f => '))
            f=int(input('상수 g => '))
            eq=q*x**6+a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
            a=solve(eq,x)
            time.sleep(0.5)
            print('\n입력한 방정식의 해는')
            time.sleep(0.5)
            print(round(complex(a[0]).real,2),'+(',round(complex(a[0]).imag,2),"i)")
            print(round(complex(a[1]).real,2),'+(',round(complex(a[1]).imag,2),"i)")
            print(round(complex(a[2]).real,2),'+(',round(complex(a[2]).imag,2),"i)")
            print(round(complex(a[3]).real,2),'+(',round(complex(a[3]).imag,2),"i)")
            print(round(complex(a[4]).real,2),'+(',round(complex(a[4]).imag,2),"i)")
            print(round(complex(a[5]).real,2),'+(',round(complex(a[5]).imag,2),"i)")
            time.sleep(0.5)
            print('입니다.\n')
            rrun = 1
            while rrun == 1:
                time.sleep(0.5)
                retry=str(input('Q. 다시 하시겠습니까?\nyes : y\nno : n\nA => '))
                time.sleep(0.5)
                if retry=='y' or retry =='n':
                    if retry == 'y':
                        time.sleep(0.5)
                        rrun=0
                    elif retry == 'n':
                        time.sleep(0.5)
                        print("프로그램을 종료합니다.")
                        time.sleep(0.5)
                        rrun=0
                        run=0
                else :
                    time.sleep(0.5)
                    print('문자를 입력해주세요.')
                    time.sleep(0.5)

        elif select == '0':
            print("프로그램을 종료합니다.")
            time.sleep(0.5)
            run=0
    else:
        time.sleep(0.5)
        print('올바른 값을 입력해주세요.')
        time.sleep(0.5)        
