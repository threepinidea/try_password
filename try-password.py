# password = 'a123456'
# i = 3
# while True:
#     pwd = input('請輸入密碼: ')
#     if pwd == password:
#         print('登入成功!')
#         break
#     else:
#         i -= 1
#         print('密碼錯誤!','還有',i,'次機會')
#         if i == 0:
#             break

password = 'a123456'
i = 3
while i > 0:
    i -= 1
    pwd = input('請輸入密碼:')
    if pwd == password:
        print('登入成功')
        break
    else:
        if i > 0:
            print('還剩:', i, '機會')
        else:
            print('密碼多次錯誤!','\n請聯絡客服')