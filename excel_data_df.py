import pandas

# Comando printar no terminal a planilha inteira

excel_data_df = pandas.read_excel('grupo.xlsx', sheet_name ='Time')
print('Planilha completa')
print(excel_data_df)

print('\n\n') #comando para pular uma linha

print('Buscar apenas o nome dos profissionais')
print(excel_data_df['Nome'].tolist())


print('\n\n')
print('Buscar apenas o nome das profissões')
print(excel_data_df['Profissão'].tolist())

#filtrar por um nome específico
wendel_data =excel_data_df.loc[excel_data_df['Nome'] == 'Wendel', 'Nome']
print(wendel_data.tolist())
