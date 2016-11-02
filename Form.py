import sys
import os
operators=['/','*','-','+','(',')']
def Operate(a,b,operation):
    if(operation=='*'):
        result=a*b
    elif(operation=='+'):
        result=a+b
    elif(operation=='-'):
        result=a-b
    else:
        if(b!=0):
            result=a/b
        else:
            os.system('cls')
            print("Error! Delenie na 0!\n")
            menu()
    return result #Вычисление действия в зависимости от оператора
def ConvertToFirstForm(line): #Для разделения поступившей строки на операторы, операнды и скобки
    firstform=[]
    temp=0
    if line[0]=='-':
        line='0'+line
    for i in range(len(line)):
        if(line[i] in operators):  
            if(line[i]!='(' and line[i-1]!=')'):      
                firstform.append(int(str(line[temp:i])))
            firstform.append(line[i])
            temp=i+1
    if(line[-1]!=')'):
        firstform.append(int(str(line[temp:])))
    return firstform
def ConverToPostForm(line): #Представление выражения в постфиксной форме
    postform=[]
    stack=[]
    for i in range(len(line)):
        if(line[i] in operators):
            if(line[i]==')'):
                revstack=list(reversed(stack))
                indbkt=revstack.index('(')
                postform.extend(revstack[:indbkt])
                stack=stack[:len(stack)-indbkt-1]
            else:
                if(len(stack)):
                    if ((stack[-1]=='*' or stack[-1]=='/') and line[i]!='(' or (stack[-1]=='+' or stack[-1]=='-') and (line[i]=='+' or line[i]=='-')):
                        revstack=list(reversed(stack))
                        if ((line[i]=='*' or line[i]=='/') and ('+' in stack or '-' in stack)):
                            if('+' in stack):   
                                indlp=revstack.index('+')
                            else:
                                indlp=revstack.index('-')
                            postform.extend(revstack[:indlp])
                            stack=stack[:len(stack)-indlp]
                        else:
                            if('(' in stack):
                                indbkt=revstack.index('(')
                                postform.extend(revstack[:indbkt])
                                stack=stack[:len(stack)-indbkt]
                            else:
                                postform.extend(revstack)                                  
                                stack=[]
                stack.append(line[i])                              
        else:
            postform.append(line[i])
    postform.extend(list(reversed(stack)))  
    return postform
def Calculation(line): #Вычисление значения выражения по его постфиксной форме
    i=2
    while(i<len(line)):
        if(line[i] in operators): 
            temp=Operate(line[i-2],line[i-1],line[i])
            line=line[:i-2]+line[i+1:]
            line.insert(i-2,temp)
            i=1
        i+=1
    return line.pop()
def menu():
    task=input("Vvedite primer:\n>>> ")
    flagmenu=int(input("MENU\n1.Vivesti postfixnuy zapis\n2.Reshit primer\n0.Exit\n>>>  "))
    if(flagmenu==1):
        print(''.join(str(x) for x in ConverToPostForm(ConvertToFirstForm(task))))
    elif(flagmenu==2):
        print(Calculation(ConverToPostForm(ConvertToFirstForm(task))))
    else:   
        sys.exit()
    flag=int(input("Vvesti esche odin primer? (1/0)\n>>> ")) 
    if(flag):
        os.system('cls')
        menu()
    else:
        sys.exit() 
menu()