# # Câu  1 thay các kí tự giống kí tự đầu tiên của chuỗi thành $
# def thaydoichucaidau():
#     a = input("Nhap: ")
#     s = "$"
#     for i in range(1,len(a)):
#         if a[i] == a[0]:
#             s+="$"
#         else:
#             s+=a[i]
#     return s
# print(f"chuoi: {thaydoichucaidau()}")

# # Câu  2 xóa bỏ ký tự thứ m không rổng, với m là số không âm, nhập từ phím.
# def xoabokitu():
#     n = input("Nhap chuoi: ")
#     m = int(input("Nhap thu tu muon xoa trong chuoi: "))
#     s = ""
#     while m < 0:
#         m= int(input("Nhap lai: "))
#     for i in range(len(n)):
#         if i!=m:
#             s+=n[i]
#     return s
# print(f"Xuat chuoi: {xoabokitu()}")

# # Câu 3 xóa bỏ kí tự có số lẻ trong chuỗi
# def xoakitule(s):
#     return s[::2]
# s=input("Nhap chuoi: ")
# print(xoakitule(s))

# # Câu 4 viết  một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
# print("Nhap chuoi: ",end="")
# chuoi=str(input())
# def dau_duoi(chuoi):
#     print(chuoi[0:2]+chuoi[-2:])
#     if len(chuoi)<2:
#         print("Chuoi rong")
# dau_duoi(chuoi)

# # Câu 5 tìm kí tự lớn nhất và nhỏ nhất, nhập từ bàn phím
# def sosanhkitu():
#     chuoi = input("Nhap chuoi: ")
#     s=""
#     for i in range(len(chuoi)):
#         s+=chuoi[i] 
#         chuoilon = max(chuoi)
#         chuoibe = min(s)
#     if chuoilon > chuoibe:
#         print("Ki tu lon nhat: ",chuoilon) 
#         print("Ki tu be nhat: ",chuoibe)
# sosanhkitu()

# # Câu 6 Kí tự thường sang hoa và ngược lại
# print("Nhap chuoi: ",end="")
# s=str(input())
# def hoa(s):
#     kq1=""
#     for i in s:
#         if i.islower():   
#             kq1+=i.upper()
#         else:
#             kq1+=i.lower()
#     return kq1
# print(f"Hoa: {hoa(s)}")