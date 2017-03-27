# real_order = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta','France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia']
# best_order = ['Germany', 'Albania', 'San Marino', 'Armenia', 'Russia', 'Malta', 'Azerbaijan', 'Poland', 'Moldova', 'Norway', 'Belarus','Montenegro', 'Italy', 'Austria', 'FYR Macedonia', 'United Kingdom', 'Ukraine', 'Estonia', 'Romania', 'Latvia', 'Finland', 'Georgia', 'Iceland', 'Hungary', 'Israel', 'Ireland', 'Switzerland', 'Greece', 'Belgium', 'Sweden', 'Portugal', 'Slovenia', 'Denmark', 'France','Lithuania', 'Spain', 'The Netherlands']
# order3 = ['Azerbaijan','Greece','Poland','Albania','San Marino','Denmark','Montenegro','Romania','Russia','The Netherlands','Malta', 'France','United Kingdom','Latvia','Armenia','Iceland','FYR Macedonia','Sweden','Belarus','Germany','Israel','Portugal','Norway','Estonia','Hungary','Moldova','Ireland','Finland','Lithuania','Austria','Spain','Belgium','Italy','Ukraine','Switzerland','Georgia','Slovenia']
# order4 = ['Belarus', 'Malta', 'Montenegro', 'Norway', 'Albania', 'Azerbaijan', 'Denmark', 'Germany', 'Lithuania', 'Estonia', 'Russia','The Netherlands', 'Armenia', 'Poland', 'San Marino', 'Moldova', 'Georgia', 'France', 'Switzerland', 'Austria', 'Greece', 'Latvia', 'Israel','Ukraine', 'Sweden', 'FYR Macedonia', 'Slovenia', 'Iceland', 'Spain', 'Romania', 'Ireland', 'Italy', 'United Kingdom', 'Belgium','Hungary','Finland', 'Portugal']

two_five_two_eight = ['San Marino', 'Armenia', 'Italy', 'Albania', 'Poland', 'Azerbaijan', 'Malta', 'Russia', 'Austria', 'United Kingdom','Belarus', 'FYR Macedonia', 'Moldova', 'Lithuania', 'Montenegro', 'Ukraine', 'Estonia', 'Germany', 'Romania', 'Latvia', 'Finland','France','Denmark', 'Belgium', 'Greece', 'Hungary', 'Switzerland', 'Israel', 'Norway', 'Sweden', 'Portugal', 'Georgia', 'Slovenia', 'Ireland','Iceland', 'Spain', 'The Netherlands']
two_five_two_nine = ['Albania', 'Belarus', 'Poland', 'San Marino', 'Armenia', 'Italy', 'Malta', 'Austria', 'Azerbaijan', 'United Kingdom','Russia', 'FYR Macedonia', 'Moldova', 'Lithuania', 'Montenegro', 'Ukraine', 'Estonia', 'Germany', 'Romania', 'Latvia', 'Denmark','Georgia', 'Sweden','Belgium', 'Portugal', 'Israel', 'Norway', 'Switzerland', 'Greece', 'Hungary', 'Finland', 'France', 'Slovenia','Ireland', 'Iceland','Spain', 'The Netherlands']

if __name__ == '__main__':
    dist = 0
    for country in (two_five_two_eight):
        index1, index2 = two_five_two_eight.index(country), two_five_two_nine.index(country)
        dist = dist + abs(index1 - index2)

    print(dist)
    
    