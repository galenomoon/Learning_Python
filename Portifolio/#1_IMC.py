# ====================== IMC ==================
calcule_again = True

def get_imc(weight, hight):
  imc = float(weight)/(float(hight)**2)
  return imc

def get_classification(imc):
  if imc < 18.5:
    classification = "MAGREZA"
  elif imc >= 18.5 and imc < 24.9:
    classification = "NORMAL"
  elif imc >= 25 and imc < 29.9:
    classification = "SOBREPESO"
  elif imc >= 30 and imc < 39:
    classification = "OBESIDADE"
  elif imc >= 40:
    classification = "OBESIDADE GRAVE"
  return classification

while calcule_again == True:
  print("===== Calculadora IMC =====")
  weight = input("Digite seu peso (kg): ")
  hight = input("Digite sua altura (m): ")
  imc = get_imc(weight, hight)
  print(f"Seu IMC é: {imc: ,.2f}")
  print(f"Classificação: {get_classification(imc)}")
  
  calcule_again = input("Deseja calcular novamente? (S/N): ")
  if calcule_again.upper() == "N":
    print("Adeus!")
    calcule_again = False
  if calcule_again != False and calcule_again.upper() == "S":  
    print("---------------------------")
    calcule_again = True