print("Football Match Analyzer")
time=float(input("enter the time of a match:- \n"))
team_a=input("Enter Team A Name:- \n ")
team_b=input("Enter Team B Name:- \n ")
time_diff=90-time
print("time diff is :-",time_diff)
team_a_score=int(input("Enter Team A Score:- \n"))
team_b_score=int(input("Enter Team B Score:- \n"))

if team_a_score>team_b_score:
    score=team_a_score-team_b_score
    print("team a score is lead by :-",team_a_score)
    team_a_win= (team_a_score/team_b_score)*time_diff
    print("team a probality of  win is :-",team_a_win,"Percent")
    team_b_win= (team_b_score/team_a_score)*time_diff
    print("team b will make a draw  is :-",team_b_win,"Percent")

elif team_a_score<team_b_score:
    score=team_b_score-team_a_score
    print("team b score is lead by :-",team_b_score)
    team_b_win= (team_b_score/team_a_score)*time_diff
    print("team b probality of win is :-",team_b_win,"Percent")
    team_a_win= (team_a_score/team_b_score)*time_diff
    print("team a probality to draw  is :-",team_a_win,"Percent")

else:
    print("team a and b score are equal")

