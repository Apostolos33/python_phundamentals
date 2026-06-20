from math import floor
biscuits_produced_per_worker = int(input())
count_of_workers = int(input())
second_factory_biscuits = int(input())
first_factory_biscuits = 0
biscuits_per_day = biscuits_produced_per_worker * count_of_workers

for day in range(1, 31):
    if day % 3 == 0:
        first_factory_biscuits += floor(biscuits_per_day * 0.75)
    else:
        first_factory_biscuits += biscuits_per_day

print(f"You have produced {first_factory_biscuits} biscuits for the past month.")

defrence = abs(first_factory_biscuits - second_factory_biscuits)
percent = defrence / second_factory_biscuits * 100

if first_factory_biscuits > second_factory_biscuits:
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    print(f"You produce {percent:.2f} percent less biscuits.")