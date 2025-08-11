import java.time.LocalDate

open class Producto(
    var valor: Int,
    var nombre: String,
    var color: String
)

class Alimento(
    valor: Int,
    nombre: String,
    color: String,
    var gusto: String,
    var vencimiento: LocalDate,
    var cantidad: Int
) : Producto(valor, nombre, color)

fun main() {
    val obj = Alimento(
        valor = 20,
        nombre = "Fideos",
        color = "Verde",
        gusto = "Salado",
        vencimiento = LocalDate.of(2026, 11, 17), // año, mes, día
        cantidad = 3
    )

    // Puedes modificar los valores si quieres:
    obj.gusto = "Salado"
    obj.vencimiento = LocalDate.of(2026, 11, 17)
    obj.cantidad = 3

    println("Gusto: ${obj.gusto}")
    println("Vencimiento: ${obj.vencimiento}")
    println("Cantidad: ${obj.cantidad}")
}