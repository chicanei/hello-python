[![hackmd-github-sync-badge](https://hackmd.io/LgcJvZRCSfe-dHRRcbShzw/badge)](https://hackmd.io/LgcJvZRCSfe-dHRRcbShzw)
# 2.函式print(),input(),變數以及四則運算

- [回目錄](/5mKoyoSOQOyK2Q0y8bKFDA)

### 本次課程目標
* 1、將文字顯示在螢幕上
* 2、可以利用python來編寫、編輯與運行程式
* 3、會使用`print()`,`input()`函式
* 4、利用python進行四則運算

---

### :a: 使用函式 print()
:::info
### :bulb:`print(value %(引數串列),sep=間隔字串,end=結尾字串)`
:::

#### :one: 在螢幕上列印 `"3+2"` ，使用 `print()`函式


```(python)
print("3+2")   #加法
```
> [ :?: 結果是列印出字串 3+2/ 還是數字3+2的和 ?]

----

#### :two: 在螢幕上列印 `7-4` ，使用` print()`函式

```(python)
print(7-4)   #減法
```
----


#### :heart: 練習

```(::python::)
print(4 * 5)   #乘法
print(5 / 3)   #浮點數除法
print(15 ** 2)   #次方(指數)
print(35 // 3)    #整數除法
print(35 % 3)     #取除法的餘數
print(3*8,(16-2)*8)   # (a,b)
print("Scott :heart: Marry!") #引號列印出字串
```


[觀看程式列印結果ideone](https://ideone.com/ootO3p)

----
:::danger
:baby_chick: 想想看，以下問題 :face_with_raised_eyebrow:
1. 41被7除，請問餘數為?
2. 列印出3的8次方
3. 請計算出 `(a,b)=((5%(101%3)),((76//3)*4))`的結果為
:::

 
---

### :b: 使用函式 input()
:::info
### :bulb:`變數 = input([提示字串])` 
:::

#### :one: 練習使用input()函式讓使用者輸入資料

```(::python::) 
print(" 請輸入你的名字 ")   #在螢幕上顯示 請輸入你的名字
name = input()              #儲存資料到name中
print(" 請輸入你的年齡 ") 
age = input()               
print('Hi ' + name + ':'+ age +'歲'+ '!')  #在螢幕上輸出資料
```
[觀看程式列印結果ideone](https://ideone.com/epMSWq)

----

#### :heart: 練習
```(:::python)
ct = int(input("輸入攝氏溫度\n")) # \n 表示換行 new line
print('攝氏%d度' %ct)
print(type(ct))
f =(((ct*9)/5)+32)
print(type(f))
print('f的記憶體位置:',id(f))
print('華氏%2.2f度' %f)
```
:::danger
:hatching_chick: 
1.`print(type())`可印出該變數的型別
2.`print(id())`可印出該變數的記憶體位址


:::
[觀看程式列印結果ideone](https://ideone.com/sVXM7x)






