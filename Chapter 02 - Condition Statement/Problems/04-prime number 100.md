# Prime Number 100

รับค่าเป็นจำนวนเต็มให้ตอบว่า จำนวนนั้นเป็นจำนวนเฉพาะหรือไม่ โดยค่าที่ใส่ไปจะไม่มีทางเกิน 100 แน่ๆ

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มบวก **n** เมื่อ 1 <= n <= 100

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบออกมาว่าเป็นจำนวนเฉพาะหรือไม่

**คำใบ้**  
สำหรับจำนวนเต็มบวกที่มีค่าน้อยกว่า 100 เราสามารถเช็คจำนวนเฉพาะได้ง่ายๆ โดยการทดลองหารจำนวนเฉพาะ 2,3,5,7 จะต้องหารไม่ลงตัวเลยสักค่า

## Example 1
<pre class="output">
N: _2_
2 is a Prime Number
</pre>

## Example 2
<pre class="output">
N: _39_
39 is not a Prime Number
</pre>

## Example 3
<pre class="output">
N: _97_
97 is a Prime Number
</pre>

::elab:begincode blank=True
n = int(input("N: "))

if n == 1 or (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0) and (n != 2 and n != 3 and n != 5 and n != 7):
    print(f"{n} is not a Prime Number")
else:
    print(f"{n} is a Prime Number")
::elab:endcode

::elab:begintest hint="-"
1
::elab:endtest

::elab:begintest hint="-"
2
::elab:endtest

::elab:begintest hint="-"
3
::elab:endtest

::elab:begintest hint="-"
5
::elab:endtest

::elab:begintest hint="-"
7
::elab:endtest

::elab:begintest hint="-"
9
::elab:endtest

::elab:begintest hint="-"
72
::elab:endtest

::elab:begintest hint="-"
19
::elab:endtest

::elab:begintest hint="-"
53
::elab:endtest

::elab:begintest hint="-"
73
::elab:endtest

::elab:begintest hint="-"
59
::elab:endtest

::elab:begintest hint="-"
91
::elab:endtest

::elab:begintest hint="-"
97
::elab:endtest