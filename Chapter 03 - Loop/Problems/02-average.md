# Average Until -1

*(โจทย์ข้อนี้นำมาจากหนังสืิอ Python ๑๐๑ ภาควิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย)*  

อ่านข้อมูลจากแป้นพิมพ์เป็นจำนวนจริงไปเรื่อยๆ จนกว่าจะพบค่า -1 จากนั้นหาค่าเฉลี่ยของจำนวนเหล่านั้น (ในการคำนวณค่าเฉลี่ยให้ตัดค่า -1 ออกไป)

<u>ข้อมูลนำเข้า</u>  
รับค่าเป็นจำนวนจริง สามารถรับค่าได้เรื่อยๆ (มีจำนวนจริงใส่เข้ามาได้หลายบรรทัด) จนกว่าจะเจอค่า -1

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดงค่าเฉลี่ยของจำนวนทั้งหมด (ไม่รวม -1)  
หากไม่มีข้อมูลใส่เข้ามาเลยให้แสดงคำว่า **No Data**

## Example 1
<pre class="output">
_2295.498850599365_
_8502.139421733784_
_515.0100470901091_
_3705.6829835190097_
_8722.343211974356_
_4446.712951812571_
_6375.086965715_
_3801.511489785674_
_7638.911577747659_
_-1_
5111.43305555306
</pre>

## Example 2
<pre class="output">
_-1_
No Data
</pre>

::elab:begincode blank=True
total = 0
count = 0

while True:
    x = float(input())
    if x == -1:
        break
    total += x
    count += 1

if count == 0:
    print("No Data")
else:
    print(total/count)
::elab:endcode

::elab:begintest hint="-"
2295.498850599365
8502.139421733784
515.0100470901091
3705.6829835190097
8722.343211974356
4446.712951812571
6375.086965715
3801.511489785674
7638.911577747659
-1
::elab:endtest
::elab:begintest hint="-"
-1
::elab:endtest
::elab:begintest hint="-"
1532.18186151561516156
321583.54153515181515
321.158181561515
12132.548614561632156
-1
::elab:endtest
::elab:begintest hint="-"
-5123.41246126414
-3412.4431264961
-31234.213421
-123.481561532
-123.515818151
-1206.61816581561
-1
::elab:endtest
::elab:begintest hint="-"
-123.518612322122
659.735151891515
-1581.61294851512
-326.518153123151
211.515151212121
212.515165151321
-848.518184165841
-521.218418716541
848.184186158415
-545.541871865411
-1
::elab:endtest
::elab:begintest hint="-"
0
0
0
0
0
-1
::elab:endtest