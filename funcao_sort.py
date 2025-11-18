def funcao_sort(num: list[int]) -> list[int]:
  lista = num[:]
  n = len(lista)

  for i in range(n):
    trocou = False;

    for j in range(0, n - i - 1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        trocou = True
    
    if not trocou:
      break

  return lista

def sort_numbers(num: list[int]) -> list[int]:
  return funcao_sort(num)


if __name__ == "__main__":
    teste = [10, 5, 3, 20, -1, 0]
    print("Lista original:", teste)
    print("Lista ordenada:", sort_numbers(teste))