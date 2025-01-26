values = input().split(' ')
A, B, C, D = map(float, values)

Media = (A + B + C + D) / 4

print(f'Media: {Media:.1f}')
if Media >= 7.0:
    print("Aluno Aprovado")
elif 5.0 <= Media < 7.0:
    print('Aluno em Exame')
else:
    print('Aluno Reprovado')
    exam_score = float(input("Nota do exame: "))
    print(f'Nota do exame: {exam_score:.1f}')

    # Recalculate the final average
    final_media = (Media + exam_score) / 2

    # Check if the student is approved or reproved after the exam
    if final_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    # Print the final average
    print(f'Media final: {final_media:.1f}')