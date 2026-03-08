import random 

workers = ["이재실", "김시현", "정시경", "정종원", "강성주"]
total_schedule = []
rest_person = "" 

time_slots = {
    1: "09:00 ~ 10:30",
    2: "10:30 ~ 12:00",
    3: "13:00 ~ 15:00",
    4: "16:00 ~ 08:00"
}

for day in range(5):
    available_workers = []
    for w in workers:
        if w != rest_person:
            available_workers.append(w)
            
    random.shuffle(available_workers)
    today_workers = available_workers[:4] 
    
    daily_schedule = []
    for i in range(len(today_workers)):
        real_time = time_slots[i + 1] 
        shift = {today_workers[i]: real_time}
        daily_schedule.append(shift)
        
    total_schedule.append(daily_schedule)
    rest_person = today_workers[3] 

# 결과 출력
print("📅 5일 치 근무 시간표")
print("-" * 60)
for day in range(5):
    print(f"{day + 1}일차: {total_schedule[day]}")