#Inicio da função pesoBase()
def pesoBase():
  print('---------- Opção 1 de 3 - Peso Cão ----------')
  while True:
    try:
      pesoB = int(input('Digite o peso do cachorro:'))
      if (pesoB < 3): #calculo de peso dos cachorros
        return pesoB * 40  
      elif (pesoB >= 3) and (pesoB < 10):
        return pesoB * 50
      elif (pesoB >= 10) and (pesoB < 30):
        return pesoB * 60
      elif (pesoB >= 30) and (pesoB < 50):
        return pesoB * 70
      else:
        print('Não aceitamos cachorros tão grandes!')
        continue
    except ValueError:
      print('Pare de digitar valores não numéricos!')
#Fim da função pesoBase()

#Inicio da função peloMulti()
def peloMulti():
  print('---------- Opção 2 de 3 - Pelo Cão ----------')
  while True:
    peloCao = input('Digite o pelo do cachorro \n' +
                    'c - pelo curto \n' +
                    'm - pelo médio \n' +
                    'l - pelo longo \n' +
                    '>> ')
    peloCao = peloCao.lower()
    peloCao = peloCao.strip()
    if peloCao == 'c':
      return 1
    elif peloCao == 'm':
      return 1.5
    elif peloCao == 'l':
      return 2
    else:
      print('Pare de digitar opções diferentes de c/m/l')
      continue #volta para o ínicio do laço
#Fim da função peloMulti()

#Inicio da função adicionalExtra()
def adicionalExtra():
  print('---------- Opção 3 de 3 - Adicional Cão ----------')
  acumulador = 0
  while True:
    adicionalEx = input('Deseja adicionar mais algum serviço: \n' +
                        '0 - Não desejo adicionar mais nada! \n' +
                        '1 - Corte de Unhas - R$ 10,00 \n' +
                        '2 - Escovar os Dentes - R$ 12,00 \n' +
                        '3 - Limpeza de Orelhas - R$ 15,00 \n' +
                        '>> ')
    if adicionalEx == '0':
      return acumulador
    elif adicionalEx == '1':
      acumulador = acumulador + 10
      continue
    elif adicionalEx == '2':
      acumulador = acumulador + 12
      continue
    elif adicionalEx == '3':
      acumulador = acumulador + 15
      continue
    else:
      print('Pare de digitar opções diferentes de 0/1/2/3')
#Fim da função adicionalExtra()

#Início do Main
print('---------- Bem-vindo ao PetShop de Lorena Muller ----------')
peso = pesoBase() #peso do cachorro
pelo = peloMulti() #pelo do cachorro 
adicional = adicionalExtra() #adicional de limpeza
total = (peso * pelo) + adicional
print('O total ficou: R$ {:.2f} (peso: R$ {:.2f}, pelo: {:.2f}, adicional: {:.2f})'. format (total,peso,pelo,adicional))
