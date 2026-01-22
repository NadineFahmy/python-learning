for i in range(1, 21):

    if i in (6, 8, 12):
        continue

    if i < 10:
        print(f"0{i}")
    else:
        print(i)

print("Loop finished successfully.")

# Needed Output
"01"
"02"
"03"
"04"
"05"
"07"
"09"
"10"
"11"
"13"
"14"
"15"
"16"
"17"
"18"
"19"
"20"
"All Numbers Printed"
