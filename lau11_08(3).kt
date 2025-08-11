open class Operaciones {
    var resultado: Int = 0
}

class Sumar(var num1: Int = 0, var num2: Int = 0) : Operaciones() {
    fun calcular() {
        resultado = num1 + num2
        println("Suma: $resultado")
    }
}

class Restar(var num1: Int = 0, var num2: Int = 0) : Operaciones() {
    fun calcular() {
        resultado = num1 - num2
        println("Resta: $resultado")
    }
}

class Multiplicar(var num1: Int = 0, var num2: Int = 0) : Operaciones() {
    fun calcular() {
        resultado = num1 * num2
        println("Multiplicación: $resultado")
    }
}

class Dividir(var num1: Int = 0, var num2: Int = 0) : Operaciones() {
    fun calcular() {
        if (num2 != 0) {
            resultado = num1 / num2
            println("División: $resultado")
        } else {
            println("Error: División por cero")
        }
    }
}

fun main() {
    val suma = Sumar()
    suma.num1 = 5
    suma.num2 = 2
    suma.calcular()

    val resta = Restar()
    resta.num1 = 10
    resta.num2 = 8
    resta.calcular()

    val multiplicacion = Multiplicar()
    multiplicacion.num1 = 2
    multiplicacion.num2 = 4
    multiplicacion.calcular()

    val division = Dividir()
    division.num1 = 20
    division.num2 = 5
    division.calcular()
}
