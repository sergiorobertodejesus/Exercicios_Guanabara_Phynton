salario = float(input(' qual é o salario do funcionario R$: '))
aumento = salario *15/100
novo_salario = aumento + salario
print(f'um funcionario que ganhava R${salario},com 15% de aumento passa a receber R${novo_salario:.2f}')