#stata_1 = [1203, 737, 595, 1332, 81, gretzky_1, howe_1, jagr_1, 36, 270]



print('Did Ovi play this night  ')
mark_game = int(input())

if mark_game == 1:
    print('How many Ovi scores this night  ')
    mark_goals = int(input())
    print('Alex asists  ')
    mark_asists = int(input())
    mark_points = mark_goals + mark_asists
    print('+/-  ')
    mark_poleznost = int(input())
    if mark_goals != 0:
        print('Power play goals  ')
        mark_ppg = int(input())



gretzky_1 = 894
howe_1 = 801
jagr_1 = 766

stata_1 = [1203, 737, 595, 1332, 81, gretzky_1, howe_1, jagr_1, 36, 270]
gr = gretzky_1 - stata_1[1]
ho = howe_1 - stata_1[1]
ja = jagr_1 - stata_1[1]
stata_2 = [1203, 737, 595, 1332, 81, gr, ho, ja, 36, 270]

print(stata_2)

if mark_game == 1:
    stata_2[0] +=1
    if mark_goals != 0:
         stata_2[1] = stata_2[1] + mark_goals
         stata_2[5] = stata_2[5] - mark_goals
         stata_2[6] = stata_2[6] - mark_goals
         stata_2[7] = stata_2[7] - mark_goals
         if mark_ppg != 0:
            stata_2[9] = stata_2[9] + mark_ppg
    if mark_asists != 0:
        stata_2[2] = stata_2[2] + mark_asists
    if mark_points != 0:
        stata_2[3] = stata_2[3] + mark_points
    if mark_poleznost != 0:
        stata_2[4] = stata_2[4] + mark_poleznost

print(stata_2)














stata = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    stata[i] = str(stata_2[i])
