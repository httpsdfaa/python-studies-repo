""" 
    EXERCÍCIO - SISTEMA DE PERGUNTAS E RESPOSTAS
"""

questions = [
    {
        'id': 1,
        'question': 'Quantos é 2 + 2?',
        'options': ['1', '2', '3', '4'],
        'answer': '4',
    },
    {
        'id': 2,
        'question': 'Quantos é 100 + 100',
        'options': ['20', '2000', '200', '100'],
        'answer': '200'
    },
    {
        'id': 3,
        'question': 'Quanto é 5 x 5?',
        'options': ['50', '100', '25', '10'],
        'answer': '25'
    }
]

def logic_question():

    asnwer_result = []

    for questions_index in questions:
        question_correct = ''
        input_user = ''

        print('----------------------------------')

        print(questions_index['question'], '\n')
        print(*questions_index['options'], '\n')
        input_user = input('Dentre as opções acima, qual o opção correta? ')

        print('----------------------------------')

        try:
            if input_user == questions_index['answer']:
                question_correct = input_user
                print(f'\nSua resposta foi {question_correct}. \nVOCÊ ESTÁ CORRETO 💥😎 \n\n')
                asnwer_result.append(f'')
            else:
                print('\nSua resposta está incorreta \n\n')
                asnwer_result.append(f'{input_user} é incorreto 😟')
        except:
            print('Algo inesperado aconteceu 😲\n\n')
    

def main():
    logic_question()

# main()