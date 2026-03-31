# 파일이름 :main.py
# 작 성 자 :60222292 송형준
bucket_list=[]

res1=input("맛집 리스트 입력:")
bucket_list.append(res1)

res2=input("맛집 리스트 입력:")
bucket_list.append(res2)

res3=input("맛집 리스트 입력:")
bucket_list.append(res3)

print(f"리스트 :{bucket_list}\n")

vip_restaurant=input("맛집 리스트 추가:")
bucket_list.insert(0,vip_restaurant)

print(f"리스트;{bucket_list}\n")

visited_restaurant=input("도장깨기:")
bucket_list.remove(visited_restaurant)

print(f"리스트:{bucket_list}")
