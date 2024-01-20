quantidade_alunos = int(input("Insira quantos alunos há na classe: \n"))
quantidade_provas = int(input("Insira quantos trabalhos avaliativos houveram no semestre: \n"))
nota_max = int(input('Insira a nota máxima do semestre: \n'))

aprovacao = int(input('Insira a porcentagem necessária para a aprovação de um aluno no semestre: \n'))
aprovacao_porcentagem = aprovacao / 100

lista_alunos = []

# Função que fará o trabalho de compilar os nomes, matriculas e notas dos alunos
def notas():
    nome = input("Insira o nome do aluno: \n")
    matricula = input("Insira a matrícula do aluno: \n")
    lista_alunos = [{"Matricula": matricula}, {"Nome": nome}]
    soma_notas = 0

    for i in range(quantidade_provas):
        nota = float(input("Insira a nota do aluno do trabalho avaliativo de número: {} \n".format(i + 1)))
        peso = float(input("Insira o peso do trabalho avaliativo (de 10 a 0) de número: {} \n".format(i + 1)))
        valor = peso / 10
        resultado = nota * valor
        soma_notas += resultado
        lista_alunos.append([{"Trabalho avaliativo {}".format(i + 1): resultado}])
    lista_alunos.append({"Soma das Notas": soma_notas})
    return lista_alunos


for _ in range(quantidade_alunos):
    lista_alunos.append(notas())

#Função para selecionar um aluno em especifico para verificar sua nota total
def nota_aluno(matricula_aluno):
    for aluno in lista_alunos:
        for item in aluno:
            if 'Matricula' in item and item ['Matricula'] == matricula_aluno:
                for nota in aluno:
                    if 'Soma das Notas' in nota:
                        return nota['Soma das Notas']
        return 'Aluno não encontrado'

    matricula_aluno = input('Insira a matrícula do aluno que você deseja verificar a nota: \n')
    print(nota_aluno(matricula_aluno))

#Função que avalia se as notas dos alunos são válidas considerando a nota máxima possível do semestre
for aluno in lista_alunos:
    soma_notas = 0
    matricula = ''
    nome = ''
    for item in aluno: 
        if 'Soma das Notas' in item:
            soma_notas = item['Soma das Notas']
        if 'Matricula' in item:
            matricula = item['Matricula']
        if 'Nome' in item: 
            nome = item['Nome']
    if soma_notas > nota_max:
        
        print('O seguinte aluno está com a nota total maior do que a nota máxima informada para o sistema: ')
        print('Matrícula: {}, nome: {}, com a nota de: {}' .format(matricula, nome, soma_notas))

#Função para verificar a média geral da turma
def media_geral():
    soma_total = 0
    for aluno in lista_alunos:
        for item in aluno:
            if 'Soma das Notas' in item:
                soma_total += item['Soma das Notas']
                media = soma_total / quantidade_alunos
                print('A média geral da turma é de: {:.2f}' .format(media))

#Função para verificar a média de um aluno
def media_aluno ():
    for aluno in lista_alunos:
        for item in aluno:
            if 'Matricula' in item and item ['Matricula'] == matricula_aluno:
                soma_notas = 0
                quantidade_notas = 0
                for nota in aluno:
                    if 'Trabalho avaliativo' in nota:
                        soma_notas += nota ['Trabalho avaliativo']
                        quantidade_notas += 1
                        if quantidade_notas > 0:
                            media = soma_notas / quantidade_notas
                            return media
        return 'Aluno não encontrado'
    
    matricula_aluno = input('Digite a matrícula do aluno que deseja verificar a nota: \n')
    print(media_aluno(matricula_aluno))
    
#Função para verificar todas as notas de um aluno especifico
def notas_aluno(matricula_aluno):
    for aluno in lista_alunos:
        for item in aluno:
            if 'Matricula' in item and item ['Matricula'] == matricula_aluno:
                notas = []
                for nota in aluno:
                    if 'Trabalho avaliativo' in nota:
                        notas.append(nota['Trabalho avaliativo'])
                        return notas
        return 'Aluno não encontrado'
    
    matricula_aluno = input('Insira a matrícula do aluno que você deseja verificar as notas: \n')
    print(notas_aluno(matricula_aluno))

#Função para verificar a aprovação de um aluno específico
def aprovacao_aluno (matricula_aluno):
    for aluno in lista_alunos:
        for item in aluno:
            if 'Matricula' in item and item ['Matricula'] == matricula_aluno:
                for nota in aluno: 
                    if 'Soma das Ntoas' in nota:
                        porcentagem = (nota['Soma das Notas']/ nota_max) * 100
                        if nota['Soma das Notas'] >= nota_max * aprovacao_porcentagem:
                            return 'O aluno está aprovado com {:.2f}% de média geral no semestre' .format(porcentagem)
                        else:
                            return 'O aluno está reprovado com {:.2f}% de média geral no semestre' .format(porcentagem)
        return 'Aluno não encontrado'
    
    matricula_aluno = input('Insira a matrícula do aluno que deseja verificar as notas')
    print(aprovacao_aluno(matricula_aluno))

#Função para verificar quais alunos foram aprovados e quais foram reprovados
def aprovados ():
    resultado = []
    for aluno in lista_alunos:
        for item in aluno:
            if 'Matricula' in item:
                matricula = item ['Matricula']
                if 'Nome' in item:
                    nome = item['Nome']
                    if 'Soma das Notas' in item:
                        porcentagem = (item['Soma das Notas'] / nota_max) * 100
                        if item ['Soma das Notas'] >= nota_max * aprovacao_porcentagem:
                            resultado.append({'Matricula': matricula, 'Nome': nome, 'Status': 'Aprovado', 'Porcentagem de Média:': f'{porcentagem:.2f}%'})
                        else: 
                            resultado.append ({'Matricula': matricula, 'Nome': nome, 'Status': 'Reprovado', 'Porcentagem de Média': f'{porcentagem:.2f}%'})
        return resultado

#Função para listar apenas alunos reprovados e suas porcentagens
def reprovados ():
    reprovados = []
    for aluno in lista_alunos:
        for item in aluno:
            if 'Matricula' in item: 
                matricula = item['Matricula']
                if 'Nome' in item: 
                    nome = item['Nome' ]
                    if 'Soma das Notas' in item: 
                        porcentagem = (item['Soma das Notas'] / nota_aluno) *100
                        if item['Soma das Notas '] < nota_max * aprovacao_porcentagem:
                            reprovados.append ({'Matricula': matricula, 'Nome': nome, 'Porcentagem de Média:': f'{porcentagem:.2f}%'})
        return reprovados

#Função para verificação de notas
verificacao = input('Deseja verificar alguma nota? \n [Sim/Nao] \n')
verificacao = verificacao.upper()

if verificacao == 'SIM':
    opcoes = [
    'Digite a opção desejada:', 
    '1 - Verificar nota total de aluno específico', 
    '2 - Verificar todas as notas de um aluno',
    '3 - Verificar todas as notas da sala', 
    '4 - Verificar a média geral da sala',
    '5 - Verificar média de aluno especifico',
    '6 - Verificar alunos aprovados e reprovados',
    '7 - Verificar se um aluno especifico está aprovado'
    '8 - Verificar alunos reprovados',
    ]
    print(opcoes)
    while True:
        selecao = int(input('Digite a opção que deseja verificar: \n'))
        if selecao == 1:
            nota_aluno()
            break
        elif selecao == 2: 
            notas_aluno()
            break
        elif selecao == 3: 
            print(lista_alunos)
            break
        elif selecao == 4:
            media_geral()
            break
        elif selecao == 5:
            media_aluno()
            break
        elif selecao == 6:
            aprovados ()
            break
        elif selecao == 7:
            aprovacao_aluno ()
            break
        elif selecao == 8:
            reprovados()
            break
        else:
            print('Opção inválida!')
elif verificacao == 'NAO':
    print('Obrigado!')
else:
    print('Opção inválida')
