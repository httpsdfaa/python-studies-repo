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

    for questions_index in questions:
        question_correct = ''
        input_user = ''

        print('----------------------------------')

        print(questions_index['question'], '\n')
        for option in questions_index['options']:
            print(option)
        input_user = input('Dentre as opções acima, qual o opção correta? ')

        print('----------------------------------')

        try:
            if input_user == questions_index['answer']:
                question_correct = input_user
                print(f'\nSua resposta foi {question_correct}. \nVOCÊ ESTÁ CORRETO 💥😎 \n\n')
            else:
                print('\nSua resposta está incorreta 😟😟\n\n')
        except:
            print('Algo inesperado aconteceu 😲\n\n')
    

def main():
    logic_question()

main()