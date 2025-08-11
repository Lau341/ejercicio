open class Vehiculo(
    var marca: String,
    var patente: String,
    var color: String
)

class Auto(
    marca: String,
    patente: String,
    color: String,
    var motor: String,
    var dominio: String,
    var legajo: Int
) : Vehiculo(marca, patente, color)

fun main() {
    val obj = Auto("Toyota", "ABC123", "Rojo", "V8", "XYZ987", 12345)

    // Modificar directamente porque son vars
    obj.motor = "2JZ"
    obj.dominio = "Lautaro"
    obj.legajo = 456983

    // Acceder directamente
    println("Motor: ${obj.motor}")
    println("Dominio: ${obj.dominio}")
    println("Legajo: ${obj.legajo}")
}
