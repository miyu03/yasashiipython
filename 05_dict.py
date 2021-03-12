point_dict = {
    '001': (100, 88, 81),
    '002': (77, 94, 85),
    '003': (80, 52, 99),
}

for student_id in point_dict:
    points = point_dict[student_id]
    subject_number = len(points)
    japanese, english, mathmatics = points
    total = japanese + english + mathmatics
    average = total / 3

    excellent = subject_number * 100 * 0.8
    good = subject_number * 100 * 0.65

    if total >= excellent:
        evaluation = 'Excellent!'
    elif total >= good:
        evaluation = 'Good'
    else:
        evaluation = 'Bad'
    print(f'学籍番号{student_id}:合計点は{total}、評価は{evaluation},平均点は{average}です。')
