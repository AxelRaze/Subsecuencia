class Subsecuencia:
    maximo = 0
    datosSecuenMax = []

    def _lis(self,arr, n):
        # caso base  _punto_quiebre
        if n == 1:
            return 1

        maxFinalizaado = 1
        for i in range(1, n):
            res = self._lis(arr, i)
            if arr[i - 1] < arr[n - 1] and res + 1 > maxFinalizaado:
                self.datosSecuenMax.append(arr[i])
                maxFinalizaado = res + 1

        self.maximo = max(self.maximo, maxFinalizaado)
        # print(self.maximum, end= '')

        return maxFinalizaado

    def lis(self,arr):
        #global maximo
        #valores = []

        # lenght of arr
        n = len(arr)

        self.maximo = 1
        self._lis(arr, n)
        return self.maximo
def main():
    arr = [3,10,2,1,20]
    secuencia = Subsecuencia()
    secuencia.lis(arr)
    print("La subsecuencia creciente más larga es de tamaño", secuencia.lis(arr))

    #n = len(arr)

if __name__ == "__main__":
    main()
