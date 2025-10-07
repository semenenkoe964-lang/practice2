def check_winners(sours,student_score):
    if (sours[-1]==student_score)or(sours[-2]==student_score)or(sours[-3]==student_score):
        print("Вы в тройке")
        return
    print("Вы не в тройке")
    return
sours_inp=list(map(int,input().split()))
score=int(input())
check_winners(sorted(sours_inp),score)
